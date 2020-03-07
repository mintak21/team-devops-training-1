# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from flask_cors import CORS

from ..usecase.poker import judge_hand

poker_bp = Blueprint('poker', __name__)
CORS(poker_bp)


@poker_bp.route('/judgement')
def judge():
    cards = request.args.get('cards')
    result = judge_hand(cards.split(','))
    return jsonify({
        'param_cards': cards,
        'result': result.disp_name, }
    )
