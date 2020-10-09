"""
This implement pascal triangle
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1

"""

#nCk=(n-1)C(k-1)+(n-1)C(k)
import time

def calculate_pascal_triangle(n_row):
	start_time=time.time()
	p=[1]
	row_size=1
	while (n_row-1):
		curr=[]
		i=row_size
		while i>=0:
			if i-1<0:
				curr.append(p[i])
			elif i>=len(p):
				curr.append(p[i-1])
			else:
				curr.append(p[i-1]+p[i])
			i-=1
		#p.append(curr)
		p=curr
		row_size+=1
		n_row-=1
	end_time=time.time()
	print("time_taken", (end_time-start_time))
	return p

def calculate_pascal_triangle_nth_row(n_row):
	start_time=time.time()
	row=[0 for i in range(n_row)]
	row[0]=1
	#print(row)
	for i in range(1,n_row):
		j=i
		while j>=0:
			if j>0:
				row[j]=row[j]+row[j-1]
			else:
				row[j]=1
			j-=1
	end_time=time.time()
	print("time_taken", (end_time-start_time))


#calculate_pascal_triangle(50000)
calculate_pascal_triangle_nth_row(50000)




