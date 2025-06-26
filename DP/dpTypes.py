class Solution:
    def climbStairs(self, n: int) -> int:

# dp bottom up constant space
        if n == 1:
            return 1

        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            prev, cur = cur, prev + cur

        return cur

 # dp bottom up tabulation
    # if n == 1:
    #     return 1

    # if n == 2:
    #     return 2

    # dp=[0] * n
    # dp[0]=1
    # dp[1]=2

    # for i in range(2,n):
    #     dp[i]=dp[i-2] + dp[i-1]

    # return dp[n-1]

# dp momoization

    # memo = {1: 1, 2: 2}

    # def f(n):
    #     if n in memo:
    #         return memo[n]

    #     else:
    #         memo[n] = f(n - 2) + f(n - 1)

    #         return memo[n]

    # return f(n)

 # normal recursion

    # if n == 1:
    #     return 1

    # if n == 2:
    #     return 2

    # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

sol= Solution()
print(sol.climbStairs(5))  # Output: 8
