from __future__ import annotations


def max_revenue(prices: [int]) -> int:
    res = 0
    cur_s = 0

    for i in range(len(prices) - 1):
        if prices[i] <= prices[cur_s]:
            cur_s = i
            continue


        if prices[i] > prices[i + 1]:
            cur_sum = prices[i] - prices[cur_s]
            res += cur_sum
            cur_s = i

    if prices[len(prices) - 1] > prices[cur_s]:
        cur_sum = prices[len(prices) - 1] - prices[cur_s]
        res += cur_sum

    return res



def main():
    n = int(input())
    prices = [int(x) for x in input().split()]
    print(max_revenue(prices))


if __name__ == "__main__":
    main()
