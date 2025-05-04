import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


# 应用配置
class Config:
    # 调试模式控制详细错误信息和自动重载
    DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

    # 临时文件配置
    TEMP_FOLDER = os.environ.get("TEMP_FOLDER", "static/temp")

    # API配置
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")
