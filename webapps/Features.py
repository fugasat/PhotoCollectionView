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
        row_area = row.loc["正面":"遠い"]
        row_dict = row_area.to_dict()
        return row_dict

    def get_scene(self, uid):
        return self.df[uid]

    def get_area(self, uid):
        return self.df[uid]

    def get_model(self, uid):
        return self.df[uid]
