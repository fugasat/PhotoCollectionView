import os.path
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from webapps.const import Const


class Features:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def get(self, uid, key):
        row = self.df[self.df["ID"] == uid].iloc[0]
        values = row[key]
        return values

    def get_angle(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.loc["正面":"曲線"]
        row_dict = row_feature.to_dict()
        return row_dict

    def get_angle_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "正面":"曲線"]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)  # 値が"1"の列だけ抽出
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)  # np.append()は遅いので使わないこと
        return list_values

    def get_rail(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.loc["直線":"曲線"]
        row_dict = row_feature.to_dict()
        return row_dict

    def get_rail_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "直線":"曲線"]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)
        return list_values

    def get_scene(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.loc["森林":"踏切"]
        row_no_feature = pd.Series({"scene特徴なし": row["scene特徴なし"]})
        row_feature = row_feature.append(row_no_feature)
        row_dict = row_feature.to_dict()
        return row_dict

    def get_scene_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "森林":"踏切"]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)
        return list_values

    def get_area(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.loc["北海道":"九州"]
        row_no_feature = pd.Series({"area特徴なし": row["area特徴なし"]})
        row_feature = row_feature.append(row_no_feature)
        row_dict = row_feature.to_dict()
        return row_dict

    def get_area_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "北海道":"九州"]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)
        return list_values

    def get_model(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.iloc[31:]
        row_dict = row_feature.to_dict()
        return row_dict

    def get_model_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        main_model = df_row["main_model"].values[0]
        df_row_feature = df_row.iloc[:, 31:]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)
        # main modelを戻り値の先頭に配置
        if main_model in list_values:
            index = list_values.index(main_model)
            if index > 0:
                list_values[0], list_values[index] = list_values[index], list_values[0]
        return list_values

    def create_df_feature(self):
        df_feature = self.df.loc[:, "正面":]
        df_feature = df_feature.drop("main_model", axis=1)
        return df_feature

    def get_relation_uids(self, pre_uid, uid, relation_type=None):
        pre_uid = int(pre_uid)
        uid = int(uid)
        if not self.exists(uid):
            return None

        type_similarity = None
        if self.exists(pre_uid):
            type_similarity = self.get_type_similarity(uid, pre_uid)

        df_feature = self.create_df_feature()

        # 特定の特徴量を強調させる
        relation_type = int(relation_type)
        relation_info = ""
        if relation_type is not None:
            rtype = Const.type_model()
            if relation_type == Const.type_model():
                current_value = self.get_model_values(uid)[0]
                relation_info = self.get_model_values(uid)
                df_feature.iloc[:, 31:] = df_feature.iloc[:, 31:] * 2
                df_feature[current_value] = df_feature[current_value] * 3
                df_feature.loc[:, "北海道":"九州"] = df_feature.loc[:, "北海道":"九州"] * 1.5
                df_feature.loc[:, "正面":"曲線"] = df_feature.loc[:, "正面":"曲線"] * 0.5
                df_feature.loc[:, "森林":"踏切"] = df_feature.loc[:, "森林":"踏切"] * 0.5
            elif relation_type == Const.type_scene():
                relation_info = self.get_scene_values(uid)
                current_value = self.get_model_values(uid)[0]
                df_feature.loc[:, "森林":"踏切"] = df_feature.loc[:, "森林":"踏切"] * 2
                df_feature.loc[:, "正面":"曲線"] = df_feature.loc[:, "正面":"曲線"] * 0.5
                df_feature.iloc[:, 31:] = df_feature.iloc[:, 31:] * 0.1
            elif relation_type == Const.type_angle():
                relation_info = self.get_angle_values(uid)
                current_value = self.get_model_values(uid)[0]
                df_feature.loc[:, "正面":"曲線"] = df_feature.loc[:, "正面":"曲線"] * 2
                df_feature.loc[:, "森林":"踏切"] = df_feature.loc[:, "森林":"踏切"] * 0.1
                df_feature.iloc[:, 31:] = df_feature.iloc[:, 31:] * 0.1
                df_feature.loc[:, "北海道":"九州"] = df_feature.loc[:, "北海道":"九州"] * 0.1
            elif relation_type == Const.type_area():
                relation_info = self.get_area_values(uid)
                current_value = self.get_model_values(uid)[0]
                df_feature.loc[:, "北海道":"九州"] = df_feature.loc[:, "北海道":"九州"] * 2
                df_feature.iloc[:, 31:] = df_feature.iloc[:, 31:] * 0.1

        return self.get_relation(df_feature, uid, relation_info, type_similarity)

    def get_relation_uids_from_history(self, uids):
        if uids is None:
            return None
        uid = int(uids[0])
        if not self.exists(uid):
            return None

        type_similarity = self.get_type_similarity_from_history(uids)
        print(type_similarity)

        df_feature = self.create_df_feature()

        # 特定の特徴量を強調させる
        current_value = self.get_model_values(uid)[0]
        relation_info = ""
        df_feature.iloc[:, 31:] = df_feature.iloc[:, 31:] * type_similarity[Const.type_model()]
        df_feature[current_value] = df_feature[current_value] * type_similarity[Const.type_model()]
        df_feature.loc[:, "正面":"曲線"] = df_feature.loc[:, "正面":"曲線"] * type_similarity[Const.type_angle()]
        df_feature.loc[:, "北海道":"九州"] = df_feature.loc[:, "北海道":"九州"] * type_similarity[Const.type_area()]
        df_feature.loc[:, "森林":"踏切"] = df_feature.loc[:, "森林":"踏切"] * type_similarity[Const.type_scene()]

        return self.get_relation(df_feature, uid, relation_info, type_similarity)

    def get_relation(self, df_feature, uid, relation_info, type_similarity):
        # 正規化(z-score)
        # df_feature = (df_feature - df_feature.mean()) / df_feature.std()
        # 正規化(min-max)
        f_max = df_feature.max().max()
        f_min = df_feature.min().min()
        df_feature = (df_feature - f_min) / (f_max - f_min)

        # 各写真ごとのコサイン類似度を計算
        array = df_feature.as_matrix()
        cs_array = cosine_similarity(array, array)

        # uidの配列をrow/column名にして"コサイン類似度"DataFrameを生成
        row_uid = self.df["ID"].as_matrix()
        df_cs = pd.DataFrame(cs_array, index=row_uid, columns=row_uid)

        # ターゲットの行indexを取得
        # (ターゲットをdrop、類似度を降順でソート)
        row_cs_target = df_cs.loc[uid].drop(uid)
        row_cs_target = row_cs_target.sort_values(ascending=False)
        result = {
            "info": relation_info,
            "uids": row_cs_target.index.values,
            "similarity": row_cs_target.values,
            "type_similarity": type_similarity,
        }
        return result



    def get_type_similarity_from_history(self, uids):
        type_similarity = self.create_type_dict(default_value=1)
        if (uids is None) or (len(uids) < 2):
            return type_similarity

        for i in range(len(uids) - 2, -1, -1):
            pre_uid = int(uids[i + 1])
            uid = int(uids[i])
            similarity = self.get_type_similarity(pre_uid, uid)
            for key in similarity.keys():
                type_similarity[key] = (type_similarity[key] + similarity[key]) / 2

        return type_similarity

    def get_type_similarity(self, uid1, uid2):
        angle1 = np.array(list(self.get_angle(uid1).values())).reshape(1, -1)
        angle2 = np.array(list(self.get_angle(uid2).values())).reshape(1, -1)
        cs_angle = cosine_similarity(angle1, angle2)[0][0]  # 1次元ベクトルはdeprecatedなので注意

        scene1 = np.array(list(self.get_scene(uid1).values())).reshape(1, -1)
        scene2 = np.array(list(self.get_scene(uid2).values())).reshape(1, -1)
        cs_scene = cosine_similarity(scene1, scene2)[0][0]

        model1 = np.array(list(self.get_model(uid1).values())).reshape(1, -1)
        model2 = np.array(list(self.get_model(uid2).values())).reshape(1, -1)
        cs_model = cosine_similarity(model1, model2)[0][0]

        area1 = np.array(list(self.get_area(uid1).values())).reshape(1, -1)
        area2 = np.array(list(self.get_area(uid2).values())).reshape(1, -1)
        cs_area = cosine_similarity(area1, area2)[0][0]

        result = self.create_type_dict()
        result[Const.type_angle()] =  cs_angle
        result[Const.type_scene()] =  cs_scene
        result[Const.type_area()] =  cs_area
        result[Const.type_model()] =  cs_model
        return result

    def create_type_dict(self, default_value=0):
        return {
            Const.type_angle(): default_value,
            Const.type_scene(): default_value,
            Const.type_area(): default_value,
            Const.type_model(): default_value,
        }

    def exists(self, uid):
        row = self.df[self.df["ID"] == uid].values
        if len(row) > 0:
            return True
        return False