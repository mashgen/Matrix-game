import numpy as np

def find_saddle_points(A):
	B = []
	for i in range(A.shape[0]):
		min_r = np.min(A[i])
		ind_r = 0
		max_c = 0
		ind_c = 0
		for j in range(A.shape[1]):
			if (A[i][j] <= min_r):
				min_r = A[i][j]
				ind_r = j
				for k in range(A.shape[0]):
					if (A[k][ind_r] >= max_c):
						max_c = A[k][ind_r]
						ind_c = k
				if (min_r == max_c): B.append(min_r)
	print('Saddle points are:', B)
	return B

def check_dominant_rows(A):
	B = []
	count = 0
	for i in range(A.shape[0]):
		for j in range(A.shape[0]):
			if (i == j):
				continue
			else:
				for k in range(A.shape[1]):
					if (A[i][k] >= A[j][k]):
						count += 1
					else:
						break
				if (count == A.shape[1]):
					if (B.count(j) == 0):
						B.append(j)
				count = 0
	print(B)	
	A = np.delete(A, (B), axis = 0)
	return A

def check_dominant_columns(A):
	print('То же самое почти')

def canonical_form(A):
	I = np.eye(A.shape[0])
	Z = np.zeros(A.shape[0])
	I = np.vstack((I, Z))
	B = np.array([-1] * A.shape[1])
	A = np.vstack((A, B))
	A = np.hstack((A, I))
	O = np.ones((A.shape[0], 1))
	A = np.hstack((O, A))
	print(A)
	return A

def select_lead_column(A):
	min_el = A[-1][1]
	index = 1
	for i in range(2, A.shape[1]):
		if (min_el >= A[-1][i]):
			min_el = A[-1][i]
			index = i
	return index

def select_lead_row(A, col):
	min_quo = A[0][0]/A[0][col]
	index = 0
	print(min_quo)
	for i in range(1, A.shape[0]-1):
		if (min_quo > (A[i][0]/A[i][col])):
			min_quo = A[i][0]/A[i][col]
			index = i
	return index
		
def check_solved(A):
	solved = True 
	for j in range(1, A.shape[1]):
		if (A[-1][j] < 0):
			solved = False
	return solved

def conversion(A, c, r):
	print(A, 'c =', c, 'r =', r)
	main_element = A[r][c]
	for i in range(A.shape[1]):
		A[r][i] /= main_element
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			if i == r : continue
			A[i][j] -= A[r][j] * A[i][c]
	print(A)
	print('\n')


def nash_equilibrium(A):
	min_elem = A.min()
	if min_elem < 0:
		A += abs(min_elem) + 1
	if (find_saddle_points(A)):
		print('Здесь решение в чистых стратегиях')
	else:
#		A = check_dominant_rows(A)
#		A = check_dominant_columns(A)
		A = canonical_form(A)
		while (check_solved(A) == False):
			column = select_lead_column(A)
			row = select_lead_row(A, column)
			conversion(A, column, row)

	

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
nash_equilibrium(A)
