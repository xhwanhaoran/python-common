# -*- coding:utf-8 -*-
# @Time      :2018/12/14 13:45
# @Author    :wanhaoran
# @FileName  :leetcode338.py


"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        count = 1
        for i in range(1, num + 1):
            if i >= 2 * count:
                count *= 2
            res[i] = res[i - count]+1
        return res


if __name__ == '__main__':

    solution = Solution()
    result = solution.countBits(11)
    print(result)
