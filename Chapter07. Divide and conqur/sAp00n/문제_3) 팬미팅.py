from sys import stdin


def simple_mult(list_of_fan, list_of_members):
    computing_que = [[0] * len(list_of_fan) for i in range(len(list_of_members))]
    for member_idx in range(len(list_of_members) - 1, -1, -1):
        current_member = list_of_members[member_idx]



def kara(list_of_fan, list_of_members):
    len_of_fan, len_of_members = len(list_of_fan), len(list_of_members)
    if len_of_members == 1:
        if list_of_members[0] == '1':
            return list_of_fan
        return '0' * list_of_fan
    diff = list_of_fan - list_of_members
    list_of_members = '0' * diff + list_of_members


def sol():
    list_of_members = ['1' if member == 'M' else '0' for member in stdin.readline().strip('\n')]
    list_of_fan = ['1' if fan == 'M' else '0' for fan in stdin.readline().strip('\n')]
    kara(list_of_fan, list_of_members)


C = int(stdin.readline())
for _ in range(C):
    sol()
