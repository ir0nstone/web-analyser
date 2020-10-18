import utils.log as log
import utils.context as context

from utils.utils import grab, get_full_response
from utils.constants import url_regex, resource_regex, jwt_regex
from helpers.analysis import redirect
from utils.constants import user_agents_list

from bs4 import BeautifulSoup, Comment
from colorama import Fore
from re import findall
from base64 import standard_b64decode

def execute(agents: bool):
    '''The function that calls all others'''

    robots()
    sitemap()
    cookies()
    get_jwts()
    redirects()
    comments()
    urls()
    resources()

    if agents:
        user_agents()


def robots():
    text = grab('robots.txt')

    log.info(f'Robots:\n{text}')


def sitemap():
    text = grab('sitemap.xml')

    log.info(f'Sitemap:\n{text}')


def cookies():
    r = context.default_req
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


def get_jwts():
    response = get_full_response(context.default_req)

    jwts = findall(jwt_regex, response)

    if len(jwts) == 0:
        log.fail('No JWTs')
        return
    
    log.success('JWTs found:')

    for jwt in jwts:
        log.success(jwt, indent=1)

        # The last section of a JWT is the signature
        for section in jwt.split('.')[:-1]:
            log.info(standard_b64decode(section), indent=2)


def redirects():
    history = context.default_req.history

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
    soup = BeautifulSoup(context.default_req.text, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    if len(comments) == 0:
        log.fail('No comments')
        return

    log.success('Comments:')

    for c in comments:
        log.info(c, indent=1)


def urls():
    urls = findall(url_regex, context.default_req.text)
    
    if len(urls) == 0:
        log.fail('No URLs')
        return

    log.success('URLs:')

    for url in urls:
        log.info(url, indent=1)


def resources():
    resources = findall(resource_regex, context.default_req.text)
    
    if len(resources) == 0:
        log.fail('No Resources')
        return

    log.success('Resources:')

    for res in resources:
        log.info(res[1], indent=1)


def user_agents():
    length = len(context.default_req.text)
    log.info(f'Standard Response Length: {length}')

    for agent in user_agents_list:
        r = context.session.get(context.url, headers={'User-Agent': agent})

        if len(r.text) != length:
            log.info(agent, indent=1)
            log.success(f'Response size is different: {len(r.text)}', indent=2)
        else:
            log.fail(agent, indent=1)
            log.fail('Default length', indent=2)
