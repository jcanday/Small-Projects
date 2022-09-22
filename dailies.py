# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

def func(h,n):
    if n not in h:
            return -1
    hPointer, nPointer, counter, hInitial = 0, 0, 0, 0
    nLength = len(n)
    while hInitial < len(h):
        if h[hPointer] == n[nPointer]:
            counter += 1
            if counter == nLength:
                return (hPointer - nLength)+1
            else:
                hPointer += 1
                nPointer += 1
        else:
            hPointer = hInitial + 1
            hInitial += 1
            nPointer = 0
            counter = 0
    # import re 
    # match = re.search(n, h)
    # if match:
    #     return match.span()[0]
    # return -1
            
print(func("sadbutsad","sad"))
    
