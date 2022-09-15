def count_satisfied(cookies, cookies_amount, greediness, child_amount):
    satisfied = 0
    cookies_index = 0

    for child_greed in greediness:

        while (cookies_index < cookies_amount) and child_greed > cookies[cookies_index]:
            cookies_index += 1

        if cookies_index < cookies_amount:
            satisfied += 1
            cookies_index += 1
        else:
            return satisfied

    return satisfied

def main():
    child_amount = int(input())
    greediness = [int(x) for x in input().split()]
    cookies_amount = int(input())
    cookies =  [int(x) for x in input().split()]

    cookies.sort()
    greediness.sort()

    print(count_satisfied(cookies, cookies_amount, greediness, child_amount))



if __name__ == "__main__":
    main()
