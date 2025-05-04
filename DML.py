import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def generate_data(n_samples=1000, ATE=0.5):
  # Generate synthetic data
  np.random.seed(42)


  # Treatment is a function of confounded variables
  # T = x1 + x2 + e
  X1 = np.random.normal(0, 1, n_samples)
  X2 = np.random.normal(0, 1, n_samples)
  e = np.random.normal(0, 0.5, n_samples)
  T = X1 + X2 + e

  # Outcome is a function of treatment and confounded variables: y = ATE*T + 2*x1 + 3*x2 + u
  u = np.random.normal(0, 1, n_samples)
  y = ATE*T + 2*X1 + 3*X2 + u

  # Create DataFrame
  data = pd.DataFrame({'X1': X1, 'X2': X2, 'T': T, 'y': y})

  return data


# Double Machine Learning
def double_ml(data, treatment, outcome, controls):
    """
    Estimates the causal effect using double machine learning.

    Args:
      treatment: Name of the treatment column.
      outcome: Name of the outcome column.
      controls: List of names of control columns.
    """

    X = data[controls].values
    T = data[treatment].values
    y = data[outcome].values

    # Split data into training and testing sets
    X_train, X_test, T_train, T_test, y_train, y_test = train_test_split(X, T, y, test_size=0.2, random_state=42)

    # First stage: predict treatment and outcome
    ml_model_t = RandomForestRegressor()
    ml_model_t.fit(X_train, T_train)
    T_hat = ml_model_t.predict(X_test)
    
    ml_model_y = RandomForestRegressor()
    ml_model_y.fit(X_train, y_train)
    y_hat = ml_model_y.predict(X_test)
    
    # Residuals
    T_res = T_test - T_hat
    y_res = y_test - y_hat

    # Second stage
    second_stage = LinearRegression()
    second_stage.fit(T_res.reshape(-1,1), y_res)
    ate = second_stage.coef_[0]

    return ate


# Estimate the causal effect
data = generate_data(n_samples=10000, ATE=0.5)
ate = double_ml(data, treatment='T', outcome='y', controls=['X1', 'X2'])

print(f"Estimated Average Treatment Effect (ATE): {ate}")