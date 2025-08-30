def perfect_number():
    number_list = [i for i in range(1001)]
    perfect_number = []

    for num in number_list:
        if num == 0:
            continue

        divisors = [i for i in range(1, num) if num % i == 0]
        # print(f"divisors: {divisors}  -- num: {num}")
        if num == sum(divisors):
            perfect_number.append(num)

    return perfect_number


if __name__ == "__main__":
    result = perfect_number()
   # print(result)
    print("Perfect numbers:", " ".join(map(str, result)))
