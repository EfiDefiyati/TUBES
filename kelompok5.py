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


