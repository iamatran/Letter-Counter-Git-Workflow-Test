def main():
    print("This will count the # of vowels in your phrase")
    
    lettersToCount = input("Enter letters to count: ").lower()
    inputPhrase = input("Enter phrase: ").lower()

    totalOccurrencesOfLettersToCount = 0

    for character in inputPhrase:
        if character in lettersToCount:
            totalOccurrencesOfLettersToCount = totalOccurrencesOfLettersToCount + 1

    print("Total occurrences of '{}' in your phrase: {}".format(lettersToCount, totalOccurrencesOfLettersToCount))

if __name__ == "__main__":
    main()


