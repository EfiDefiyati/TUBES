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


