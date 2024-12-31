from sklearn.preprocessing import MinMaxScaler

def cleaning(df, label_column_name):
  data = df.drop_duplicates()
  data = data.dropna()
  x = data.drop(columns=[label_column_name]).to_numpy()
  y = data[label_column_name].to_numpy()
  return x, y

def minmaxscaler(x):
  scaler = MinMaxScaler()
  scaler.fit(x)
  return scaler.transform(x), scaler