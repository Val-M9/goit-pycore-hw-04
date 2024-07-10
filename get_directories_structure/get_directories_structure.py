import sys
from pathlib import Path
from colorama import Fore

path = Path(sys.argv[1])


def get_directories_structure(path: Path, level=0) -> None:
  print(path)
  try:
    indent = ' ' * level
    for p in path.iterdir():
      if p.is_dir():
        print(f'{indent}{Fore.BLUE}{str(p).split('\\')[-1]}\\{Fore.RESET}')
        get_directories_structure(p, level + 2)
      else:
        print(f'{indent}{Fore.YELLOW}{str(p).split('\\')[-1]}{Fore.RESET}')
  except FileNotFoundError as e:
    print(f'{Fore.RED}Sorry, input directory was not found! {Fore.RESET}{e}')
  except Exception as e:
    print(f'{Fore.RED}Sorry, an error ocurred! {Fore.RESET}{e}')


get_directories_structure(path)
