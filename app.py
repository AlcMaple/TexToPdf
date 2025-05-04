import os
from flask import Flask
from flask_cors import CORS
from config import Config
from api.routes import api_bp
import logging


def create_app(config_class=Config):
    """
    创建Flask应用

    Args:
        config_class: 配置类

    Returns:
        Flask: Flask应用实例
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 配置跨域资源共享
    CORS(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})

    # 注册蓝图
    app.register_blueprint(api_bp)

    # 确保临时目录存在
    os.makedirs(app.config["TEMP_FOLDER"], exist_ok=True)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=5001)
