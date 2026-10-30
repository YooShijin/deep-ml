import  math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = []
	b= matrix[0][0] + matrix[1][1]
	a = 1
	c= matrix[0][0]*matrix[1][1] - matrix[0][1] * matrix[1][0]
	D = math.sqrt(b*b - 4*a*c)
	eigenvalues.append((b + D)/2*a)
	eigenvalues.append((b - D)/2*a)
	eigenvalues[0], eigenvalues[1] = max(eigenvalues), min(eigenvalues)
	return eigenvalues