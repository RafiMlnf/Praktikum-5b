# Praktikum 5b

> Flowchart  

![00](https://user-images.githubusercontent.com/115614668/207367487-636ccdd4-9065-42de-a645-9a150c6b728d.png)

# Penjelasan
> Berikan deklarasi yang berisikan _dictionary_ kosong yang akan diisi sebuah data.

```python
data_mahasiswa = {}
```

> Terdapat sebuah metode perulangan `while` yang kondisinya `True` artinya, dalam perulangan itu akan terus mengulang sampai kode di dalamnya memberikan sebuah kondisi yang menggunakan metode `break`.

```python
while True:
```

> Kode ini dituliskan di dalam perulangan `while`, fungsinya user dapat menginputkan pilihan yang ada pada program dan inputan tersebut akan dibuatkan sebuah kondisi-kondisi tertentu jika menginputkan pilihan tertentu, kondisi tersebut disebut `if else`.

```python
user = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
```

> Tambahkan opsi tambah data dengan huruf "t" artinya user akan diberikan tampilan inputan seperti dibawah. Inputan-inputan tersebut dimasukkan ke dalam `dictionary` kosong dengan inputan user.

```python
if user.lower() == 't':
        os.system("cls")
        print("Tambah Data")
        nama = input("Nama           : ")
        nim = int(input("NIM            : "))
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        akhir = tugas*30/100 + uts*35/100 + uas*35/100
        data_mahasiswa[nama] = nim, uts, uas, tugas, akhir
```  
![01](https://user-images.githubusercontent.com/115614668/207361233-ce143349-ef89-472e-ab77-bf8545e9c2b3.png)

> Tambahkan opsi ubah data dengan huruf "u', maka user harus memasukkan nama yang diubahnya. Jika nama tersebut ada di dalam `dictionary`.

```python
elif user.lower() == 'u':
        os.system("cls")
        print("Ubah Data")
        nama = input("Masukkan Nama  : ")
        if nama in data_mahasiswa.keys():
            nim = int(input("NIM            : "))
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            tugas = int(input("Nilai Tugas    : "))
            akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
            data_mahasiswa[nama] = nim, uts, uas, tugas, akhir
        else:
            print(f"Nama {nama} tidak ditemukan")
```  

![02](https://user-images.githubusercontent.com/115614668/207361243-f37086fc-7242-451c-a63b-c6749b7bb67f.png)

> Jika nama tersebut tidak terdaftar di dictionary, maka akan mengirimkan pesan nama tidak ditemukan.

![03](https://user-images.githubusercontent.com/115614668/207362276-8c3436cb-62ae-410d-ad79-515fd73aba42.png)

> Tambahkan opsi hapus dengan huruf "h", maka user diharuskan mengisi data nama yang ingin di hapus. Jika nama tidak terdaftar di `dictonary`, maka akan menampilkan pesan nama tidak ditemukan.

```python
elif user.lower() == 'h':
        os.system("cls")
        print("Hapus Data")
        nama = input("Masukkan Nama  : ")
        if nama in data_mahasiswa.keys():
            del data_mahasiswa[nama]
        else:
            print(f"Nama {nama} Tidak Ditemukan")
```

> Tambahkan opsi cari dengan huruf "c", maka diharuskan mengisi data nama yang ingin di cari, data yang di cari akan mengambil data yang sudah ditambahkan pada `dictionary`, lalu ditampilkan ke user. 

```python
elif user.lower() == 'c':
        os.system("cls")
        print("Cari Data")
        nama = input("Masukkan Nama : ")
        if nama in data_mahasiswa.keys():
            print("="*73)
            print("|                             Daftar Mahasiswa                          |")
            print("="*73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*73)
            print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nama, nim, uts, uas, tugas, akhir))
            print("="*73)
        else:
            print(f"Nama {nama} Tidak Ditemukan")
```

![04](https://user-images.githubusercontent.com/115614668/207362163-c16a353e-f51a-4488-93f4-87a20512669e.png)  

> Jika nama tersebut tidak ada pada data _dictionary_, maka akan menampilkan pesan nama tidak ditemukan.

![05](https://user-images.githubusercontent.com/115614668/207362174-074c83e1-4124-40d0-8019-cf95e1e7f38d.png)  

> Tambahkan opsi lihat data dengan huruf "l", maka user akan diberikan tampilan daftar mahasiswa yang sudah ditambahkan. 

```python
elif user.lower() == 'l':
        os.system("cls")
        if data_mahasiswa.items():
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for data in data_mahasiswa.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(data[0], data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], no=i))
            print("=" * 78)
        else:
            os.system("cls")
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)
```

![06](https://user-images.githubusercontent.com/115614668/207362249-19b0b4b1-d68a-4871-a095-12505a90c6ce.png)

> Jika data sebelumnya belum ditambahkan, akan menampilkan tidak ada data.

![07](https://user-images.githubusercontent.com/115614668/207362156-d7be17ad-1eee-44af-bcb9-a91401c71bc9.png)

> Tambahkan opsi keluar dengan huruf "k", maka program akan berakhir, fungsi dari `break` akan memberhentikan program tersebut.

```python
elif user.lower() == 'k':
        os.system("cls")
        break
```

> Jika tidak menginputkan apapun di dalam program, maka akan menampilkan pesan "Pilih menu yang tersedia".

```python
else:
        print("Pilih menu yang tersedia")
```
