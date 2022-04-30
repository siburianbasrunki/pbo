import pygame
import os # os adalah library untuk mengakses file 
import random
pygame.init() # ini adalah inisialisasi pygame yang akan digunakan untuk membuat game yang akan dijalankan 


TINGGI_LAYAR = 800
LEBAR_LAYAR =  1100
LAYAR = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR)) # ini adalah fungsi untuk membuat layar yang akan digunakan untuk menampilkan game

LARI = [pygame.image.load(os.path.join("Assets/Dino", "dinolari1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "dinolari2.png"))]
LOMPAT = pygame.image.load(os.path.join("Assets/Dino", "dinolompat.png"))
NUNDUK = [pygame.image.load(os.path.join("Assets/Dino", "dinonunduk1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "dinonunduk2.png"))]

BATU = [pygame.image.load(os.path.join("Assets/batu", "batukecil1.png")),
                pygame.image.load(os.path.join("Assets/batu", "batukecil2.png")),
                pygame.image.load(os.path.join("Assets/batu", "batubesar.png"))]
KAKTUS = [pygame.image.load(os.path.join("Assets/kaktus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/kaktus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/kaktus", "LargeCactus3.png"))]

BURUNG = [pygame.image.load(os.path.join("Assets/burung", "burunggg1-01.png")),
        pygame.image.load(os.path.join("Assets/burung", "burunggg2-01.png"))]

AWAN = pygame.image.load(os.path.join("Assets/Other", "awan.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "jalan-01.png"))

#class dinosaurus

class dinosaur:
    POSISI_X = 80 
    POSISI_y = 310
    POSISI_Y_NUNDUK = 340
    LOMPAT = 8.5

    def __init__(self): 
        self.image_nunduk = NUNDUK
        self.image_lari =  LARI
        self.lompat_img = LOMPAT

        self.dino_nunduk = False
        self.dino_lari = True
        self.dino_lompat = False

        self.langkah_index = 0
        self.nilai_lompat =self.LOMPAT
        self.image =self.image_lari[0]
        self.rect_dino = self.image.get_rect()
        self.rect_dino.x = self.POSISI_X
        self.rect_dino.y = self.POSISI_y

    def update(self,UserInput):
        if self.dino_nunduk:
            self.nunduk()
        if self.dino_lari:
            self.lari()
        if self.dino_lompat:
            self.lompat()

        if self.langkah_index >=10:
            self.langkah_index = 0

        if UserInput[pygame.K_UP] and not self.dino_lompat:
            self.dino_nunduk =False
            self.dino_lari = False
            self.dino_lompat = True
        elif UserInput[pygame.K_DOWN] and not self.dino_lompat:
            self.dino_nunduk = True
            self.dino_lari = False
            self.dino_lompat = False
        elif not (self.dino_lompat or UserInput[pygame.K_DOWN]):
            self.dino_nunduk =False
            self.dino_lari = True
            self.dino_lompat = False
    
    def nunduk(self):
        self.image = self.image_nunduk[self.langkah_index // 5] # 
        self.rect_dino = self.image.get_rect()
        self.rect_dino.x = self.POSISI_X
        self.rect_dino.y =self.POSISI_Y_NUNDUK
        self.langkah_index += 1

    def lari(self):
        self.image = self.image_lari[self.langkah_index // 5] # 5 artinya gambar lari akan dijalankan setiap 5 frame
        self.rect_dino = self.image.get_rect()
        self.rect_dino.x = self.POSISI_X
        self.rect_dino.y = self.POSISI_y
        self.langkah_index += 1
    
    def lompat(self):
        self.image = self.lompat_img
        if self.dino_lompat:
            self.rect_dino.y -= self.nilai_lompat * 4
            self.nilai_lompat -= 0.8
        if self.nilai_lompat < - self.LOMPAT : 
            self.dino_lompat = False
            self.nilai_lompat = self.LOMPAT
            
    def draw(self, LAYAR) : 
        LAYAR.blit(self.image, (self.rect_dino.x, self.rect_dino.y))

class Awan : 
    def __init__(self) :
        self.x = LEBAR_LAYAR + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = AWAN
        self.lebar = self.image.get_width()
        
    def update(self) : 
        self.x -= kecepatan_game
        if self.x < -self.lebar :
            self.x = LEBAR_LAYAR + random.randint(2500, 3000)
            self.y = random.randint(50, 100)
            
    def draw(self, LAYAR) : 
        LAYAR.blit(self.image, (self.x, self.y))
        
class Rintangan : 
    def __init__(self, gambar, type):
        self.image = gambar
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = LEBAR_LAYAR
        
    def update(self) : 
        self.rect.x -= kecepatan_game
        if self.rect.x < -self.rect.width : 
            rintangan.pop()
            
    def draw(self, LAYAR): 
        LAYAR.blit(self.image[self.type], self.rect)
        
class BatuKecil(Rintangan): 
    def __init__ (self, gambar):
        self.type = random.randint(0, 2)
        super().__init__(gambar, self.type)
        self.rect.y = 325
        
class BatuBesar(Rintangan):
    def __init__(self, gambar): 
        self.type = random.randint(0, 2)
        super().__init__(gambar, self.type)
        self.rect.y = 300
        
class Burung(Rintangan):
    def __init__(self, gambar):
        self.type = 0
        super().__init__(gambar, self.type)
        self.rect.y = 250
        self.index = 0
        
    def draw(self, LAYAR):
        if self.index >= 9 : 
            self.index = 0
        LAYAR.blit(self.image[self.index//5], self.rect)
        self.index += 1
        

def main():
    global kecepatan_game, x_pos_bg, y_pos_bg, point, rintangan
    lari = True
    waktu = pygame.time.Clock()
    player = dinosaur()
    awan = Awan()
    kecepatan_game = 20
    x_pos_bg = 0
    y_pos_bg = 380
    point = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    rintangan = []
    death_count = 0
    
    def score():
        global point, kecepatan_game
        point += 1
        if point % 100 == 0:
            kecepatan_game += 1
        
        text = font.render("Points: " + str(point), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        LAYAR.blit(text, textRect)
        
    def background():
        global x_pos_bg, y_pos_bg
        image_lebar = BG.get_width()
        LAYAR.blit(BG, (x_pos_bg, y_pos_bg))
        LAYAR.blit(BG, (image_lebar + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_lebar:
            LAYAR.blit(BG, (image_lebar + x_pos_bg, y_pos_bg))
            x_pos_bg -= kecepatan_game
            
    while lari:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lari = False
                
        LAYAR.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()
        
        player.draw(LAYAR)
        player.update(userInput)
        
        if len(rintangan) == 0:
            if random.randint(0, 2) == 0:
                rintangan.append(BatuKecil(BATU))
            elif random.randint(0, 2) == 1:
                rintangan.append(BatuBesar(KAKTUS))
            elif random.randint(0, 2) == 2:
                rintangan.append(Burung(BURUNG))
                
        for Rintangan in rintangan:
            Rintangan.draw(LAYAR)
            Rintangan.update()
            if player.rect_dino.colliderect(Rintangan.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)
                
        background()
        
        awan.draw(LAYAR)
        awan.update()
        
        score()
        
        waktu.tick(30)
        pygame.display.update()
        
class buff:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = LEBAR_LAYAR
        
    def update(self):
        self.rect.x -= kecepatan_game
        if self.rect.x < -self.lebar.rect:
            buff.pop()
            
    def draw(self, LAYAR):
        LAYAR.blit(self.imgae[self.type], self.rect)
    
class kecepatanmenurun(buff):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
        
    def draw(self, LAYAR):
        if self.index >= 9:
            self.index = 0
        LAYAR.blit(self.image[self.index//5], self.rect)
        self.index += 1
    
def menu(death_count):
    global point
    lari = True
    while lari:
        LAYAR.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)
        
        if death_count == 0:
            text = font.render("Klik dimanapun untuk Memulai", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Klik dimanapun untuk Memulai Ulang", True, (0, 0, 0))
            score = font.render("Score anda : " + str(point), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (LEBAR_LAYAR // 2, TINGGI_LAYAR // 2 + 50)
            LAYAR.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (LEBAR_LAYAR // 2, TINGGI_LAYAR // 2)
        LAYAR.blit(text, textRect)
        LAYAR.blit(LARI[0], (LEBAR_LAYAR // 2, TINGGI_LAYAR // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lari = False
            if event.type == pygame.KEYDOWN:
                main()
                
menu(death_count=0)