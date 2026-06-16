class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for i in s:
            if i.isalnum():
                strs+= i.lower()
        return strs==strs[::-1]   