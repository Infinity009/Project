import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from datetime import datetime

# Untuk mengimpor module. os untuk memanipulasi atau pengaturan tingkat tinggi file dan direktori (mengubah jalur direktori, mendaftar file), shutil untuk memanipulasi (men-copy, menghapus) file, tkinter untuk antarmuka pengguna (GUI), dan datetime untuk menangani tanggal dan waktu.

def program_filter(direktori_awal, akhir_direktori, menghapus_original, cara_organisir):
    # Membuat fungsi dengan parameter direktori awal, direktori akhir, menghapus original, dan cara organisir
    os.chdir(direktori_awal)
    # Mengubah direktori kerja menuju direktori sumber/awal
    files = [f for f in os.listdir() if os.path.isfile(f)]
    # Variabel files :
    # os.listdir() = Berfungsi untuk menghasilkan daftar semua entri di file direktory sekarang
    # f for f in = Mengambil nama dari direktory kerja semisal (Monepol_KCSC2024.pdf, Oktober.xlxs, Screenshot.png). Kemudian akan dimasukkan di os.listdir()
    # if os.path.isfile(f) = Memeriksa, apakah f itu merupakan file biasa. Semisal (Monepol_KCSC2024.pdf[Benar], Oktober.xlxs[Benar], Screenshot.png[Benar], folder testing[Salah])

    for file in files:
    # Memulai loop untuk memproses setiap file dalam daftar files.
        if "ext" in cara_organisir:
        # Memeriksa apakah "ext" ada di dalam variabel cara_organisir (Sudah di check/belum di dalam variabel cara_organisir)
            ext = file.split('.')[-1]
            # ext = file.split('.')[-1] = Mengambil ekstensi dari file. Semisal (Monepol_KCSC2024.pdf). Maka yang diambil adalah "pdf"
            ext_directory = os.path.join(akhir_direktori, ext)
            # Membuat variabel ext_directory
            # Di dalamnya ada os.path.join() = berfungsi untuk menentukan jalan hasil beserta file yang nantinya akan dibuat.
            if not os.path.exists(ext_directory):
            # Memeriksa di dalam path akhir_direktori (Baris 26) apakah ada folder yang namanya sesuai dengan ext?
                os.makedirs(ext_directory)
                # Jika belum ada maka akan dibuat direktori tersebut, semisal (pdf, docx, dll) 
            shutil.copy(file, os.path.join(ext_directory, file))
            # Kemudian menyalin file ke direktori yang telah dibuat
            if menghapus_original:
            # Memeriksa apakah menghapus_original sudah bernilai true atau false. Dala arti di check/uncheck oleh user?
                os.remove(file)
                # Jika sudah bernilai true/check maka akan menghapus file asli

        if "date" in cara_organisir:
        # Memeriksa apakah "date" ada di dalam variabel cara_organisir (Sudah di check/belum di dalam variabel cara_organisir)
            creation_time = os.path.getctime(file)
            # os.path.getctime(file) = Berfungsi untuk mendapatkan tanggal dan waktu file dibuat dalam format timestamp seperti 1643723400.0 yang nantinya jika di convert ke tanggal dan waktu akan menjadi 2022-02-01 00:00:00
            date_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            # Membuat variabel date_folder =
            # datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d') = Berfungsi untuk mengubah tanggal dan waktu file dibuat menjadi format tanggal (YYYY-MM-DD) yang awalnya yakni bernilai timestamp. Semisal waktu file dibuat : "1732838400" maka jika diubah menjadi format tanggal maka akan menjadi "2024-11-29" dalam format string
            date_directory = os.path.join(akhir_direktori, date_folder)
            # Membuat variabel date_directory = 
            # Di dalamnya ada os.path.join() = Berfungsi untuk menggabungkan kedua variabel (akhir_direktori, date_folder) yang dimana akan menghasilkan path lengkap untuk direktori yang akan dibuat atau digunakan untuk menyimpan file.
            if not os.path.exists(date_directory):
            # Memeriksa di dalam path akhir_direktori (Baris 47) apakah ada folder yang namanya sesuai dengan date?
                os.makedirs(date_directory)
                # Jika belum ada maka akan dibuat direktori tersebut, semisal (2024-11 -29, 2024-11-30, dll) dalam bentuk string
            shutil.copy(file, os.path.join(date_directory, file))
            # Menyalin file ke direktori yang telah dibuat
            if menghapus_original:
            # Memeriksa, apakah menghapus_original sudah bernilai true atau false (dalam arti sudah di check atau belum)
                os.remove(file)
                # Jika sudah bernilai true/di check, maka akan menghapus file asli

        if "size" in cara_organisir:
        # Memeriksa apakah "size" ada di dalam variabel cara_organisir
            size = os.path.getsize(file)
            # os.path.getsize(file) = Berfungsi untuk mendapatkan ukuran file dalam byte (6KB, 1KB, dll)
            if size < 1024 * 1024:
                size_folder = 'Kecil'
            # Membuat variabel size_folder = Kecil jika kurang 1MB
            elif size < 10 * 1024 * 1024:
                size_folder = 'Sedang'
            # Membuat variabel size_folder = Sedang jika kurang 10MB
            else:
                size_folder = 'Besar'
            # Membuat variabel size_folder = Besar jika melebihi 10MB
            size_directory = os.path.join(akhir_direktori, size_folder)
            # Membuat variabel size_directory =
            # Di dalamnya ada os.path.join() = Berfungsi untuk menggabungkan kedua variabel (akhir_direktori, size_folder) yang dimana akan menghasilkan path lengkap untuk direktori yang akan dibuat atau digunakan untuk menyimpan file.
            if not os.path.exists(size_directory):
            # kode memeriksa apakah direktory/folder yang telah dibuat pada path (akhir_directory) sudah ada atau belum
                os.makedirs(size_directory)
                # Jika belum ada maka akan dibuat folder di dalam path tersebut, semisal (Kecil,Sedang,Besar,dll)
            shutil.copy(file, os.path.join(size_directory, file))
            # Menyalin file ke direktori/folder yang telah dibuat
            if menghapus_original:
            # Memeriksa, apakah menghapus_original sudah bernilai true atau false (dalam arti sudah di check atau belum?)
                os.remove(file)
                # Jika sudah bernilai true/di check, maka akan menghapus file asli

    messagebox.showinfo("Sukses", "File telah diorganisir ke dalam folder berdasarkan metode yang dipilih.")
    # Menampilkan pop-up informasi bahwa file telah diorganisir ke dalam folder berdasarkan metode yang dipilih, yang dimana message.showinfo ini ialah modul dari tkinker

def browse_source():
    direktori_awal = filedialog.askdirectory()
    # Membuat variabel direktori_awal = membuka dialog untuk memilih direktori awal
    source_entry.delete(0, tk.END)
    # menghapus teks yang ada di dalam widget entri.
    source_entry.insert(0, direktori_awal)
    # Menambahkan direktori awal yang dipilih ke dalam widget entri.

def browse_target():
    akhir_direktori = filedialog.askdirectory()
    # Membuat variabel akhir_direktori = membuka dialog untuk memilih direktori target/akhir
    target_entry.delete(0, tk.END)
    # menghapus teks yang ada di dalam widget entri.
    target_entry.insert(0, akhir_direktori)
    # Menambahkan direktori target/akhir yang dipilih ke dalam widget entri.

def organize_files():
    direktori_awal = source_entry.get()
    # Membuat variabel direktori_awal = mendapatkan direktori awal yang telah dipilih
    akhir_direktori = target_entry.get()
    # Membuat variabel akhir_direktori = mendapatkan direktori target/akhir yang telah dipilih
    menghapus_original = menghapus_original_var.get()
    # Membuat variabel menghapus_original = mendapatkan nilai dari checkbox menghapus_original_var
    
    cara_organisir = []
    # Membuat variabel cara_organisir = nantinya akan di isi oleh metode mana saja yang dipilih/check oleh user
    if ext_var.get():
    # Memeriksa, apakah ext_var sudah bernilai true atau false (dalam arti sudah di check atau belum?)
        cara_organisir.append("ext")
        # Jika sudah bernilai true/di check, maka akan menambahkan "ext" ke dalam variabel cara_organisir 
    if date_var.get():
    # Memeriksa, apakah date_var sudah bernilai true atau false (dalam arti sudah di check atau belum?)
        cara_organisir.append("date")
        # Jika sudah bernilai true/di check, maka akan menambahkan "date" ke dalam variabel cara_organisir
    if size_var.get():
    # Memeriksa, apakah size_var sudah bernilai true atau false (dalam arti sudah di check atau belum?)
        cara_organisir.append("size")
        # Jika sudah bernilai true/di check, maka akan menambahkan "size" ke dalam variabel cara_organisir

    if not direktori_awal or not akhir_direktori:
    # Memeriksa, apakah direktori_awal dan akhir_direktori sudah bernilai true atau false (dalam arti sudah di check atau belum?)
        messagebox.showwarning("Peringatan", "Silakan pilih direktori sumber dan target.")
        return
    # Jika direktori_awal dan akhir_direktori belum bernilai true/check, maka akan menampilkan pop-up peringatan dan menghentikan proses.

    if not direktori_awal or not os.path.exists(direktori_awal) or not os.listdir(direktori_awal):
    # Memeriksa, apakah direktori_awal ada filenya?
        messagebox.showwarning("Peringatan", "Direktori sumber tidak ada atau kosong.")
        return
        # Jika tidak ada maka akan muncul peringatan, namun jika ada lanjut ke baris (142)

    if not cara_organisir:
    # Memeriksa, apakah cara_organisir sudah bernilai true atau false (dalam arti sudah di check atau belum? oleh pengguna [Minimal 1])
        messagebox.showwarning("Peringatan", "Silakan pilih setidaknya satu metode pengorganisasian.")
        return
    # Jika cara_organisir belum bernilai true/check, maka akan menampilkan pop-up peringatan dan menghentikan proses.

    program_filter(direktori_awal, akhir_direktori, menghapus_original, cara_organisir)
    # Membuat program_filter(direktori_awal, akhir_direktori, meng hapus_original, cara_organisir) = menjalankan fungsi program_filter dengan parameter yang telah di tentukan.


root = tk.Tk() # Membuat variabel root = membuat sebuah jendela aplikasi berdasarkan modul yang sudah kita import tadi, dalam arti fungsi dari module Tkinter
root.title("Pengorganisasian File") # Judul program .exe kita
root.geometry("600x400")  # Ukuran jendela yang lebih besar
root.configure(bg="#f0f0f0") # Membuat background jendela utama berwarna abu-abu

# Membuat frame untuk mengorganisir widget
frame = ttk.Frame(root, padding="10") # Membuat frame dengan padding 10
frame.pack(fill=tk.BOTH, expand=True) # Membuat frame dapat menyesuaikan ukuran jendela utama


tk.Label(frame, text="Direktori Sumber:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
# Membuat label "Direktori Sumber:" dengan background abu-abu
source_entry = ttk.Entry(frame, width=40)
# Membuat entry untuk direktori sumber dengan lebar 40
source_entry.grid(row=0, column=1, padx=10, pady=10)
# Membuat entry direktori sumber berada di posisi (0,1)
ttk.Button(frame, text="Browse", command=browse_source).grid(row=0, column=2, padx=10, pady=10)
# Membuat button "Browse" untuk memilih direktori sumber dengan command browse_source


tk.Label(frame, text="Direktori Target:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
# Membuat label "Direktori Target:" dengan background abu-abu 
target_entry = ttk.Entry(frame, width=40 )
# Membuat entry untuk direktori target dengan lebar 40
target_entry.grid(row=1, column=1, padx=10, pady=10)
# Membuat entry direktori target berada di posisi (1,1)
ttk.Button(frame, text="Browse", command=browse_target).grid(row=1, column=2, padx=10, pady=10)
# Membuat button "Browse" untuk memilih direktori target dengan command browse_target

# Checkbox untuk menghapus file asli
menghapus_original_var = tk.BooleanVar()
# Membuat variabel Boolean untuk checkbox menghapus file asli, apakah bernilai true/check atau false/not check
ttk.Checkbutton(frame, text="Hapus file asli setelah dipindahkan", variable=menghapus_original_var).grid(row=2, columnspan=3, padx=10, pady=5)
# Membuat checkbox "Hapus file asli setelah dipindahkan" dengan variabel Boolean menghapus_original_var dan dapat menyesuaikan ukuran jendela utama 

# Opsi untuk memilih metode pengorganisasian
ext_var = tk.BooleanVar()
# Membuat variabel Boolean untuk checkbox ekstensi, apakah bernilai true/check atau false/not check 
date_var = tk.BooleanVar()
# Membuat variabel Boolean untuk checkbox tanggal, apakah bernilai true/check atau false /not check
size_var = tk.BooleanVar()
# Membuat variabel Boolean untuk checkbox ukuran, apakah bernilai true/check atau false/not check

tk.Label(frame, text="Metode Pengorganisasian:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="w")
# Membuat label "Metode Pengorganisasian:" dengan background abu-abu
ttk.Checkbutton(frame, text="Organisasi Berdasarkan Ekstensi", variable=ext_var).grid(row=3, column=1, padx=10, pady=5, sticky="w")
# Membuat checkbox "Organisasi Berdasarkan Ekstensi" dengan variabel Boolean ext
ttk.Checkbutton(frame, text="Organisasi Berdasarkan Tanggal", variable=date_var).grid(row=4, column=1, padx=10, pady=5, sticky="w")
# Membuat checkbox "Organisasi Berdasarkan Tanggal" dengan variabel Boolean date
ttk.Checkbutton(frame, text="Organisasi Berdasarkan Ukuran", variable=size_var).grid(row=5, column=1, padx=10, pady=5, sticky="w")
# Membuat checkbox "Organisasi Berdasarkan Ukuran" dengan variabel Boolean size


ttk.Button(frame, text="Organisir File", command=organize_files).grid(row=6, columnspan=3, padx=10, pady=20)
# Membuat button "Organisir File" dengan command organize_files untuk menjalankan variable organize_files

root.mainloop() # Jalankan aplikasi GUI