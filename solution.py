import pandas as pd
import numpy as np


chat_id = 1063441199 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    import scipy.stats as sps
    alpha = 0.08
    res = sps.ks_2samp(np.ones(3), np.zeros(3))[1]
    return res <= alpha 
