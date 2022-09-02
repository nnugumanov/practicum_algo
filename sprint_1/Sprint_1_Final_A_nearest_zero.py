# ID посылки - 69681722

# From task description: "Номера домов (положительные числа) уникальны и не превосходят 10^9"
# We'll use 10^10 as INFINITY value. '-1' also could be used, but we'll had to add 'if' check
UNLIMITED_DISTANCE_VALUE = 10000000000


def main() -> None:
    result = []
    current_distance = UNLIMITED_DISTANCE_VALUE

    def refine_previous_marks(start_pos: int) -> None:
        """
        Update distance values backwards, while newly calculated distance is less than previously calculated
         distance.
        :param start_pos:
        :return:
        """
        corrected_value = 1

        for j in range(start_pos):
            if result[start_pos - j - 1] > corrected_value:
                result[start_pos - j - 1] = corrected_value
            else:
                return

            corrected_value += 1

    _ = int(input())
    street = [int(x) for x in input().split()]

    for i in range(len(street)):
        if street[i] == 0:
            current_distance = 0
            refine_previous_marks(i)

        result.append(current_distance)
        current_distance += 1

    print(*result)


if __name__ == "__main__":
    main()
