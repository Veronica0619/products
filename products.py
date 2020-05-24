import os #operating system
#讀取檔案
def read_file(filename):
	products = []#放在最外面，不管檔案存不存在都要用
	with open (filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續，跳過直接到下一回
			name, price = line.strip().split(',') #先把尾巴換行符號 /n 去掉 #split 切割 用, 當切割的標準
			#name = s[0]
			#price = s[1]
			products.append([name , price])
		print(products)
	return products



	 
	
	
 #讀取檔案



# 2 維度清單，讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1])

#字串可以做加乘
#'abc'+'123'='abc123'
#'abc'*3 = 'abcabcabc'

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: # 'w' 是寫入模式 # as 當作
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #f.wtite 才能真正寫入
#encoding='utf-8' 最廣泛使用的編碼

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 作業系統裡path 模組的isfile功能，檢查檔案在不在
		print('Yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()