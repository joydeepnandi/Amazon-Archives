'''
Input: A[] = {1, 2, 3, 4, 5}, B[] = {5, 4, 3, 2, 1}, X = 3, Y = 3 
Output: 21 
1st, 2nd and 3rd orders are taken by waiter Y. 
4th and 5th orders are taken by waiter X.

Input: A[] = {2, 2, 2}, B[] = {3, 3, 3}, X = 3, Y = 3 
Output: 9 
'''
#recursive 2^n

i=0
def MaximumTipCalculator( i, A, B, X, Y):
	
	if i == len(A):
		return 0
	
	if X<=0:
		return (B[i] + MaximumTipCalculator(i+1, A, B, X, Y-1))

	if Y<=0:
		return (A[i] + MaximumTipCalculator(i+1, A, B, X-1, Y))
	
	else:
		return max( A[i] + MaximumTipCalculator(i+1, A, B, X-1, Y), B[i] + MaximumTipCalculator(i+1, A, B, X, Y-1))
		
#dp tc- O(n) | sc - O(n^2)

