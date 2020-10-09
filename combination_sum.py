output_list=[]
def findcomb(start,num_list, num, count):
	
	if(num==0 and count==0 ):
		global output_list
		output_list.append(num_list[:])
		#print(output_list)
		return

	if num<0 or count<=0:
		num_list=set([])
		return
	for i in range(start,10):
		if(i<=num and count>0):
			num_list.append(i)
			findcomb(i,num_list,num-i,count-1)
			num_list.pop()


findcomb(1,[],10,3)
print(output_list)