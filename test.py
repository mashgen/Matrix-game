import numpy as np

def find_saddle_points(A):
	B = []
	for i in range(A.shape[0]):
		min_r = np.min(A[i])
		ind_r = 0
		max_c = 0
		ind_c = 0
		for j in range(A.shape[1]):
			if (A[i][j] == min_r):
				min_r = A[i][j]
				ind_r = j
				for k in range(A.shape[0]):
					if (A[k][ind_r] >= max_c):
						max_c = A[k][ind_r]
						ind_c = k
				if (min_r == max_c): B.append(min_r)
	print('Saddle points are:', B)
	return B

'''
def check_dominant_rows(A):
	B = []
	for i in range(A.shape[0]-1):
		for j in range(i+1, A.shape[0]):
			if (all(np.greater_equal(A[i], A[j]))):
				if (B.count(j) == 0):
					B.append(j)
			elif (all(np.less_equal(A[i], A[j]))):
				if (B.count(i) == 0):
					B.append(i)
	print(B)	
	A = np.delete(A, (B), axis = 0)
	print(A)
	return A

def check_dominant_columns(A):
	B = []
	for i in range(A.shape[1]-1):
		for j in range(i+1, A.shape[1]):
			if (all(np.greater_equal(A[:,i], A[:,j]))):
				if (B.count(i) == 0):
					B.append(i)
			elif (all(np.less_equal(A[:,i], A[:,j]))):
				if (B.count(j) == 0):
					B.append(j)
	print(B)
	A = np.delete(A, (B), axis = 1)
	print(A)
	return A
'''

def canonical_form(A):
	I = np.eye(A.shape[0])
	Z = np.zeros(A.shape[0])
	I = np.vstack((I, Z))
	B = np.array([-1] * A.shape[1])
	A = np.vstack((A, B))
	A = np.hstack((A, I))
	O = np.ones((A.shape[0], 1))
	A = np.hstack((O, A))
	A[-1][0] = 0
	print('Канонический вид матрицы:\n', A, '\n')
	return A

def select_lead_column(A):
	min_el = A[-1][1]
	index = 1
	for i in range(2, A.shape[1]):
		if ((min_el >= A[-1][i]) and (A[-1][i] < 0)):
			min_el = A[-1][i]
			index = i
	print('Главный столбец с индексом', index)
	return index

def select_lead_row(A, col):
	for i in range(A.shape[0]):
		if (A[i][col] > 0):
			min_quo = A[i][0] / A[i][col]
			index = i
			break
	for i in range(1, A.shape[0]-1):
		if (A[i][col] == 0): continue
		if ((min_quo >= (A[i][0] / A[i][col])) and (A[i][col] > 0)):
			min_quo = A[i][0] / A[i][col]
			index = i
	print('Главная строка с индексом', index)
	return index
		
def check_solved(A):
	solved = True 
	for j in range(1, A.shape[1]):
		if (A[-1][j] < 0):
			solved = False
	return solved

def conversion(A, c, r):
	main_element = A[r][c]
	print('Главный элемент = ', main_element, '\n')
	for i in range(A.shape[1]):
		A[r][i] /= main_element
	for i in range(A.shape[0]):
		if (i != r):
			A[i] += (A[r] * A[i][c] * (-1))	
	print(A)

def nash_equilibrium(A):
	min_elem = A.min()
	if min_elem < 0:
		A += abs(min_elem) + 1
	if (find_saddle_points(A)):
		print('Здесь решение в чистых стратегиях')
	else:
		f = A.shape[0]
		A = canonical_form(A)
		while (check_solved(A) == False):
			column = select_lead_column(A)
			row = select_lead_row(A, column)
			conversion(A, column, row)
		get_strategies(A, f)

def get_strategies(A, f):
	P = []
	Q = []
	F = 1 / A[-1][0]
	for i in range(f+1, A.shape[1]):
		P.append(F * A[-1][i])
#       Исправить для Q		
	print('Цена игры равна = ', F)
#	print('Стратегии первого игрока:', Q)
	print('Стратегии второго игрока:', P)

'''
n = int(input())
m = int(input())
A = []

for i in range(n):
	row = input().split()
	if (len(row) != m):
		sys.exit()
	for i in range(len(row)):
		row[i] = int(row[i])

	A.append(row)

A = np.array(A)

A = np.array([[0, 2, 7],
	[12, 11, 1]])

A = np.array([[6, 5, 7],
	[10, 4, 7],
	[13, 10, 4],
	[7, 11, 5]])
'''

A = np.array([[4, 0, 6, 2, 2, 1],
	[3, 8, 4, 10, 4, 4],
	[1, 2, 6, 5, 0, 0],
	[6, 6, 4, 4, 10, 3],
	[10, 4, 6, 4, 0, 9],
	[10, 7, 0, 7, 9, 8]])

nash_equilibrium(A)
