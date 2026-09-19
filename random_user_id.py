import random
import string
def random_user_id(length=6):
    a = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b = random.choice(a)
    return ''.join(random.choice(a) for _ in range(length))

print(random_user_id())