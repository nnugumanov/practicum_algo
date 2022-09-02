"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""
def max_houses(house_amount,budget, houses):
    houses.sort()

    amount = 0
    index = 0
    while budget > 0 and index < house_amount:
        budget -= houses[index]
        index += 1
        amount += 1

        if budget < 0:
            return amount - 1

    return amount


def main():
    house_amount, budget = [int(x) for x in input().split()]

    houses = [int(x) for x in input().split()]

    print(max_houses(house_amount,budget, houses))


if __name__ == "__main__":
    main()
