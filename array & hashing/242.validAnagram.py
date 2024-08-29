# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 


s = "anagram"
t = "nagaram"
c=0
if len(s)==len(t):
  for i in s:
    if i in t:
      c+=1
      t = t.replace(i, '',1)
      print(t)
  if c==len(s):
    print(True)
  else:
    print(False)
else:
  print(False)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

