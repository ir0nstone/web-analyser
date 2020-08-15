import utils.log as log
from utils.utils import grab, url_regex, resource_regex
from helpers.analysis import redirect

from bs4 import BeautifulSoup, Comment
from colorama import Fore
from re import findall

def execute():
    '''The function that calls all others'''

    robots()
    sitemap()
    cookies()
    redirects()
    comments()
    urls()
    resources()



def robots():
    text = grab('robots.txt')

    log.info(f'Robots:\n{text}')


def sitemap():
    text = grab('sitemap.xml')

    log.info(f'Sitemap:\n{text}')


def cookies():
    r = grab(text=False)

    cookies = r.cookies.get_dict()

    if len(cookies) == 0:
        log.fail('No cookies found')
        return


    log.info('Cookies:')

    for x in cookies:
        cookie_data = x
        cookie_data = cookie_data.ljust(10, ' ')
        cookie_data += cookies[x]

        log.info(cookie_data, indent=1)


def redirects():
    r = grab(text=False)

    history = r.history

    if len(history) == 0:
        log.fail('No redirects')
        return

    log.success('Redirects:')

    for url in history:
        red = Fore.RED + str(url.status_code) + Fore.RESET
        red = red.ljust(20, ' ')
        red += url.url

        log.info(red, indent=1)

        redirect(url.url)


def comments():
    r = grab()

    soup = BeautifulSoup(r, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    if len(comments) == 0:
        log.fail('No comments')
        return

    log.success('Comments:')

    for c in comments:
        log.info(c, indent=1)


def urls():
    urls = findall(url_regex, grab())
    
    if len(urls) == 0:
        log.fail('No URLs')
        return

    log.success('URLs:')

    for url in urls:
        log.info(url, indent=1)


def resources():
    resources = findall(resource_regex, grab())
    
    if len(resources) == 0:
        log.fail('No Resources')
        return

    log.success('Resources:')

    for res in resources:
        log.info(res[1], indent=1)
