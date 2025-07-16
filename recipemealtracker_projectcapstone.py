password = {"molly":'123a56t','akusiapa':'hepibgt','akunku':'purwadhik','fred':'passwordku','masak':'resepku','cookbook':'mas4kmasak','buat_akun':'20019t','iniaku':'090823'}


resep_ku = [
    {
        "id_resep": 1,
        "nama": "ayam kecap",
        "kategori": "main",
        "bahan": [
            {"nama_bahan": "Dada ayam", "jumlah": 200, "satuan": "gram", "kalori_per_unit": 2.4, "harga_per_unit": 0.02},
            {"nama_bahan": "Kecap manis", "jumlah": 2, "satuan": "sdm", "kalori_per_unit": 20, "harga_per_unit": 500}
        ],
        "instruksi": "Tumis ayam dengan kecap hingga matang.",
        "dibuat_oleh": "aku",
        "time_minutes": 25,
        "rating": 4,
        "favorit": True,
        "tingkat_kesulitan" : "menengah",
        "is_shared": False
    },
    {
        "id_resep": 2,
        "nama": "puding cokelat",
        "kategori": "dessert",
        "bahan": [
            {"nama_bahan": "Susu cair", "jumlah": 500, "satuan": "ml", "kalori_per_unit": 0.64, "harga_per_unit": 0.015},
            {"nama_bahan": "Cokelat bubuk", "jumlah": 3, "satuan": "sdm", "kalori_per_unit": 25, "harga_per_unit": 1000},
            {"nama_bahan": "Gula pasir", "jumlah": 2, "satuan": "sdm", "kalori_per_unit": 48, "harga_per_unit": 300}
        ],
        "instruksi": "Masak semua bahan sambil diaduk hingga mengental, lalu dinginkan.",
        "dibuat_oleh": "aku",
        "time_minutes": 15,
        "rating": 5,
        "favorit": True,
        "tingkat_kesulitan": "mudah",
        "is_shared": False
    },
    {
        "id_resep": 3,
        "nama": "es jeruk",
        "kategori": "drink",
        "bahan": [
            {"nama_bahan": "Jeruk peras", "jumlah": 2, "satuan": "buah", "kalori_per_unit": 45, "harga_per_unit": 1500},
            {"nama_bahan": "Air", "jumlah": 100, "satuan": "ml", "kalori_per_unit": 0, "harga_per_unit": 0},
            {"nama_bahan": "Es batu", "jumlah": 5, "satuan": "kotak", "kalori_per_unit": 0, "harga_per_unit": 0}
        ],
        "instruksi": "Peras jeruk, campur air dan es batu, aduk rata.",
        "dibuat_oleh": "aku",
        "time_minutes": 5,
        "rating": 4,
        "favorit": False,
        "tingkat_kesulitan": "mudah",
        "is_shared": False
    },
    {
        "id_resep": 4,
        "nama": "roti isi selai",
        "kategori": "snack",
        "bahan": [
            {"nama_bahan": "Roti tawar", "jumlah": 2, "satuan": "lembar", "kalori_per_unit": 65, "harga_per_unit": 1500},
            {"nama_bahan": "Selai stroberi", "jumlah": 1, "satuan": "sdm", "kalori_per_unit": 50, "harga_per_unit": 800}
        ],
        "instruksi": "Oleskan selai di antara dua roti, sajikan langsung.",
        "dibuat_oleh": "aku",
        "time_minutes": 3,
        "rating": 3,
        "favorit": False,
        "tingkat_kesulitan": "mudah",
        "is_shared": False
    },
    {
        "id_resep": 5,
        "nama": "tumis buncis",
        "kategori": "side",
        "bahan": [
            {"nama_bahan": "Buncis", "jumlah": 100, "satuan": "gram", "kalori_per_unit": 0.31, "harga_per_unit": 0.015},
            {"nama_bahan": "Bawang putih", "jumlah": 2, "satuan": "siung", "kalori_per_unit": 5, "harga_per_unit": 200},
            {"nama_bahan": "Minyak goreng", "jumlah": 1, "satuan": "sdm", "kalori_per_unit": 120, "harga_per_unit": 400}
        ],
        "instruksi": "Tumis bawang putih dan buncis sampai matang.",
        "dibuat_oleh": "aku",
        "time_minutes": 10,
        "rating": 4,
        "favorit": True,
        "tingkat_kesulitan": "sulit",
        "is_shared": False
    }
]



resep_lain = [
    {
        "id_resep": 1,
        "nama": "spaghetti aglio olio",
        "kategori": "main",
        "bahan": [
            {"nama_bahan": "Spaghetti", "jumlah": 100, "satuan": "gram", "kalori_per_unit": 3.6, "harga_per_unit": 0.025},
            {"nama_bahan": "Bawang putih", "jumlah": 3, "satuan": "siung", "kalori_per_unit": 5, "harga_per_unit": 200},
            {"nama_bahan": "Minyak zaitun", "jumlah": 2, "satuan": "sdm", "kalori_per_unit": 119, "harga_per_unit": 1000}
        ],
        "instruksi": "Tumis bawang, campur spaghetti matang dengan minyak.",
        "dibuat_oleh": "alexa",
        "time_minutes": 15,
        "rating": 4,
        "favorit": False,
        "tingkat_kesulitan": "sulit",
        "is_shared": True
    },
    {
        "id_resep": 2,
        "nama": "pisang goreng cokelat",
        "kategori": "dessert",
        "bahan": [
            {"nama_bahan": "Pisang", "jumlah": 2, "satuan": "buah", "kalori_per_unit": 89, "harga_per_unit": 3000},
            {"nama_bahan": "Cokelat batangan", "jumlah": 20, "satuan": "gram", "kalori_per_unit": 5.2, "harga_per_unit": 150},
            {"nama_bahan": "Minyak goreng", "jumlah": 1, "satuan": "sdm", "kalori_per_unit": 120, "harga_per_unit": 400}
        ],
        "instruksi": "Masukkan cokelat ke pisang lalu goreng.",
        "dibuat_oleh": "bayu",
        "time_minutes": 12,
        "rating": 5,
        "favorit": True,
        "tingkat_kesulitan": "mudah",
        "is_shared": True
    },
    {
        "id_resep": 3,
        "nama": "jus alpukat",
        "kategori": "drink",
        "bahan": [
            {"nama_bahan": "Alpukat", "jumlah": 1, "satuan": "buah", "kalori_per_unit": 160, "harga_per_unit": 5000},
            {"nama_bahan": "Susu kental manis", "jumlah": 1, "satuan": "sdm", "kalori_per_unit": 60, "harga_per_unit": 500},
            {"nama_bahan": "Es batu", "jumlah": 5, "satuan": "kotak", "kalori_per_unit": 0, "harga_per_unit": 0}
        ],
        "instruksi": "Blender semua bahan hingga lembut.",
        "dibuat_oleh": "citra",
        "time_minutes": 7,
        "rating": 4,
        "favorit": False,
        "tingkat_kesulitan": "mudah",
        "is_shared": True
    },
    {
        "id_resep": 4,
        "nama": "kue cubit",
        "kategori": "snack",
        "bahan": [
            {"nama_bahan": "Tepung terigu", "jumlah": 100, "satuan": "gram", "kalori_per_unit": 3.6, "harga_per_unit": 0.02},
            {"nama_bahan": "Telur", "jumlah": 1, "satuan": "butir", "kalori_per_unit": 70, "harga_per_unit": 2500},
            {"nama_bahan": "Gula", "jumlah": 2, "satuan": "sdm", "kalori_per_unit": 48, "harga_per_unit": 300}
        ],
        "instruksi": "Aduk adonan lalu panggang setengah matang.",
        "dibuat_oleh": "dedi",
        "time_minutes": 10,
        "rating": 5,
        "favorit": False,
        "tingkat_kesulitan": "menengah",
        "is_shared": True
    },
    {
        "id_resep": 5,
        "nama": "sambal matah",
        "kategori": "side",
        "bahan": [
            {"nama_bahan": "Bawang merah", "jumlah": 5, "satuan": "butir", "kalori_per_unit": 5, "harga_per_unit": 300},
            {"nama_bahan": "Cabai rawit", "jumlah": 10, "satuan": "buah", "kalori_per_unit": 4, "harga_per_unit": 200},
            {"nama_bahan": "Minyak kelapa", "jumlah": 2, "satuan": "sdm", "kalori_per_unit": 120, "harga_per_unit": 800}
        ],
        "instruksi": "Iris bahan, siram minyak panas, aduk rata.",
        "dibuat_oleh": "eka",
        "time_minutes": 5,
        "rating": 4,
        "favorit": False,
        "tingkat_kesulitan": "mudah",
        "is_shared": True
    },
    {
        "id_resep": 6,
        "nama": "telur dadar bayam",
        "kategori": "main",
        "bahan": [
            {"nama_bahan": "Telur", "jumlah": 2, "satuan": "butir", "kalori_per_unit": 70, "harga_per_unit": 2500},
            {"nama_bahan": "Bayam", "jumlah": 50, "satuan": "gram", "kalori_per_unit": 0.2, "harga_per_unit": 0.015},
            {"nama_bahan": "Minyak", "jumlah": 1, "satuan": "sdm", "kalori_per_unit": 120, "harga_per_unit": 400}
        ],
        "instruksi": "Kocok telur dan bayam lalu goreng.",
        "dibuat_oleh": "fina",
        "time_minutes": 8,
        "rating": 4,
        "favorit": False,
        "tingkat_kesulitan": "menengah",
        "is_shared": True
    },
    {
        "id_resep": 7,
        "nama": "sup jagung",
        "kategori": "side",
        "bahan": [
            {"nama_bahan": "Jagung manis", "jumlah": 100, "satuan": "gram", "kalori_per_unit": 0.96, "harga_per_unit": 0.02},
            {"nama_bahan": "Wortel", "jumlah": 50, "satuan": "gram", "kalori_per_unit": 0.4, "harga_per_unit": 0.015},
            {"nama_bahan": "Kaldu ayam", "jumlah": 250, "satuan": "ml", "kalori_per_unit": 0.3, "harga_per_unit": 0.01}
        ],
        "instruksi": "Rebus semua bahan sampai matang dan empuk.",
        "dibuat_oleh": "gilang",
        "time_minutes": 20,
        "rating": 5,
        "favorit": True,
        "tingkat_kesulitan": "menengah",
        "is_shared": True
    }
]



def create_recipe() : 
    while True: 
        back = False
        print("Anda mau menambah resep! Silakan pilih dari 3 pilihan di bawah")
        print("1. Tambah Resep untuk Koleksi Resep Masakan Pribadi")
        print("2. Share Resep dari Koleksi Resep Makanan Pribadi ke Resep Makanan Publik")
        print("3. Kembali ke Menu Utama")
        while True: 
            input_menu_create = input('Silakan pilih no 1, 2, atau 3 : ')
            if input_menu_create.isdigit(): 
                input_menu_create = int(input_menu_create)
                if input_menu_create == 1: 
                    print('Anda mau menambah resep untuk koleksi resep makanan pribadi. Tolong isi berikut')
                    nama = input('nama makanan : ').lower().strip()
                    while True : 
                        time_min = input('lama pembuatan (menit), jika diisi dengan bukan angka bulat maka nanti akan dibulatkan: ')
                        if time_min.isdigit(): 
                            time_min = int(time_min)
                            break
                        else : 
                            print('harus ditulis dalam angka')
                            continue
                    
                    while True: 
                        rating = input('rate masakan (1-5), tidak boleh pakai koma atau titik: ')
                        if rating.isdigit():
                            rating = int(rating)
                            if rating in [1,2,3,4,5]:
                                break
                            else : 
                                print('rating harus berada dalam pilihan angka 1 hingga 5, tidak pakai koma atau titik, tolong isi kembali')
                                continue
                        else : 
                            print('rating harus berbentuk angka, tidak pakai koma atau titik, tolong ulangi')
                            continue
                    while True : 
                        fav = input("Untuk kategori favorit \n1. Favorite \n2. Tidak Favorite \nTolong pilih nomor dari pilihan tersedia: ")
                        if fav.isdigit():
                            fav = int(fav)
                            if fav == 1 : 
                                fav = True
                                break
                            elif fav == 2:
                                fav = False
                                break
                            else:
                                print("harus diisi dengan angka 1 atau 2, tolong isi kembali")
                                continue
                        else : 
                            print('input harus berupa angka, tolong isi kembali')
                            continue
                    while True: 
                        kesulitan = input('Untuk kategori tingkat kesulitan\n1. sulit\n2. menengah\n3. mudah\nTolong pilih nomor dari pilihan tersedia : ')
                        if kesulitan.isdigit() : 
                            kesulitan = int(kesulitan)
                            if kesulitan == 1:
                                kesulitan = 'sulit'
                                break
                            elif kesulitan == 2:
                                kesulitan = 'menengah'
                                break
                            elif kesulitan == 3:
                                kesulitan = 'mudah'
                                break
                            else:
                                print('harus diisi dengan pilihan angka (1/2/3), tolong ulangi')
                                continue
                        else : 
                            print('input harus diisi dengan angka, tolong ulangi')
                            continue
                    share = False
                    dibuat_oleh = 'aku'
                    instruksi = input('Tulis instruksi disini : ')
                    while True : 
                        kategori = input('Untuk pilihan kategori makanan \n1. main\n2. drink\n3. dessert\n4. snack\n5. side\nTolong pilih nomor dari pilihan tersedia: ')
                        if kategori.isdigit() : 
                            kategori = int(kategori)
                            if kategori == 1 : 
                                kategori = 'main'
                                break
                            elif kategori == 2: 
                                kategori = 'drink'
                                break
                            elif kategori == 3:
                                kategori = 'dessert'
                                break
                            elif kategori == 4: 
                                kategori = 'snack'
                                break
                            elif kategori == 5: 
                                kategori = 'side'
                                break
                            else : 
                                print('input harus diisi dengan pilihan (1/2/3/4/5), tolong isi ulang')
                                continue
                        else: 
                            print('input harus diisi dengan angka, tolong isi ulang')
                            continue
                    idresep = len(resep_ku)+1
                    while True:
                        jumlah_bahan = input('mau input berapa bahan : ')
                        if jumlah_bahan.isdigit():
                            jumlah_bahan = int(jumlah_bahan)
                            bahan = []
                            for j in range(jumlah_bahan):
                                nama_bahan = input("tulis nama bahan: ").capitalize().strip()
                                while True:
                                    jmlh = input("tulis jumlah : ")
                                    if jmlh.isdigit():
                                        jmlh = int(jmlh)
                                        break
                                    else:
                                        print('tolong ulangi, harus diisi dengan angka')
                                        continue
                                satuan = input("tulis nama satuan: ").lower().strip()
                                while True:
                                    kalori_per_unit = input("tulis jumlah kalori per unit: ").strip()
                                    try : 
                                        kalori_per_unit = float(kalori_per_unit)
                                        break
                                    except ValueError:
                                        print("tolong ulangi, input harus diisi dengan angka") 

                                while True:
                                    harga_per_unit = input("tulis jumlah harga per unit: ").strip()
                                    try : 
                                        harga_per_unit = float(harga_per_unit)
                                        break
                                    except ValueError:
                                        print("tolong ulangi, input harus diisi dengan angka") 

                                bahan.append({"nama_bahan":nama_bahan, "jumlah":jmlh, "satuan":satuan, "kalori_per_unit":kalori_per_unit, "harga_per_unit":harga_per_unit})
                                print(bahan)
                            break
                        else: 
                            print('input jumlah bahan harus berupa angka, tolong ulangi')
                            continue
                    while True:
                        create_atau_tidak = input('apakah anda yakin mau menambahkan?\nKetik 1 jika yakin dan ketik 0 jika tidak jadi menambahkan : ')
                        if create_atau_tidak.isdigit():
                            create_atau_tidak = int(create_atau_tidak)
                            if create_atau_tidak == 1:
                                resep_ku.append({"id_resep":idresep, "nama":nama, "kategori": kategori, "bahan":bahan, "instruksi":instruksi, "dibuat_oleh":dibuat_oleh, "time_minutes":time_min, "rating":rating, "favorit":fav, "tingkat_kesulitan":kesulitan, "is_shared":share})
                                print('resep sudah ditambahkan! ')
                                break
                            elif create_atau_tidak == 0 : 
                                print('resep tidak jadi ditambahkan! ')
                                break
                            else:
                                print('harus diinput dengan 1 atau 0, tolong ulangi')
                                continue
                        else:
                            print('input harus angka tolong ulangi')
                            continue
                    break
                elif input_menu_create == 2 : 
                    print('Silakan pilih resep dari koleksi pribadi anda yang ingin dishare')
                    print(f'{"id resep":<10} | {"nama makanan":<20} | {"share":<6}')
                    print('-' * 45)
                    for j in range(len(resep_ku)):
                        print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {str(resep_ku[j]["is_shared"]):<6}')
                    while True:
                        id_share = input('ketik id resep disini : ')
                        if id_share.isdigit():
                            id_share = int(id_share)
                            if 0 < id_share <= len(resep_ku):
                                break
                            else : 
                                print('id yang diinput diluar indeks database yang ada, tolong ulangi')
                                continue
                        else : 
                            print('id yang diinput harus berupa angka, tolong ulangi')
                            continue
                    while True:
                        yakin = input("apakah anda yakin mau share? ketik 1 jika yakin dan ketik 0 jika tidak jadi share : ")
                        if yakin.isdigit():
                            yakin = int(yakin)
                            if yakin == 1 : 
                                if resep_ku[(id_share-1)]["is_shared"] == True: 
                                    print("resep sudah pernah dishare. Anda akan balik ke menu sebelumnya.")
                                    break
                                resep_ku[(id_share-1)]["is_shared"] = True
                                resep_lain.append(resep_ku[(id_share-1)])
                                print('resep sudah dishare')
                                break
                            elif yakin == 0:
                                print('resep tidak jadi dishare')
                                break
                            else : 
                                print('angka harus berupa 1 atau 0, tolong ulangi')
                                continue
                        else : 
                            print('input harus berupa angka, tolong ulangi')
                            continue
                    break
                elif input_menu_create == 3 :
                    print("anda mau kembali ke menu utama")
                    back = True
                    break
                else : 
                    print('input harus berupa nomor 1, 2, atau 3. tolong ulangi')
                    continue
            else : 
                print('input harus berupa angka tolong ulangi')
                continue       
        if back == True:
            break            
                               

def input_kategori_untuk_browse_recipes(resep_ku) : 
    while True:
        idlist_kategori = []
        input_kategori = input("silakan pilih kategori makanan!\n1. main\n2. dessert\n3. snack\n4. drink\n5. side\nTolong ketik disini : ")
        if input_kategori.isdigit():
            input_kategori = int(input_kategori)
            if input_kategori == 1:
                for i in range(len(resep_ku)):
                    if resep_ku[i]["kategori"] == 'main':
                        idlist_kategori.append(resep_ku[i]['id_resep'])

                if len(idlist_kategori) == 0:
                    print("tidak ada menu makanan di kategori ini")
                    break

                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)

                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kategori:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {resep_ku[j]["favorit"]:<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                        
                break
            elif input_kategori == 2:
                for i in range(len(resep_ku)):
                    if resep_ku[i]["kategori"] == 'dessert':
                        idlist_kategori.append(resep_ku[i]['id_resep'])
                if len(idlist_kategori) == 0:
                    print("tidak ada menu makanan di kategori ini")
                    break

                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)

                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kategori:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {resep_ku[j]["favorit"]:<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                            
                break
            elif input_kategori == 3:
                for i in range(len(resep_ku)):
                    if resep_ku[i]["kategori"] == 'snack':
                        idlist_kategori.append(resep_ku[i]['id_resep'])
                if len(idlist_kategori) == 0:
                    print("tidak ada menu makanan di kategori ini")
                    break

                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kategori:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {resep_ku[j]["favorit"]:<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            elif input_kategori == 4:
                for i in range(len(resep_ku)):
                    if resep_ku[i]["kategori"] == 'drink':
                        idlist_kategori.append(resep_ku[i]['id_resep'])
                if len(idlist_kategori) == 0:
                    print("tidak ada menu makanan di kategori ini")
                    break

                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kategori:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {resep_ku[j]["favorit"]:<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            elif input_kategori == 5:
                for i in range(len(resep_ku)):
                    if resep_ku[i]["kategori"] == 'side':
                        idlist_kategori.append(resep_ku[i]['id_resep'])
                if len(idlist_kategori) == 0:
                    print("tidak ada menu makanan di kategori ini")
                    break
                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kategori:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {resep_ku[j]["favorit"]:<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            else : 
                print("input harus berada di pilihan nomor 1, 2, 3, 4, atau 5. Tolong ulangi")
                continue
        else: 
            print("input harus berupa angka, tolong ulangi")
            continue

def input_tingkat_kesulitan_browse_recipe(resep_ku) : 
    while True: 
        idlist_kesulitan = []
        input_kesulitan = input("1. mudah\n2. menengah\n3. sulit\nTolong ketik pilihan anda : ")
        if input_kesulitan.isdigit():
            input_kesulitan = int(input_kesulitan)
            if input_kesulitan == 1 : 
                for i in range(len(resep_ku)): 
                    if resep_ku[i]["tingkat_kesulitan"] == "mudah": 
                        idlist_kesulitan.append(resep_ku[i]["id_resep"])
                if len(idlist_kesulitan) == 0:
                    print("tidak ada menu makanan di tingkat kesulitan ini")
                    break
                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kesulitan:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {str(resep_ku[j]["favorit"]):<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            elif input_kesulitan == 2:
                for i in range(len(resep_ku)): 
                    if resep_ku[i]["tingkat_kesulitan"] == "menengah": 
                        idlist_kesulitan.append(resep_ku[i]["id_resep"])
                if len(idlist_kesulitan) == 0:
                    print("tidak ada menu makanan di tingkat kesulitan ini")
                    break
                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kesulitan:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {str(resep_ku[j]["favorit"]):<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            elif input_kesulitan == 3:
                for i in range(len(resep_ku)): 
                    if resep_ku[i]["tingkat_kesulitan"] == "sulit": 
                        idlist_kesulitan.append(resep_ku[i]["id_resep"])
                if len(idlist_kesulitan) == 0:
                    print("tidak ada menu makanan di tingkat kesulitan ini")
                    break
                print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                print('-' * 95)
                for j in range(len(resep_ku)):
                    if resep_ku[j]["id_resep"] in idlist_kesulitan:
                        for g in range(len(resep_ku[j]["bahan"])):
                            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {str(resep_ku[j]["favorit"]):<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
                break
            else : 
                print('input tingkat kesulitan harus berupa angka 1,2, atau 3. Tolong ulangi')
                continue
        else:
            print("input harus berupa angka, tolong ulangi")
            continue

def fav(resep_ku) : 
    idlist_fav = []
    for i in range(len(resep_ku)): 
        if resep_ku[i]["favorit"] == True: 
            idlist_fav.append(resep_ku[i]["id_resep"])
    if len(idlist_fav) == 0:
        print("tidak ada menu makanan favorit dalam koleksi pribadi anda")
    else:   
        print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
        print('-' * 95)
        for j in range(len(resep_ku)):
            if resep_ku[j]["id_resep"] in idlist_fav:
                for g in range(len(resep_ku[j]["bahan"])):
                    print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][g]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][g]["jumlah"]:<10} | {resep_ku[j]["bahan"][g]["satuan"]:<10} | {resep_ku[j]["bahan"][g]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][g]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {str(resep_ku[j]["favorit"]):<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
        

def total_biaya_per_resep(resep_ku):
    dict_biaya = []
    for k in range(len(resep_ku)):
        jumlah_biaya = 0
        for m in range(len(resep_ku[k]["bahan"])):
            jumlah_biaya += resep_ku[k]["bahan"][m]["jumlah"] * resep_ku[k]["bahan"][m]["harga_per_unit"]
        dict_biaya.append({k:jumlah_biaya})
    print(f'{"id resep":<10} | {"nama":<20} | {"total biaya":<10}')
    print('-' * 50)
    for k in range(len(dict_biaya)):
        print(f'{resep_ku[k]["id_resep"]:<10} | {resep_ku[k]["nama"]:<20} | {dict_biaya[k][k]:<10}')
    
def total_kalori_per_resep(resep_ku):
    dict_kalori = []
    for k in range(len(resep_ku)):
        jumlah_kalori = 0
        for m in range(len(resep_ku[k]["bahan"])):
            jumlah_kalori += resep_ku[k]["bahan"][m]["jumlah"] * resep_ku[k]["bahan"][m]["kalori_per_unit"]
        dict_kalori.append({k:jumlah_kalori})
    print(f'{"id resep":<10} | {"nama":<20} | {"total biaya":<10}')
    print('-' * 50)
    for k in range(len(dict_kalori)):
        print(f'{resep_ku[k]["id_resep"]:<10} | {resep_ku[k]["nama"]:<20} | {dict_kalori[k][k]:<10}')
    
def lihat_semua_resep(resep_ku):
    print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"favorit":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
    print('-' * 95)
    for j in range(len(resep_ku)):
        for h in range(len(resep_ku[j]["bahan"])):
            print(f'{resep_ku[j]["id_resep"]:<10} | {resep_ku[j]["nama"]:<20} | {resep_ku[j]["kategori"]:<10} | {resep_ku[j]["bahan"][h]["nama_bahan"]:<10} | {resep_ku[j]["bahan"][h]["jumlah"]:<10} | {resep_ku[j]["bahan"][h]["satuan"]:<10} | {resep_ku[j]["bahan"][h]["kalori_per_unit"]:<10} | {resep_ku[j]["bahan"][h]["harga_per_unit"]:<10} | {str(resep_ku[j]["instruksi"]):<20} | {resep_ku[j]["dibuat_oleh"]:<10} | {resep_ku[j]["time_minutes"]:<10} | {resep_ku[j]["rating"]:<10} | {str(resep_ku[j]["favorit"]):<10} | {resep_ku[j]["tingkat_kesulitan"]:<10} | {str(resep_ku[j]["is_shared"]):<6}')
        


def browse_recipes() : 
        
    while True:
        print("Anda mau melihat-lihat resep! Silakan pilih dari menu berikut")
        print("1. Browsing Recipes dari koleksi pribadi")
        print("2. Browsing Recipes dari koleksi umum")
        print("3. Kembali ke menu awal")
        menu_browse = input("silakan ketik pilihan nomor menu : ")
        if menu_browse.isdigit() : 
            menu_browse = int(menu_browse)
            if menu_browse == 1:
                
                while True:
                    print("anda mau browsing resep dari koleksi pribadi anda")
                    if len(resep_ku) == 0:
                        print("anda tidak punya koleksi pribadi")
                        break
                    print("1. Browsing semua resep")
                    print("2. Browsing berdasarkan kata kunci")
                    print("3. kembali")
                    menu_browse_pribadi = input("silakan ketik pilihan nomor menu : ")
                    if menu_browse_pribadi.isdigit() : 
                        menu_browse_pribadi = int(menu_browse_pribadi)
                        if menu_browse_pribadi == 1 : 
                            
                            print("berikut semua koleksi resep pribadi anda!")
                            lihat_semua_resep(resep_ku)
                               
                            
                        elif menu_browse_pribadi == 2:
                            
                            while True:
                                print("Apa yang ingin Anda lakukan dengan koleksi pribadi Anda?")
                                print("1. Cari berdasarkan kategori makanan (main/dessert/snack/drink/side)")
                                print("2. Cari berdasarkan tingkat kesulitan (mudah/menengah/sulit)")
                                print("3. Lihat menu favorit")
                                print("4. Tampilkan total biaya untuk tiap resep")
                                print("5. Tampilkan total kalori untuk tiap resep")
                                print("6. Kembali")
                                pilih = input("silakan ketik nomor pilihan disini : ")
                                if pilih.isdigit(): 
                                    pilih = int(pilih)
                                    if pilih == 1: 
                                        input_kategori_untuk_browse_recipes(resep_ku)
                                        
                                    elif pilih == 2:
                                        print("silakan pilih tingkat kesulitan!")
                                        input_tingkat_kesulitan_browse_recipe(resep_ku)

                                    elif pilih == 3:
                                        print("anda akan melihat menu favorit dari koleksi pribadi anda")
                                        fav(resep_ku)
                                        continue

                                    elif pilih == 4:
                                        print('anda akan melihat total biaya per resep!')
                                        total_biaya_per_resep(resep_ku)
                                        continue

                                    elif pilih == 5:
                                        print('anda akan melihat total kalori per resep!')
                                        total_kalori_per_resep(resep_ku)
                                        continue

                                    elif pilih == 6:
                                        print("anda akan kembali")
                                        
                                        break
                                    else:
                                        print('harus diisi dengan no 1,2,3,4,5, atau 6. tolong ulangi')
                                        continue
                                else : 
                                    print("harus diisi dengan angka, tolong ulangi")
                                    continue
                            

                        elif menu_browse_pribadi == 3 : 
                            #
                            print("anda akan kembali")
                            break
                        else: 
                            print("input harus diisi dengan nomor 1, 2, atau 3. Tolong ulangi")
                            continue
                    else : 
                        print("input harus berupa angka, tolong ulangi")
                        continue
                
            elif menu_browse == 2 : 
                
                print('anda mau browsing resep dari koleksi umum')
                while True : 
                    if len(resep_lain) == 0: 
                        print("saat ini belum ada yang menambahkan resep masakan di koleksi umum")
                        break
                    print("1. Browsing semua resep")
                    print("2. Browsing berdasarkan kata kunci")
                    print("3. Kembali")
                    menu_browse_umum = input("silakan pilih nomor menu : ")
                    if menu_browse_umum.isdigit() : 
                        menu_browse_umum = int(menu_browse_umum)
                        if menu_browse_umum == 1 : 
                            print("berikut semua resep di koleksi umum!")
                            lihat_semua_resep(resep_lain)      

                        elif menu_browse_umum == 2 : 
                                
                            while True:
                                print("Apa yang ingin Anda lakukan dengan koleksi umum?")
                                print("1. Cari berdasarkan kategori makanan (main/dessert/snack/drink/side)")
                                print("2. Cari berdasarkan tingkat kesulitan (mudah/menengah/sulit)")
                                print("3. Lihat menu favorit")
                                print("4. Tampilkan total biaya untuk tiap resep")
                                print("5. Tampilkan total kalori untuk tiap resep")
                                print("6. Kembali")
                                pilih = input("silakan ketik nomor pilihan disini : ")
                                if pilih.isdigit():
                                    pilih = int(pilih)
                                    if pilih == 1 :
                                        
                                        input_kategori_untuk_browse_recipes(resep_lain)
                                    elif pilih == 2: 
                                        print("silakan pilih tingkat kesulitan!")
                                        input_tingkat_kesulitan_browse_recipe(resep_lain)

                                    elif pilih == 3 : 
                                        print("anda akan melihat resep kategori favorit dari koleksi umum!")
                                        fav(resep_lain)

                                    elif pilih == 4:
                                        print("anda akan melihat total biaya per resep!")
                                        total_biaya_per_resep(resep_lain)
                                        continue
                                    elif pilih == 5:
                                        print("anda akan melihat total kalori per resep!")
                                        total_kalori_per_resep(resep_lain)
                                        continue
                                    elif pilih == 6:
                                        print("anda akan kembali")
                                        break
                                    else : 
                                        print("input harus berupa angka 1,2,3,4,5 atau 6. Tolong ulangi")
                                        continue
                                else : 
                                    print("input harus berupa angka, tolong ulangi")
                                    continue
                        elif menu_browse_umum == 3:
                            
                            print("anda akan kembali")
                            break
                            
                    else : 
                        print("input pilihan harus berupa angka, tolong ulangi")
                        continue
                    
                    
            elif menu_browse == 3:
                print("anda akan kembali ke menu awal")
                
                break
            else: 
                print('input harus diisi dengan nomor 1, 2, atau 3, tolong ulangi')
                continue
        else : 
            print('input harus berupa angka, tolong ulangi')
            continue
    
    
def update_recipes():
    while True: 
        print('anda mau update resep! Silakan pilih dari menu berikut')
        print("1. Update Resep dari Koleksi Pribadi")
        print("2. Update Resep kategori Favorit dari Koleksi Umum")
        print("3. Kembali")
        input_menu_update = input("Silakan ketik pilihan menu disini : ")
        if input_menu_update.isdigit() : 
            input_menu_update = int(input_menu_update)
            if input_menu_update == 1 : 
                print("anda mau update resep dari koleksi pribadi anda! \nBerikut kumpulan resep anda ")
                lihat_semua_resep(resep_ku)
                
                while True :     
                    input_id_update = input("silakan masukkan id resep yang mau diupdate : ")
                    if input_id_update.isdigit() : 
                        input_id_update = int(input_id_update)
                        if 0 < input_id_update <= len(resep_ku) : 
                            if resep_ku[(input_id_update-1)]["is_shared"] == True:
                                for j in range(len(resep_lain)):
                                    if (resep_lain[j]["dibuat_oleh"] == 'aku') and (resep_lain[j]["nama"] == resep_ku[(input_id_update-1)]["nama"]):
                                        del resep_lain[j]
                                        resep_ku[(input_id_update-1)]["is_shared"] = False

                            while True : 
                                print("silakan ketik nama bagian resep yang mau diupdate!")
                                print("1. nama")
                                print("2. kategori")
                                print("3. bahan")
                                print("4. instruksi")
                                print("5. time_minutes")
                                print("6. rating")
                                print("7. favorit")
                                print("8. tingkat_kesulitan")
                                
                                bagian_resep = input("silakan ketik nama pilihan disini (e.g.: nama): ").lower().strip()
                                if bagian_resep in ["nama", "kategori","bahan", "instruksi", "time_minutes", "rating", "favorit", "tingkat_kesulitan"] : 
                                    print(f'{bagian_resep} sebelumnya : {resep_ku[(input_id_update-1)][bagian_resep]}')
                                    while True : 
                                        yakin_update = input("apakah anda yakin mau update? ketik 1 jika yakin, ketik 0 jika tidak jadi update : ")
                                        if yakin_update.isdigit() : 
                                            yakin_update = int(yakin_update)
                                            if yakin_update == 1 :
                                                while True: 
                                                    if bagian_resep != "bahan":
                                                        updat = input("ketik input baru disini : ").lower().strip()
                                                    if bagian_resep == "kategori" : 
                                                        if updat in ["main", "dessert", "snack", "drink", "side"] : 
                                                            resep_ku[(input_id_update-1)][bagian_resep] = updat
                                                            break
                                                        else : 
                                                            print("input tidak ada dalam pilihan kategori, tolong ulangi")
                                                            continue
                                                    elif bagian_resep == "rating" : 
                                                        if updat in ["1", "2", "3", "4", "5"]:
                                                            updat = int(updat)
                                                            resep_ku[(input_id_update-1)][bagian_resep] = updat
                                                            break
                                                        else : 
                                                            print("input tidak ada dalam range rating. Tolong ulangi")
                                                            continue
                                                    elif bagian_resep == "favorit":
                                                        if updat == "true":
                                                            updat = True
                                                            
                                                        elif updat == "false":
                                                            updat = False
                                                        
                                                        else : 
                                                            print("input salah. tolong ulangi")
                                                            continue
                                                        resep_ku[(input_id_update-1)][bagian_resep] = updat
                                                        break
                                                    elif bagian_resep == "tingkat_kesulitan":
                                                        if updat in ["sulit","menengah","mudah"]:
                                                            resep_ku[(input_id_update-1)][bagian_resep] = updat
                                                            break
                                                        else : 
                                                            print("input salah, tolong ulangi")
                                                            continue
                                                    elif bagian_resep == "bahan": 
                                                        while True:
                                                            jumlah_bahan = input('mau input berapa bahan : ')
                                                            if jumlah_bahan.isdigit():
                                                                jumlah_bahan = int(jumlah_bahan)
                                                                bahan = []
                                                                for j in range(jumlah_bahan):
                                                                    nama_bahan = input("tulis nama bahan: ").capitalize().strip()
                                                                    while True:
                                                                        jmlh = input("tulis jumlah : ")
                                                                        if jmlh.isdigit():
                                                                            jmlh = int(jmlh)
                                                                            break
                                                                        else:
                                                                            print('tolong ulangi, harus diisi dengan angka')
                                                                            continue
                                                                    satuan = input("tulis nama satuan: ").lower().strip()
                                                                    while True:
                                                                        kalori_per_unit = input("tulis jumlah kalori per unit: ").strip()
                                                                        try: 
                                                                            kalori_per_unit = float(kalori_per_unit)
                                                                            break
                                                                        except ValueError:
                                                                            print("tolong ulangi, input harus diisi dengan angka")
                                                                        
                                                                    while True:
                                                                        harga_per_unit = input("tulis jumlah harga per unit: ").strip()
                                                                        try : 
                                                                            harga_per_unit = float(harga_per_unit)
                                                                            break
                                                                        except ValueError:
                                                                            print("tolong ulangi, input harus diisi dengan angka") 
 
                                                                    bahan.append({"nama_bahan":nama_bahan, "jumlah":jmlh, "satuan":satuan, "kalori_per_unit":kalori_per_unit, "harga_per_unit":harga_per_unit})
                                                                    print(bahan)
                                                                break
                                                            else: 
                                                                print('input jumlah bahan harus berupa angka, tolong ulangi')
                                                                continue
                                                        resep_ku[(input_id_update-1)][bagian_resep] = bahan
                                                        break
                                                    elif bagian_resep in ["nama", "instruksi", "time_minutes"]:
                                                        resep_ku[(input_id_update-1)][bagian_resep] = updat
                                                        break
                                                    else : 
                                                        print("input bagian resep yang mau diupdate salah, tolong ulangi")
                                                        break

                                                
                                                print("resep sudah diupdate!")
                                                break
                                            elif yakin_update == 0 : 
                                                print("tidak jadi update. Anda akan kembali")
                                                break
                                            else : 
                                                print("input harus antara nomor 1 atau 0. Tolong ulangi")
                                                continue
                                        else : 
                                            print("input harus berupa angka, tolong ulangi")
                                            continue
                                    break
                                else : 
                                    print("input tidak ada dalam bagian resep, tolong ulangi")
                                    continue
                            break   


                        else : 
                            print("id yang diinput harus berada dalam indeks. Tolong ulangi")
                            continue
                    else : 
                        print("id yang diinput harus berupa angka. tolong ulangi")
                        continue 
            elif input_menu_update == 2:
                print("anda mau update resep favorit anda di koleksi resep umum!")
                lihat_semua_resep(resep_lain)
                while True :     
                    input_id_update = input("silakan masukkan id resep yang mau diupdate : ")
                    if input_id_update.isdigit() : 
                        input_id_update = int(input_id_update)
                        if 0 < input_id_update <= len(resep_lain) :
                            print(f'kategori favorit sebelumnya : {resep_lain[(input_id_update-1)]["favorit"]}')
                            while True : 
                                yakin_update = input("apakah anda yakin mau update? ketik 1 jika yakin, ketik 0 jika tidak jadi update : ")
                                if yakin_update.isdigit() : 
                                    yakin_update = int(yakin_update)
                                    if yakin_update == 1 :
                                        while True : 
                                            fav = input("Untuk kategori favorit \n1. Favorite \n2. Tidak Favorite \nTolong pilih nomor dari pilihan tersedia: ")
                                            if fav.isdigit():
                                                fav = int(fav)
                                                if fav == 1 : 
                                                    fav = True
                                                    resep_lain[(input_id_update-1)]["favorit"] = fav
                                                    print("resep favorit di koleksi umum sudah diupdate!")
                                                    break
                                                elif fav == 2:
                                                    fav = False
                                                    resep_lain[(input_id_update-1)]["favorit"] = fav
                                                    print("resep favorit di koleksi umum sudah diupdate!")
                                                    break
                                                else:
                                                    print("harus diisi dengan angka 1 atau 2, tolong isi kembali")
                                                    continue
                                            else : 
                                                print('input harus berupa angka, tolong isi kembali')
                                                continue
                                        break
                                    elif yakin_update == 0 : 
                                        print("anda tidak jadi mau update resep favorite di koleksi umum. Anda akan kembali")
                                        break
                                    else : 
                                        print("input harus bernilai 0 atau 1. Tolong ulangi")
                                        continue
                                else : 
                                    print("input harus berupa angka tolong ulangi")
                                    continue
                            break

                        else : 
                            print("input id diluar indeks, tolong ulangi")
                            continue
                    else : 
                        print("input harus berupa angka, tolong ulangi")
                        continue

            elif input_menu_update == 3 : 
                print("anda akan kembali")
                break
            else : 
                print("input harus berupa nomor 1,2 atau 3. Tolong ulangi")
                continue
        else :
            print("input harus berupa angka, tolong ulangi")
            continue


def delete_recipes() : 
    while True: 
        print('anda mau menghapus resep! Silakan pilih dari menu berikut')
        print("1. Delete Resep")
        print("2. Kembali")
        input_menu_delete = input("Silakan ketik pilihan menu disini : ")
        if input_menu_delete.isdigit() : 
            input_menu_delete = int(input_menu_delete)
            if input_menu_delete == 1 : 
                print("anda mau menghapus resep dari koleksi pribadi anda! \nBerikut kumpulan resep anda ")
                lihat_semua_resep(resep_ku)
                
                while True :     
                    input_id_del = input("silakan masukkan id resep yang mau didelete : ")
                    if input_id_del.isdigit() : 
                        input_id_del = int(input_id_del)
                        if 0 < input_id_del <= len(resep_ku) :
                            while True : 
                                yakin_update = input("apakah anda yakin mau delete? ketik 1 jika yakin, ketik 0 jika tidak jadi delete : ")
                                if yakin_update.isdigit() : 
                                    yakin_update = int(yakin_update)
                                    if yakin_update == 1 :
                                        if resep_ku[(input_id_del-1)]["is_shared"] == True:
                                            for j in range(len(resep_lain)):
                                                if (resep_lain[j]["dibuat_oleh"] == 'aku') and (resep_lain[j]["nama"] == resep_ku[(input_id_del-1)]["nama"]):
                                                    del resep_lain[j]
                                        del resep_ku[(input_id_del-1)]
                                        for p in range(len(resep_lain)):
                                            resep_lain[p]['id_resep'] = (p+1)
                                        print("resep sudah didelete!")
                                        for g in range(len(resep_ku)) : 
                                            resep_ku[g]['id_resep'] = (g+1)
                                        break
                                    elif yakin_update == 0 : 
                                        print("resep tidak jadi didelete!")
                                        break
                                    else : 
                                        print('input harus berupa 0 atau 1. tolong ulangi')
                                        continue
                                else :
                                    print('input harus berupa angka, tolong ulangi')
                                    continue
                            break
                        else :
                            print("input id resep yang mau didelete ada di luar indeks, tolong ulangi")
                            continue
                    else : 
                        print("input id harus berupa angka, tolong ulangi")
                        continue
                continue 

            elif input_menu_delete == 2 :
                print("anda akan kembali")
                break
            else : 
                print("input harus diisi dengan no 1 atau 2. tolong ulangi")
                continue
        else : 
            print("input harus berupa angka")
            continue        



## ==== program utama ====
while True:
    akun = input('Welcome! Apakah anda punya akun? \n Ketik 1 jika Iya dan 0 Jika Tidak : ')
    if akun.isdigit(): 
        akun = int(akun)
        if akun == 1: 
            while True: 
                kembali_menu_awal = False
                input_username = input("tolong masukkan username anda : ").lower().strip()
                if input_username in password:
                    while True:
                        
                        isi_ulang_pw = False
                        input_pw = input('Masukkan password: ').strip()
                        if input_pw == password[input_username]:
                            print("login berhasil!")
                            break
                        else : 
                            print("password salah. Apakah anda mau coba kembali isi password atau kembali ke menu awal?")
                            while True: 
                                kembali = input("tulis 0 untuk kembali ke menu awal dan 1 untuk isi ulang password : ")
                                if kembali.isdigit(): 
                                    kembali = int(kembali)
                                    if kembali == 0 : 
                                        print("anda kembali ke menu awal")
                                        kembali_menu_awal = True
                                        break
                                    elif kembali == 1:
                                        print('anda isi ulang password')
                                        isi_ulang_pw = True
                                        break
                                    else:
                                        print("harus diisi dengan 0 atau 1. tolong isi ulang")
                                        continue
                                else : 
                                    print('harus diisi dengan angka.')
                                    continue
                            if isi_ulang_pw == True:
                                continue
                            break
                    
                    break
                else : 
                    print('anda tidak punya akun. anda akan kembali ke menu awal')
                    kembali_menu_awal = True
                    break
            if kembali_menu_awal == True:
                continue
            
            while True:
                print('=== Menu ===')
                print('1. Create Recipe')
                print('2. Browsing Recipe')
                print('3. Update Recipe')
                print('4. Delete Recipe')
                print('5. exit program')
                menu = input('Tolong masukkan piihan menu (1-5): ')
                if menu.isdigit() : 
                    menu = int(menu)
                    if menu == 1 :
                        create_recipe()
                    elif menu == 2 :
                        browse_recipes()
                    elif menu == 3 :
                        update_recipes()
                    elif menu == 4 :
                        delete_recipes()
                    elif menu == 5:
                        print('goodbye , thank you')
                        break
                    else : 
                        print('menu harus diisi dengan pilihan 1-5. Tolong Ulangi.')
                        continue
                    #break
                else :
                    print('input menu harus angka, tolong ulangi.')
                    continue
            break
        elif akun == 0 : 
            while True : 
                goodbye = False
                register = input('Anda belum punya akun. \nMau Register? Ketik 1 Jika Iya, Ketik 0 Jika Tidak : ')
                if register.isdigit() : 
                    register = int(register)
                    if register == 1 : 
                        while True : 
                            buat_username = input('Tulis username anda disini: ').lower().strip()
                            buat_pw = input('Tulis Password anda disini: ').strip()
                            password[buat_username] = buat_pw
                            print('username dan password sudah tersimpan! Anda akan kembali ke menu awal')
                            break
                    elif register == 0 : 
                        print('Anda hanya bisa browsing resep saja. Silakan lihat-lihat!')
                        print(f'{"id resep":<10} | {"nama":<20} | {"kategori":<10} | {"nama bahan":<10} | {"jumlah bahan":<10} | {"satuan bahan":<10} | {"kalori per unit bahan":<10} | {"harga per unit bahan":<10} | {"instruksi":<20} | {"dibuat oleh":<10} | {"time minutes":<10} | {"rating":<10} | {"tingkat kesulitan":<10} | {"share":<6}')
                        print('-' * 95)
                        for j in range(len(resep_lain)):
                            for h in range(len(resep_lain[j]["bahan"])):
                                print(f'{resep_lain[j]["id_resep"]:<10} | {resep_lain[j]["nama"]:<20} | {resep_lain[j]["kategori"]:<10} | {resep_lain[j]["bahan"][h]["nama_bahan"]:<10} | {resep_lain[j]["bahan"][h]["jumlah"]:<10} | {resep_lain[j]["bahan"][h]["satuan"]:<10} | {resep_lain[j]["bahan"][h]["kalori_per_unit"]:<10} | {resep_lain[j]["bahan"][h]["harga_per_unit"]:<10} | {str(resep_lain[j]["instruksi"]):<20} | {resep_lain[j]["dibuat_oleh"]:<10} | {resep_lain[j]["time_minutes"]:<10} | {resep_lain[j]["rating"]:<10} | {resep_lain[j]["tingkat_kesulitan"]:<10} | {str(resep_lain[j]["is_shared"]):<6}')
                        print("thank you sudah browsing! Good bye!")
                        goodbye = True

                    else : 
                        print("Angka harus diisi dengan 0 atau 1. Silakan ulangi.")
                        continue
                else : 
                    print('Input harus diisi dengan angka. Silakan ulangi.')     
                    continue
                break
            if goodbye == True:
                break        
        else : 
            print("harus diisi dengan 0 atau 1, tolong isi ulang")
    else: 
        print("harus diisi dengan angka, tolong isi ulang")