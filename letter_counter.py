#added refactor to separate input
def getInputPhrase():
    return input("Enter phrase: ").lower()

def getTotalOccurrencesOfLettersToCount(phrase, lettersToCount):
    totalOccurrences = 0
    for character in lettersToCount:
        if character in lettersToCount:
            totalOccurrences = totalOccurrences + 1
    return totalOccurrences


def main():
    print("This will count the # of vowels in your phrase")
    
    lettersToCount = input("Enter letters to count: ").lower()
    phrase = getInputPhrase()

    totalOccurrencesOfLettersToCount = getTotalOccurrencesOfLettersToCount( phrase, lettersToCount )


    print("Total occurrences of '{}' in your phrase: {}".format(lettersToCount, totalOccurrencesOfLettersToCount))

if __name__ == "__main__":
    main()

