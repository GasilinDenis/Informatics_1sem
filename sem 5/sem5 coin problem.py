coins=[1,2,5]
sum=21
dp = [float('inf')] * (sum + 1)  #'inf' is a special value bigger then any other number
dp[0] = 0
for c in coins:
    for x in range(c, sum + 1):
        dp[x] = min(dp[x], dp[x - c] + 1)
         #If with current coin (c) it is possible to reach certain x with less number of coins than stated in dp[x], we write this min number in dp[x]
    print(dp)

print(dp[sum])
