#!/usr/bin/python3
import utils.context as context
import utils.log as log
import helpers.recon as recon
from utils.utils import fix_url, fix_filepath, cookie_string_to_dict

from argparse import ArgumentParser
from requests import Session, get


# Arguments
parser = ArgumentParser(description='A Web Analyser')
parser.add_argument('-u', '--url', type=str, help='The URL')
parser.add_argument('-o', '--output', type=str, help='The Output File')
parser.add_argument('--user', '--user-agent', type=str, help='The User-Agent to use')
parser.add_argument('-c', '--cookies', type=str, help='Any cookies you need')
parser.add_argument('--hide', '--hide-fail', help='Hide "info" logs', action='store_true')
args = parser.parse_args()


# Set the Context
context.url = fix_url(args.url)
context.file = fix_filepath(args.output)

context.session = Session()

if args.user:
    context.session.headers.update({'User-Agent': args.user})

if args.cookies:
    context.session.cookies.update(cookie_string_to_dict(args.cookies))

if args.hide:
    context.hide_fail = True

# Log it all
log.success(f'Analysing {context.url}')
log.success(f'Saving output to {context.file}')


# Execute the different modules
recon.execute()
