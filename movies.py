import pandas as pd
df= pd.read_csv('movies.csv')
def get_title_from_index(index):
      return df.loc[index, "original_title"]
def get_rating_from_index(index):
  return df.loc[index, "original_title"],df.loc[index, "reviews_from_users"]

def get_index_from_title(original_title):
  return df.loc[df.original_title == original_title].index[0]
