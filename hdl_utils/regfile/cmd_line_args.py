
import argparse
import sys


def parse_command_line_arguments():
    """Parses the command line arguments and returns them."""

    parser = argparse.ArgumentParser(
        prog='regfile',
        description='''Generates a VHDL register file using a JSON file.'''
    )

    parser.add_argument('jsonFile', help='JSON File with register definitions')
    parser.add_argument('outputFile', help='Output VHDL register file.')

    args_ = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        return args_
