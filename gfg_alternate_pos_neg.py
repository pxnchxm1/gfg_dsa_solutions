'''Alternate positive and negative numbers
......................................................'''

'''User function Template for python3
 Given an unsorted array Arr of N positive and negative numbers.
 Your task is to create an array of alternate positive and negative numbers without
changing the relative order of positive and negative numbers.
 Note: Array should start with a positive number and 0 (zero) should be considered a positive element.
 .....................................................................'''
class Solution:
    def rearrange(self,arr, n):
        # code here
        pos=[]
        neg=[]
        
        for i in arr:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        j=1
        for i in range(len(neg)):
            pos.insert(j,neg[i])
            j+=2
        for i in range(n):
            arr[i]=pos[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends