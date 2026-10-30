import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    try:
        ans = np.matmul(a, b)
    except Exception as e:
        ans = -1
    return ans