# palindrome
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
    def palindrome(self,head):
        if head is None:
            return True
        # split into two parts
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # reversing second part
        prev=None
        curr=slow*
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        # check for palindrome
        first=head
        second=prev*
        while second:
            if first.val is second.val:
                return False
            first=first.next
            second=second.next
        return True
obj=linkedlist()
n=int(input("value of n: "))
obj.createLL(n)
obj.show(obj.head)
obj.head=obj.palindrome(obj.head)
print("\n palindrome or not: ")
obj.show(obj.head)
