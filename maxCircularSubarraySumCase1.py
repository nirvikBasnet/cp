sum = 0
maxSum =0
a = [5,4,-2,-1,3,-12,4,6,7]
n = len(a)
#iterating and adding the sum of all the elements, if the sum is less than 0 the total sum becomes 0.
for i in range(n):
    sum += a[i]
    if sum < 0:
        sum = 0
    else:
        maxSum = max(sum,maxSum)

print(maxSum)
