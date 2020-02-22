# -*- coding: utf-8 -*-
from flask import Flask

from .handler.health import healthBp
from .handler.poker import pokerBp

app = Flask(__name__)
app.register_blueprint(healthBp, url_prefix='/api/v1/health')
app.register_blueprint(pokerBp, url_prefix='/api/v1/poker')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
