def calculate_positive_average(numbers):
    """
    Вычисляет среднее арифметическое положительных элементов в списке `numbers`.
    Возвращает 0, если положительных элементов нет.
    """
    if not isinstance(numbers, list):
      raise TypeError("Input must be a list.")
    total = 0
    count = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers.")
        if num > 0:
            total += num
            count += 1
    if count > 0:
        average = total / count  # Строка A
    else:
        average = 0
    return average
