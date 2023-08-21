#User function Template for python3
#Link: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        l = [(start[i],end[i]) for i in range(len(start))]
        l.sort(key = lambda x:x[1])
        ans = 1
        end = l[0][1]
        for i in range(1,len(start)):
            if l[i][0]>end:
                ans+=1
                end = l[i][1]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends