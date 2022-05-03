import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

nato_alpha_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_alpha_csv.iterrows()}
should_continue = True
while should_continue:
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only enter alphabets please.")
    else:
        print(output)
        should_continue = False
