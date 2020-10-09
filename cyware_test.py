"""Given two arrays A[] and B[], the task is to check if array B can be made equal to A by 
reversing the subarrays of B by any number of times.
Examples: 
    Input:  A[] =  {1 2 3}, B[] =  {3 1 2}
    Output: Yes
    Explanation: 
    Reverse subarrays in array B as shown below:
    Reverse subarray [3, 1], B becomes [1, 3, 2]
    Reverse subarray [3, 2], B becomes [1, 2, 3] = A
    There are multiple ways to convert B to A.
    Input:  A[] = {1 2 3}, B[] = {3 4 1 }
    Output: No"""
def check_equal(a,b):
	if len(a)!=len(b):
		return False
	a_dict={}
	b_dict={}
	for i in range(len(a)):
		if a[i] in a_dict:
			a_dict[a[i]]+=1
		else:
			a_dict[a[i]]=1
		if b[i] in b_dict:
			b_dict[b[i]]+=1
		else:
			b_dict[b[i]]=1
	for key in a_dict.keys():
		if key not in b_dict:
			return False
		if a_dict[key]!=b_dict[key]:
			return False
	return True


a=[1,2,3]
b=[2,3,1]
check_equal(a,b)