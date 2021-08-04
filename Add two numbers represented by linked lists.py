#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        len1=0
        len1=0
        temp=first
        l1=''
        l2=''
        while(temp!=None):
            l1+=str(temp.data)
            len1+=1
            temp=temp.next
        len2=0
        temp=second
        while(temp!=None):
            l2+=str(temp.data)
            len2+=1
            temp=temp.next
        
        total=str(int(l1)+int(l2))
        if(len1>len2):
            temp=first
            i=0
            prev=temp
            while(temp!=None):
                prev=temp
                temp.data=total[i]
                temp=temp.next
                i+=1
            if(i<len(total)):
                prev.next=Node(total[i])
            #print(first.data)
            return first
        else:
            temp=second
            i=0
            prev=temp
            while(temp!=None):
                prev=temp
                temp.data=total[i]
                temp=temp.next
                i+=1
            if(i<len(total)):
                prev.next=Node(total[i])
            return second
            
            
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    #print('hello')
    while(n!=None):
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
