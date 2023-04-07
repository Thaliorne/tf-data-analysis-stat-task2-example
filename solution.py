import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 259636079 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    b = np.max(x)
    se = (b - 0.095) / norm.ppf(1 - alpha/2)
    left = max(0.095, b - se*norm.ppf(1 - alpha/2))
    right = b + se*norm.ppf(1 - alpha/2)
    return (left, right)
