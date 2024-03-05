# a = 5

# if a == 5:
#     print('yes')

# print('hello')


# mevalar = ["olma", "anor", "uzum"]
# print(mevalar[3])


def salom_ber(ism):
    if ism == '':
        print('bos qaldiriw mk emes')
    else:
        print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber(input('at kim ? '))