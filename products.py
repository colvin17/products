# 記帳程式

products = []
while True: # while loop 比for loop適合用在這裡，因為不知道會輸入幾項記帳物品。
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入價格:')
    p = [] # 開始建立二維度清單，同時儲存一項商品名稱及價格到products清單。
    p.append(name)
    p.append(price)
    # 以上三行可縮成下面一行
    p = [name, price]
    products.append(p)
    # 以上兩行可縮成下面一行
    products.append([name, price])

print(products)
products[0][0] # 讀取二維清單，第一個[0]是product清單的第0格位置，第二個[0]是p清單的第0個位置。即先讀大清單的位置再讀小清單的位置。

for p in products:
    print(p) # 單獨印出products每項物品資訊(name & price)直到印完所有物品。
    print(p[0]) # 只印出商品名字。
    print(p[0], '的價格是', p[1], '元。')