class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def createLL(self,n):
        i=0
        while i<n:
            val=int(input("enter data :"))
            new_node=Node(val)
            if self.head==None:
                self.head=new_node
            else:
                t=self.head
                while t.next!=None:
                    t=t.next
                t.next=new_node
            i=i+1
    def show(self,head):
        t=head
        print("list of nodes: ")
        s=0
        while t:
            print(t.val,end=" ")
            s=s+t.val
            t=t.next
        print("\nTotal",s)
    def split(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        second=slow
        prev.next=None
        print("\nFirst Linkedlist: ")
        self.show(self.head)
        print("\nSecond Linkedlist: ")
        self.show(second)
obj=linkedlist()
n=int(input("value of n: "))
obj.createLL(n)
obj.show(obj.head)
obj.split()
