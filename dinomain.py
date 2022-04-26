import pygame
import os # os adalah library untuk mengakses file 
import random
pygame.init() # ini adalah inisialisasi pygame yang akan digunakan untuk membuat game yang akan dijalankan 


TINGGI_LAYAR = 800
LEBAR_LAYAR =  1100
LAYAR = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR)) # ini adalah fungsi untuk membuat layar yang akan digunakan untuk menampilkan game


LARI = [pygame.gambar.load(os.path.join("Assets/Dino", "Dinolari1.png")),pygame.gambar.load(os.path.join("Assets/Dino", "Dinolari2.png"))]
LOMPAT = pygame.gambar.load(os.path.join("Assets/Dino", "Dinolompat.png"))
NUNDUK = [pygame.gambar.load(os.path.join("Assets/Dino", "Dinonunduk1.png")),
           pygame.gambar.load(os.path.join("Assets/Dino", "Dinonunduk2.png"))]

BATU = [pygame.gambar.load(os.path.join("Assets/batu", "batukecil1.png")),
                pygame.gambar.load(os.path.join("Assets/batu", "batukecil2.png")),
                pygame.gambar.load(os.path.join("Assets/batu", "batubesar.png"))]
KAKTUS = [pygame.gambar.load(os.path.join("Assets/kaktus", "LargeCactus1.png")),
                pygame.gambar.load(os.path.join("Assets/kaktus", "LargeCactus2.png")),
                pygame.gambar.load(os.path.join("Assets/kaktus", "LargeCactus3.png"))]
BURUNG = [pygame.gambar.load(os.path.join("Assets/burung", "bird1-01.png")),
        pygame.gambar.load(os.path.join("Assets/burung", "bird1-02.png"))]

AWAN = pygame.gambar.load(os.path.join("Assets/Other", "awan.png")) #cloud

JALAN = pygame.gambar.load(os.path.join("Assets/Other", "jalan-01.png")) #bg

#class dinosaurus

class dinosaur:
    POSISI_X = 80 #posisi dinosaurus pada X
    POSISI_y = 310 #posisi awal dino pada Y
    POSISI_X_NUNDUK = 340 #posisi dari dinosaurus ketika nunduk
    LOMPAT = 8.5 #kecepatan lompat

    def __init__(self): 
        self.gambar_nunduk = NUNDUK
        self.gambar_lari =  LARI
        self.lompat_img = LOMPAT

        self.dino_nunduk = False #false karena awalnya dinosaurus tidak nunduk
        self.dino_lari = True #true karena awalnya dinosaurus lari
        self.dino_lompat = False #false karena awalnya dinosaurus tidak lompat

        self.langkah_index = 0 #bernilai 0 karena
        self.nilai_lompat =self.LOMPAT
        self.gambar =self.gambar_lari[0]
        self.aksi_dino = self.gambar.get_aksi()
        self.aksi_dino.X = self.POSISI_X
        self.aksi_dino.Y = self.POSISI_y

    def update(self,UserInput):
        if self.dino_nunduk:
            self.nunduk()
        if self.dino_lari:
            self.lari()
        if self.dino_lompat:
            self.lompat()

        if self.langkah_index >=10:
            self.langkah_index = 0

        if UserInput(pygame.TOMBOL_ATAS) and not self.dino_lompat:
            self.dino_nunduk =False
            self.dino_lari = False
            self.dino_lompat = True
        elif UserInput(pygame.TOMBOL_BAWAH) and not self.dino_lompat:
            self.dino_nunduk = True
            self.dino_lari = False
            self.dino_lompat = True
        elif not (self.dino_lompat or UserInput[pygame.TOMBOL_BAWAH]):
            self.dino_nunduk =False
            self.dino_lari = True
            self.dino_lompat = False
    
    def nunduk(self):
        self.gambar = self.gambar_nunduk[self.langkah_index // 5] # 
        self.aksi_dino = self.gambar.get_rect()
        self.aksi_dino.x = self.POSISI_X
        self.aksi_dino.y =self.POSISI_Y_NUNDUK
        self.langkah_index += 1

    def lari(self):
        self.gambar = self.gambar_lari[self.gambar_lari_index // 5] # 5 artinya gambar lari akan dijalankan setiap 5 frame
        self.aksi_dino = self.gambar.get_rect()
        self.aksi_dino.x = self.POSISI_X
        self.aksi_dino.y = self.POSISI_Y
        self.gambar_lari_index += 1
    
    def lompat(self):
        self.image = self.lompat_img
        if self.dino_lompat:
            self.aksi_dino.y -= self.nilai_lompat * 4
            self.nilai_lompat -= 0.8
        if self.nilai_lompat < - self
