# Ali Kyrouz
# CS 021
# This is a program to do basic text analytics on given documents. It will
# return a word count for each document, as well as a list of the top five most
# used words in each document and a visualization of the data. 

def main():

# input on how many files
    twofiles = input('Would you like info on one file or two files? (one or two) ')
    while twofiles != 'one' and twofiles != 'two':
        print('Type either "one" or "two"')
        twofiles = input('Would you like info on one file or two files? ')

    if twofiles == 'one':
        file1 = input('What is the name of the file you would like to use? ')
        # I would put input validation here but I don't think there's a way without
        # try/except statements?
# get input for file 1 name
    if twofiles == 'two':
        file1 = input('What is the name of the first file you would like to use? (File 1) ')
# get input for file 2 name
        file2 = input('What is the name of the second file you would like to use? (File 2) ')

# make list of words in each file
    list1 = makeList(file1)
    if twofiles == 'two':
        list2 = makeList(file2)

# total word count of each list
    total1 = len(list1)
    if twofiles == 'two':
        total2 = len(list2)
    
# make dictionary from list, removing repeated words
    dict1 = makeDict(list1)
    if twofiles == 'two':
        dict2 = makeDict(list2)
# find total unique words from length of dictionaries
    totUnique1 = len(dict1)
    if twofiles == 'two':
        totUnique2 = len(dict2)
    
    
# receive input for words not to count in top 5 list
    exclude = input('Would you like to exclude any words from analytics (besides word count)? (y or n) ')
    # validate response
    while exclude != 'y' and exclude != 'n':
        print('Type either "y" or "n"')
        exclude = input('Would you like to exclude any words from analytics (besides word count)? ')
    if exclude == 'y':
        badWords = input("Type the words you would like to exclude as a list separated by spaces, not commas: ")
# remove inputted words from dictionary
        dict1 = removeWords(dict1, badWords)
        if twofiles == 'two':
            dict2 = removeWords(dict2, badWords)

# find top 5 most used words
    topnum1, topwords1 = top5(dict1)
    if twofiles == 'two':
        topnum2, topwords2 = top5(dict2)


# print results
    if twofiles == 'one':
        print('\n')
        print(f'The total length of your file is {total1} words. The number of unique words' +
              f' in your file is {totUnique1} words.')
    if twofiles == 'two':
        print('\n')
        # total words and total unique words for each file
        print(f'The total lengths of File 1 and File 2 are, respectively, {total1} and {total2} words. The number of unique words' +
              f' in File 1 is {totUnique1} words and {totUnique2} words in File 2.')
        # difference between most used words in each file
        if topnum1[0] > topnum2[0]:
            print(f'The most used word in File 1 is "{topwords1[0]}", used {topnum1[0]} times.' +
                  f' This is {topnum1[0]-topnum2[0]} uses more than the most used word in File 2, which is "{topwords2[0]}",' +
                  f' used {topnum2[0]} times.')
        if topnum2[0] > topnum1[0]:
            print(f'The most used word in File 1 is "{topwords1[0]}", and it was used {topnum1[0]} times.' +
                  f' This is {topnum2[0]-topnum1[0]} uses less than the most used word in File 2, which is "{topwords2[0]}",' +
                  f' used {topnum2[0]} times.')
    print('\n')
    # table 
    print('The top 5 most used words are: ')
    makeTable(1, topnum1, topwords1)
    if twofiles == 'two':
        print('\n')
        makeTable(2, topnum2, topwords2)
        

    # make graph
    plot1 = makeGraph(1, topwords1, topnum1)
    if twofiles == 'two':
        plot2 = makeGraph(2, topwords2, topnum2)
    #show graph without stopping program
    plot1.ion()
    plot1.show()
    plot1.pause(0.000001)
    if twofiles == 'two':
        plot2.ion()
        plot2.show()
        plot2.pause(0.000001)

    # get input on additional word counts
    print('\n')
    again = input("Are there any other words you would like info on? (y or n) ")
    # validate response
    while again != 'y' and again != 'n':
            print('Type either "y" or "n"')
            again = input('Are there any other words you would like info on? ')
    while again == 'y':
        word = input('Type word: ')
        # match word to dictionaries
        word = word.lower()
        # if one file is used
        if twofiles == 'one' and (word in dict1):
            print(f'The word "{word}" was used {dict1[word]} time(s).')
        if twofiles == 'one' and (word not in dict1):
            print(f'The word "{word}" was not used in your file')
        # if two files are used
        if twofiles == 'two' and (word in dict1) and (word in dict2):
            print(f'The word "{word}" was used {dict1[word]} time(s) in File 1 and {dict2[word]} time(s) in File 2')
        if twofiles == 'two' and (word not in dict1) and (word in dict2):
            print(f'The word "{word}" was used {dict2[word]} time(s) in File 2 and was not in File 1')
        if twofiles == 'two' and (word in dict1) and (word not in dict2):
            print(f'The word "{word}" was used {dict1[word]} time(s) in File 1 and was not in File 2')
        if twofiles == 'two' and (word not in dict1) and (word not in dict2):
            print(f'The word "{word}" was not in either of your files')
        again = input("Are there any other words you would like info on? (y or n) ")
        # validate response
        while again != 'y' and again != 'n':
            print('Type either "y" or "n"')
            again = input('Are there any other words you would like info on? ')
            

# this function takes in a file name and opens, reads, and breaks the file into a list of single words
# it returns the list
def makeList(file):
    # read in both files
    infile = open(file, 'r')
    infile = infile.read()
    words = infile.split()
    return words

# this function takes in a list, removes any special characters from the beginning or end of the items in the list, and
# creates and returns a dictionary where the word is the key and the number of occurances of each word is the corresponding value
def makeDict(l):
    d = {}
    for word in l:
        # strip special characters
        word2 = word.strip(':')
        word2 = word2.strip("'")
        word2 = word2.strip('?')
        word2 = word2.strip('!')
        word2 = word2.strip('.')
        word2 = word2.strip(',')
        word2 = word2.lower()
    # if word is already in dictionary, add 1 to counter for each occurance
        if word2 in d:
            val = d[word2] +1
            d[word2] = val
    # if the word is not already in the dictionary, add it with a count of 1
        else:
            d[word2] = 1
    return d

# this function takes in dictionary and a string of words to remove from keys, it creates a list from of words to remove, makes them
# lowercase to match the dictionary, and pops each word to remove it, then returns the edited dictionary
def removeWords(d, badWords):
    # convert string to list of strings to remove
    remove = badWords.split()
    for word in remove:
        # make lowercase
        word = word.lower()
        # if present, remove word from d
        if word in d:
            d.pop(word)
    return d

# this function takes in a dictionary, and assigns some of its keys to variables based on largest to fifth largest value pair, then
# returns a list of the top 5 values in descending order and a list of the keys they correspond to in descending order of the value. 
def top5(d):
    # initialize 5 variables
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    # loop through values in dict, every larger variable is assigned to next highest level
    for i in d:
        if d[i] > first:
            first = d[i]
            word1 = i
        elif d[i] > second:
            second = d[i]
            word2 = i
        elif d[i] > third:
            third = d[i]
            word3 = i
        elif d[i] > fourth:
            fourth = d[i]
            word4 = i
        elif d[i] > fifth:
            fifth = d[i]
            word5 = i
    # lists of top 5 values, and the keys they correspond to
    top5num = [first, second, third, fourth, fifth]
    top5word = [word1, word2, word3, word4, word5]
    return top5num, top5word

# this function takes in a variable to title a table, and lists for a column of words, and a column of times used, then
# prints the table created
def makeTable(fileNum, numList, wordList):
    print(f'File {fileNum}')
    print('Word      Times Used')
    print('----------------------')
    for i in range(len(numList)):
        print(f'{wordList[i]:10} {numList[i]}')

# this function takes in a variable for the file name
#, a list for x values and a list for y values, then plots them on a bar graph and returns the graph
def makeGraph(name,x, y):
    # import matplotlib
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots()
    ax.bar(x, y, width = 1, edgecolor = "white", color = "purple")
    plt.title(f'Words Used in File {name}')
    return plt
    
          
main()






