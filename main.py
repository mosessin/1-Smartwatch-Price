# Importing libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Loading dataset
df = pd.read_csv("smartwatches_dataset.csv")

# Data preprocessing
scaler = StandardScaler()
df = df.drop(columns=["name", "price_category", "savings_amount", "rating", "num_reviews", "has_reviews", "scraped_date", "dataset_version"])
df = pd.get_dummies(df, columns=["brand", "category"], drop_first=True)
X = df.drop("current_price", axis=1)
y = df["current_price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Building models
LRg = LinearRegression()
Rdg = Ridge(alpha=1.0)
Las = Lasso(alpha=1.0, max_iter=100)
model = LRg         # Choose the model here

# Applying models
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Printing results
coef = pd.DataFrame({"Feature": X.columns, "Coefficient": model.coef_})
mse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"RMSE = {mse:.3f}")
print(f"R² score = {r2 * 100:.3f}%")
print(coef[["Feature", "Coefficient"]].round(3))        # For printing coefficient values
