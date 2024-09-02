class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        found_word = False

        for i in reversed(s):
            if i != ' ':  # skip trailing spaces
                c += 1
                found_word = True
            elif found_word:  # break if a space is found after the last word starts
                break
        return c
    

