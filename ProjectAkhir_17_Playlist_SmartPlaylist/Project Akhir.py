GENRE = ("Pop", "Rock", "Jazz", "Hip Hop", "Klasik")

playlist_utama = []  
user_accounts = {}  
kunjungan_playlist = {"playlist_utama": 0}  

def input_data(teks):
    data = ""
    while data == "":
        data = input(teks)
        if data == "":
            print("Input tidak boleh kosong...")
    return data

def registrasi_user():
    print("\n✦ Registrasi ✦")
    while True:
        username = input_data("Masukkan username: ")
        if username in user_accounts:
            print("Username sudah terdaftar. Gunakan username lain.")
        else:
            break

    password = input_data("Masukkan password: ")
    user_accounts[username] = {"password": password, "playlists": {}, "stats": {}}
    print(f"User '{username}' berhasil didaftarkan!")
    return username

def login_user():
    print("\n✦ Login ✦")
    username = input_data("Masukkan username: ")
    if username not in user_accounts:
        print("Username tidak ditemukan.")
        return None

    password = input_data("Masukkan password: ")
    if user_accounts[username]["password"] == password:
        print(f"Login berhasil. Selamat datang, {username}!")
        return username
    else:
        print("Password salah.")
        return None


def tampilkan_semua_playlist(user):
    playlists = user_accounts[user]["playlists"]
    if not playlists:
        print(f"User '{user}' tidak memiliki playlist.")
        return None
    
    print("\n✦ Daftar Playlist ✦")
    print(f"{'No':<5}{'Nama Playlist':<30}{'Jumlah Lagu':<15}")
    print("-" * 50)  
    for i, (nama_playlist, lagu_playlist) in enumerate(playlists.items(), start=1):
        print(f"{i:<5}{nama_playlist:<30}{len(lagu_playlist):<15}")

    return list(playlists.keys())

def pilih_playlist(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return None
    
    while True:
        pilihan = input_data("Masukkan nomor playlist yang ingin dibuka: ")
        if pilihan.isdigit():
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar_playlist):  
                return daftar_playlist[pilihan - 1]
            else:
                print("Masukkan nomor yang valid.")
        else:
            print("Input harus berupa angka.")

def tambah_lagu_admin():
    judul = input_data("Masukkan judul lagu: ")
    artis = input_data("Masukkan nama artis: ")
    durasi = input_data("Masukkan durasi lagu (menit:detik): ")

    print("\nPilih genre:")
    for i, genre in enumerate(GENRE, start=1):
        print(f"{i}. {genre}")

    while True:
        genre_pilihan = input_data("Masukkan nomor pilihan genre: ")
        if genre_pilihan.isnumeric() and 1 <= int(genre_pilihan) <= len(GENRE):
            genre = GENRE[int(genre_pilihan) - 1]
            break
        else:
            print(f"Masukkan nomor genre yang valid antara 1 dan {len(GENRE)}.")

    lagu = {
        "judul": judul,
        "artis": artis,
        "durasi": durasi,
        "genre": genre
    }

    playlist_utama.append(lagu)
    print(f"Lagu '{judul}' berhasil ditambahkan ke playlist utama!")

def hapus_lagu_admin():
    tampilkan_lagu_bawaan(playlist_utama, "playlist_utama")
    judul = input_data("Masukkan judul lagu yang ingin dihapus: ")
    for lagu in playlist_utama:
        if lagu['judul'].lower() == judul.lower():
            playlist_utama.remove(lagu)
            print(f"Lagu '{judul}' berhasil dihapus dari playlist utama.")
            return
    print(f"Lagu '{judul}' tidak ditemukan di playlist utama.")

def tambah_lagu_user(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return

    nama_playlist = pilih_playlist(user)
    if nama_playlist:
        tambah_lagu_admin()  
        lagu = playlist_utama[-1]  
        user_accounts[user]["playlists"][nama_playlist].append(lagu)
        print(f"Lagu '{lagu['judul']}' berhasil ditambahkan ke playlist '{nama_playlist}'.")

def hapus_lagu_user(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return

    nama_playlist = pilih_playlist(user)
    if nama_playlist:
        tampilkan_lagu_bawaan(user_accounts[user]["playlists"][nama_playlist], nama_playlist)
        judul = input_data("Masukkan judul lagu yang ingin dihapus: ")
        for lagu in user_accounts[user]["playlists"][nama_playlist]:
            if lagu['judul'].lower() == judul.lower():
                user_accounts[user]["playlists"][nama_playlist].remove(lagu)
                print(f"Lagu '{judul}' berhasil dihapus dari playlist '{nama_playlist}'.")
                return
        print(f"Lagu '{judul}' tidak ditemukan di playlist '{nama_playlist}'.")

def buat_playlist(user):
    nama_playlist = input_data("Masukkan nama playlist baru: ")
    if nama_playlist in user_accounts[user]["playlists"]:
        print(f"Playlist '{nama_playlist}' sudah ada untuk user '{user}'.")
    else:
        user_accounts[user]["playlists"][nama_playlist] = []
        kunjungan_playlist[nama_playlist] = 0  
        print(f"Playlist '{nama_playlist}' berhasil dibuat untuk user '{user}'!")

def hapus_playlist(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return

    nama_playlist = pilih_playlist(user)
    if nama_playlist:
        del user_accounts[user]["playlists"][nama_playlist]
        del kunjungan_playlist[nama_playlist]
        print(f"Playlist '{nama_playlist}' berhasil dihapus!")

def lihat_playlist_user(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return

    nama_playlist = pilih_playlist(user)
    if nama_playlist:
        tampilkan_lagu_bawaan(user_accounts[user]["playlists"][nama_playlist], nama_playlist)

def memutar_lagu(lagu):
    lagu = input("masukkan judul lagu yang ingin di putar: ")
    for plylist in playlist_utama:
        if plylist ['judul'] == lagu:
            print(f"lagu yang sedang diputar: {plylist['judul']}, nama artis: {plylist['artis']}, {plylist['durasi']}, genre: {plylist['genre']}")
            return
    print('nama lagu tidak ada dalam plylist')

def tampilkan_lagu_bawaan(playlist, nama_playlist):
    if not playlist:
        print(f"Playlist '{nama_playlist}' kosong.")
    else:
        print(f"\n✦ ── Playlist: {nama_playlist} ── ✦")
        print(f"{'No':<5}{'Judul':<30}{'Artis':<25}{'Durasi':<10}{'Genre':<15}")  
        print("-" * 85)  
        for i, lagu in enumerate(playlist, start=1):
            print(f"{i:<5}{lagu['judul']:<30}{lagu['artis']:<25}{lagu['durasi']:<10}{lagu['genre']:<15}")

    kunjungan_playlist[nama_playlist] = kunjungan_playlist.get(nama_playlist, 0) + 1

def tampilkan_statistik_playlist():
    print("\n✦ Statistik Kunjungan Playlist ✦")
    if not kunjungan_playlist:
        print("Tidak ada data kunjungan.")
    else:
        playlist_diurutkan = sorted(kunjungan_playlist.items(), key=lambda x: x[1], reverse=True)
        for playlist, kunjungan in playlist_diurutkan:
            print(f"{playlist}: {kunjungan} kali dibuka")

def cari_lagu_admin():
    if not playlist_utama:
        print("Playlist utama kosong. Tambahkan lagu terlebih dahulu.")
        return

    print("\n✦ Pencarian Lagu ✦")
    print("1. Cari berdasarkan Judul")
    print("2. Cari berdasarkan Artis")
    print("3. Cari berdasarkan Genre")
    pilihan = input_data("Pilih metode pencarian: ")

    if pilihan == "1":
        kata_kunci = input_data("Masukkan judul lagu: ").lower()
        hasil = [lagu for lagu in playlist_utama if kata_kunci in lagu["judul"].lower()]
    elif pilihan == "2":
        kata_kunci = input_data("Masukkan nama artis: ").lower()
        hasil = [lagu for lagu in playlist_utama if kata_kunci in lagu["artis"].lower()]
    elif pilihan == "3":
        print("\nPilih genre:")
        for i, genre in enumerate(GENRE, start=1):
            print(f"{i}. {genre}")
        while True:
            genre_pilihan = input_data("Masukkan nomor pilihan genre: ")
            if genre_pilihan.isnumeric() and 1 <= int(genre_pilihan) <= len(GENRE):
                genre = GENRE[int(genre_pilihan) - 1]
                hasil = [lagu for lagu in playlist_utama if lagu["genre"] == genre]
                break
            else:
                print(f"Masukkan nomor genre yang valid antara 1 dan {len(GENRE)}.")
    else:
        print("Pilihan tidak valid.")
        return

    if hasil:
        print(f"\n✦ ── Hasil Pencarian ── ✦")
        print(f"{'No':<5}{'Judul':<30}{'Artis':<25}{'Durasi':<10}{'Genre':<15}")  
        print("-" * 85)
        for i, lagu in enumerate(hasil, start=1):
            print(f"{i:<5}{lagu['judul']:<30}{lagu['artis']:<25}{lagu['durasi']:<10}{lagu['genre']:<15}")
    else:
        print("Tidak ditemukan lagu yang sesuai dengan kata kunci pencarian.")

def cari_lagu_user(user):
    daftar_playlist = tampilkan_semua_playlist(user)
    if not daftar_playlist:
        return

    nama_playlist = pilih_playlist(user)
    if nama_playlist:
        playlist = user_accounts[user]["playlists"][nama_playlist]
        if not playlist:
            print(f"Playlist '{nama_playlist}' kosong. Tidak ada lagu untuk dicari.")
            return
        
        print("\n✦ Pencarian Lagu di Playlist ✦")
        kriteria = input_data("Masukkan judul atau artis untuk pencarian: ").lower()
        hasil = [
            lagu for lagu in playlist
            if kriteria in lagu['judul'].lower() or kriteria in lagu['artis'].lower()
        ]
        
        if hasil:
            print(f"\nDitemukan {len(hasil)} lagu yang sesuai di playlist '{nama_playlist}':")
            print(f"{'No':<5}{'Judul':<30}{'Artis':<25}{'Durasi':<10}{'Genre':<15}")
            print("-" * 85)
            for i, lagu in enumerate(hasil, start=1):
                print(f"{i:<5}{lagu['judul']:<30}{lagu['artis']:<25}{lagu['durasi']:<10}{lagu['genre']:<15}")
        else:
            print(f"Tidak ada lagu yang sesuai dengan kriteria pencarian di playlist '{nama_playlist}'.")


def jalankan_program():
    print("\n───── Smart Playlist ─────")
    while True:
        print("\n1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Registrasi User Baru")
        print("4. Lihat Statistik Playlist")
        print("5. Keluar")
        cek = input_data("Pilih menu: ")

        if cek == "1":
            while True:
                print("\n───── Menu Admin ─────")
                print("1. Tambah Lagu")
                print("2. Hapus Lagu")
                print("3. Lihat lagu Utama")
                print("4. Cari Lagu")
                print("5. Keluar")
                pilihan = input_data("Pilih menu: ")

                if pilihan == "1":
                    tambah_lagu_admin()
                elif pilihan == "2":
                    hapus_lagu_admin()
                elif pilihan == "3":
                    tampilkan_lagu_bawaan(playlist_utama, "playlist_utama")
                elif pilihan == "4":
                    cari_lagu_admin()
                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif cek == "2":
            user = login_user()
            if user:
                while True:
                    print(f"\n───── Menu User: {user} ─────")
                    print("\n1. Buat Playlist")
                    print("2. Tambah Lagu ke Playlist")
                    print("3. Hapus Lagu dari Playlist")
                    print("4. Hapus Playlist")
                    print("5. Lihat Playlist")
                    print("6. lihat lagu bawaan")
                    print("7. putar lagu bawaan")
                    print("8. Cari Lagu di Playlist")
                    print("9. Lihat Statistik Playlist")
                    print("10. Keluar\n")
                    pilihan = input_data("Pilih menu: ")

                    if pilihan == "1":
                        buat_playlist(user)
                    elif pilihan == "2":
                        tambah_lagu_user(user)
                    elif pilihan == "3":
                        hapus_lagu_user(user)
                    elif pilihan == "4":
                        hapus_playlist(user)
                    elif pilihan == "5":
                        lihat_playlist_user(user)
                    elif pilihan == "6":
                        tampilkan_lagu_bawaan(playlist_utama, "playlist_utama")
                    elif pilihan == "7":
                        memutar_lagu('judul')
                    elif pilihan == "8":
                        cari_lagu_user(user)
                    elif pilihan == "9":
                        tampilkan_statistik_playlist()
                    elif pilihan == "10":
                        break
                    else:
                        print("Pilihan tidak valid.")

        elif cek == "3":
            registrasi_user()

        elif cek == "4":
            tampilkan_statistik_playlist()

        elif cek == "5":
            print("Program selesai.")
            break

jalankan_program()