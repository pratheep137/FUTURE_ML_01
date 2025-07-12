import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('data/processed_sales.csv')
train = df[df['date'] < '2024-12-01']
test = df[df['date'] >= '2024-12-01']

features = ['day_of_week', 'month', 'lag_7', 'rolling_mean_7']
X_train, y_train = train[features], train['sales']
X_test, y_test = test[features], test['sales']

model = XGBRegressor(n_estimators=100)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Save predictions
forecast = test[['date', 'store']].copy()
forecast['predicted_sales'] = predictions
forecast.to_csv('data/forecast_output.csv', index=False)

mae = mean_absolute_error(y_test, predictions)
print(f'Model MAE: {mae:.2f}')
