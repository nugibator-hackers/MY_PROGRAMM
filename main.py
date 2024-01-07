# 104349944
def instructions(string: str):
    stack = []
    result: str = ''
    number_in_string: int = 0
    for character in string:
        if character.isdigit():
            number_in_string = number_in_string*10 + int(character)

        elif character == '[':
            stack.append((number_in_string, result))
            number_in_string = 0
            result = ''
        elif character == ']':
            old_number_in_string, old_result = stack.pop()
            result = old_result + result * old_number_in_string
        else:
            result += character
    return result


if __name__ == '__main__':
    print(instructions(input()))
