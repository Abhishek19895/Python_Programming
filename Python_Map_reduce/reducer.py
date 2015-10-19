__author__ = 'abhisheksingh29895'

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    for word_sort, group in groupby(data, itemgetter(0)):
        try:
            total_words  =  [word.lower()  for  word_sort, word  in  group]
            myset  =  set(total_words)
            new_list  =  ' '.join(myset)
            if  len(myset)  >  1:
                print new_list
        except ValueError:
            pass

if __name__ == "__main__":
    main()




