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

def most_spoken_languages(file,num):
    with open(file, encoding="utf-8") as file: 
        countries = json.load(file)
        spoken_languages = {}
        for i in countries[0:-1]:
            for j in i["languages"]:
                spoken_languages[j] = spoken_languages.get(j, 0) + 1
        spoken_languages_sorted = sorted(spoken_languages.items(), key=lambda item : item[1], reverse=True)
    return spoken_languages_sorted[0:num]

print(most_spoken_languages(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json",10))
print(most_spoken_languages(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json",3))


# with open(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json", encoding="utf-8") as file: # my understanding of this
#     countries = json.load(file)
#     spoken_languages = {}
#     for i in countries[0:-1]:
#         for j in i["languages"]:
#             spoken_languages[j] = spoken_languages.get(j, 0) + 1
#     spoken_languages_sorted = sorted(spoken_languages.items(), key=lambda item : item[1], reverse=True)

# print(spoken_languages_sorted)



def most_populated_countries(file,num):
    with open(file, encoding="utf-8") as file:
        data =  json.load(file)
        countries = {}
        for i in data :
            countries[i["name"]] = i["population"]
        countries_sorted = sorted(countries.items(), key=lambda item : item[1], reverse=True)
        countries_num = countries_sorted[0:num]
        result = []
        for country , population in countries_num:
            result.append(f"country: {country}, populations: {population}")

        return result

print(most_populated_countries(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json", 10))
print(most_populated_countries(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json",3))

# with open(r"C:\Users\Nico\OneDrive\VS code stuff\30 days python\countries_data.json", encoding="utf-8") as file:
#     data =  json.load(file)
#     countries = {}
#     for i in data :
#         countries[i["name"]] = i["population"]
# print(countries)
