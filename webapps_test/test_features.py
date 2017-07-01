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


def test_get_angle_values():
    assert ["斜面", "低い", "近い"] == features.get_angle_values(1386)
    assert ["正面", "高い", "遠い"] == features.get_angle_values(1395)


def test_get_rail():
    assert {"直線": 0, "曲線": 1} == features.get_rail(1267)
    assert {"直線": 1, "曲線": 0} == features.get_rail(1213)


def test_get_rail_values():
    assert ["直線"] == features.get_rail_values(1213)
    assert ["曲線"] == features.get_rail_values(1395)


def test_get_scene():
    assert {"森林": 0, "駅": 1, "畑": 0, "鉄橋": 0, "踏切": 0, "scene特徴なし": 0} == features.get_scene(1386)
    assert {"森林": 0, "駅": 0, "畑": 0, "鉄橋": 0, "踏切": 0, "scene特徴なし": 1} == features.get_scene(1395)


def test_get_scene_values():
    assert ["駅", "鉄橋"] == features.get_scene_values(1384)
    assert ["森林", "踏切"] == features.get_scene_values(1318)
    assert [] == features.get_scene_values(1395)


def test_get_area():
    assert {"北海道": 1, "東北": 0, "東海": 0, "首都圏": 0, "中央": 0, "信越": 0, "北陸": 0, "九州": 0, "area特徴なし": 0}\
           == features.get_area(1267)
    assert {"北海道": 0, "東北": 0, "東海": 1, "首都圏": 1, "中央": 0, "信越": 1, "北陸": 0, "九州": 0, "area特徴なし": 0}\
           == features.get_area(1384)


def test_get_area_values():
    assert ["東海", "首都圏", "信越"] == features.get_area_values(1384)
    assert ["北海道", "東北", "中央", "信越", "北陸", "九州"] == features.get_area_values(1211)
    assert [] == features.get_area_values(1404)


def test_get_model():
    assert {'dc72': 0, '24': 0, '24h': 0, '415': 0, 'old_pc': 1, 'ef58': 1, 'dc40h': 0, 'ef64': 0, 'ef62': 0, 'd51': 0, 'dc40': 0, '113y': 0, '113': 0, 'dc58': 0, 'c62': 0, '14': 0, 'ed75': 0, 'dc52': 0, 'dc281': 0, '10': 0, 'ef65pf': 0, 'df50': 0, '457': 0, 'dd51': 0, 'dd13': 0, 'ef65': 0, 'ed76': 0, 'ef63': 0, 'dc30': 0, 'nimotu': 0, '485': 0, 'de10': 0, '455': 0, 'dc91': 0, 'dc22': 0, 'fre': 0, 'ef66': 0, '157': 0, '14z': 0, 'ef15': 0, 'ef80': 0, 'ed78': 0, '183': 0, 'dc82': 0, '115': 0, 'ef64_10': 0, 'iida': 0, '153': 0, '583': 0, '165': 0, '20': 0, 'ef81': 0, '185': 0, 'nse': 0, '403': 0}\
           == features.get_model(1384)
    assert {'ef62': 0, 'c62': 0, '185': 0, '113': 0, 'ed76': 0, '14': 1, 'ef58': 0, 'nimotu': 1, '20': 0, 'dc82': 0, 'ef64': 0, '485': 0, 'dc91': 0, 'dc281': 0, '455': 0, 'dc22': 0, 'dc58': 0, 'ef64_10': 0, 'fre': 0, '24': 0, 'dc52': 0, '14z': 0, 'ef65pf': 0, '415': 0, '10': 0, '183': 0, 'ef81': 0, 'de10': 0, 'ef65': 0, 'df50': 0, 'ed75': 0, '153': 0, 'ef80': 0, 'ef66': 0, '457': 0, 'ef63': 0, '113y': 0, 'ef15': 0, '583': 0, '165': 0, 'dc40h': 0, 'iida': 0, '24h': 0, '115': 0, 'dc40': 0, 'd51': 0, 'ed78': 0, 'dc30': 0, '403': 0, 'nse': 0, '157': 0, 'dc72': 0, 'dd13': 0, 'old_pc': 0, 'dd51': 1}\
           == features.get_model(1267)


def test_get_model_values():
    assert ["14", "dd51", "nimotu"] == features.get_model_values(1267)
    assert ["ef58", "old_pc"] == features.get_model_values(1384)


def test_similarity():
    uids = features.get_similarity_uids(1395)
