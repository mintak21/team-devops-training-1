# -*- coding: utf-8 -*-

from flask import Blueprint, Response
from flask_api import status

healthBp = Blueprint('health', __name__)


@healthBp.route('/', methods=['GET'])
def health():
    return Response(
        status=status.HTTP_200_OK,
        response="pass")
