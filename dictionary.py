# Adalah pasangan key-value nya, yang indeksnya bisa dirubah dari numerik menjadi tipe data lainnya
# contoh 
dict = {'Name' : ['Rafi', 'Don'],
		'Age' : 19,
		'Class' : ['TIA4']
		}
print("dict[\"Name\"] : ", dict['Name'])
# ouput: dict["Name"] : Rafi

# Mengakses nilai pada dictionary
# name = dict['Name']
# print(name)
# output : Rafi
# clas = dict.get("Class")
# print(clas)
# output : TIA4

# Menghapus element dictionary
# del dict['Name']
# print(dict)
# output : {'Age': 19, 'Class': 'TIA4'}
# dict.clear()
# print(dict)
# output : {}

# Menambahkan 
dict.update({"Country": "Indonesian"}) # menambahkan key-value terbaru
print(dict)