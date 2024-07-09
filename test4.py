import random
import string

l1 = string.ascii_letters + string.digits
l2 = string.ascii_letters
l3 = string.digits


def get_rand_member_ID():
    alphabet_numbes = "abcdefghizklmnopqrstuvwxyz0123456789"
    digit = random.randint(4,10)

    while(True):
        member_ID = "".join(random.sample(alphabet_numbes, digit))
        if(member_ID[0] not in '0123456789'): # 첫 번째 자리가 숫자인지 확인해서
            break # 숫자이면 while문을 빠져나감

    return member_ID

print(get_rand_member_ID())