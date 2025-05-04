import os
import json
from utils.tex_converter import TexConverter


class CompilationService:
    def __init__(self, config):
        """
        初始化编译服务

        Args:
            config: 应用配置
        """
        # 使用字典访问方式而不是属性访问方式
        self.converter = TexConverter(config["TEMP_FOLDER"])

    def compile_tex(self, tex_code):
        """
        编译TeX代码

        Args:
            tex_code (str): TeX源代码

        Returns:
            dict: 包含编译结果的字典
        """
        success, result = self.converter.compile_tex(tex_code)

        if success:
            # 从结果路径中提取PDF ID
            pdf_path = result
            pdf_id = os.path.basename(os.path.dirname(pdf_path))

            return {"success": True, "pdf_id": pdf_id, "message": "编译成功"}
        else:
            # 错误情况
            return {"success": False, "error": result, "message": "编译失败"}

    def get_pdf(self, pdf_id):
        """
        获取编译好的PDF

        Args:
            pdf_id (str): PDF文件ID

        Returns:
            str: PDF文件路径或None
        """
        return self.converter.get_pdf_path(pdf_id)
