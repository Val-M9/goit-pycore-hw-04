from pathlib import Path
from salaries import get_total_salary
from cats import get_cats_info

salaries_file = Path(__file__).parent / 'salaries/salaries.txt'
cats_file = Path(__file__).parent / 'cats/cats_info.txt'

total, average = get_total_salary(salaries_file)
print(f"Загальна сума заробітної плати: {
      total}, Середня заробітна плата: {average}")

cats_info = get_cats_info(cats_file)
print(cats_info)
