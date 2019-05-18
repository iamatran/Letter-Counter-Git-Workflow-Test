def main():
    print("This will count the # of vowels in your phrase")
    inputPhrase = input("Enter phrase: ").lower()

    totalVowels = 0
    for character in inputPhrase:
        if character in ['a', 'e', 'i', 'o', 'u']:
            totalVowels = totalVowels + 1

    print("Total vowels: {}".format(totalVowels))

if __name__ == "__main__":
    main()

    