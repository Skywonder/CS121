# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import fileinput
import os
import sys
import re
import time

#for assignment 1

#Requirements:
# 1. Read an input file passed as a command line argument
# 2. Tokenize the text of the file
# 3. Count the number of occurrence of each word in the tokens generated
# 4. Print out the word frequency counts onto the screen. The print out should be ordered by decreasing frequency


#Plan
# Set up inputfile
# Put all avaliable words into list
# process the entire word list to freq dict
# order the dictionary and print out result

#Global variable: Dict - wordfreq , List - wordlist
wordfreq = {}
wordlist = []
BUFFER_SIZE = 65536
start_time = time.time()
wordcount = {}
#main function 
def main():
    try:
        s = os.stat(sys.argv[1])
        if s.st_size == 0:
            print "The file {} is empty".format(sys.argv[1])
            sys.exit(1)
        if len(sys.argv) > 2:
            print "Too many arguments. The program only accepts at max 1 text file."
            sys.exit(1)
        with open(sys.argv[1], 'r') as f:
            while True:
                lines = f.readlines(BUFFER_SIZE)
                if not lines:
                    break
                
                for line in lines:
                    splitline(line)
               
        toOrdDict(wordlist)
        f.close()

    except OSError as EmptyFileError:
        print "The entered file {} is either empty or does not exist".format(sys.argv[1])
        sys.exit(1)
    except IndexError as FileIndexError:
        print "The required text file is missing"
        sys.exit(1)

    
#handles splitting the line
def splitline(line):
    line = re.sub('[^a-zA-Z0-9]',' ', line)
    while '  ' in line:
        line = line.replace('  ', ' ')
            
    token = line.strip().lower().split(' ')

    for word in token:
        wordlist.append(word)


#add words to ordered dictionary 
def toOrdDict(wordlist):

    for word in wordlist:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for keys, values in sorted(wordcount.items(), key=lambda x:x[1], reverse = True):
        print(str(keys) + " - " + str(values))
  
    

if __name__ == "__main__":
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    
