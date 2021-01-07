class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		
	def __repr__(self):
		return self.data
		

class LinkedList:
	
	def __init__(self, nodes=None):
	
		self.head = None
		
		if nodes:
			node = Node(data=nodes.pop(0))
			self.head = node

			for ele in nodes:
				node.next = Node(data=ele)
				node = node.next		

	def __repr__(self):
		
		node = self.head
		nodes = []
		
		while node is not None:
			nodes.append(node.data)
			node = node.next
			
		nodes.append("None")
		return " -> ".join(nodes)
		
	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next
        
	def add_node_at_end(self, new_node):

		if not self.head:
			self.head = new_node
			return 
		
		for current_node in self:
			pass

		current_node.next = new_node

	def add_node_at_start(self, new_node):

		if not self.head:
			self.head = new_node
			return 
		new_node.next = self.head
		self.head = new_node

	def add_after(self, target_node, new_node):
	
		node = self.head
		
		while node is not None:
			
			if node.data == target_node:
				if node.next:
					next_node = node.next
					node.next = new_node
					new_node.next = next_node
					
			node = node.next
			
	def add_before(self, target_node, new_node):
	
		if not self.head:
			raise Exception("List is empty")
		
		if self.head.data == target_node:
			return self.add_node_at_start(new_node)
		
		node = self.head
		
		while node is not None:
			
			if node.next.data == target_node:
				_node = node.next 
				node.next = new_node
				new_node.next = _node
				return 
			node = node.next

	def remove_node(self, target_node):
	
		if not self.head:
			raise Exception("List is empty")
			
		if self.head.data == target_node:
			self.head = self.head.next
			return
		
		node = self.head
		
		while node is not None:
		
			if node.next.data == target_node:
				node.next = node.next.next
				return 
				
			node = node.next
				
if __name__ == "__main__":
	
	lList = LinkedList(["a","b","c","e","f","g"])
	print(lList)
	
	lList.add_node_at_end(Node(data="X"))
	print(lList)
	
	lList.add_node_at_start(Node(data="O"))
	print(lList)
	
	lList.add_after("f", Node(data="Z"))
	print(lList)
	
	lList.add_before("b", Node(data="R"))
	print(lList)
	
	lList.remove_node("c")
	print(lList)
	
	
	
	
	
	
	
	
	
	
	
	
	
