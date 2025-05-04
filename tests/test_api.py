import requests
import json

# API基础URL
BASE_URL = "http://localhost:5001/api"


def test_minimal_compile():
    """测试最简单的TeX编译"""
    print("测试编译最简单的TeX文档...")

    # 非常简单的TeX文档
    minimal_tex = r"\documentclass{article}\begin{document}Hello World\end{document}"

    # 发送编译请求
    response = requests.post(
        f"{BASE_URL}/compile",
        json={"tex_code": minimal_tex},
        headers={"Content-Type": "application/json"},
    )

    # 打印结果
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")


if __name__ == "__main__":
    test_minimal_compile()
