# -*- coding: utf-8 -*-
import pytest

from app.domain.model.cards import Card, CardNumber, Suit


class TestSuit(object):
    def test_value_of(self):
        assert Suit.SPADE == Suit.value_of('S')
        assert Suit.CLUB == Suit.value_of('C')
        assert Suit.DIAMOND == Suit.value_of('D')
        assert Suit.HEART == Suit.value_of('H')
        with pytest.raises(ValueError):
            Suit.value_of('X')


class TestCardNumber(object):
    def test_value_of(self):
        assert CardNumber.ACE == CardNumber.value_of('A')
        assert CardNumber.TWO == CardNumber.value_of('2')
        assert CardNumber.THREE == CardNumber.value_of('3')
        assert CardNumber.FOUR == CardNumber.value_of('4')
        assert CardNumber.FIVE == CardNumber.value_of('5')
        assert CardNumber.SIX == CardNumber.value_of('6')
        assert CardNumber.SEVEN == CardNumber.value_of('7')
        assert CardNumber.EIGHT == CardNumber.value_of('8')
        assert CardNumber.NINE == CardNumber.value_of('9')
        assert CardNumber.TEN == CardNumber.value_of('10')
        assert CardNumber.JACK == CardNumber.value_of('J')
        assert CardNumber.QUEEN == CardNumber.value_of('Q')
        assert CardNumber.KING == CardNumber.value_of('K')
        with pytest.raises(ValueError):
            CardNumber.value_of('14')
        with pytest.raises(ValueError):
            CardNumber.value_of('0')


class TestCard(object):
    def setup_method(self, method):
        self.s2 = Card('S2')
        self.dj = Card('DJ')
        self.ca = Card('CA')
        self.hq = Card('HQ')
        self.ten = Card('S10')

    def teardown_method(self, method):
        pass

    def test_create_instance(self):
        assert Suit.SPADE == self.s2.suit
        assert CardNumber.TWO == self.s2.number
        assert Suit.DIAMOND == self.dj.suit
        assert CardNumber.JACK == self.dj.number
        assert Suit.CLUB == self.ca.suit
        assert CardNumber.ACE == self.ca.number
        assert Suit.HEART == self.hq.suit
        assert CardNumber.QUEEN == self.hq.number
        assert Suit.SPADE == self.ten.suit
        assert CardNumber.TEN == self.ten.number
        with pytest.raises(ValueError):
            Card('M87')
        with pytest.raises(ValueError):
            Card('H100')
