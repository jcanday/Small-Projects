# # Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# # This is also the LeetCode question of the day here: https://leetcode.com/problems/first-unique-character-in-a-string/
# def func(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else: 
#             d[i] = 1
            
#     for i in range(len(s)):
#         if d[s[i]] <= 1:
#             return i
        
#     return -1 

# print(func("loveleetcode"))



# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
# Example 1:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# Example 2:
# Input: words = ["a"]
# Output: 1
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.

# def func(words):
#     morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#     alph = "abcdefghijklmnopqrstuvwxyz"
#     d = {}
#     trans = []
#     for i in range(len(alph)):
#         d[alph[i]] = morse[i]
#     for i in words:
#         trans.append("".join(list(map(lambda x:d[x], i))))
        
#     return len(list(set(trans)))

# print(func(["gin","zen","gig","msg"]))

# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.
# Example 1:
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
# Example 2:
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.

# from collections import Counter
# def func(arr) -> int:
#     uni = list(set(arr))
#     if len(arr) == 2 or uni == [arr[0]]:
#         return 1
#     minimum = len(arr)
#     left = 0
#     right = 1
#     counter = Counter(arr)
    
#     while left < len(uni):
#         len_arr = len(arr)
#         for i in range(left,right):
#             len_arr -= counter[uni[i]]
#         minimum = min(minimum,len_arr)
#         right += 1
#         if right > len(uni):
#             left += 1
#             right = left + 1
            
#     return minimum
# print(func([3,3,3,3,5,5,5,2,2,7]))


# Simple question to start off the week!
# Given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# Added challenge: do this in O(1) space (without making another data structure)
# Example 1:
# s = "Hello World JavaScript!"
# output: 5
# explained: "Hello" and "World" both have 5 characters
# Example 2:
# s = "We built a nest and tested it."
# output: 1
# explained: "a" is the shortest word with a length of 1

# def func(s):
#     m = len(s)
#     currmin = 0
#     for i in range(len(s)):
#         if s[i] != " ":
#             currmin += 1
#         else:
#             m = min(currmin,m)
#             currmin = 0
            
#     return m

# print(func("We built a nest and tested it."))

# Given an array containing two strings. The strings contain keypresses of printable characters and "-B" separated by commas. "-B" is considered a backspace. Return true if the strings form the same word, return False if not.
# example input:
# [''c,a,r,d","c,a,r,-B,r,d"] #true

# a = ["c,a,r,d","c,a,r,-B,r,d"]
# b = ["","-B,-B,-B"]

# c = ["c,a,r,d","-B,-B,-B,c,a,r,-B,r,d"]
# def backSpace(arr):
#     def typeWord(words):
#         out = []
#         for char in words:
#             if char != '-B' and char != "":
#                 out.append(char)
#             else:
#                 if len(out):
#                     out.pop()
#         return ''.join(out)      
#     word_1 = arr[0].split(",")
#     word_2 = arr[1].split(",")
#     return typeWord(word_1) == typeWord(word_2)
    
# print(backSpace(c))

#  Given two ordered integer lists of any length and a limit, return an ordered list of the n smallest elements from the lists where n equals the limit. This should be accomplished in linear time and O(n) space where n is the limit, and is doable using no built-in functions.
# Notes:
# This is a problem with intentionally unclear wording - make sure you use the examples to help figure out what the problem is asking.
# This a problem that involves a lot of edge cases- make sure you consider all possible inputs and how they may affect your solution.
# Examples:
# 	list_a = [1, 3, 5, 7]
# 	list_b = [0, 6, 8]
# 	limit = 4

# 	Answer = [0, 1, 3, 5]
# ---
# 	List_a = [1, 1, 5, 5, 9]
# 	List_b =    
# 	Limit = 8

# 	Answer = [1, 1, 5, 5, 7, 9]

# def func(l1,l2,limit):
#     if limit <= 0:
#         return []
#     l3 = []
#     l = 0
#     r = 0
#     while len(l3) < limit:
#         if len(l1) <= l and len(l2) <= r:
#             return l3
#         if len(l1) > l and len(l2) > r:
#             if l1[l] < l2[r]:
#                 l3.append(l1[l])
#                 l += 1
#             else:
#                 l3.append(l2[r])
#                 r += 1
#         elif len(l1) <= l and len(l2) > r:
#             l3.append(l2[r])
#             r += 1
#         else:
#             l3.append(l1[l])
#             l += 1
#     return l3
    
# print(func([1, 3, 5, 7],[0, 6, 8],4))
        
# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
# 0


# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# def func(grid):
#     # edge case if there is no grid
#         if not grid:
#             return 0
#         # initialize island counter
#         count = 0
#         # loop over every value in the matrix
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 # if we find a 1, trigger a dfs to updated all touching 1's
#                 if grid[i][j] == '1':
#                     dfs(grid, i, j)
#                     # once that dfs is complete, count that as one island
#                     count += 1
#         return count
# # dfs helper function
# def dfs(grid, i, j):
#     # if we have stepped outside of the grid or run into a 0 or #, return
#     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
#         return
#     # if this is a 1, update to a placeholder so we don't count it again
#     grid[i][j] = '#'
#     # keep looking for more 1's in every direction!
#     dfs(grid, i+1, j)
#     dfs(grid, i-1, j)
#     dfs(grid, i, j+1)
#     dfs(grid, i, j-1)
                
# print(func([
#    ["1","1","1","1","0"],
#    ["1","1","0","1","0"],
#    ["1","1","0","0","0"],
#    ["0","0","0","0","0"]
#  ]))
# Given a non-empty array of integers nums, every element appears twiceexcept for one. Find that single one.
# BONUS: You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1


# add bits to single using XOR
# def func(nums):
#     unique = 0
#     for i in nums:
#         unique = unique ^ i
#     return unique

# print(func([2,2,1]))