import utils.context as context
import utils.log as log

from utils.constants import url_regex, resource_regex, file_regex

from requests import get, Request
from os import getcwd
from os.path import exists, join

accept_codes = [200, 301]

def grab(file: str='', text=True):
    r = context.session.get(context.url + '/' + file)

    if r.status_code not in accept_codes:
        if file != '':
            log.fail(f'Could not grab {file} - failed with status code {r.status_code}')
    
    if not r:
        return ''

    if text:
        return r.text
    
    return r


def fix_url(url: str):
    '''Fixes incomplete urls'''

    splits = url.split('.')
    
    # URL => 3
    # IP  => 4
    if not 3 <= len(splits) <= 4:
        raise ValueError('Not a valid URL or IP')


    # Assume https, but ":" could also define port
    if ':' not in splits[0]:
        url = 'https://' + url
    
    return url


def fix_filepath(file: str):
    '''Updates the file path to the current working directory'''

    if not file:
        return

    # If there is a / or \, it's probably the full path already
    if '/' in file or '\\' in file:
        return file

    full_path = join(getcwd(), file)

    if exists(full_path):
        raise EnvironmentError('The output file already exists!')
    
    return full_path


def cookie_string_to_dict(cookies: str):
    cookie_dict = {}
    
    cookies = cookies.split('; ')

    for c in cookies:
        name, value = c.split('=')

        cookie_dict[name] = value
    
    return cookie_dict


def get_full_response(resp: Request):
    return ''.join(f'{header.lower()}: {value}\r\n' for header, value in resp.headers.items()) + '\r\n' + resp.text