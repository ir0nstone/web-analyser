#!/usr/bin/python3
import utils.context as context
import utils.log as log
import helpers.recon as recon
from utils.utils import fix_url, fix_filepath, cookie_string_to_dict, grab

from argparse import ArgumentParser
from requests import Session


# Arguments
parser = ArgumentParser(description='A Web Analyser')

parser.add_argument('-u', '--url', type=str, help='The URL', required=True)
parser.add_argument('-o', '--output', type=str, help='The Output File')

parser.add_argument('--agent', type=str, help='The User-Agent to use')
parser.add_argument('-c', '--cookies', type=str, help='Any cookies you need')


parser.add_argument('-U', '--username', type=str, help='Username (for auth)')
parser.add_argument('-P', '--password', type=str, help='Password (for auth)')

parser.add_argument('--nagent', '--no-agents', help='Don\'t attempt to brute User-Agents', action='store_true')
parser.add_argument('--verbose', help='Print all findings', action='store_true')
parser.add_argument('--hide', '--hide-fail', help='Hide "fail" logs', action='store_true')


args = parser.parse_args()


# Set the Context
context.url = fix_url(args.url)
context.file = fix_filepath(args.output)

context.session = Session()

context.default_req = grab(text=False)
context.verbose = args.verbose
context.hide_fail = args.hide

if args.agent:
    context.session.headers.update({'User-Agent': args.user})

if args.cookies:
    context.session.cookies.update(cookie_string_to_dict(args.cookies))

if args.username and args.password:
    context.session.auth = (args.username, args.password)

# Log it all
log.success(f'Analysing {context.url}')

if context.file:
    log.success(f'Saving output to {context.file}')


# Execute the different modules
recon.execute(not args.nagent)
