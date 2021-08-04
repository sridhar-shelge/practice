class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if(self.root==None):
            self.root=Node(data)
        else:
            curr=self.root
            while(curr.next!=None):
                curr=curr.next
            curr.next=Node(data)
    def display(self,root):
        curr=root
        if(curr==None):
            print('Empty')
        else:
            while(curr!=None):
                print(curr.data,end=" ")
                curr=curr.next

    def merge_sorted_lists(self,root1,root2):
        if(root1==None):
            return root2
        if(root2==None):
            return root1
        else:
            if(root1.data<root2.data):
                head=root1
                ptr1=root1
                ptr2=root2
            else:
                head=root2
                ptr1=root2
                ptr2=root1
            while(ptr1.next!=None or ptr2==None):
                if(ptr1.next.data<ptr2.data):
                    ptr1=ptr1.next
                else:
                    temp1=ptr1.next
                    temp2=ptr2.next
                    ptr1.next=ptr2
                    ptr2.next=temp1
                    ptr2=temp2
                    ptr1=ptr1.next
            if(ptr2!=None):
                ptr1.next=ptr2

            return head
    
        

list1=SLL()
list2=SLL()
#number of elements in each Linked List and data inserted
for i in range(int(input('enter no. of elements in list1'))):
    data=int(input())
    list1.insert(data)
for i in range(int(input('enter no. of elements in list2'))):
    data=int(input())
    list2.insert(data)
list1.display(list1.root)
print()
list2.display(list2.root)
list3=SLL()
list3.root=list3.merge_sorted_lists(list1.root,list2.root)
print()
list3.display(list3.root)

