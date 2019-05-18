#added refactor to separate input
def getInputPhrase():
    return input("Enter phrase: ").lower()

def getVowelCount(phrase):
    vowelCount = 0
    for character in phrase:
        if character in ['a', 'e', 'i', 'o', 'u']:
            vowelCount = vowelCount + 1
    return vowelCount


def main():
    print("This will count the # of vowels in your phrase")
    inputPhrase = getInputPhrase()

    totalVowels = getVowelCount(inputPhrase)

    print("Total vowels: {}".format(totalVowels))

if __name__ == "__main__":
    main()

