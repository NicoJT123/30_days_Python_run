empty_list = []
print(empty_list)

lists = ['apple','mango','orange','banana','lime']
print(lists)
print(len(lists))
print(lists[0])
print(lists[2])
print(lists[4])

mixed_data_types = ['Nico justin tanryo','17','1.8','not married','tandun street']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
print(it_companies)
print(len(it_companies))
print([it_companies[0],it_companies[int((len(it_companies)-1)/2)],it_companies[-1]])
print(it_companies[0::3])

it_companies[0] = 'Youtube'
print(it_companies)

it_companies.append('Nvidia')
print(it_companies)

it_companies.insert(4,'Facebook')
print(it_companies)

it_companies[2] = it_companies[2].upper()
print(it_companies)

string = ['#;']

join_lists = it_companies + string
print(join_lists)
it_companies.extend(string)
print(it_companies)

print('Google' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])

print(it_companies[-3:])

print(it_companies[int((len(it_companies)-1)/2)])
print(it_companies[3:-3])

it_companies.remove('Youtube')
print(it_companies)
it_companies.pop(int((len(it_companies)-1)/2))
print(it_companies)
del it_companies[-1]
print(it_companies)

del it_companies[0:]
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(5,'Python'),full_stack.insert(6,'SQL')
print(full_stack)

print("Level 2")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_Val = min(ages)
max_Val = max(ages)
print(ages)
print(min_Val)
print(max_Val)
n = len(ages)
if n%2 == 0 :
   M1 = ages[n//2]
   M2 = ages[(n//2)-1]
   M = int((M1+M2)/2)
else:
   M = int(ages[n//2])

Median = M
print(Median)

Avg = sum(ages)/len(ages)
print(Avg)

range = max_Val - min_Val
print(range)

a=abs(min_Val - Avg)
b=abs(max_Val - Avg)
print(f'{a:.2f}')
print(f'{b:.2f}')

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

n = len(countries)
if n%2 == 0 :
   M1 = countries[n//2]
   M2 = countries[(n//2)-1]
   M = int((M1+M2)/2)
else:
   M = countries[n//2]

Median = M
print(Median)

print(len(countries))
print(countries[0:99])
print(countries[99:-1])

country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china , russia , usa , *scandic_countries = country
print('First Three:',country[0:3])
print(f'scandic countries: {scandic_countries}')

