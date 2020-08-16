import utils.context as context
import utils.log as log
import helpers.recon as recon
from utils.utils import fix_url, fix_filepath

from argparse import ArgumentParser

parser = ArgumentParser(description='A Web Analyser')
parser.add_argument('-u', '--url', type=str, help='The URL')
parser.add_argument('-o', '--output', type=str, help='The Output File')
args = parser.parse_args()

context.url = fix_url(args.url)
context.file = fix_filepath(args.output)

log.success(f'Analysing {context.url}')
log.success(f'Saving output to {context.file}')

recon.execute()