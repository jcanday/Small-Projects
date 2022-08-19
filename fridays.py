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

def func(lst):
    left = 0
    multiplier = 0
    res = []
    while left < len(lst):
        prod = 1
        if left != multiplier:
            prod *= multiplier
        multiplier += 1
        if multiplier >= len(lst):
            res.append(prod)
            multiplier = 0
            left += 1
            
    return res

        
    

print(func([-5, 2, -4, 14, -6] ))        
        
    