#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.')

#positional arguments
parser.add_argument('first_file')
parser.add_argument('second_file')

#optional arguments
parser.add_argument('-f', '--format', help='set format of output')


def main():
    parser.print_help()


if __name__ == "__main__":
    main()
