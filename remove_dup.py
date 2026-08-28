#remove duplicate integers from the list
def remove_duplicate(x):

	result_lst = []

	for i in x:

		if i not in result_lst:
			result_lst.append(i)

	return result_lst

a = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicate(a)) 