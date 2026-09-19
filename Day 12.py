import random
def random_user_id(length=6):
    a = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    return ''.join(random.choice(a) for _ in range(length))

# print(random_user_id())

def user_id_gen_by_user(length=6,a=1):
    for i in range(a):
        print(random_user_id(length))

user_id_gen_by_user(16,5)

def rgb_color_gen(halo=1):
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    return f'rgb({a},{b},{c})'

print(rgb_color_gen())

def list_of_hexa_colors(a):
    d = []
    for i in range(a):
        b='abcdef0123456789'
        c = f"#{''.join(random.choice(b) for j in range(6))}"
        d.append(c)    
    return d

# list_of_hexa_colors(3)             

def list_of_rgb_colors(a):
    b = []
    for i in range(a):
        c = rgb_color_gen()
        b.append(c)
    return b
# print(list_of_rgb_colors(3))

def generate_colors(a,b):
    if 'hexa' in a:
        return list_of_hexa_colors(b)
    elif 'rgb' in a:
        return list_of_rgb_colors(b)

print(generate_colors('rgb',4))

def shuffle_list(a):
    random.shuffle(a)
    return a
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

import random

def get_unique_random_numbers():
    return random.sample(range(10), 7)

print(get_unique_random_numbers())

