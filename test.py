import numpy as np

def find_saddle_points(A):
	B = []
	for i in range(A.shape[0]):
		min_r = np.min(A[i])
		ind_r = 0
		max_c = 0
		for j in range(A.shape[1]):
			if (A[i][j] <= min_r):
				min_r = A[i][j]
				ind_r = j
				for k in range(A.shape[0]):
					if (A[k][ind_r] >= max_c):
						max_c = A[k][ind_r]
						ind_c = k
				if (min_r == max_c):
					B.append(min_r)
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

def check_dominant_colums(A):
	print('То же самое почти')


def change(A):
	I = np.eye(A.shape[0])
	Z = np.zeros(A.shape[0])
	I = np.vstack((I, Z))
	B = np.array([-1] * A.shape[1])
	A = np.vstack((A, B))
	A = np.hstack((A, I))
	print(A)


def nash_equilibrium(A):
	min_elem = A.min()
	if min_elem < 0:
		A += abs(min_elem) + 1
#	if (find_saddle_points(A)):
#		print('Здесь решение в чистых стратегиях')
	
	
#	A = check_dominant_rows(A)
#	A = check_dominant_colums(A)i
#	print(A)
	change(A)

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
