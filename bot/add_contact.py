from colorama import Fore


def add_contact(args: list[str], contacts: dict) -> str:
  try:
    name, phone = args
    if not contacts.get(name):
      contacts[name] = phone
      return f'{Fore.GREEN}Contact added!{Fore.RESET}'
    else:
      return f'Contact with this name already exists. If you want to update it, please, use {Fore.YELLOW}"change"{Fore.RESET} command.'
  except ValueError:
    return f'{Fore.YELLOW}Please provide two values:{
        Fore.RESET} name and phone number'
