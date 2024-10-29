# color = input('enter your phone color: ')
# model = input('enter your phone model: ')
# print(color==('gold') and model==('iphone 12'))

# ------------------------------------------------

# shan_tariq = int(input('grir shan tariqy: '))
# if 0 < shan_tariq <= 2:
#     print(f' mardu_tariq = {shan_tariq * 10.5}')
# elif shan_tariq > 2:
#     print(f'mardu_tariq = {shan_tariq * 4}')

#  -----------------------------------------------------------------

# amis = input('grir amisy: ')  
# if amis == 'hunvar' or amis == 'mayis' or amis == 'ogostos' or amis == 'hoktember' or amis == 'dektember' or amis == 'hulis' or amis == 'mart':
#      print('31')
# elif amis == 'april' or amis == 'september' or amis == 'noyember' or amis == 'hunis':
#      print('30')
# elif amis == 'petrvar':
#      print('28 kam 29 ete nahanj tari e')
# else:
#      print('amsva sxal anun')
# --------------------------------------------------------------
# text = 'p,y,t,h,o,n'
# text = text.replace(',', '')
# print(text)
# --------------------------------------------------------------
# import random

# user = int(input ('enter followers count: '))
# pc = random.randint(1, 10000)
# if user + pc * 20 / 100 >= pc:
#     print('user is blogger')
# elif pc + user * 20 / 100 >= user:
#     print('pc is blogger')

# n = int(input('enter n: '))
# summ = 0 
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
# summ += fact
# print(summ)
# number_count = int(input('enter number count: '))
# for i in range(n(umber_count)):
#     number = int(input('enter number: '))
# import random

# count_o = 0
# count_r = 0
# s = ''
# while True:
#     pc = random.choice("OR")
#     s += pc
#     if count_o == 3 or count_r == 3:
#         print(s)
#         break
#     if pc == 'O':
#         count_o += 1
#         count_r = 0
#     else:
#         count_r += 1
#         count_o = 0

# n = 1000
# for i in range(1, n):
#     if i % 2 != 0:
#         print(i)
#     else:
#         continue
#---------------------------------------------------------------
# x = [3, 1, 2, 1, 3, 4]
# count = 0

# while count < len(x):
#     qayler = x[count]
#     print(f'nerkayis tiv: {count}, catker: {qayler}')
#     count += qayler
    
#     if count >= len(x):  
#         print('duq partveciq')
#         break

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# while True:
#     # вводим первое число
#     num1 = int(input("Введите первое число: "))
#     # вводим второе число
#     num2 = int(input("Введите второе число: "))
#     # вычисление суммы чисел
#     print("Сумма чисел: ", num1+num2 )
#     # запрос на выход из цикла
#     str = input ("Нажмите Y или y для завершения программы: ")
#     # выходим из цикла
#     if (str =="Y" or str =="y"):  break
#---------------------------------------------------------------
# n = 7
# for i in range(0, n):
#     for j in range(0, n):
#         if i == 0 or i == n -1 or j == i or j == n -i -1:
#             print('*', end='')
#         else: 
#             print(' ', end='')
#     print()
#-----------------------------------------------------
# n = int(input('grir tiv: '))
# sum = 0
# for i in range(1, n +1):
#     if i % 3 == 0 and i % 5 == 0:
#         sum += 1
#         print(n,sum)
# #---------------------------------------------------
# n = int(input('Գրիր թիվ: '))  # Օրինակ n = 15
# sum = 0

# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:  # Թվերը, որոնք բաժանվում են 3-ի և 5-ի վրա
#         sum += i  # Ավելացնում ենք այդ թվերը
# print(f"1-ից {n} մինչև բոլոր թվերի գումարը, որոնք բաժանվում են 3-ի և 5-ի վրա՝ {sum}]


# number = 10
# for i in range(1, number):
#     for j in range(1, number):
#         print(f"{i * j:4}", end='  ')
#     print()


# def func(nums):

#     val = 3
#     while val in nums:
#         nums.remove(val)
#     return nums
# print(func([3,2,2,3]))


# nums = [2,7,11,15]
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] + nums[j] == 9:
#             print(i + j)
#         else:
#             break


