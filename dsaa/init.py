class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(11)
b = Node(52)
c = Node(18)

a.next = b
b.next = c
b = None
C = None

print(a)
print(a.next)
print(a.next.next)

print(a.next.data)
print(a.next.next.data)