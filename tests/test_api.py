import subprocess
import requests
import json

# API基础URL
BASE_URL = "http://localhost:5001/api"


def test_minimal_compile():
    """测试最简单的TeX编译"""
    print("测试编译最简单的TeX文档...")

    # 检查pdflatex命令是否可用
    try:
        result = subprocess.run(["which", "pdflatex"], capture_output=True, text=True)
        print(f"pdflatex路径: {result.stdout.strip()}")
        result = subprocess.run(
            ["pdflatex", "--version"], capture_output=True, text=True
        )
        first_line = result.stdout.split("\n")[0] if result.stdout else "无输出"
        print(f"pdflatex版本: {first_line}")
    except Exception as e:
        print(f"检查pdflatex命令时出错: {str(e)}")

    # 非常简单的TeX文档
    minimal_tex = r"""\documentclass{article}
    \begin{document}
    Hello World
    \end{document}
    """

    # 发送编译请求
    response = requests.post(
        f"{BASE_URL}/compile",
        json={"tex_code": minimal_tex},
        headers={"Content-Type": "application/json"},
    )

    # 打印结果
    print(f"状态码: {response.status_code}")
    try:
        print(f"响应内容: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except:
        print(f"原始响应: {response.text}")


if __name__ == "__main__":
    test_minimal_compile()
