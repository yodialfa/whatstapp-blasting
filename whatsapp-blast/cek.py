import pandas as pd

# a = 'andi'
# f = open("message.txt", "r", encoding="utf8")
# message = f.read()
# message = quote('Hi,',a,message)
# print(message)
name = 'yodi'
message = f'Hi, {name} '
baca_nomor = pd.read_excel("phone.xlsx")
numb = baca_nomor['phone']
name = baca_nomor['name']
for i,j in zip(numb,name):
    print(i, message)
    print(j)