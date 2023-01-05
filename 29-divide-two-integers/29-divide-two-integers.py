class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count=0
        if dividend==0:
            return 0
        if dividend <0 and divisor < 0:
            sign=1
        elif dividend < 0 or divisor < 0:
            sign = -1
        else:
            sign =1
        dividend= abs(dividend)
        divisor= abs(divisor)
        count=0
        val=divisor
        while val <= dividend:
            i=1
            while val+val < dividend:
                i+=i
                val=val+val
            dividend -=val
            count+=i
            val=divisor
        if dividend < 0:
            count-=1
            
        count = count*sign
        if count > 2**31 -1:
            return 2**31-1
        elif count < -2**31:
            return -2**31
        else:
            return count
        