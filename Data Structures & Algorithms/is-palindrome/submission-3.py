class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right= len(b)-1
        while left < right :
            if b[left]== b[right]:
                left +=1
                right -=1
            else:
                return False
        return True
        

        