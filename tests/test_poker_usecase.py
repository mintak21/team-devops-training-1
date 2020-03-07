# -*- coding: utf-8 -*-
import pytest

from app.domain.model.hands import HandType
from app.usecase.poker import judge_hand


class TestPokerUseCase(object):
    def setup_method(self, method):
        self.rss = ['S10', 'SJ', 'SQ', 'SK', 'SA']
        self.rsd = ['DJ', 'DQ', 'DK', 'DA', 'D10']
        self.rsh = ['HQ', 'HK', 'HA', 'H10', 'HJ']
        self.rsc = ['CA', 'CK', 'CQ', 'CJ', 'C10']
        self.h1 = ['S2', 'DJ', 'CA', 'HQ', 'S10']
        self.h2 = ['SA', 'S10', 'S8', 'H4', 'H2']
        self.o1 = ['SA', 'DA', 'H3', 'H4', 'H5']
        self.o2 = ['SA', 'S2', 'D3', 'H3', 'H8']
        self.th1 = ['SA', 'DA', 'S8', 'HA', 'H2']
        self.th2 = ['H2', 'S2', 'D2', 'H4', 'S6']
        self.f1 = ['SA', 'DA', 'CA', 'HA', 'CK']
        self.f2 = ['SK', 'DK', 'C10', 'HK', 'CK']
        self.fl = ['SA', 'S2', 'SJ', 'SQ', 'SK']
        self.st = ['H7', 'D6', 'H5', 'S4', 'C3']
        self.st_dummy = ['C2', 'H2', 'S3', 'D4', 'C6']
        self.st_fl = ['S9', 'S10', 'SJ', 'SQ', 'SK']
        self.fl1 = ['H2', 'S2', 'D2', 'H4', 'S4']
        self.tp1 = ['H4', 'S4', 'D2', 'HJ', 'SJ']
        self.tp2 = ['D2', 'SQ', 'H2', 'HK', 'SK']

    def teardown_method(self, method):
        pass

    def test_royal_straight(self):
        assert HandType.ROYAL_STRAIGHT == judge_hand(self.rss)
        assert HandType.ROYAL_STRAIGHT == judge_hand(self.rsd)
        assert HandType.ROYAL_STRAIGHT == judge_hand(self.rsh)
        assert HandType.ROYAL_STRAIGHT == judge_hand(self.rsc)

    def test_high_card(self):
        assert HandType.HIGH_CARDS == judge_hand(self.h1)
        assert HandType.HIGH_CARDS == judge_hand(self.h2)

    def test_one_pair(self):
        assert HandType.ONE_PAIR == judge_hand(self.o1)
        assert HandType.ONE_PAIR == judge_hand(self.o2)

    def test_three_of_a_kind(self):
        assert HandType.THREE_OF_A_KIND == judge_hand(self.th1)
        assert HandType.THREE_OF_A_KIND == judge_hand(self.th2)

    def test_straight_flush(self):
        # LEVEL C:ストレートフラッシュ判定テストの実装箇所
        pass

    def test_straight(self):
        # LEVEL C:ストレート判定テストの実装箇所
        pass

    def test_flush(self):
        assert HandType.FLUSH == judge_hand(self.fl)

    def test_four_of_a_kind(self):
        assert HandType.FOUR_OF_A_KIND == judge_hand(self.f1)
        assert HandType.FOUR_OF_A_KIND == judge_hand(self.f2)

    def test_full_house(self):
        assert HandType.FULL_HOUSE == judge_hand(self.fl1)

    def test_two_pair(self):
        assert HandType.TWO_PAIR == judge_hand(self.tp1)
        assert HandType.TWO_PAIR == judge_hand(self.tp2)
