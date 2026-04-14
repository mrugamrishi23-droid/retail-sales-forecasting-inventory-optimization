from src.data_preprocessing import load_data, preprocess_data
from src.forecasting import forecast_sales
from src.inventory import calculate_inventory
from src.visualization import plot_forecast

# Load data
df = load_data("data/raw_sales.csv")

# Preprocess
df = preprocess_data(df)

# Forecast
forecast_df = forecast_sales(df)

# Inventory optimization
inventory_df = calculate_inventory(forecast_df)

# Save outputs
forecast_df.to_csv("outputs/forecasts.csv", index=False)
inventory_df.to_csv("outputs/inventory_plan.csv", index=False)

# Plot
plot_forecast(df, forecast_df)

print("Project executed successfully!")