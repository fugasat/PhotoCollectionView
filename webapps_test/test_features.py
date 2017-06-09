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
    assert {"正面": 0, "側面": 0, "斜面": 1, "高い": 0, "遠い": 0} == features.get_angle(1386)
    assert {"正面": 1, "側面": 0, "斜面": 0, "高い": 1, "遠い": 1} == features.get_angle(1395)


def test_get_rail():
    assert {"直線": 0, "曲線": 1} == features.get_rail(1267)
    assert {"直線": 1, "曲線": 0} == features.get_rail(1213)


def test_get_scene():
    assert {"森林": 0, "駅": 1, "畑": 0, "鉄橋": 0, "踏切": 0, "scene特徴なし": 0} == features.get_scene(1386)
    assert {"森林": 0, "駅": 0, "畑": 0, "鉄橋": 0, "踏切": 0, "scene特徴なし": 1} == features.get_scene(1395)


def test_get_area():
    assert {"北海道": 1, "東北": 0, "東海": 0, "首都圏": 0, "中央": 0, "信越": 0, "北陸": 0, "九州": 0, "area特徴なし": 0}\
           == features.get_area(1267)
    assert {"北海道": 0, "東北": 0, "東海": 1, "首都圏": 1, "中央": 0, "信越": 1, "北陸": 0, "九州": 0, "area特徴なし": 0}\
           == features.get_area(1384)
