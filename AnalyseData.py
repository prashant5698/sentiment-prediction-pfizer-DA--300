import pandas as pd

class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.df.drop(columns=['id'], inplace=True)
        cols = self.df.columns[:-7]
        self.df.rename(columns=dict(zip(cols, [col[5:] for col in cols])), inplace = True)

    def getDataframe(self):
        return self.df
