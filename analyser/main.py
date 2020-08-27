import utils.context as context
import utils.log as log
import helpers.recon as recon
from utils.utils import fix_url, fix_filepath

from argparse import ArgumentParser
from requests import Session


# Arguments
parser = ArgumentParser(description='A Web Analyser')
parser.add_argument('-u', '--url', type=str, help='The URL')
parser.add_argument('-o', '--output', type=str, help='The Output File')
parser.add_argument('--user', '--user-agent', type=str, help='The User-Agent to use', default='requests')
args = parser.parse_args()


# Set the Context
context.url = fix_url(args.url)
context.file = fix_filepath(args.output)

context.session = Session()
context.session.headers.update({'User-Agent': args.user})


# Log it all
log.success(f'Analysing {context.url}')
log.success(f'Saving output to {context.file}')


# Execute the different modules
recon.execute()
