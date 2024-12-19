import tkinter as tk
from tkinter import messagebox, simpledialog

# Kelas untuk mendefinisikan Node yang menyimpan data pada linked list
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

# Kelas untuk operasi-operasi pada LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  

    # Fungsi untuk menambahkan node baru di akhir linked list
    def append(self, data):
        new_node = Node(data)  
        if self.head is None:  
            self.head = new_node  
        else:
            current = self.head  
            while current.next:  
                current = current.next
            current.next = new_node  

    # Fungsi untuk menghapus node pada indeks tertentu
    def delete(self, index):  
        try:
            if self.head is None:  
                raise IndexError("Linked list kosong, tidak ada node untuk dihapus.")

            if index == 0:  
                self.head = self.head.next  
                return True

            current = self.head
            prev = None
            count = 0

            # Mencari node yang sesuai dengan indeks
            while current and count != index:
                prev = current
                current = current.next
                count += 1

            # Jika tidak ditemukan node pada indeks yang dimaksud
            if current is None:
                raise IndexError("Indeks tidak ditemukan.")

            # Memutuskan hubungan antara node sebelumnya dengan node setelahnya
            prev.next = current.next 
            return True
        except IndexError as e:
            messagebox.showerror("Kesalahan", str(e))  
            return False

    # Mengubah linked list menjadi list Python
    def to_list(self):
        result = [] 
        current = self.head

        while current:  
            result.append(current.data) 
            current = current.next

        return result  
        
# Struktur Data Stack, digunakan untuk menyimpan score kuis yang telah dijalankan
class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity  
        self.items = []  

    # Memeriksa apakah stack kosong
    def is_empty(self):  
        return len(self.items) == 0

    # Menambahkan item (score) ke stack
    def push(self, item): 
        if len(self.items) >= self.capacity:
            raise OverflowError("Stack penuh")  
        if not isinstance(item, int):  
            raise ValueError("Score harus berupa integer")
        self.items.append(item)
        print(f"Score {item} ditambahkan ke stack") 

    # Menghapus item (score) dari stack
    def pop(self):  
        if self.is_empty():  
            raise IndexError("Stack kosong")  
        return self.items.pop() 
    
    # Melihat item teratas stack tanpa menghapusnya
    def peek(self):  
        if self.is_empty():  
            raise IndexError("Stack kosong")  
        return self.items[-1]  


    # Mengembalikan ukuran stack
    def size(self):
        return len(self.items)

# Daftar penggunaan
account = {"admin":"admin"} 
pertanyaan = LinkedList() 
score_kuis = Stack()

# 10 list soal
list_pertanyaan = [
    {"pertanyaan": "Apa yang dimaksud dengan struktur data?", "options": ["Sebuah program", "Sebuah cara untuk menyimpan data", "Sebuah algoritma", "Sebuah bahasa pemrograman"], "answer": "Sebuah cara untuk menyimpan data"},
    {"pertanyaan": "Apa yang dimaksud dengan Array?", "options": ["Struktur data yang menyimpan elemen secara terurut", "Struktur data berbasis pohon", "Struktur data berbasis graf", "Struktur data yang hanya menyimpan satu nilai"], "answer": "Struktur data yang menyimpan elemen secara terurut"},
    {"pertanyaan": "Manakah yang bukan termasuk tipe data struktur data linear?", "options": ["Stack", "Queue", "Tree", "Array"], "answer": "Tree"},
    {"pertanyaan": "Bagaimana cara mengakses elemen dalam Linked List?", "options": ["Melalui indeks", "Dengan menggunakan pointer", "Melalui pointer atau referensi", "Tidak bisa diakses"], "answer": "Dengan menggunakan pointer"},
    {"pertanyaan": "Apa yang dimaksud dengan Stack?", "options": ["Struktur data dengan prinsip LIFO (Last In First Out)", "Struktur data dengan prinsip FIFO (First In First Out)", "Struktur data dengan akses acak", "Struktur data berbasis graf"], "answer": "Struktur data dengan prinsip LIFO (Last In First Out)"},
    {"pertanyaan": "Apa yang dimaksud dengan Queue?", "options": ["Struktur data dengan prinsip LIFO", "Struktur data dengan prinsip FIFO (First In First Out)", "Struktur data yang menyimpan data secara acak", "Struktur data berbasis linked list"], "answer": "Struktur data dengan prinsip FIFO (First In First Out)"},
    {"pertanyaan": "Apa itu Binary Search Tree?", "options": ["Pohon biner di mana setiap node memiliki dua anak", "Pohon biner yang memiliki nilai kiri lebih kecil dari nilai kanan", "Pohon dengan urutan acak", "Pohon yang hanya memiliki satu anak"], "answer": "Pohon biner yang memiliki nilai kiri lebih kecil dari nilai kanan"},
    {"pertanyaan": "Apa perbedaan antara Array dan Linked List?", "options": ["Array memiliki ukuran tetap, Linked List memiliki ukuran dinamis", "Array menyimpan data secara acak, Linked List terurut", "Linked List tidak bisa diubah ukurannya, Array bisa", "Array menggunakan pointer, Linked List tidak"], "answer": "Array memiliki ukuran tetap, Linked List memiliki ukuran dinamis"},
    {"pertanyaan": "Apa fungsi dari operasi 'Push' pada Stack?", "options": ["Mengambil elemen dari stack", "Menambahkan elemen ke stack", "Memeriksa elemen teratas stack", "Menghapus elemen teratas stack"], "answer": "Menambahkan elemen ke stack"},
    {"pertanyaan": "Manakah yang merupakan operasi dasar pada Linked List?", "options": ["Insert, Delete, Search", "Push, Pop, Peek", "Enqueue, Dequeue", "Insert, Pop, Search"], "answer": "Insert, Delete, Search"}
]

for q in list_pertanyaan:
    pertanyaan.append(q)

# Fungsi Register
def create_account():
    username_baru = simpledialog.askstring("Register", "Masukkan Username:")
    if not username_baru:
        return messagebox.showerror("Error", "Username harus diisi.")

    password_baru = simpledialog.askstring("Register", "Masukkan Password:")
    if not password_baru:
        return messagebox.showerror("Error", "Password harus diisi.")

    account[username_baru] = password_baru
    messagebox.showinfo("Sukses", f"Akun baru telah dibuat : {username_baru}")

# Fungsi Login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in account and account[username] == password:
        messagebox.showinfo("Berhasil", "Login berhasil")
        login_window.destroy()
        show_menu()
    else:
        messagebox.showerror("Error", "Username atau Password salah")

# Fungsi untuk menampilkan menu utama setelah login
def show_menu():
    menu_window = tk.Tk()
    menu_window.title("Menu Kuis")
    menu_window.configure(bg="#ffffe0")
    menu_window.geometry("350x350")

    tk.Button(menu_window, text="Tambah Pertanyaan", command=tambah_pertanyaan, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)
    tk.Button(menu_window, text="Lihat Pertanyaan", command=daftar_pertanyaan, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)
    tk.Button(menu_window, text="Edit Pertanyaan", command=edit_pertanyaan, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)
    tk.Button(menu_window, text="Hapus Pertanyaan", command=hapus_pertanyaan, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)
    tk.Button(menu_window, text="Mulai Kuis", command=mulai_kuis, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)
    tk.Button(menu_window, text="Skor Akhir", command=score_total, font=("Arial", 12), bg="#00008b", fg="white", width=20).pack(pady=10)

    menu_window.mainloop()

# Fungsi untuk menambahkan pertanyaan baru
def tambah_pertanyaan():
    soal_baru = simpledialog.askstring("Tambah Pertanyaan", "Tambahkan Pertanyaan:")
    if not soal_baru:
        return
    options = []
    pilihan = ["A", "B", "C", "D"]  

    for i in range(4):  
        option = simpledialog.askstring("Tambah Pilihan", f"Tambahkan Pilihan {pilihan[i]}:")
        if option:
            options.append(option)

    jawaban_benar = simpledialog.askstring("Jawaban Benar", "Masukkan jawaban yang benar (A-D):")
    if jawaban_benar not in ["A", "B", "C", "D"]:
        return messagebox.showerror("Error", "Jawaban berupa A, B, C, atau D")
    
    pertanyaan_baru = {"pertanyaan": soal_baru, "options": options, "jawaban": jawaban_benar}
    pertanyaan.append(pertanyaan_baru) 
    messagebox.showinfo("Berhasil", "Pertanyaan berhasil ditambahkan")

# Fungsi untuk mencetak daftar pertanyaan dengan rekursi
def print_questions(node, idx=1):
    if node is None:
        return ""
    return f"{idx}. {node.data['pertanyaan']}\n" + print_questions(node.next, idx + 1)

# Fungsi untuk menampilkan pertanyaan yang ada
def daftar_pertanyaan():
    if pertanyaan.head is None:
        return messagebox.showinfo("Pertanyaan", "Tidak ada pertanyaan yang tersedia.")
    
    daftar_pertanyaan = pertanyaan.to_list()
    tampilan_pertanyaan = "\n".join([f"{idx+1}. {q['pertanyaan']}" for idx, q in enumerate(daftar_pertanyaan)])
    messagebox.showinfo("Pertanyaan", tampilan_pertanyaan)

# Fungsi untuk mengedit pertanyaan
def edit_pertanyaan():
    if pertanyaan.head is None:
        return messagebox.showinfo("Error", "Tidak ada pertanyaan yang tersedia.")
        
    daftar_pertanyaan = pertanyaan.to_list()
    tampilan_pertanyaan = "\n".join([f"{idx+1}. {q['pertanyaan']}" for idx, q in enumerate(daftar_pertanyaan)])
    selected_idx = simpledialog.askinteger("Edit Pertanyaan", f"Pilihan pertanyaan yang ingin diubah:\n{tampilan_pertanyaan}")
    if selected_idx is None or selected_idx < 1 or selected_idx > len(daftar_pertanyaan):
        return messagebox.showerror("Error", "Pilihan tidak valid.")

    pilih_pertanyaan = daftar_pertanyaan[selected_idx-1]
    pertanyaan_baru = simpledialog.askstring("Edit Pertanyaan", f"Edit pertanyaan:\n{pilih_pertanyaan['pertanyaan']}")
    jawaban_baru = simpledialog.askstring("Edit Jawaban", "Edit jawaban yang benar (A-D):")
    if jawaban_baru not in ["A", "B", "C", "D"]:
        return messagebox.showerror("Error", "Jawaban harus A, B, C, atau D")
    
    pilih_pertanyaan["pertanyaan"] = pertanyaan_baru
    pilih_pertanyaan["jawaban"] = jawaban_baru
    messagebox.showinfo("Sukses", "Pertanyaan berhasil diperbarui")

# Fungsi untuk menghapus pertanyaan
def hapus_pertanyaan():
    if pertanyaan.head is None:
        return messagebox.showinfo("Error", "Tidak ada pertanyaan yang tersedia.")
    
    daftar_pertanyaan = pertanyaan.to_list()
    tampilan_pertanyaan = "\n".join([f"{idx+1}. {q['pertanyaan']}" for idx, q in enumerate(daftar_pertanyaan)])
    selected_idx = simpledialog.askinteger("Hapus Pertanyaan", f"Pilihan pertanyaan yang ingin dihapus:\n{tampilan_pertanyaan}")
    
    if selected_idx in range(1, len(daftar_pertanyaan) + 1):
        pertanyaan.delete(selected_idx - 1)
        messagebox.showinfo("Berhasil", "Pertanyaan berhasil dihapus!")
    else:
        messagebox.showerror("Error", "Pilihan tidak valid.")


# Fungsi untuk memulai kuis dan mengupdate score
def mulai_kuis():
    if pertanyaan.head is None:
        return messagebox.showerror("Error", "Tidak ada pertanyaan untuk kuis.")
    
    current_pertanyaan = pertanyaan.head
    jawaban_benar = 0
    total_pertanyaan = len(list_pertanyaan)  

    while current_pertanyaan:
        q = current_pertanyaan.data
        pilihan_ganda = "\n".join([f"{chr(65+idx)}. {pilihan}" for idx, pilihan in enumerate(q["options"])])
        jawaban = simpledialog.askstring("Kuis", f"{q['pertanyaan']}\n{pilihan_ganda}\nPilih jawaban (A-D):")
        
        if jawaban:
            jawaban = jawaban.upper()  
            if jawaban in ["A", "B", "C", "D"]: 
                if q["options"][["A", "B", "C", "D"].index(jawaban)] == q["answer"]:  
                    jawaban_benar += 1 
            else:
                messagebox.showwarning("Peringatan", "Jawaban harus A, B, C, atau D.")
        
        current_pertanyaan = current_pertanyaan.next  
