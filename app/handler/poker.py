# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request

from ..usecase.poker import judge_hand

pokerBp = Blueprint('poker', __name__)


@pokerBp.route('/judge', methods=['GET'])
def judge():
    cards = request.args.get('cards')
    result = judge_hand(cards.split(','))
    return jsonify({
        'param_cards': cards,
        'result': result.disp_name, }
    )