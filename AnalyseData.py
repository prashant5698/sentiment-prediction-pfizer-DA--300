import pandas as pd
from datetime import date

class Analyse:

    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        pass

    def getDataframe(self):
        self.df['acc_class'] = self.df['user_followers'].apply(lambda x:'weak'if x<=100 else ('norm' if 1000>=x>100 else 
                                                                       ('strong' if 10000>=x>1000
                                                                        else 'influencer')))
        self.df['total_engagement']=self.df['retweets']+self.df['favorites']

        self.df['med'] = self.df['text'].apply(lambda word:word.count('https://t.co/'))
        self.df['med'] = self.df['med'].apply(lambda x:'No Media' if x==0 else 'Media')

        self.df['today']=date.today()
        self.df['user_created']=pd.to_datetime(self.df['user_created']).dt.year
        self.df['today']=pd.to_datetime(self.df['today'])
        self.df['today']=self.df['today'].dt.year
        self.df['acc_age']= self.df['today']-self.df['user_created']


        return self.df
