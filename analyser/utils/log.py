from colorama import init, Fore

init(autoreset=True)


def __log(text, symbol, colour, end='\n', indent=0):
    text = str(text)

    print('\t' * indent + f'[{colour}{symbol}{Fore.RESET}] {text}', end=end)


def info(text, end='\n', indent=0):             __log(text, '*', Fore.BLUE, end=end, indent=indent)
def fail(text, end='\n', indent=0):             __log(text, '-', Fore.RED, end=end, indent=indent)
def success(text, end='\n', indent=0):          __log(text, '+', Fore.GREEN, end=end, indent=indent)
