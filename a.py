from collections import Counter
import re
def Counts_Lines_and_Words(a):
    with open(a) as file:
        lines = file.read().splitlines()
        lines_count = len(lines)

        words = "".join(lines)
        cleand_words = re.sub(r'[^\w\s]',' ',words)
        words_count_clean = len(cleand_words.split())
        words_count = len(words.split())

        print(f"lines in file: {lines_count} \nwords in file: {words_count} or {words_count_clean}")
        # print(words_count_clean)
        # print(cleand_words)

Counts_Lines_and_Words(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\obama_speech.txt")
Counts_Lines_and_Words(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\michelle_obama_speech.txt")
Counts_Lines_and_Words(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\donald_speech.txt")
Counts_Lines_and_Words(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\melina_trump_speech.txt")

with open(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\obama_speech.txt") as file:           #my undertanding of this and trying it
    lines = file.read().splitlines()
    lines_count = len(lines)

    words = "".join(lines)
    cleand_words = re.sub(r'[^\w\s]',' ',words)
    b = len(cleand_words.split())
    words_count = len(words.split())

    print(f"lines in file: {lines_count} \nwords in file: {words_count}")
    # print(b)
    # print(cleand_words)
import json

# def most_spoken_languages(file):
#     with open(file) as file:
#         countries = file.read()
#         for countries


with open(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json") as file:
    countries = json.load(file)
print(countries)