import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Create simple sales data
months = list(range(1, 13))
sales = [100, 120, 130, 150, 160, 180, 200, 190, 170, 160, 140, 130]
advertising = [50, 60, 65, 75, 80, 90, 100, 95, 85, 80, 70, 65]

sales_df = pd.DataFrame({
    'month': months,
    'sales': sales,
    'advertising': advertising
})

print("=== SALES FORECASTING ===")
print("\nSales Data:")
print(sales_df)

# Prepare data for regression
X = sales_df[['month', 'advertising']]
y = sales_df['sales']

# Train model
model = LinearRegression()
model.fit(X, y)

print(f"\nModel Coefficients:")
print(f"Month coefficient: {model.coef_[0]:.2f}")
print(f"Advertising coefficient: {model.coef_[1]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Make predictions
predictions = model.predict(X)

# Future prediction
future_month = 13
future_advertising = 100
future_prediction = model.predict([[future_month, future_advertising]])

print(f"\nPredicted sales for month {future_month}: ${future_prediction[0]:.2f}")

# Simple plots
plt.figure(figsize=(12, 5))

# Plot 1: Sales trend
plt.subplot(1, 2, 1)
plt.plot(sales_df['month'], sales_df['sales'], 'bo-', label='Actual Sales', linewidth=2)
plt.plot(sales_df['month'], predictions, 'ro--', label='Predicted Sales', linewidth=2)
plt.axvline(x=future_month, color='green', linestyle=':', label='Future Prediction')
plt.scatter([future_month], future_prediction, color='green', s=100, zorder=5)
plt.title('Sales Forecasting')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Advertising vs Sales
plt.subplot(1, 2, 2)
plt.scatter(sales_df['advertising'], sales_df['sales'], color='purple', s=100)
plt.title('Advertising vs Sales')
plt.xlabel('Advertising Budget')
plt.ylabel('Sales')

# Add trend line
z = np.polyfit(sales_df['advertising'], sales_df['sales'], 1)
p = np.poly1d(z)
plt.plot(sales_df['advertising'], p(sales_df['advertising']), "r--", alpha=0.8)

plt.tight_layout()
plt.show()

# Simple insights
print("\nBusiness Insights:")
print(f"- Sales generally increase over time (month coefficient: +{model.coef_[0]:.2f})")
print(f"- Every $1 in advertising generates ${model.coef_[1]:.2f} in sales")
print(f"- Predicted next month sales: ${future_prediction[0]:.2f}")

