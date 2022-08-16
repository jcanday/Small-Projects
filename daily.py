# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# This is also the LeetCode question of the day here: https://leetcode.com/problems/first-unique-character-in-a-string/
def func(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
            
    for i in range(len(s)):
        if d[s[i]] <= 1:
            return i
        
    return -1 

print(func("loveleetcode"))