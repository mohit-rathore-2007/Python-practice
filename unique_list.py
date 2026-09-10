# Write a Python program to find the common elements between two lists


def find_common_elements(list1, list2):
	common_elements = []

	for item in list1:
		if item in list2:
			common_elements.append(item)

	return common_elements

list1 = ["mohit", "rathod", "he", "is", "hello world"]
list2 = ["mohit", "rathod", "he", "hello python"]

result = find_common_elements(list1,list2)
print(result)
