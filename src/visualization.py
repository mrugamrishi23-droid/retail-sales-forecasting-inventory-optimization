import matplotlib.pyplot as plt

def plot_forecast(df, forecast_df):
    plt.plot(df['sales'], label='Actual')
    plt.plot(range(len(df), len(df)+len(forecast_df)), forecast_df['forecast_sales'], label='Forecast')
    plt.legend()
    plt.savefig("images/forecast.png")
    plt.show()