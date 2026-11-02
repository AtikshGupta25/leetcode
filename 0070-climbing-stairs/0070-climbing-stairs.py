class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        one_step_back = 2 
        two_step_back = 1 
        for _ in range(3, n + 1):
            current_ways = one_step_back + two_step_back

            two_step_back = one_step_back
            one_step_back = current_ways
        return one_step_back