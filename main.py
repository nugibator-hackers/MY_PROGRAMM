def is_interger(string: str) -> bool:
    """Проверить что подстрока это число."""
    flag: bool = True
    try:
        int(string)
    except ValueError:
        flag = False
    return flag

def repeater(string: str, count: int) -> str:
    """Повтрорить строку count раз."""
    return decoder(string) * (count - 1)


def decoder(string: str) -> str:
    """Декодировать строку."""
    result = str()
    value: int = 0 # Счетчик для умножения строки
    pos_right: int = 0
    for i in range(len(string)):
        if string[i] == '[':
            value_stack: int = 0 # Глубина скобок(нахождение парной скобки)
            for j in range(i + 1, len(string)): # Цикл для нахождения парной скобки
                if string[j] == '[': # Если встретили еще одну открывающую скобку глубина - 1 (внутреннего вырожения)
                    value_stack += 1
                if string[j] == ']':   # Если глубина равна нулю приравниваем правую позицию и выходим из цикла иначе глубина плюс один (вылезаем из внутреннего выражения)
                    if value_stack == 0:
                        pos_right = j
                        break
                    value_stack -= 1 
            result += repeater(string[i + 1: pos_right], value) # Повторить выражение value раз
            value = 0
        elif is_interger(string[i]): # проверка что символ это цифра
            value = value * 10 + int(string[i]) 
        elif string[i] != ']': # Проверка что это обычный символ
            result += string[i]
    return result
 
def main() -> None:
    string = str(input())
    print(decoder(string))
 
if __name__ == '__main__': 
    main()
