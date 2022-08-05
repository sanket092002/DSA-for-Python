import logging
logging.basicConfig(filename='linkedlist.log', level=10, format='%(levelname)s %(name)s %(asctime)s %(message)s')

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insertatbeg(self, data):
        """Insert at beginning of linked list.."""
        try:
            node=Node(data,self.head)
            self.head=node
        except Exception as e:
            logging.error(e)


    def insertatend(self, data):
        """Insert at end of linked list"""
        try:
            if self.head==None:
                self.insertatbeg(data)
            else :
                itr=self.head
                while(itr.next):
                    itr=itr.next
                node=Node(data,None)
                itr.next=node
        except Exception as e:
            logging.error(e)

    def insertvalues(self, data):
        """Enter a single Linked List"""
        try:
            self.head=None
            for i in data:
                self.insertatend(i)
        except Exception as e:
            logging.error(e)

    def getlength(self):
        """Get the length of the linked list"""
        try:
            count=0
            itr=self.head
            while(itr):
                itr=itr.next
                count+=1
            return count
        except Exception as e:
            logging.error(e)

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
        try:
            itr=self.head
            count=0
            while(itr):
                if(itr.data==elmt):
                    return count
                count+=1
                itr=itr.next
        except Exception as e:
            logging.error(e)

    def insert_after_value(self, data_after, data_to_insert):
        """Insert after a certain value in linked list"""
        self.insertatindex(data_to_insert,self.firstoccrn(data_after)+1)

    def remove_by_value(self, data):
        """Remove an element having a particular value"""
        self.removeatindex(self.firstoccrn(data))

    def print(self):
        """Print the entire LinkedLists"""
        try:
            itr=self.head
            l1=' '
            while(itr):
                l1+=str(itr.data)+'-->'
                itr=itr.next
            logging.info(l1)
        except Exception as e:
            logging.error(e)


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


