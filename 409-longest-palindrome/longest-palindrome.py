class Solution:
    def longestPalindrome(self, s):
        m = {}
        cnt = 0
        one = 0

        for ch in s:
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1

        for freq in m.values():
            if freq > 1:
                cnt += (freq // 2) * 2   
            if freq % 2 == 1:     
                one = 1

        return cnt + one