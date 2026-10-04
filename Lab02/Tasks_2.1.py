#!/usr/bin/env python3

STANDARD_DELIMITED: str = ', '

if __name__ == '__main__':
    def main(strings):
        try:
            total_length = 0
            for s in strings:
                total_length += len(s)
            avg_length = total_length / len(strings)
            result = []
            for s in strings:
                if len(s) > avg_length:
                    result.append(s)
            return result
        except ZeroDivisionError:
            print("Список не должен быть пустым!")
            return []

    user_word = input(f'Введите слова, используя "{STANDARD_DELIMITED}"\n ')
    words = user_word.split(STANDARD_DELIMITED)
    print(main(words))
