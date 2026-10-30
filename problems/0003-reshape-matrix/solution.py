import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m = len(a)
	n = len(a[0])
	mm = new_shape[0]
	nn = new_shape[1]
	if( m*n != mm*nn):
		return []

	reshaped_matrix = [[0]*nn for _ in range(mm)]
	for i in range(m):
		for j in range(n):
			sum = i*n + j
			reshaped_matrix[sum//nn][sum%nn] = a[i][j]
	return reshaped_matrix