#added refactor to separate input
def getInputPhrase():
    return input("Enter phrase: ").lower()


def main():
    print("This will count the # of vowels in your phrase")
    inputPhrase = getInputPhrase()

    totalVowels = 0
    for character in inputPhrase:
        if character in ['a', 'e', 'i', 'o', 'u']:
            totalVowels = totalVowels + 1

    print("Total vowels: {}".format(totalVowels))

if __name__ == "__main__":
    main()

