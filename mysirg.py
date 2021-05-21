class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def viewList(self):
        if self.head is None:
            print("List is Empty")

        else:
            temp = self.head
            while(temp.next):
                print(temp.data, end=" ")
                temp = temp.next

            print(temp.data)

    def deleteFirst(self):
        if self.head is None:
            print("Linked List is empty")

        else:
            self.head = self.head.next

    def insertLast(self, value):
        newNode = node(value)

        if (self.head is None):
            self.head = newNode

        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode


mylist = linkedlist()
for i in range(5):
    insert = int(input())
    mylist.insertLast(insert)


mylist.viewList()
# mylist.deleteFirst()
# mylist.viewList()
