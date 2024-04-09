def f(x, k):
    #if mid element is less than k, we need to fill remaining with 1s
    if x <= k:
        return (x+1)*x//2 + (k - x)
    #if mid is greater than k then we need to do 1 + ... + mid - 1 + ... + k
    else:
        return ((x+1)*x//2) - ((x - k + 1)*(x-k)//2)
        # return (x + (x - k + 1)) * k // 2
        

def solution(n, m, k):
    if m < n:
        return -1

    left, right = m//n, m
    while left <= right:
        mid = (left + right) // 2
        #were seeing for either sides 
        #subtracting k because considered twice
        if f(mid, k) + f(mid, n - k + 1) - mid <= m:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

print("Output: ",solution(5, 11, 5))
print("Output: ",solution(5, 11, 3))
print("\n\n\n\n")
print("Output: ",solution(5, 15, 4))
print("Output: ",solution(5, 10, 3))