import os.path
from datetime import datetime
import numpy as np
import pandas as pd

from django.core.management.base import BaseCommand, CommandError
from webapps.models import Photo

class Command(BaseCommand):
    help = 'import data.csv into the models.'

    def handle(self, *args, **options):
        df = pd.read_csv('instagram_data_all.csv')
        root_path = os.getcwd()
        photo_root_path = "{0}/webapps/static/photos".format(root_path)

        for i, row in df.iterrows():
            photo = Photo()
            photo.uid = row["ID"]
            photo.regression_error = row["回帰誤差"]
            photo.date = datetime.strptime(row["日付"], '%Y-%m-%d')
            photo.favorites = row["f"]
            photo.comments = row["c"]

            photo.file_path = "{0}.jpg".format(str(photo.uid))
            if not os.path.isfile("{0}/{1}".format(photo_root_path, photo.file_path)):
                photo.file_path = "{0}.png".format(str(photo.uid))
                if not os.path.isfile("{0}/{1}".format(photo_root_path, photo.file_path)):
                    print("photo file not found.({0})".format(str(photo.uid)))
                    continue

        pass
