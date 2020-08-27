from analyser.utils.utils import url_regex, resource_regex, file_regex
import analyser.utils.log as log

from urllib.parse import unquote

def redirect(url):
    if '?' not in url:
        log.fail('Redirect contains no GET parameters', indent=2)
        return
    

    # URL Decode
    params = unquote(url.split('?')[1]).split('&')

    for p in params:
        name, value = p.split('=')

        if re.match(url_regex, value):
            log.success('Redirect appears to contain a URL - possible RFI or use of another URL scheme?', indent=2)
            continue
        
        if re.match(resource_regex, value):
            log.success('Redirect appears to contain a resource - possible LFI?', indent=2)
            continue

        if re.match(file_regex, value):
            log.success('Redirect appears to contain a filename - possible LFI?', indent=2)
            continue
