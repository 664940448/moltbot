from flask import Flask, render_template, jsonify

# 创建Flask应用实例
app = Flask(__name__)

# 根路由，返回HTML页面
@app.route('/')
def index():
    return "hello world"

# 也可以添加一个JSON格式的API接口
@app.route('/api/hello')
def api_hello():
    return jsonify({
        "message": "hello world",
        "status": "success"
    })

# 健康检查端点
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    return "Internal server error", 500

if __name__ == '__main__':
    # 启动服务，监听7000端口
    # debug=True 仅在开发环境中使用
    app.run(
        host='0.0.0.0',  # 监听所有网络接口
        port=7000,
        debug=False  # 生产环境设为False
    )