# -*- coding: utf-8 -*-
import pytest

from app.domain.model.hands import HandType
from app.usecase.poker import judge_hand


class TestPokerUseCase(object):
    def setup_method(self, method):
        self.h1 = ['S2', 'DJ', 'CA', 'HQ', 'S10']
        self.h2 = ['SA', 'S10', 'S8', 'H4', 'H2']
        self.o1 = ['SA', 'DA', 'H3', 'H4', 'H5']
        self.o2 = ['SA', 'S2', 'D3', 'H3', 'H8']
        self.th1 = ['SA', 'DA', 'S8', 'HA', 'H2']
        self.th2 = ['H2', 'S2', 'D2', 'H4', 'S4']
        self.f1 = ['SA', 'DA', 'CA', 'HA', 'CK']
        self.f2 = ['SK', 'DK', 'C10', 'HK', 'CK']
        self.fl = ['SA', 'S2', 'SJ', 'SQ', 'SK']

    def teardown_method(self, method):
        pass

    def test_high_card(self):
        assert HandType.HIGH_CARDS == judge_hand(self.h1)
        assert HandType.HIGH_CARDS == judge_hand(self.h2)

    def test_one_pair(self):
        assert HandType.ONE_PAIR == judge_hand(self.o1)
        assert HandType.ONE_PAIR == judge_hand(self.o2)

    def test_three_of_a_kind(self):
        assert HandType.THREE_OF_A_KIND == judge_hand(self.th1)
        assert HandType.THREE_OF_A_KIND == judge_hand(self.th2)

    def test_flush(self):
        assert HandType.FLUSH == judge_hand(self.fl)

    def test_four_of_a_kind(self):
        assert HandType.FOUR_OF_A_KIND == judge_hand(self.f1)
        assert HandType.FOUR_OF_A_KIND == judge_hand(self.f2)
