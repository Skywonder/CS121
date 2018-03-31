# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import fileinput
import os
import sys
import time
import re

#for assignment 2

#Requirements:
# 1. Read an input 2 file passed as a command line argument
# 2. Tokenize the text of the files
# 3. get the occurrence of each word that they have in common
# 4. Print out the words that are common in both file. The print out should be ordered by decreasing frequency
# 4. or just print out the number of words that they have in common

#Plan
# Set up inputfile
# Put all avaliable words into list
# process the entire word list to freq dict
# order the dictionary and print out result

wordfreq1 = {}
wordfreq2 = {}
list1 = []
list2 = []
BUFFER_SIZE = 65536
COUNT = 0
start_time = time.time()

#main function 
def main():
    try:
        s = os.stat(sys.argv[1])
        s2 = os.stat(sys.argv[2])
        if s.st_size == 0:
            print "The file {} is empty".format(sys.argv[1])
            sys.exit(1)
        if s2.st_size == 0:
            print "The file {} is empty".format(sys.argv[2])
            sys.exit(1)
        if len(sys.argv) > 3:
            print "Too many arguments. The program only accepts at max 2 text file."
            sys.exit(1)

        with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'r') as f2:
            while True:
                line_1 = f.readlines(BUFFER_SIZE)#we are reading this many lines into memory
                if not line_1:
                    break
                for line in line_1:
                    splitline(line, list1)
                

            while True:
                line_2 = f2.readlines(BUFFER_SIZE)
                if not line_2:
                    break
                for line in line_2:
                    splitline(line, list2)
                   
        #check for same words
        intersect(list1, list2)
        
        f.close()
        f2.close()
            
    except OSError as EmptyFileError:
        print "One of the entered file is either empty or does not exist"
        sys.exit(2)
    except IndexError as FileIndexError:
        print "The required text file(s) is missing"
        sys.exit(1)

    
#handles splitting the line
def splitline(line, alist):
    line = re.sub('[^a-zA-Z0-9]', ' ', line)
    while '  ' in line:
        line = line.replace('  ', ' ')
            
    #print(line)
    token = line.strip().lower().split(' ')
   
    for word in set(token):
        if word not in alist:
            alist.append(word)

#check for same words, making lists set will make iteration O(n) -> O(1)
def intersect(wordlist, wordlist2):
    global COUNT
    s1 = set(wordlist) 
    s2 = set(wordlist2)
    for word in s1 & s2: #O(min(len(s1),len(s2)) for comparing 2 set
        COUNT += 1
        #print word
    print COUNT



if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
