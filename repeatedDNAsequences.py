# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
import collections

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        '''sliding window 10 long, find duplicates'''
        if len(s) < 10:
            return []
        ten_letters = [s[i:i+10] for i in range(len(s)-9)]
        '''find duplicates now'''
        dups = [k for k,v in collections.Counter(ten_letters).items() if v > 1]
        return dups
