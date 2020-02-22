# -*- coding: utf-8 -*-
from enum import Enum


class HandType(Enum):
    """役一覧
    """

    ROYAL_STRAIGHT = ('ロイヤルストレート')
    STRAIGHT_FLUSH = ('ストレートフラッシュ')
    FOUR_OF_A_KIND = ('フォーカード')
    FULL_HOUSE = ('フルハウス')
    FLUSH = ('フラッシュ')
    STRAIGHT = ('ストレート')
    THREE_OF_A_KIND = ('スリーカード')
    TWO_PAIR = ('ツーペア')
    ONE_PAIR = ('ワンペア')
    HIGH_CARDS = ('ハイカード')

    def __init__(self, display_name):
        self._display_name = display_name

    @property
    def disp_name(self):
        return self._display_name
