# # # a = ['alma', 'banan', 'almurt']
# # # a[0] = 'almurt'
# # # print(a)


# # # atin = input("atinin kim ? ")


# # # a = input('atin kim ? ')

# # # a = a.lower()

# # # if a == 'kallibek':
# # #     print('Qalay Kallibek')

# # # elif a == 'uldawlet':
# # #     print('Saelm Uldawlet')

# # # else:
# # #     print('Salem ')


# # # at = 'kallibek uldawlet'

# # # print(at[0])


# # # lits

# # # shkaf = []

# # # print(shkaf)

# # # # ? mag qosiw

# # # shkaf.append('kitap1')

# # # shkaf.append('kitap2')

# # # print(f'Men usi {shkaf[0]} oqip shiqtim')


# # # spsk = ['aza', 'maza', 'saza']


# # # spsk.append('jana')

# # # print(spsk)


# # # cars = ['Lacetti', 'Nexia 3', 'Cobalt']

# # # cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz

# # # print(cars)


# # # mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']


# # # del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz


# # # print(mevalar)


# # bazarliq = ['un', 'konfet', 'shokolad']


# # aldim = bazarliq.pop(2)

# # print(bazarliq)

# # print(aldim)


# # stdentler = ['zayirov', 'minajov', 'salemnov','baxtiyarov']
# # stdentler.sort(reverse=False)

# # print(stdentler)


# # # ! royhattin sanin biliw ushin

# # stdentler = ['zayirov', 'minajov', 'salemnov','baxtiyarov']


# # print(len(stdentler))


# # # ! sanlardi jiynaqlaw, kombinatsiyalaw

# # jup_sanlar = list(range(0,11,2))
# # taq_sanlar = list(range(1,12,2))
# # print(jup_sanlar)
# # print(taq_sanlar)


# # narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]


# # arzon = min(narhlar)
# # qimmat = max(narhlar)
# # jami = sum(narhlar)

# # print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)


# # cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']


# # print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)


# # sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz


# # sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz


# # sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz


# # sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz


# # print("Bu sonlar ro'yxati:", sonlar)

# # print("Bu sonlar2 ro'yxati:", sonlar2)


# # sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz

# # sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi

# # sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz

# # sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz

# # print("Bu sonlar ro'yxati:", sonlar)

# # print("Bu sonlar2 ro'yxati:", sonlar2)


# # ~ tuppel - bul ozgermes list
# ozgermes = (12, 215, 25)

# print(ozgermes)


# print(type(ozgermes))

# # ! ----------------------------
# # * tupledi listke aylandiriw
# ozgermes = list(ozgermes)

# print(ozgermes)


# print(type(ozgermes))


# ozgermes.append(2024)


# print(ozgermes)

# del ozgermes[0]

# print(ozgermes)


# # ! ----------------------
# # * qaytarip tuplega aylandiriw 

# ozgermes = tuple(ozgermes)

# print(ozgermes)

# print(type(ozgermes))
