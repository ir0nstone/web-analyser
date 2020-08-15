import utils.context as context
import utils.log as log

from requests import get

accept_codes = [200, 301, 404]

url_regex = r'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}'
resource_regex = r'("|\'){1}(/[\w\/]+)("|\'){1}'
file_regex = r'\w+\.\w+'

def grab(file: str='', text=True):
    r = get(context.url + '/' + file)

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