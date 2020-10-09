""" All subset with distinct number"""
def all_subset(nums,index,curr_list,res):
	""" 
	print all subset recursive
	"""
	res.append(curr_list)
	for i in range(index,len(nums)):
		all_subset(nums,i+1,curr_list+[nums[i]],res)
all_subset(nums,0,[],[])

""" All Subset Iterative"""
all_subset=[[]]
for num in nums:
	all_subset+=[[num]+res for res in all_subset]
return all_subset

"""
Subset Sum with duplicate element, print distinct subset
"""
def all_subset_with_duplicate(nums):
	"""Iterative"""
	nums.sort()
	all_subset=[[]]
	last_len=0
	for i in range(lenn(nums)):
		if i==0 or a[i]!=a[i-1]:
			last_len=len(all_subset)
			all_subset+=[nums[i]+item for item in all_subset]
		else:
			val=last_len
			last_len=len(all_subset)
			all_subset+=[nums[i]+all_subset[j] for j in range(val,last_len) ]
	return all_subset
def all_subset_with_duplicate(nums):
	"""Recursive"""
	nums.sort()
	def helper(nums,index,curr_list,res):
		res.append(curr_list)
		for i in range(index,len(nums)):
			if i==index or a[i]!=a[i-1]:
				helper(nums,i+1,curr_list+[nums[i]],res)





