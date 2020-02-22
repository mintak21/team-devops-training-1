# -*- coding: utf-8 -*-
import collections

from ..domain.model.cards import Card
from ..domain.model.hands import HandType


class PokerUseCase:
    _ROYAL_STRAIGHTS = [
        (Card('S10'), Card('SJ'), Card('SQ'), Card('SK'), Card('SA')),
        (Card('D10'), Card('DJ'), Card('DQ'), Card('DK'), Card('DA')),
        (Card('H10'), Card('HJ'), Card('HQ'), Card('HK'), Card('HA')),
        (Card('C10'), Card('CJ'), Card('CQ'), Card('CK'), Card('CA')),
    ]

    def execute(self, str_cards):
        """ポーカーの役を判定します。

        Args:
            str_cards (list(string)): 文字列のcardリスト

        Returns:
            Handtype: 役の判定結果
        """
        cards = self._convert_param(str_cards)
        return HandType.ROYAL_STRAIGHT if self._has_royal_straight(cards) else \
            HandType.STRAIGHT_FLUSH if self._has_straight_flush(cards) else \
            HandType.FOUR_OF_A_KIND if self._has_four_of_a_kind(cards) else \
            HandType.FLUSH if self._has_flush(cards) else \
            HandType.STRAIGHT if self._has_straight(cards) else \
            HandType.THREE_OF_A_KIND if self._has_three_of_a_kind(cards) else \
            HandType.ONE_PAIR if self._has_one_pair(cards) else \
            HandType.HIGH_CARDS

    def _has_royal_straight(self, cards):
        for s in PokerUseCase._ROYAL_STRAIGHTS:
            if set(s) <= set(cards):
                return True
        return False

    def _has_straight_flush(self, cards):
        return self._has_flush(cards) and \
            self._has_straight(cards)  # 5枚以上の場合はNG

    def _has_four_of_a_kind(self, cards):
        return self._has_more_same_cards(cards, 4)

    def _has_flush(self, cards):
        suit_set = set([c.suit for c in cards])
        return len(suit_set) == 1  # 5枚以上の場合はNG

    def _has_straight(self, cards):
        # LEVEL C:ストレート判定の実装箇所
        return False

    def _has_three_of_a_kind(self, cards):
        return self._has_more_same_cards(cards, 3)

    def _has_one_pair(self, cards):
        return self._has_more_same_cards(cards, 2)

    def _has_more_same_cards(self, cards, target_num):
        """{cards}が{target_num}枚以上のペアを含むかを判定します

        Args:
            cards (list(Card)): 判定対象のカード
            target_num (int): 調べたい枚数

        Returns:
            bool: {target_num}枚以上のペアが1つでもあればTrue、そうでなければFalse
        """
        number_list = [c.number for c in cards]
        collection = collections.Counter(number_list)
        for l in collection.most_common():
            if (l[1] >= target_num):
                return True
        return False

    def _convert_param(self, str_cards):
        """stringのカードリストをCardに変換します

        Args:
            str_cards (list(string)): 文字列のカード一覧

        Returns:
            list(Card): 変換されたカード一覧
        """
        result = [Card(s) for s in str_cards]
        return result


_pokerUseCase = PokerUseCase()
judge_hand = _pokerUseCase.execute
