#Day 17
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# *nordic_countries , es , ru = names
# print(nordic_countries)

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Something went wrong')

#Day 18
from collections import Counter
import re

# text = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# # Convert to lowercase and remove punctuation
# cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

# # Split into words and count frequencies
# word_counts = Counter(cleaned_text.split())

# # Get the single most common word
# most_common_word, frequency = word_counts.most_common(1)[0]

# print(f"Most frequent word: '{most_common_word}' (appears {frequency} times)")

# print(word_counts)
# print(cleaned_text)

# import re

# # 1. Input text
# text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# # 2. Extract all integer numbers (including negative ones) using regex
# extracted_numbers = [int(num) for num in re.findall(r'-?\d+', text)]

# # 3. Find the two furthest points
# min_point = min(extracted_numbers)
# max_point = max(extracted_numbers)

# # 4. Calculate total distance
# distance = max_point - min_point

# # Output results
# print(f"Extracted Points: {extracted_numbers}")
# print(f"Furthest Left: {min_point}")
# print(f"Furthest Right: {max_point}")
# print(f"Distance: {distance}")

# import re

# def is_valid_variable(name):
#     # Must start with a letter or underscore, followed by letters, numbers, or underscores
#     pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
#     return bool(re.match(pattern, name))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    a = re.sub(r'[%$@&#;]','',sentence)
    return a

clean_text(sentence)

# def most_frequent_words(text):
#     cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
#     word_counts = Counter(cleaned_text.split())
#     freq_list = [(count, word) for word, count in word_counts.items()]
#     freq_list.sort(key=lambda x: (-x[0], x[1]))
#     # most_common_word, frequency = word_counts.most_common(1)[0]
#     print(f"Most frequent word: {freq_list[:3]}")


# most_frequent_words(sentence)

# def most_frequent_words(text):
#     words = text.split()
#     counts = Counter(words)
#     # Format as list of tuples: (frequency, word)
#     freq_list = [(count, word) for word, count in counts.items()]
#     # Sort primarily by frequency descending, then alphabetically ascending
#     freq_list.sort(key=lambda x: (-x[0], x[1]))
#     return f"{freq_list[:3]} {counts}"


# print(most_frequent_words(clean_text(sentence)))

def most_frequent_words(text,num):
    words =  text.split()
    counts = {}
    for i in words:
        counts[i] = counts.get(i, 0) + 1
    counts_sorted = sorted(counts.items(), key=lambda a: a[1], reverse=True)
    # print(counts)
    print("diffrent word =",len(counts_sorted))
    return counts_sorted[0:num]

print(most_frequent_words(clean_text(sentence),20))
