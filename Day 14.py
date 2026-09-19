# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mix = [1, 2, 3, 4, 5,'Asabeneh', 'Lidiya', 'Ermias', 'Abraham', 6, 7, 8, 9, 10,'Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Map translates data by transforming every individual element.
# Filter narrows down data by keeping only the elements that match a specific condition.
# Reduce synthesizes data by combining all elements into a single accumulated result

# def a(b):
#     for i in b:
#         print(i)

# a(countries)
# a(names)
# a(numbers)

# def upper(a):
#     return a.upper()

# upper_countries = map(upper,countries)
# print(list(upper_countries))
# # print(upper(countries))

# def square(a):
#     return a**2

# square_numbers = map(square,numbers)
# print(list(square_numbers))

# upper_names = map(upper,names)
# print(list(upper_names))

# def land(a):
#     if 'land' in a:
#         return True
#     return False

# countries_no_land =  filter(land,countries)
# print(list(countries_no_land))

# def six(a):
#     if len(a) == 6:
#         return True
#     return False

# countries_no_six =  filter(six,countries)
# print(list(countries_no_six))

# def more_six(a):
#     if len(a) >= 6:
#         return True
#     return False

# countries_no_more_six =  filter(more_six,countries)
# # print(list(countries_no_more_six))

# def e(a):
#     if 'E' in upper(a):
#         return True
#     return False

# countries_e = filter(e,countries)
# print (f'[{list(countries_e)}, {list(countries_no_more_six)}]')

# def get_string_lists(a):
#     if isinstance(a,str):
#         return True
#     return False

# string_lists = filter(get_string_lists,mix)
# print(list(string_lists))

from functools import reduce

# def sum(a,b):
#     return int(a) + int(b)

# total = reduce(sum,numbers)
# print(total)

# from functools import reduce

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# # Using reduce to concatenate all except the last country, then appending it
# concatenated_countries = reduce(lambda x, y: f"{x}, {y}", countries[:-1])
# final_sentence = f"{concatenated_countries}, and {countries[-1]} are north European countries"

# print(final_sentence)
# # Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries


# def a(x,y):
#     return f'{x}, {y}'

# b = reduce(a,countries[:-1])
# print(f'{b}, and {countries[-1]} are north European countries')


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

# def categorize_countries(a):
#     c = a.lower()
#     return [country for country in countries if c in country.lower()]
        
# print(categorize_countries("land"))
# # b = map(categorize_countries,'a')
# # print(list(b))

# def count_countries_by_letter(country_list):
#     letter_counts = {}
#     for country in country_list:
#         if country:
#             first_letter = country[0].upper()
#             letter_counts[first_letter] = letter_counts.get(first_letter, "") + country + ', '
#     # Return a new dictionary sorted by its keys
#     return dict(sorted(letter_counts.items()))

# print(count_countries_by_letter(countries))

# def count_countries_by_letter(country_list):
#     letter_counts = {}
#     for country in country_list:
#         if country:
#             first_letter = country[0].upper()
#             letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1
#     # Return a new dictionary sorted by its keys
#     return dict(sorted(letter_counts.items()))

# print(count_countries_by_letter(countries))

def get_first_ten_countries(a):
    b =[]
    for i in a[0:10]:
        b.append(i)
    return b
print(get_first_ten_countries(countries))

def get_last_ten_countries(a):
    b =[]
    for i in a[-10:]:
        b.append(i)
    return b 
print(get_last_ten_countries(countries))