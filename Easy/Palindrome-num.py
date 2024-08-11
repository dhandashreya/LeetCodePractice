# LeetCode Problem: Palindrome Number
# Problem Link: https://leetcode.com/problems/palindrome-number/description/

# Given an integer x, return true if x is a palindrome, and false otherwise.
# Solution 1
# Converts a number to a string. If the string length is 1, return True.
# If the string starts with "-" or ends with "0", return False.
# Compares characters from the beginning and end of the string.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = len(x)
        if l>1 and (x[0] == "-" or x[l-1] == "0"):
            return False
        elif l == 1:
            return True
        else:
                for i in range(0, l):
                    if x[i] == x[l-i-1]:
                        pass
                    else:
                        return False
        return True

# solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10 == 0):
            return False
        rev_num = 0

        while x>rev_num:
            rev_num = rev_num*10 + x%10
            x //= 10

        return x == rev_num or x == rev_num // 10
