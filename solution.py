import pandas as pd
import numpy as np
from scipy.stats import wilcoxon


chat_id = 816831722  # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, p = wilcoxon(x, y)
    if p <= 0.07:
        return True
    else:
        return False
    
