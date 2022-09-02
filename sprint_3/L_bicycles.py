def main():

    def binary_search(value, left, right):
        if left > right:
            return -1

        middle = left + (right - left) // 2
        if value <= nums[middle]:
            if middle == right:
                return middle + 1
            return binary_search(value, left, middle)
        else:
            return binary_search(value, middle + 1, right)

    _ = int(input())
    nums = [int(x) for x in input().split()]
    cost = int(input())

    day_for_one_bicycle = binary_search(cost, 0, len(nums) - 1)
    day_for_two_bicycles = binary_search(cost*2, 0, len(nums) - 1)

    print(day_for_one_bicycle, day_for_two_bicycles)


if __name__ == "__main__":
    main()
