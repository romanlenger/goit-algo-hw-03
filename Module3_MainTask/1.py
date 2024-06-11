from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Розраховує кількість днів між заданою датою та поточною датою

    Аргументи:
    date (str): Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
    Повертає:
    int: Кількість днів між заданою датою та поточною датою. Результат може бути від'ємним, якщо задана дата пізніша за поточну

    ValueError: Виникає, якщо неправильний формат вхідних даних
    """
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date_object = datetime.strptime(date, '%Y-%m-%d').date()

        current_date = datetime.today().date()
        difference = current_date - date_object

        return difference.days
    
    except ValueError:
        raise ValueError("Неправильний формат вхідних даних. Очікується рядок у форматі 'РРРР-ММ-ДД'.")


print(get_days_from_today('2020.01.10'))