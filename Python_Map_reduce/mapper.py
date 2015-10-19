__author__ = 'abhisheksingh29895'

import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            a  =  [ch for ch in word.lower()]
            a.sort()
            word_sort  =  ""
            for  i  in  a:
                word_sort  =  word_sort  +  i
            print '%s\t%s' %  (word_sort,  word)

if __name__ == "__main__":
    main()