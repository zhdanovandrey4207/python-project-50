#!/usr/bin/env python3
import argparse
import json

parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.')

#positional arguments
parser.add_argument('first_file')
parser.add_argument('second_file')

#optional arguments
parser.add_argument('-f', '--format', help='set format of output')


def start():
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def main():
    parser.print_help()


if __name__ == "__main__":
    main()


def generate_diff(file_path1, file_path2):
    first_pars = json.load(open(file_path1))
    second_pars = json.load(open(file_path2))
    uni_keys = sorted(set(list(first_pars) + list(second_pars)))
    fin_list = ['{\n']
    for el in uni_keys:
        if el in first_pars and el in second_pars:
            if first_pars[el] == second_pars[el]:
                fin_list.append(f'    {el}: {transform(first_pars[el])}\n')
            else:
                fin_list.append(f'  - {el}: {transform(first_pars[el])}\n')
                fin_list.append(f'  + {el}: {transform(second_pars[el])}\n')
        elif el in first_pars:
            fin_list.append(f'  - {el}: {transform(first_pars[el])}\n')
        else:
            fin_list.append(f'  + {el}: {transform(second_pars[el])}\n')
    fin_list.append('}')
    print(''.join(fin_list))


def transform(item):
    if item == True:
        return 'true'
    elif item == False:
        return 'false'
    elif item == None:
        return 'null'
    else:
        return item

