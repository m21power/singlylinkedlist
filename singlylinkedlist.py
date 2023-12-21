class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Insert_End(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=new_node
    def inserting_near(self,data,near):
        iter=self.head
        prev=None
        off=True
        new_node=Node(data)
        ch=input("where did you wanna put? R or L: ").upper()
        if ch=="L":
            if iter.data==near:
                a=iter
                self.head=new_node
                new_node.next=a
                return 

            while iter and off:
                if iter.data==near:
                    prev.next=new_node
                    new_node.next=iter
                    off=False
                    return
                prev=iter
                iter=iter.next
        elif ch=="R":
            while iter and off:
                if iter.data==near:
                    a=iter.next
                    iter.next=new_node
                    new_node.next=a
                iter=iter.next
        else:
            print('Oops! no such choice exist! ')
    def removing(self,data):
        iter=self.head
        prev=None
        off=True
        if iter.data==data:
            a=iter.next
            self.head=a
            return
        while iter and off:
            if iter.data==data:
                a=iter.next
                prev.next=a
                off=False
                return
            prev=iter
            iter=iter.next
        print("Oops! There is no such element in the list! ")
    def reversing(self):
        iter=self.head
        prev=None
        while iter:
            n=iter.next
            iter.next=prev
            prev=iter
            iter=n
        self.head=prev
    def printing(self):
        cur=self.head
        while cur:
            print(cur.data,end=' ')
            cur=cur.next
