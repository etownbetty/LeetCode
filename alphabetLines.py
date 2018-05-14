
'''
We are to write the letters of a given string S, from left to right into lines. 
Each line has maximum width 100 units, and if writing a letter would cause the width of 
the line to exceed 100 units, it is written on the next line. We are given an array widths, 
an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ...,
and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, 
and what is the width used by the last such line? 
Return your answer as an integer list of length 2.
'''

def calcLines(widths, S):

	letters = 'abcdefghijklmnopqrstuvwxyz'
	assoc = {k:v for k,v in zip(letters, range(26))}

	n = 0
	lines = 1
	for i in S:
		curr = widths[assoc[i]]
		if n+curr>100:
			lines+=1
			n = curr
		else:
			n+=curr

	return [lines, n]