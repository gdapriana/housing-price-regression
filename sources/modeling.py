from sklearn.linear_model import LinearRegression

def regression(x, y):
  model = LinearRegression()
  model.fit(x, y)
  return model