# coding: utf-8
from unittest import TestCase
from webapps.features import Features

features = Features("webapps_test/test.csv")


def test_get():
    assert 77.23106517484075 == features.get(1386, "回帰誤差")
    assert 186 == features.get(1386, "f")
    assert 0 == features.get(1267, "正面")
    assert 1 == features.get(1213, "iida")


def test_get_angle():
    assert {"正面":0, "側面":0, "斜面":1, "高い":0, "遠い":0} == features.get_angle(1386)
