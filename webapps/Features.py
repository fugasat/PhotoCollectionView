import os.path
import pandas as pd


class Features():
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def get(self, uid, key):
        row = self.df[self.df["ID"] == uid].iloc[0]
        values = row[key]
        return values

    def get_angle(self, uid):
        row = self.df[self.df["ID"] == uid].iloc[0]
        row_feature = row.loc["正面":"遠い"]
        row_dict = row_feature.to_dict()
        return row_dict

    def get_angle_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "正面":"遠い"]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)  # 値が"1"の列だけ抽出
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)  # np.append()は遅いので使わないこと
        if "高い" not in list_values:
            list_values.append("低い")
        if "遠い" not in list_values:
            list_values.append("近い")
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
        row_feature = row.loc["183":]
        row_dict = row_feature.to_dict()
        return row_dict

    def get_model_values(self, uid):
        df_row = self.df[self.df["ID"] == uid]
        df_row_feature = df_row.loc[:, "183":]
        df_row_feature_on = df_row_feature[df_row_feature > 0].dropna(axis=1)
        array_values = df_row_feature_on.columns.values
        list_values = list(array_values)
        return list_values
