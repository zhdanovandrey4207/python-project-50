#!/usr/bin/env pyhton3
import json


def generate_diff():
    a = json.load(open('/home/andrey/python-project-50/gendiff/files/file1.json'))
    b = json.load(open('/home/andrey/python-project-50/gendiff/files/file2.json'))
    return (a, b)


def main():
    generate_diff()


if __name__ == "__main__":
    main()

