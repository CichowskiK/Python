
roman2arabic = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

def roman2int(roman):
    result = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman2arabic[char]

        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result



print("XVI= ", roman2int("XVI"))
print("MCDXLI=",roman2int("MCDXLI"))
