import numpy as np

def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]] | int:
    try:
        ans = np.matmul(a, b).tolist()
    except ValueError:
        ans = -1

    return ans