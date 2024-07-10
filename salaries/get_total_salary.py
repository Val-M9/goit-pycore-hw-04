from colorama import Fore


def get_total_salary(path: str) -> tuple:
  try:
    with open(path, 'r', encoding='utf-8') as file:
      overall_list = [line.strip() for line in file.readlines()]

    salaries = []
    for item in overall_list:
      _, salary = item.split(',')
      salaries.append(float(salary))

    salaries_sum = sum(salaries)
    average_salary = round(salaries_sum / len(salaries), 2)

    return (salaries_sum, average_salary)

  except FileNotFoundError as e:
    print(f'{Fore.RED}Sorry file was not found. {Fore.RESET}', e)
    return (0, 0)

  except Exception as e:
    print(f'{Fore.RED}Sorry, an error ocurred: {Fore.RESET}', e)
    return (0, 0)
