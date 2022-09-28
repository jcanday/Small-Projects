# # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# # Example 1:
# # Input: haystack = "sadbutsad", needle = "sad"
# # Output: 0
# # Explanation: "sad" occurs at index 0 and 6.
# # The first occurrence is at index 0, so we return 0.
# # Example 2:
# # Input: haystack = "leetcode", needle = "leeto"
# # Output: -1
# # Explanation: "leeto" did not occur in "leetcode", so we return -1.
# # Constraints:
# # 1 <= haystack.length, needle.length <= 104
# # haystack and needle consist of only lowercase English characters.

# # def func(h,n):
# #     if n not in h:
# #             return -1
# #     hPointer, nPointer, counter, hInitial = 0, 0, 0, 0
# #     nLength = len(n)
# #     while hInitial < len(h):
# #         if h[hPointer] == n[nPointer]:
# #             counter += 1
# #             if counter == nLength:
# #                 return (hPointer - nLength)+1
# #             else:
# #                 hPointer += 1
# #                 nPointer += 1
# #         else:
# #             hPointer = hInitial + 1
# #             hInitial += 1
# #             nPointer = 0
# #             counter = 0
# #     # import re 
# #     # match = re.search(n, h)
# #     # if match:
# #     #     return match.span()[0]
# #     # return -1
            
# # print(func("sadbutsad","sad"))
 
 
# ## How many increasing or decreasing numbers in up to 10 to the power of x 
# ## ie 123456 increasing, 654321 decreasing   

# ## [11,12,22,33,44,55,66,77,88,99,111,122,133,144,155..... 222...333...444...555..1111,] 

# ##increasing
# # Last Man Standing
# # A king gathers all the men in the kingdom who are to be put to death for their crimes, but because of his mercy, he will pardon one. He gathers the men into a circle and gives the sword to one man. The man kills the man to his left, and gives the sword to the man to the dead man's left. The last man alive is pardoned. 

# # With 5 men, the 3rd man holding the sword is the last man alive. 

# # Write a program that accepts a single parameter: a number N that represents the number of criminals to start with. The program should output the number of the last two men alive.

# # Example #1: myProgram 5

# # would output:

# # 5, 3

# # Example #2: myProgram 7

# # would output:

# # 3, 7


# # Requirements
# #   * If you choose a language where the code dictates the name of output (for example, Java classes), you must name your objects such that the resulting binary / machine code will be named "Criminal"
# #   * The provided answer must run / compile as is, with no modifications. This means that all external libraries that may need to be added / included / used should be present.
# #   * All parameters must be passed in as command line arguments, as shown in the example above.
# #   * The provided solution must not rely on user input.
# #   * All code must begin with a comment indicating the language.
# # #Python

# #circular linked list structure
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# #n = number of criminals       
# def last_man(n):
    
#     if n == 1: return [1]
#     if n == 2: return [1,2]
    
#     head = Node(1)
#     curr = head
    
    
#     #creating linked list
#     for i in range(2, n+1):
#         newNode = Node(i)
#         curr.next = newNode
#         curr = newNode
#     curr.next = head
    
    
#     #going through the circle and killing criminals
#     #making nextt criminal to the criminal left of the next criminal
#     #setting the current criminal to the next criminal after making it to the left of the next criminal
#     curr = head
#     res = []
#     while curr.next != curr:
#         res.append(curr.data)
#         curr.next = curr.next.next
#         curr = curr.next
        
#     #grabbing the last two criminals alive:
#     criminal1 = res.pop()
#     criminal2 = res.pop()
    
#     return [criminal2,criminal1]


# # The Towers of Hanoi
# # There is an old legend about a monastery, which contains three poles. One of them filled with 64 gold disks. The disks are of different sizes, and they are put on top of each other, according to their size, i.e. each disk on the pole is a little smaller than the one beneath it. The monks have to move this stack from one of the three poles to another one. But one rule has to be applied: a large disk can never be placed on top of a smaller one. 

# # The rules of the game are very simple, but the solution is not so obvious. The game "Towers of Hanoi" uses three poles. A number of disks is stacked in decreasing order from the bottom to the top of one pole, i.e. the largest disk at the bottom and the smallest one on top. The disks build a conical tower. 

# # The aim of the game is to move the tower of disks from one pole to another pole. 

# # The following rules have to be obeyed:
# # Only one disk may be moved at a time.
# # Only the most upper disk from one of the pole can be moved in a single move
# # It can be put on another pole, if this rod is empty or if the most upper disk of this pole is larger than the one which is moved.

# # Write a program, in any language with which you are comfortable, that outlines the steps requires to complete the Towers of Hanoi given N number of disks. Success will be judged by comparing the output to a standardized known solution. All solutions will be run in the command line with the following sort of command:

# # ./interpreter Hanoi.program 3

# # For example:

# # $ python Hanoi.py 3
# # moving disk 1 from pole 1 to pole 2
# # moving disk 2 from pole 1 to pole 3
# # moving disk 1 from pole 2 to pole 3
# # moving disk 3 from pole 1 to pole 2
# # moving disk 1 from pole 3 to pole 1
# # moving disk 2 from pole 3 to pole 2
# # moving disk 1 from pole 1 to pole 2
# # ... etc util all disk are on pole 3

# # Requirements
# #   * If you choose a language where the code dictates the name of output (for example, Java classes), you must name your objects such that the resulting binary / machine code will be named "Hanoi"
# #   * The provided answer must run / compile as is, with no modifications. This means that all external libraries that may need to be added / included / used should be present.
# #   * All parameters must be passed in as command line arguments, as shown in the example above.
# #   * The provided solution must not rely on user input.
# #   * All code must begin with a comment indicating the language.

# def hanoi(N, start = "pole 1", end = "pole 2", util = "pole3"):
    
#     if N == 1:
#         print(f"moving disk 1 from ${start} to ${end}")
#         return
#     hanoi(N-1, start, util, end)
#     print(f"moving disk ${n} from ${start} to ${end}")
#     hanoi(N-1,util,end,start)

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ithathlete.
# Example 1:
# Input: score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

def func(score):
    sortedScores = sorted(score, reverse=True)
    hashMap = {}
    for i in range(len(sortedScores)):
        if i == 0:
            hashMap[sortedScores[0]] = "Gold Medal"
        elif i == 1:
            hashMap[sortedScores[1]] = "Silver Medal"
        elif i == 2:
            hashMap[sortedScores[2]] = "Bronze Medal"
        else:
            hashMap[sortedScores[i]] = str(i + 1)
        
    return list(map(lambda x: hashMap[x], score))