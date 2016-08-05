"""
#請使用者輸入兩個整數,並將上一頁提到的所有運算方式的結果印出
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("a+b={0}".format(a+b))
print("a-b={0}".format(a-b))
print("a*b={0}".format(a*b))
print("a/b={0}".format(a/b))
print("a//b={0}".format(a//b))
print("a%b={0}".format(a%b))
print("a**b={0}".format(a**b))
"""
"""
#請使用者輸入x的值，並計算y=10X^3+3X^2+16X
a = int(input("Enter an integer: "))
answer =  10*(a**3) + 3*(a**2) + 16*a
print(answer)
"""
"""
#請使用者輸入自己的身高和體重，並計算他的BMI值
height = int(input("Enter your height(cm): "))
weight = int(input("Enter your weight(kg): "))
bmi = weight/ ( (height/100) **2)
print(bmi)
"""
"""
#請使用者輸入x、y,列出x and y、x or y的結果
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print(a and b)
print(a or b)
"""
"""
#請使用者輸入自己的身高和體重，並計算他的BMI值
#並且同時印出使⽤者的BMI範圍為何
height = int(input("Enter your height(cm): "))
weight = int(input("Enter your weight(kg): "))
bmi = weight/ ( (height/100) **2)
print(bmi)
print("\n")
if bmi < 18.5:
	print("體重過輕")
if bmi > 24:
	print("體重過重")
else:
	print("體重適中")
"""
"""
#請使用者輸入1個正整數a，並比較100*a或a的平方哪個比較大，並把較大的結果印出
a = int(input("Enter an integer: "))
i = 100*a
j = a**2
if i>j:
	print("100*a較大，值為{0}".format(i))
else:
	print("a平方較大，值為{0}".format(j))
"""
"""
#使用者輸入階層數，印出聖誕樹
a = int(input("Please enter the number of levels: "))
for i in range(0,a):
	for j in range(0,i+1):
		print("*",end="")
	print("\n",end="")
"""
"""
#使用者輸入階層數，印出倒過來的聖誕樹
a = int(input("Please enter the number of levels: "))
for i in range(0,a):
	for j in range(0,i):
		print(" ",end="")
	for k in range(0,a-i):
		print("*",end="")
	print("\n",end="")
"""
"""
#使用者輸入階層數，印出完整的聖誕樹
a = int(input("Please enter the number of levels: "))
for i in range(0,a+1):
	for j in range(0,a-i):
		print(" ",end="")
	for k in range(0,2*i-1):
		print("*",end="")
	print("\n",end="")
"""
#使用者輸入半徑大小，畫出一個圓形
"""
#請用for迴圈印出這個每個直轄市對應的市長名字
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]	
mayor= ["柯文哲","朱立倫","鄭文燦","林佳龍","賴清德","陳菊"]	
for i in range(0,len(country)):
	print(country[i],mayor[i])
"""
"""
#請使用while把使用者輸入的數轉成二進位
a = int(input("Enter an integer: "))
b=[]
while a>0:
	if a%2==0:
		b.append(0)
	if a%2==1:
		b.append(1)
	a=a/2
for i in range(len(b)-1,-1,-1):
	print(b[i],end="")
"""
#有1、2、3、4個數字，能組成多少個互不相同且無重複數字的三位數?這些三位數各是多少?
#請使用者輸入某年某月某日（格式為mm-dd），請判斷這一天是這一年的第幾天
#請用for和while輸出9*9乘法表

#請判斷101-200之間有多少個質數，並輸出所有質數
"""
#請設計一個程式，讓使用者可以連續輸入學生的數學成績，直到輸入的值為-1時停只，並把剛剛的數學成績存成一個list印出來
score=[];
while True:
	a = int(input("Enter a math score ,enter -1 to end: "))
	if a==-1:
		break
	else:
		score.append(a)
print(score)
"""
"""
lst = range(1,101)
comprehension_list = [num for num in lst if num % 11 == 0]
print(comprehension_list)
"""
"""
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]	
mayor = ["柯文哲","朱立倫","鄭文燦","林佳龍","賴清德","陳菊"]
dic = {cou:may for cou,may in zip(country,mayor)}
print(dic)	
"""
"""
names = ['caterpillar', 'justin', 'openhome']
passwds = [123456, 654321, 13579]
print({name : passwd for name, passwd in zip(names, passwds)})	
"""
"""
#試著把下面的list寫進一個叫做country.txt的檔案中，每印出一個城市名字就換一行
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
i=0
with open("country.txt","a") as f:
	while i<len(country):
		f.write(country[i]+"\n")
		i+=1	
"""
"""
#請先把下面這兩個list組合成一個dict（還記得zip嗎～）
#然後把這個dict寫進剛剛的CM.txt，不可以覆蓋剛剛已經存在的內容，把新的內容加在
#原本內容的後面
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]	
mayor = ["柯文哲","朱立倫","鄭文燦","林佳龍","賴清德","陳菊"]
dic = {cou:may for cou,may in zip(country,mayor)}
with open("country.txt","a") as f:
	for cou , may in dic.items():
		f.write(cou + ":" + may + "\n")
"""
#打開一個空的文件nine.txt，並把九九乘法寫入該文件
#去網路上隨便找一篇新聞，把該新聞存成news.txt，並且使用python讀檔並去除新聞內所有英文及數字後存檔
#新增一個空白資料夾，在裡面新增365個空白文件，每個⽂件請命名為”月份-日.txt”並在文件內寫入該文件檔名是屬於一年中的第幾天










	


