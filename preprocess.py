import pandas as pd

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path, parse_dates=['date'])
    df.sort_values('date', inplace=True)
    
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['lag_7'] = df['sales'].shift(7)
    df['rolling_mean_7'] = df['sales'].shift(1).rolling(7).mean()
    
    df.dropna(inplace=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess('data/raw_sales.csv', 'data/processed_sales.csv')
