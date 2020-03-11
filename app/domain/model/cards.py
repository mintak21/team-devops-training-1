# -*- coding: utf-8 -*-
from enum import Enum


class Card(object):
    """１枚のトランプを表します。

    Attributes:
        suit (Suit)  : カードのスート
        number (CardNumber)  : カードの番号
    """

    def __init__(self, card_str):
        suit_str = card_str[0]
        number_str = card_str[1:]
        self._suit = Suit.value_of(suit_str)
        self._number = CardNumber.value_of(number_str)

    @property
    def suit(self):
        return self._suit

    @property
    def number(self):
        return self._number

    def __str__(self):
        return self._suit.string_style + self._number.string_style

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self._suit == other.suit and self._number == other.number
        return NotImplemented

    def __hash__(self):
        return hash((self._suit, self._number))


class Suit(Enum):
    """カードのスートを表す。
    """
    SPADE = ('S')
    HEART = ('H')
    DIAMOND = ('D')
    CLUB = ('C')

    def __init__(self, string_style):
        self._string_style = string_style

    @property
    def string_style(self):
        return self._string_style

    @classmethod
    def value_of(cls, string_style):
        """引数に対応するSuitを返却します

        Args:
            string_style (string): S, H, D, Cの文字

        Raises:
            ValueError: 未定義の文字が指定され、変換に失敗した場合

        Returns:
            Suit: 変換したSuit
        """
        for e in Suit:
            if e.string_style == string_style:
                return e
        raise ValueError()


class CardNumber(Enum):
    """カードの数字を表す。
    <=>で比較可能　※<=、>=は使用不可。
    """

    ACE = (1, 'A')
    KING = (13, 'K')
    QUEEN = (12, 'Q')
    JACK = (11, 'J')
    TEN = (10, '10')
    NINE = (9, '9')
    EIGHT = (8, '8')
    SEVEN = (7, '7')
    SIX = (6, '6')
    FIVE = (5, '5')
    FOUR = (4, '4')
    THREE = (3, '3')
    TWO = (2, '2')

    def __init__(self, int_number, string_style):
        self._int_number = int_number
        self._string_style = string_style

    @property
    def number(self):
        return self._int_number

    @property
    def string_style(self):
        return self._string_style

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self._int_number > other.number
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self._int_number < other.number
        return NotImplemented

    def __add__(self, other):
        if self.__class__ is other.__class__:
            return self._int_number + other.number
        return NotImplemented

    def __sub__(self, other):
        if self.__class__ is other.__class__:
            return self._int_number - other.number
        return NotImplemented

    @classmethod
    def value_of(cls, string_style):
        """引数に対応するCardNumberを返却します

        Args:
            string_style (string): A,K,Q,J,10~2の文字

        Raises:
            ValueError: 未定義の文字が指定され、変換に失敗した場合

        Returns:
            CardNumber: 変換したCardNumber
        """
        for e in CardNumber:
            if e.string_style == string_style:
                return e
        raise ValueError()
