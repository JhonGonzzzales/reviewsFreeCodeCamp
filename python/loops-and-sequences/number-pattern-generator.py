def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    else:
        numbers_pat = list(range(1, n + 1))
        result = " ".join(str(num) for num in numbers_pat)
    return result

print(number_pattern(4))
print(number_pattern(12))