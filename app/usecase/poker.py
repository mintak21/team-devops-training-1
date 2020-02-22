# -*- coding: utf-8 -*-
import collections

from ..domain.model.cards import Card
from ..domain.model.hands import HandType


class PokerUseCase:
    def execute(self, str_cards):
        """ポーカーの役を判定します。

        Args:
            str_cards (list(string)): 文字列のcardリスト

        Returns:
            Handtype: 役の判定結果
        """
        cards = self._convert_param(str_cards)
        return HandType.FOUR_OF_A_KIND if self._has_four_of_a_kind(cards) else \
            HandType.THREE_OF_A_KIND if self._has_three_of_a_kind(cards) else \
            HandType.ONE_PAIR if self._has_one_pair(cards) else HandType.HIGH_CARDS

    def _has_four_of_a_kind(self, cards):
        return self._has_more_same_cards(cards, 4)

    def _has_three_of_a_kind(self, cards):
        return HandType.THREE_OF_A_KIND if self._has_more_same_cards(
            cards, 3) else None

    def _has_one_pair(self, cards):
        return HandType.ONE_PAIR if self._has_more_same_cards(
            cards, 2) else None

    def _has_more_same_cards(self, cards, target_num):
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
        # Issue Level Cの実装箇所目処
        result = [Card(s) for s in str_cards]
        return result


_pokerUseCase = PokerUseCase()
judge_hand = _pokerUseCase.execute
