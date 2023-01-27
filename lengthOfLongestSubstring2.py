def lengthOfLongestSubstring(s):
    maxsize = 1
    #basically, I want to do a double loop to cover all possibilities of the substr where left<right
    for right in range(len(s)+1):
        for left in range(right-1):
            if unique_letters(s[left:right]) and len(s[left:right])>maxsize:
                maxsize = len(s[left:right])
    return maxsize

def unique_letters(str):
    #I want to see if all letters in substr are unique
    if len(set(str))==len(str):
        return True
    else:
        return False

#or let's try the first one, a little more elegant
def lengthOfLongestSubstring(s):
    # I want a right and left pointer, iterate over s, if I find a letter already seen then reset left pointer to that letter
    start=0
    longest=0
    #dictionary of positions of letters
    seenbefore = {}
    for i, letter in enumerate(s):
        if letter in seenbefore and start<=seenbefore[letter]:
            #restart at index after letter that has been seen before
            start = seenbefore[letter]+1
        else:
            longest=max(longest, i-right+1)
        seenbefore[letter] = i
    return longest
