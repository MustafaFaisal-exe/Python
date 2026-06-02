from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Life Expectancy Data.csv')

df.fillna(df.median(numeric_only=True), inplace=True)

df.plot(kind="scatter", x='Total expenditure', y='Life expectancy')
plt.show()

X = df[['Total expenditure']]
Y = df['Life expectancy']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)



y_pred = model.predict(x_test)

print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))
print("RMSE:", root_mean_squared_error(y_test, y_pred))
print("R²  :", r2_score(y_test, y_pred))