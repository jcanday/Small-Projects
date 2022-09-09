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

# def runLength(s):
#     newS = []
#     pointer = 0
#     prev = s[0]
#     counter = 0
#     while pointer < len(s):
#         if s[pointer] == prev:
#             counter += 1
#             if counter == 9:
#                 newS.append(f'{counter}{prev}')
#                 counter = 0
#         else:
#             newS.append(f'{counter}{prev}')
#             prev = s[pointer]
#             counter = 1
#         if pointer == len(s) - 1:
#             newS.append(f'{counter}{prev}')
        
#         pointer += 1
            
#     return "".join(newS)
        
# print(runLength("AAAAA11BBBBBBBBBBCCC"))


# def trap(height):
#         left = 0
#         right = len(height) -1
#         res = 0
#         maxL = 0
#         maxR = 0
#         while left < right:
#             if height[left] > height[right]:
#                 if height[right] >= maxR:
#                     maxR = height[right]
#                 else:
#                     res += maxR - height[right]
#                 right -= 1
                 
#             else:
#                 if height[left] >= maxL:
#                     maxL = height[left]
#                 else:
#                     res += maxL - height[left]
#                 left += 1   
                
#         return res

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) 


# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the output array is equal to the product of every other number in the input array.
# In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].
# NOTE: You're expected to solve this problem without using division.
# Most Efficient: O(n) Time | O(n) Space
# Case 1:
# Input: arr = [5, 1, 4, 2]
# Output: [8, 40, 10, 20]
# Explained:
# // 8 is equal to 1 x 4 x 2
# // 40 is equal to 5 x 4 x 2
# // 10 is equal to 5 x 1 x 2
# // 20 is equal to 5 x 1 x 4
# Case 2:
# Input: arr = [1, 8, 6, 2, 4]
# Output: [384, 48, 64, 192, 96] 

def func(arr):
    length = len(arr)
    res = [1 for i in range(length)]
    temp = 1
    #left side multiply
    for i in range(length):
        res[i] = temp
        temp *= arr[i]
        
    temp = 1
    #right side multiply
    for i in range(length-1, -1, -1):
        res[i] *= temp
        temp *= arr[i]
        
    return res
print(func([5, 1, 4, 2]))
        
         
        
    