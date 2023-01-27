'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    #take out spaces, 
    s1 = s.lower()
    right = len(s)-1
    left = 0
    while left<right:
        if s1[left].isalnum() and s1[right].isalnum():
            if s1[left] == s1[right]:
                left+=1
                right-=1
            else:
                return False
        elif not s1[left].isalnum():
            left+=1
        elif not s1[right].isalnum():
            right-=1
    return True
                