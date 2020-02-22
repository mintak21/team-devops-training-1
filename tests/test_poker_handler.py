# -*- coding: utf-8 -*-
import pytest

from app.manage import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_judge(client):
    # ステータスレベルのハンドリングテスト
    # このレベルならmockはなくていい
    res = client.get('/api/v1/poker/judge?cards=S2,S3,S4,S5,S10')
    assert 200 == res.status_code
