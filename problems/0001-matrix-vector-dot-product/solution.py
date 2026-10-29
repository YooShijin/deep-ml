def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	n = len(a)
	m = len(a[0])
	if(len(b) != m):
		return -1

	ans = [0]*m
	for i in range(n):
		for j in range((m)):
			ans[i] += a[i][j]*b[j]
	
	return ans