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
