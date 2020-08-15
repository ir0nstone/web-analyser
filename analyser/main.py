import utils.context as context
import utils.log as log
import helpers.recon as recon
from utils.utils import fix_url

from argparse import ArgumentParser

parser = ArgumentParser(description='A Web Analyser')
parser.add_argument('-u', '--url', type=str, help='The URL')
args = parser.parse_args()

context.url = fix_url(args.url)

log.success(f'Analysing {context.url}')

recon.execute()