from matplotlib.lines import lineStyles
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



df = pd.read_csv('./titanic/bitUSD_data.csv')

features = ["Open","Low","Volume_BTC","Volume_USD"]
target = "High"

df.rename(columns = {'Volume_(Currency)':'Volume_USD', 'Volume_(BTC)':'Volume_BTC'}, inplace = True)
df = df[features + [target]]
df.dropna(inplace=True) #결측값 제거
df.drop_duplicates(inplace=True) #중복행 제거

fcols = df.select_dtypes('float').columns
icols = df.select_dtypes('integer').columns

df[fcols] = df[fcols].apply(pd.to_numeric, downcast='float')
df[icols] = df[icols].apply(pd.to_numeric, downcast='integer')

x_train, x_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.3)
model = LinearRegression()
model.fit(x_train,y_train)
predictions = model.predict(x_test)

plt.scatter(y_test,predictions,color='blue')
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)],linestyle='--',color = 'green',linewidth=2)
plt.title('실제값 vs 예측값')
plt.xlabel('실제값')
plt.ylabel('예측값')
plt.show()


y_prediction = model.predict(x_test)
residuals = y_test - y_prediction

plt.scatter(y_prediction, residuals, color='blue')
plt.hlines(y=0, xmin=0, xmax=max(y_prediction), color='red')
plt.title('잔차 계산')
plt.xlabel('예측값')
plt.ylabel('잔차')
plt.show()
