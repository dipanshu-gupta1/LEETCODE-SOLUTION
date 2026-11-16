class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while (len(s)>k) :
            next_chunc = []

            for i in range(0,len(s),k):
                chunck = s[i : i+k]
                digit_sum = sum(int(digit) for digit in chunck)
                next_chunc.append(str(digit_sum))
            s = "".join(next_chunc)
        return s 