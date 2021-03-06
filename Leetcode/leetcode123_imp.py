# -*- coding:utf-8 -*-
# @Time      :2018/11/21 16:49
# @Author    :wanhaoran
# @FileName  :leetcode123_imp.py


"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。


参照leetcode188
"""

class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 时间复杂度O(kN^2) 空间复杂度O(kN)
        #
        # def maxProfit(k,prices):
        #     if not prices or len(prices) == 0:
        #         return 0
        #     dp= [[0] * len(prices) for i in range(k+1)]
        #
        #     for m in range(1,k+1):
        #         for i in range(1,len(prices)):
        #             dp[m][i] = prices[i]-prices[0]
        #             for j in range(1,i+1):
        #                 dp[m][i] = max(dp[m][i],prices[i]-prices[j]+dp[m-1][j-1])
        #             dp[m][i] = max(dp[m][i],dp[m][i-1])
        #     return dp[-1][-1]

        def maxProfit(k,prices):
            if not prices or len(prices)==0:
                return 0
            if k>= len(prices)//2:
                # res = 0
                # for i in range(1,len(prices)):
                #     res+=prices[i]-prices[i-1] if prices[i]-prices[i-1]>0 else 0
                # return res
                # 一种写法
                return sum([prices[i]-prices[i-1] if prices[i]>prices[i-1] else 0 for i in range(1,len(prices))])

            dp = [[0] * len(prices) for i in range(k+1)]
            tmp = [-prices[0]] * (k+1)
            for m in range(1,k+1):
                for i in range(1,len(prices)):
                    tmp[m]=max(tmp[m],dp[m-1][i-1]-prices[i])
                    dp[m][i] = max(tmp[m]+prices[i],dp[m][i-1])
            return dp[-1][-1]

        return maxProfit(2,prices)


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([1,2,3,4,5])
    print(result)