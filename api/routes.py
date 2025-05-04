from flask import Blueprint, request, jsonify, send_file, current_app
from services.compilation import CompilationService
import os

api_bp = Blueprint("api", __name__, url_prefix="/api")
compilation_service = None


@api_bp.record
def record_params(setup_state):
    global compilation_service
    app = setup_state.app
    compilation_service = CompilationService(app.config)


@api_bp.route("/compile", methods=["POST"])
def compile_tex():
    """
    接收TeX代码并编译为PDF
    """
    data = request.get_json()

    if not data or "tex_code" not in data:
        return jsonify({"success": False, "message": "请提供TeX代码"}), 400

    result = compilation_service.compile_tex(data["tex_code"])

    if result["success"]:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@api_bp.route("/preview/<pdf_id>", methods=["GET"])
def preview_pdf(pdf_id):
    """
    获取PDF预览
    """
    pdf_path = compilation_service.get_pdf(pdf_id)

    if not pdf_path or not os.path.exists(pdf_path):
        return jsonify({"success": False, "message": "PDF文件不存在"}), 404

    return send_file(pdf_path, mimetype="application/pdf")


@api_bp.route("/download/<pdf_id>", methods=["GET"])
def download_pdf(pdf_id):
    """
    下载PDF文件
    """
    pdf_path = compilation_service.get_pdf(pdf_id)

    if not pdf_path or not os.path.exists(pdf_path):
        return jsonify({"success": False, "message": "PDF文件不存在"}), 404

    return send_file(
        pdf_path,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="document.pdf",
    )
