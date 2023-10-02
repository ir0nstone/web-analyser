import utils.context as context
import utils.log as log

from os import getcwd
from os.path import exists, join

accept_codes = [200, 301]

def grab(file: str='', text=True):
    r = context.session.get(context.url + '/' + file)

    if r.status_code not in accept_codes:
        if file != '':
            log.fail(f'Could not grab {file} - failed with status code {r.status_code}')
            return False


    if text:
        return r.text
    
    return r


def fix_url(url: str):
    '''Fixes incomplete urls'''

    # isolate the scheme and the url
    url_split = url.split('://')
    url = url_split[-1]

    # add www. if not full
    if url.count('.') == 1:
        url = 'www.' + url

    # add http:// if no scheme
    if len(url_split) == 1:
        return 'http://' + url
    
    # otherwise add scheme
    return url_split[0] + '://' + url


def fix_filepath(file: str):
    '''Updates the file path to the current working directory'''

    if not file:
        return

    # If it starts with C:, \ or / it's likely an absolute path
    if file.lower().startswith('c:') or file.startswith('\\') or file.startswith('/'):
        return file

    full_path = join(getcwd(), file)

    if exists(full_path):
        raise EnvironmentError('The output file already exists!')
    
    return full_path


def cookie_string_to_dict(cookies: str):
    '''Converts a string of cookies into a dictionary

    username=bob; password=yes
    {'username': 'bob', 'password': 'yes'}
    '''

    cookie_dict = {}
    
    cookies = cookies.split('; ')

    for c in cookies:
        name, value = c.split('=', 1)

        cookie_dict[name] = value
    
    return cookie_dict


def get_full_response(resp):
    '''Return full response, including all headers'''
    return ''.join(f'{header.lower()}: {value}\r\n' for header, value in resp.headers.items()) + '\r\n' + resp.text