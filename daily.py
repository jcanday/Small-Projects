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

a = ["c,a,r,d","c,a,r,-B,r,d"]
b = ["","-B,-B,-B"]

c = ["c,a,r,d","-B,-B,-B,c,a,r,-B,r,d"]
def backSpace(arr):
    def typeWord(words):
        out = []
        for char in words:
            if char != '-B' and char != "":
                out.append(char)
            else:
                if len(out):
                    out.pop()
        return ''.join(out)      
    word_1 = arr[0].split(",")
    word_2 = arr[1].split(",")
    return typeWord(word_1) == typeWord(word_2)
    
print(backSpace(c))
    
    
    