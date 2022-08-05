class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertatbeg(self, data):
        """Insert at beginning of linked list.."""
        node=Node(data,self.head)
        self.head=node

    def insertatend(self, data):
        """Insert at end of linked list"""
        if self.head==None:
            self.insertatbeg(data)
        else :
            itr=self.head
            while(itr.next):
                itr=itr.next
            node=Node(data,None)
            itr.next=node

    def insertvalues(self, data):
        """Enter a single Linked List"""
        self.head=None
        for i in data:
            self.insertatend(i)

    def getlength(self):
        """Get the length of the linked list"""
        count=0
        itr=self.head
        while(itr):
            itr=itr.next
            count+=1
        return count

    def insertatindex(self, data, index):
        """Insert at Index of the Linked List"""
        if(index<0 or index>=self.getlength()):
            raise Exception("Invalid Index")
        elif index==0:
            self.insertatbeg(data)
            return
        else:
            count=0
            itr=self.head
            while(itr):
                if(count==index-1):
                    node=Node(data,itr.next)
                    itr.next=node
                    break
                itr=itr.next
                count+=1

    def removeatindex(self, index):
        """Remove the data at a particular index"""
        if(index<0 or index>=self.getlength()):
            raise Exception("Invalid Index")
        elif index==0:
            self.head=self.head.next
            return
        else:
            count=0
            itr=self.head
            while(itr):
                if(count==index-1):
                    itr.next=itr.next.next
                    break
                itr=itr.next
                count+=1

    def firstoccrn(self, elmt):
        """Know the first occurence of a an element in a linked list"""
        itr=self.head
        count=0
        while(itr):
            if(itr.data==elmt):
                return count
            count+=1
            itr=itr.next

    def insert_after_value(self, data_after, data_to_insert):
        """Insert after a certain value in linked list"""
        self.insertatindex(data_to_insert,self.firstoccrn(data_after)+1)

    def remove_by_value(self, data):
        """Remove an element having a particular value"""
        self.removeatindex(self.firstoccrn(data))

    def print(self):
        """Print the entire LinkedLists"""
        itr=self.head
        l1=' '
        while(itr):
            l1+=str(itr.data)+'-->'
            itr=itr.next
        print(l1)


ll=LinkedList()
ll.insertatbeg(9)
ll.insertatbeg(10)
ll.insertatend(15)
l2=LinkedList()
l2.insertvalues([10,12,34,56,100])
l2.insert_after_value(34,45)
l2.print()
l2.remove_by_value(34)
l2.print()
ll.print()


