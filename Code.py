class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        if '6' in num:
            num[num.index('6')] = '9'
        return int(''.join(num))
