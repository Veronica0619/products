# 2 維度清單
products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	p = []
	p.append(name)
	p.append(price)
	#price =[name , price]
	products.append([name , price])  #product.append(p)
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

#字串可以做加乘
#'abc'+'123'='abc123'
#'abc'*3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: # 'w' 是寫入模式 # as 當作
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #f.wtite 才能真正寫入
#encoding='utf-8' 最廣泛使用的編碼
