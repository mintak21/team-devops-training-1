# -*- coding: utf-8 -*-
import pytest

from app.manage import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    res = client.get('/api/v1/health/')
    assert b'pass' == res.data
