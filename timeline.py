#!/usr/bin/env python3

import sys

def main(args):
    print("Hello world!")


    with open(sys.argv[1], 'r') as f:
    
        for line in f:
            print(line)

    return 0

if __name__ == "__main__":
    main(sys.argv)

