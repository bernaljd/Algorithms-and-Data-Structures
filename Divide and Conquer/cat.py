"""
Author: Juan David Bernal Maldonado
Date: 05/07/26
"""
# finds the exact number of cats and levels that can be stacked in a given height and width
def binarySearch(l, r, levels, H, W):
    ans = -1
    flag = True
    while((l <= r) and flag):
        mid = (l + r) // 2
        N = mid ** levels
        if N > W:
            r = mid - 1
        elif N < W:
            l = mid + 1
        else:
            # prove with the equivalent formula
            N = (mid + 1) ** levels
            if H == N:
                ans = mid
            flag = False
    return ans

# calculates the number of cats that are not working and the height of the stack of cats
def cat(H, W):
    k = 32
    flag = True
    while((k > 0) and flag):
        N = binarySearch(0, W, k, H, W)
        if N != -1:
            flag = False
        else:   
            k -= 1
    notWorking = ((N ** k) - 1) / (N - 1)
    catStack = H
    for i in range(1, k + 1):
        catStack += ((H/(N + 1) ** i)) * (N ** i)
    # Also a valid formula to calculate the height of the stack of cats:
    # catStack = H * (N + 1) - N * W
    print("%d %d" % (notWorking, catStack))

def main():
    H, W = map(int, input().split())
    while(H != 0 and W != 0):
        cat(H, W)
        H, W = map(int, input().split()) 
    
main()