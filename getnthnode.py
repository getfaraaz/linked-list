class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    
 
    def push(self, new_data):  # make new node and add
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
 
    
    def search(self,x):
        position = 1
        p = self.head
        while p is not None:
            if p.data == x:
                print(x, 'is at the position', position)
                return True
            position += 1
            p = p.next
        else:
            print(x,'Not found in list')
            return False



 
 
# Driver Code
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)
    # llist.getNth(llist,int(input()))
    # Enter the node position here
    # first argument is instance of LinkedList
 
    llist.search(4)
  

    