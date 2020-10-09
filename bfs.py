from collections import defaultdict
class Graph:
	def __init__(self,size):
		self.graph=defaultdict(list)
		self.visited_matrix=[False]*size
		self.connected_comp=0
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)
		self.visited_matrix[u]=False
		self.visited_matrix[v]=False
	def bfs(self,s):
		no_of_nodes=len(self.graph)
		#visited_matrix=no_of_nodes*[False]
		queue=[]
		queue.append(s)
		self.visited_matrix[s]=True
		while queue:
			s=queue.pop(0)
			print(s, end= "  ")
			#self.visited_matrix[s]=True
			for i in self.graph[s]:
				if self.visited_matrix[i]==False:
					queue.append(i)
					self.visited_matrix[i]=True
	def connected_component(self):
		#self.visited_matrix=len(self.graph)*[False]
		for i in range(len(self.visited_matrix)):
			if self.visited_matrix[i]==False:
				self.bfs(i)
				print("---------")
				self.connected_comp+=1





g = Graph(8) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(3, 4) 
g.addEdge(4, 5) 
g.addEdge(6, 7) 

  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
#g.bfs(2)
g.connected_component()
print("no of connected_component is "+ str(g.connected_comp))


