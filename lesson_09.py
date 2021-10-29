from random import randint

num_list=[]

def list_generate():
    while len(num_list) < 11:
        num_list.append(randint(0, 100))

    print(num_list)
    return

list_generate()

sel_num = input("Введите число от 0 до " + str(len(num_list))+ " ")
sel_num = int(sel_num)

num_list[sel_num] = sel_num
print(num_list)