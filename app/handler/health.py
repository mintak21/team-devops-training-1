# -*- coding: utf-8 -*-

from flask import Blueprint, Response
from flask_api import status

health_bp = Blueprint('health', __name__)


@health_bp.route('/', methods=['GET'])
def health():
    return Response(
        status=status.HTTP_200_OK,
        response="pass")
