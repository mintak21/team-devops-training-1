# -*- coding: utf-8 -*-
from flask import Flask

from .handler.health import health_bp
from .handler.poker import poker_bp

app = Flask(__name__)
app.register_blueprint(health_bp, url_prefix='/api/v1/health')
app.register_blueprint(poker_bp, url_prefix='/api/v1/poker')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
