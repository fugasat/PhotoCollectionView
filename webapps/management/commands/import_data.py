import pandas as pd
import numpy as np

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'import data.csv into the models.'

    def handle(self, *args, **options):
        df = pd.read_csv('instagram_data_all.csv')
        print('OK')
        pass
