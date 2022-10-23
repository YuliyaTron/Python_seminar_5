with open('task_2_text_1.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст, необходимый для сжатия: '))
with open('task_2_text_1.txt', 'r') as file:
    my_text = file.readline()
    txt_new = my_text.split()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if (count>1) or  (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

txt_new1 = coding(my_text)
txt_new2 = decoding(coding(my_text))

with open('task_2_text_2.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_new1}')
print(txt_new1)

with open('task_2_text_3.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_new2}')
print(txt_new2)