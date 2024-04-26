def print_multiplication_table(n: int) -> None:
    """
    Функция для вывода таблицы умножения до числа n включительно.
    """
    # Печать заголовка таблицы
    print("Таблица умножения до", n, ":\n")

    # Печать верхней строки с номерами столбцов
    print("   ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (n * 5 + 3))

    # Печать содержимого таблицы
    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()


if __name__ == "__main__":
    number = 5
    print_multiplication_table(number)
    number = 7
    print_multiplication_table(number)
    number = 10
    print_multiplication_table(number)
