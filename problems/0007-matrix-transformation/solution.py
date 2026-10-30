import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	t = np.array(T)
	a = np.array(A)
	s = np.array(S)
	if(np.linalg.det(S) == 0 or np.linalg.det(T) == 0):
		return -1
	
	mat = np.matmul(np.linalg.inv(t),a)
	mat  = np.matmul(mat, s)
	return mat