def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = 0
    start = 0
    seen_before = {}
    for i, letter in enumerate(s):
        if (letter in seen_before) and start<=seen_before[letter]:
            #reset the start point to the last seen index+1, new character, with previously-seen character at the end
            start = seen_before[letter]+1
        else:
            #account for the 0-th start and find the length of the current string vs the longest
            longest = max(longest, i-start+1)
        seen_before[letter] = i
    return longest