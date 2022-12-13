# Membuat dictionary daftar kontak 
data = {
	"Rafi": "0896",
	"Don": "0896"
}
print(data)
# output : {'Rafi': '0896', 'Don': '0896'}

# Menampilkan kontak milik Don
print(data['Don'])
# output: 0896

# Menambahkan kontak baru
data.update({'Reza': '0869'})
print(data)
# output : {'Rafi': '0896', 'Aji': '0896', 'Reza': '0869'}

# Ubah kontak don dengan nomor baru
data['Don'] = '0800'
print(data)
# output : {'Rafi': '0896', 'Don': '0800', 'Reza': '0869'}

# Menghaous kontak Reza
del data['Reza']
print(data)
# output : {'Rafi': '0812', 'Don': '0889'}

# Menampilkan seluruh nama
for data in data.items():
	print(data[0])
	print(data[1])
# output: Rafi Don  Reza
# output: 0896 0800 0869