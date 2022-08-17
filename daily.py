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

def func(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alph = "abcdefghijklmnopqrstuvwxyz"
    d = {}
    trans = []
    for i in range(len(alph)):
        d[alph[i]] = morse[i]
    for i in words:
        trans.append("".join(list(map(lambda x:d[x], i))))
        
    return len(list(set(trans)))

print(func(["gin","zen","gig","msg"]))
    