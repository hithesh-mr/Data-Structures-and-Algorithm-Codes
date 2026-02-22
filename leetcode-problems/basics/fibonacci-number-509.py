class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def solve(k):
            if k in memo:
                return memo[k]
            if k == 0:
                return 0
            if k == 1:
                return 1

            memo[k] = solve(k - 1) + solve(k - 2)
            return memo[k]

        return solve(n)