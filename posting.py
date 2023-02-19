#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='filename')
    parser.add_argument('string', type=str)
    return parser

def main(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    f.close()
    lines[3] = lines[3].replace("true", "false")

    with open(filename, 'w') as f:
        f.writelines(lines)
    f.close()

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    main(args.string)
