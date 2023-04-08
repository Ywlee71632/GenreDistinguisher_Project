import random
# This function reads in a file of all of the words which appear in the texts. 
# Arguments: None
# Return: returns a list of strings. Each element represents 1 word.
def genDictionary():
    # Read in a file of all of the words in the texts provided (pre-computed)
    dictFile = open("Texts/dictionary.csv")
    allWords = dictFile.read().split(",")
    dictFile.close()

    return allWords

# This function creates and returns a list of the specified length containing only 0s.
# Arguments: length (integer): the desired length of the list
# Return: returns a list of the specified length, containing only 0s
def createEmptyList(length):
    return [0] * length

# This function returns the index of “word” inside of the list “allWords”
# Arguments: 
#   allWords - a list of strings to search inside of;
#   word - a string to search for
# Return: returns an integer representing the index of word inside of allWords
def getIndexOfWord(allWords, word):
    return allWords.index(word)

# This function opens the requested file and returns the text in it as a list of individual words.
# Arguments: fileName (string) - the name of the file you want to open and read the text from.
# Return: returns a list of strings. Each string is one word.
def readWordsFromText(fileName):
    file = open(fileName, "r")
    fileContents = file.read()      
    file.close()
    return fileContents.split()


# ---------- ADD YOUR FUNCTIONS BELOW THIS LINE - DON'T TOUCH THE ONES ABOVE ------------- #

def computeDistribution (origText, allWords):

    # create an empty list that has the same length as allWords
    computedList =  createEmptyList(len(allWords))

    '''
    i and j (or x) are usually reserved for variables that represent
    indexes. If you are creating a loop that iterates over the 
    elements of a list you should name your variables appropiately. 
    '''
    # count how many times each word in allWords appears in origText
    for words in allWords:
        count = 0
        for target in origText : 
            if (target == words):
                count += 1

        # append the percentage of i appearing in origText to computedList at the index corresponding to the order of allWords
        computedList[getIndexOfWord(allWords,words)] = count / len(origText)

    return computedList

def compareDistribution(distA, distB):

    sumOfSq = 0

    # calculate the sum of squared difference between two novels with the same length 

    '''
    your program should not assume the size of the lists, it should
    use their length as a reference for the number of times to 
    loop.
    '''
    for i in range(len(distA)):
        sumOfSq = sumOfSq + ((distA[i]-distB[i]) ** 2)
        
    return sumOfSq

def main():

    # genDictionary & readWords must be ran here 
    allWords = genDictionary()

    # Text and the word distribution of Philosopy: A Critique of Pure Reason
    critiqueText = readWordsFromText("Texts/ACritiqueOfPureReason.txt")
    critiqueDist = computeDistribution(critiqueText, allWords)

    # Text and the word distribution of FairyTale: Anderson's Fairy Tales
    andersenText = readWordsFromText("Texts/AndersensFairyTales.txt")
    andersenDist = computeDistribution(andersenText, allWords)

    # Text and the word distribution of Science Fiction: Frankenstein
    frankensteinText = readWordsFromText("Texts/Frankenstein.txt")
    frankensteinDist = computeDistribution(frankensteinText, allWords)

    # Text and the word distribution of the sample text
    discourseText = readWordsFromText("Texts/ADiscourse.txt")
    discourseDist = computeDistribution(discourseText, allWords)

    '''
    Your program should print out the names of the books that are being compared,
    not only the comparison numbers. Without that information printed to the user
    it is hard to know what the numbers represent.
    '''

    # print the sum of squred difference between 4th novel and each genre
    print("Comparison between Discourse and Frankenstein:", compareDistribution(discourseDist, frankensteinDist))
    print("Comparison between Discourse and Andersen's Fairy Tales:", compareDistribution(discourseDist, andersenDist))
    print("Comparison between Discourse and Critique:", compareDistribution(discourseDist, critiqueDist))
    
if __name__ == "__main__":
    main()