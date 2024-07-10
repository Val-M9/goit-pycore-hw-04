from colorama import Fore


def change_contact(args: list[str], contacts: dict) -> str:
  try:
    name, phone = args
    old_phone = contacts.get(name)
    if old_phone:
      contacts[name] = phone
      return f'{Fore.GREEN}Contact updated{Fore.RESET}'
    else:
      return f'{Fore.YELLOW}There is no contact with provided name{Fore.RESET}'
  except ValueError:
    return f'{Fore.YELLOW}Please provide two values:{
        Fore.RESET} name and phone number'
