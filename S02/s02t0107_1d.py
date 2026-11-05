class Node:
#constructor
 def __init__(self,data=None):
      self.data = data
      self.next = None

#testear nuestra clase nodo
node_01 = Node("eggs")
node_02 = Node("ham")
node_03 = Node("bacon")

print(" 🔗 Nodes sin enlazar 🔗")
print(f"Node 01: D:{node_01.data} - N:{node_01.next}")
print(f"Node 02: D:{node_02.data} - N:{node_02.next}")
print(f"Node 03: D:{node_03.data} - N:{node_03.next}")

#enlazanado nodos
node_01.next= node_02
node_02.next= node_03

print(" 🔗 NODOS ENLAZADOS🔗")
print(f"Node 01: D:{node_01.data}- N:{node_01.next}")
print(f"Node 02: D:{node_02.data}- N:{node_02.next}")
print(f"Node 03: D:{node_03.data}- N:{node_03.next}")

#list traversal  (recorrido )
current = node_01
#for es cuando sabemos cuantas veces vamos a iterar
#while es cuando no sabemos cuantas veces vamos a iterar

while current:
   print(current.data, end="->")
   current = current.next
print("")