# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[i]  is equal to the product of every number in the input array other than input[i].
# Note that you're expected to solve this problem without using division.
# MOST EFFICIENT SOLUTION: Time: O(n) | Space O(n)
# Case 1:
# Input: array = [5, 1, 4, 2]
# Output: [8, 40, 10, 20]
# Explained:
# 8 == 1*4*2
# 40 == 5*4*2
# 10 == 5*1*2
# 20 == 5*1*4
# Case 2:
# Input: array = [-5, 2, -4, 14, -6] 
# Output: [672, -1680, 840, -240, 560]

# def func(lst):
#     new_arr = []
#     for i in lst:
#         prod = 1
#         for j in lst:
#             if j != i:
#                 prod *= j
#         new_arr.append(prod)
        
#     return new_arr

# def func(lst):
#     left = 0
#     multiplier = 0
#     res = []
#     while left < len(lst):
#         prod = 1
#         if left != multiplier:
#             prod *= multiplier
#         multiplier += 1
#         if multiplier >= len(lst):
#             res.append(prod)
#             multiplier = 0
#             left += 1
            
#     return res

        
    

# print(func([-5, 2, -4, 14, -6] ))

# Write a function that takes in a non-empty string and returns its run-length encoding.
# Wikipedia: "run length encoding is a form of lossless data compression in which runs of data are stored as a singls data value and count, rather than as the original run." For this problem, a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".
# To make things more complicated, however, the input string can contain all sorts of special characters, including numbers. Since encoded data must be decodable, this means that we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (12 A's), can't be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". Thus, long runs (10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
# Optimal Time/Space will be revealed later on! I see some very small optimizations taking the "most efficient" prize today!
# Case 1:
# s = "AAAAAAAAAAAAABBCCCCDD"
# Output: "9A4A2B4C2D"
# Case 2:
# s = AAAAA11BBBBBBBBBBCCC"
# Ouput: "5A219B1B3C"

from collections import Counter
def runLength(s):
    newS = ""
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for x,y in d.items():
        if y > 9:
            while y > 9:
                newS += f'9{x}'
                y -= 9
        newS += f'{y}{x}'         
    return newS
    
    
print(runLength("AAAAA11BBBBBBBBBBCCC"))
         
        
    