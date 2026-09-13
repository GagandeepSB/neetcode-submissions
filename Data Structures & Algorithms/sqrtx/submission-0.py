class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0

        while l <= r:
            m = l + ((r - l) // 2) # Will prevent overflow
            
            # m**2 is how to square a number in python
            if m**2 == x:
                return m

            # Check if m^2 is greater than x, if so, then it cannot be the sqrt of x
            # So cut the search space in half
            elif m**2 > x:
                r = m - 1

            # If m^2 is less than x, then we cut our search space by moving the left ptr
            # When m^2 is less than x, then it is a candidate to be the sqrt(x)
            # This could be the result since we want the larget m^2 which is less than x
            else:
                l = m + 1
                result = m

        return result
            
        