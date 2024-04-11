money = int(input())

animals = ['chicken', 'goat', 'pig', 'cow', 'sheep']
price = [23, 678, 1296, 3848, 6769]

if money >= price[4]:
    k = money // price[4]
    name = animals[4]
    print(k, name)
elif money < price[0]:
    print('None')
else:
    i = 4
    while price[i] > money:
        i -= 1
        
    k = money // price[i]
    name = animals[i]
    if k > 1:
        name += 's'
    print(k, name)
