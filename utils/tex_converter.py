import os
import subprocess
import tempfile
import shutil
import uuid
from PyPDF2 import PdfReader
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TexConverter:
    def __init__(self, temp_dir):
        """
        初始化TeX转换器

        Args:
            temp_dir (str): 临时文件存储目录
        """
        self.temp_dir = temp_dir
        os.makedirs(temp_dir, exist_ok=True)

    def compile_tex(self, tex_code):
        """
        编译TeX代码为PDF

        Args:
            tex_code (str): TeX源代码

        Returns:
            tuple: (成功标志, PDF文件路径或错误信息)
        """
        # 生成唯一ID作为临时文件名
        file_id = str(uuid.uuid4())
        work_dir = os.path.join(self.temp_dir, file_id)

        try:
            # 创建临时工作目录
            os.makedirs(work_dir, exist_ok=True)

            # 保存TeX代码到临时文件
            tex_file_path = os.path.join(work_dir, f"{file_id}.tex")
            with open(tex_file_path, "w", encoding="utf-8") as f:
                f.write(tex_code)

            # 编译TeX文件
            result = self._run_pdflatex(tex_file_path, work_dir)

            if not result["success"]:
                return False, result["error"]

            # 生成的PDF文件路径
            pdf_file_path = os.path.join(work_dir, f"{file_id}.pdf")

            # 检查PDF文件是否存在和有效
            if not os.path.exists(pdf_file_path):
                return False, "PDF文件生成失败"

            try:
                # 验证PDF文件是否可读
                PdfReader(pdf_file_path)
            except Exception as e:
                return False, f"生成的PDF文件无效: {str(e)}"

            return True, pdf_file_path

        except Exception as e:
            logger.error(f"TeX编译过程中发生错误: {str(e)}")
            # 清理临时文件
            self._clean_temp_files(work_dir)
            return False, f"编译过程中发生错误: {str(e)}"

    def _run_pdflatex(self, tex_file_path, work_dir):
        """
        运行pdflatex命令编译TeX文件

        Args:
            tex_file_path (str): TeX文件路径
            work_dir (str): 工作目录

        Returns:
            dict: 包含编译结果的字典
        """
        try:

            # 运行pdflatex命令，指定非交互模式(-interaction=nonstopmode)
            process = subprocess.Popen(
                ["pdflatex", "-interaction=nonstopmode", tex_file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=work_dir,
            )

            # 等待编译完成
            stdout, stderr = process.communicate(timeout=60)  # 60秒超时

            # 检查编译是否成功
            if process.returncode != 0:
                error_log = os.path.join(
                    work_dir, f"{os.path.basename(tex_file_path)[:-4]}.log"
                )
                error_message = "TeX编译失败"

                # 尝试从日志中提取错误信息
                if os.path.exists(error_log):
                    with open(error_log, "r", encoding="utf-8", errors="ignore") as f:
                        log_content = f.read()
                    logger.error(f"编译日志内容: {log_content[:500]}...")

                    # 寻找错误消息 (! 开头)
                    import re

                    error_matches = re.findall(
                        r"!(.*?)(?=\n[^\n])", log_content, re.DOTALL
                    )
                    if error_matches:
                        error_message = error_matches[0].strip()
                        logger.error(f"提取的错误信息: {error_message}")

                return {"success": False, "error": error_message}

            return {"success": True}

        except subprocess.TimeoutExpired:
            process.kill()
            logger.error("编译超时")
            return {"success": False, "error": "编译超时"}
        except Exception as e:
            logger.error(f"编译过程中发生异常: {str(e)}")
            return {"success": False, "error": str(e)}

    def _clean_temp_files(self, directory):
        """
        清理临时文件

        Args:
            directory (str): 要清理的目录
        """
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
        except Exception as e:
            logger.error(f"清理临时文件时发生错误: {str(e)}")

    def get_pdf_path(self, pdf_id):
        """
        获取PDF文件路径

        Args:
            pdf_id (str): PDF文件ID

        Returns:
            str: PDF文件路径或None
        """
        pdf_path = os.path.join(self.temp_dir, pdf_id, f"{pdf_id}.pdf")
        return pdf_path if os.path.exists(pdf_path) else None
