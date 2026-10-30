def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	m = len(matrix)
	n = len((matrix[0]))

	if mode == "column":
		for i in range(n):
			temp = 0
			for j in range(m):
				temp += matrix[j][i]
			means.append(temp/m)
	else:
		for i in range(m):
			temp = 0
			for j in range(n):
				temp += matrix[i][j]
			means.append(temp/n)

	return means