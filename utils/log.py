from colorama import init, Fore

import utils.context as context

init(autoreset=True)


def __log(text, symbol, colour, end='\n', indent=0):
    text = str(text)

    plain_text = '\t' * indent + f'[{symbol}] {text}'
    coloured_text = '\t' * indent + f'[{colour}{symbol}{Fore.RESET}] {text}'

    if context.file:
        with open(context.file, 'a') as f:
            f.write(plain_text.rstrip() + '\n')

    print(coloured_text, end=end)


def info(text, end='\n', indent=0):             __log(text, '*', Fore.BLUE, end=end, indent=indent)
def fail(text, end='\n', indent=0):             __log(text, '-', Fore.RED, end=end, indent=indent)
def success(text, end='\n', indent=0):          __log(text, '+', Fore.GREEN, end=end, indent=indent)