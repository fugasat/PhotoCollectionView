import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand, CommandError

"""
    usage: python manage.py convert_data
"""
class Command(BaseCommand):
    help = 'import data.csv into the models.'

    @staticmethod
    def read_csv():
        df = pd.read_csv("instagram_data.csv")

        # 不要な列を削除
        # df = df.drop("低い", axis=1)
        # df = df.drop("近い", axis=1)

        # nanを0に変換
        df.ix[:, "f":"JR"] = df.ix[:, "f":"JR"].fillna(0)

        # 日付文字列をdatetimeに変換
        df["日付"] = pd.to_datetime(df["日付"])

        # 登録された車両形式を抽出
        type_df = df.iloc[:, 27:33].fillna("0")  # 17〜23列を取得
        type_array = type_df.as_matrix().flatten()  # 1次配列に変換
        type_array = type_array.astype('str')  # 文字列に変換
        type_array = np.unique(type_array)  # 重複値を除外
        type_array = np.sort(type_array)  # ソート
        type_array = np.delete(type_array, 0)
        type_dic = {}
        for item in type_array:
            type_dic[item] = []

        no_feature = []
        no_area = []
        main_model = []
        for i, row in df.iterrows():
            # 風景の特徴が無いデータを「特徴なし」とする
            feature_count = row["森林":"踏切"].sum()
            if feature_count > 0:
                feature_count = 0
            else:
                feature_count = 1
            no_feature.append(feature_count)

            # 地域の特徴が無いデータを「特徴なし」とする
            area_count = row["北海道":"九州"].sum()
            if area_count > 0:
                area_count = 0
            else:
                area_count = 1
            no_area.append(area_count)

            # 特定の車両が存在するかどうかチェック
            types = row[27:33].astype('str')
            first_model = row[27]  # 最初に指定された車両をメインとする
            for item in type_array:
                exists = item in types.as_matrix()
                array = type_dic[item]
                array.append(int(exists))
                type_dic[item] = array

            # 先頭の車両データをメインの車両とする
            main_model.append(first_model)

        # 車両名を格納する列を削除
        df = df.iloc[:, :27]

        # 特徴が無いデータのカラムを追加
        df["scene特徴なし"] = no_feature
        df["area特徴なし"] = no_area
        df["main_model"] = main_model

        # 特定の車両が存在するかどうか表すカラムを追加
        for key, value in type_dic.items():
            df[key] = value

        return df

    @staticmethod
    def linalg(data):
        x = data["日付"]
        x = np.array([[v.timestamp(), 1] for v in x])
        y = data["f"]
        m, c = np.linalg.lstsq(x, y)[0]
        return m, c

    def handle(self, *args, **options):
        data = self.read_csv()

        #
        # いいねの数を正規化する
        #

        # (x軸)日付を整数に変換
        x = data["日付"]
        x = np.array([v.timestamp() for v in x])

        # (y軸)いいねの数を取得
        y = data["f"]

        # 回帰直線を取得
        m, c = self.linalg(data)
        y_lr = m * x + c

        # 回帰直線といいね数の差分を取得する
        # (回帰直線が水平になるように(y軸)いいね数を調整する)
        y_lr_e = y - y_lr  # (m * x + c)

        # 回帰誤差を２番目の列に挿入する
        data["回帰誤差"] = y_lr_e
        columns = data.columns.values
        columns = np.delete(columns, np.where(columns == "回帰誤差"))
        columns = np.insert(columns, 1, "回帰誤差")
        data = data.ix[:, columns]

        # IDでソートしてCSVに出力
        all = data.sort_values(by="ID", ascending=True)
        all.to_csv("instagram_data_all.csv", index=False)

        pass
