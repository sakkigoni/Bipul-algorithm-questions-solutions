#--------------------------- question 1 solution----------------------#
from collections import deque
def permute (arr,curnum,permutes):
    if len(arr) ==0:
        permutes.append(curnum)
    for i in range(len(arr)):
        x = arr.popleft()
        permute(arr,curnum*10 + x,permutes)
        arr.append(x)

def get_permutation(arr):
    nums = deque()
    for q in arr:
        nums.appendleft(q)
    perms=[]
    permute(nums,0,perms)
    print ("The permutation:",perms)
    return perms

if __name__ == "__main__":
    print("Enter numbers separated by space:")
    num_arr = list(map(int,input().split()))
    get_permutation(num_arr)
