from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_sales(df):
    sales = df['sales']
    
    model = ARIMA(sales, order=(2,1,1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=7)

    forecast_df = pd.DataFrame({
        'forecast_sales': forecast
    })

    return forecast_df