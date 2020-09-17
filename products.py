# 記帳程式

products = []
while True: # while loop 比for loop適合用在這裡，因為不知道會輸入幾項記帳物品。
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入價格:')
    price = int(price) # 將price從字串轉成整數。
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

# 字串可以加、乘，無法減、除
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc' #很少用到
with open('products.csv', 'w', encoding = 'utf-8') as f: # 加入編碼格式避免印出亂碼
	f.write('商品,價格\n') 
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # \n換行, 中間加逗點方便csv檔用excel打開時自動將商品名字及價錢分成兩個儲存格。
        # 字串無法和整數相加，所以要將price再從int轉換成str。

