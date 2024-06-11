import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Генерує набір унікальних випадкових чисел у заданому діапазоні.

    Аргументи:
    min_num (int): Мінімальне можливе число у наборі.
    max_num (int): Максимальне можливе число у наборі.
    quantity (int): Кількість чисел, які потрібно вибрати.

    Повертає:
    list: Список випадково вибраних, відсортованих чисел. Пустий список, якщо вхідні параметри некоректні.
    """
    # Перевірка коректності вхідних даних
    if not (isinstance(min_num, int) and isinstance(max_num, int) and isinstance(quantity, int)):
        return []
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity <= 0:
        return []

    # Генерація набору унікальних випадкових чисел
    numbers = random.sample(range(min_num, max_num + 1), min(quantity, max_num - min_num + 1))
    
    # Сортування та повернення результату
    return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)