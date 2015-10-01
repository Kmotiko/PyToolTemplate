#!/usr/bin/env python
import argparse
import sys
from tool.lib import common
from tool.command import sample
import os

#######################################
#
#
parser = argparse.ArgumentParser(
        description='pytool template',
        prog='pytool')
subparsers = parser.add_subparsers(help='subcommand')

#######################################
# sample options
#
str2bool = lambda opt_str:  False if opt_str == 'False' or opt_str == 'false' else True
parser_install = \
    subparsers.add_parser('sample', help='sample of pytool')
parser_install.add_argument('positional', type=str, default='sample', help='str sample')
parser_install.add_argument('--foo', type=str2bool, default=False, help='')
parser_install.add_argument('--bar', action='store_true', default=False, help='')



def main():
    #######################################
    # init logger and load config
    #
    root = os.getenv('TOOL_ROOT') if os.getenv('TOOL_ROOT') else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ['TOOL_HOME'] = home = os.getenv('TOOL_HOME') if os.getenv('TOOL_HOME') else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(root, 'etc', 'tool.conf')
    log_level = common.load_config(file_path).get('default', 'LOG_LEVEL') if os.path.exists(file_path) else 'info'
    common.init_logger(log_level, os.path.join(home, 'tool.log'))

    #######################################
    # parse
    #
    options= parser.parse_args()
    subcommand = sys.argv[1]

    #######################################
    # check command type and create it 
    #
    if subcommand == 'sample':
        command = sample.SampleSubcommand(options)

    return command.run()
