import numpy as np
import pandas as pd

def calculate_inventory(forecast_df):
    lead_time = 2
    z = 1.65  # 95% service level
    
    demand_std = np.std(forecast_df['forecast_sales'])

    safety_stock = z * demand_std * np.sqrt(lead_time)

    forecast_df['reorder_point'] = forecast_df['forecast_sales'] * lead_time + safety_stock
    forecast_df['safety_stock'] = safety_stock

    return forecast_df