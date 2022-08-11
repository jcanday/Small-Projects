# from urllib.request import parse_keqv_list


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
        
# head = Node(4)
# head.next = Node(3)
# head.next.next = Node(2)
# head.next.next.next = Node(1)

# def traverse(h):
#     temp = h
#     while temp != None:
#         print(temp.value)
#         temp = temp.next

# #iterative
# def reverseLL(head):
#     prev = None
#     while head:
#         next_node = head.next
#         head.next = prev
#         prev = head
#         head = next_node
        
#     return prev

# #recursive
# def reverseLLR(node, prev=None):
#     if not node:
#         return prev
#     next_node = node.next
#     node.next = prev
#     return reverseLLR(next_node, node)

# traverse(head)
# # traverse(reverseLL(head))
# traverse(reverseLLR(head))

# Starter Code to create 2 inputs for question
# You can test your function by passing linkedListOne and 
# LinkedListTwo as arguments
class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
    def insert(self, value):
        tail = self
        while tail.next:
            tail = tail.next
        tail.next = LinkedList(value)
        
# Creating first LL for test case        
linkedListOne = LinkedList(2)
linkedListOne.insert(4)
linkedListOne.insert(7)
linkedListOne.insert(1)
# Creating second LL input
linkedListTwo = LinkedList(9)
linkedListTwo.insert(4)
linkedListTwo.insert(5)

# def yourFunctionName(linkedList1, linkedList2):
#     str1 = ""
#     str2 = ""
#     l1 = linkedList1
#     l2 = linkedList2
#     while l1 != None:
#         str1 += str(l1.value)
#         l1 = l1.next
        
#     while l2 != None:
#         str2 += str(l2.value)
#         l2 = l2.next
        
#     int1 = int(str1[::-1])
#     int2 = int(str2[::-1])
#     sum = int1 + int2
#     sum_str = str(sum)[::-1]
    
#     linkedListThree = LinkedList(int(sum_str[0]))
    
#     for i in range(1,len(sum_str)):
#         linkedListThree.insert(int(sum_str[i]))
#     return linkedListThree.value

def yourFunctionName(linkedList1, linkedList2):
    sum2 = 0
    sum1 = 0
    l1 = linkedList1
    l2 = linkedList2
    m1 = 1
    m2 = 1
    
    while l1 != None:
        sum1 += l1.value * m1
        l1 = l1.next
        m1 *= 10
    while l2 != None:
        sum2 += l2.value * m2
        l2 = l2.next
        m2 *= 10
        
        
    total = sum1 + sum2
    reverse_total = 0
    
    while total > 0 :
        remain3 = total % 10
        reverse_total = (reverse_total * 10) + remain3
        total = total//10
    reverse_total_list = [int(i) for i in str(reverse_total)]
    linkedListThree = LinkedList(reverse_total_list[0])
    
    for i in range(1,len(reverse_total_list)):
        linkedListThree.insert(reverse_total_list[i])
    return linkedListThree.value

print(yourFunctionName(linkedListOne,linkedListTwo))


    
