from colorama import Fore


def show_phone(args: list[str], contacts: dict) -> str:
  try:
    name = args[0]
    phone = contacts.get(name)
    if not phone:
      return f'There is no contact named {Fore.YELLOW}{name}{Fore.RESET}'
    else:
      return phone
  except Exception as e:
    return f'{Fore.RED}Sorry an error ocurred!{Fore.RESET} {e}'
