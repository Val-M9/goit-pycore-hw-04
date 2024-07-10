from colorama import Fore


def get_cats_info(path: str) -> list[dict]:
  try:
    with open(path, 'r', encoding='utf-8') as file:
      cats_list = [line.strip() for line in file.readlines()]

      result = []
      for cat in cats_list:
        id, name, age = cat.split(',')
        result.append({'id': id, 'name': name, 'age': age})

      return result

  except FileNotFoundError as e:
    print(f'{Fore.RED}Sorry file was not found. {Fore.RESET}', e)

  except Exception as e:
    print(f'{Fore.RED}Sorry, an error ocurred: {Fore.RESET}', e)
