import os
import time
import curses

liste = []

screen = curses.initscr()
screen.keypad(True)
curses.start_color()
# curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK )
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(4,curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5,curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(6,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(7,curses.COLOR_BLUE,curses.COLOR_BLACK)
curses.init_pair(8,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.curs_set(0)
screen.bkgd(' ', curses.color_pair(3))
screen.clear()

class YurumeAlgoritmasi:
    def isNear(self, other_position_x, other_position_y):
        return abs(other_position_x - self.x) <= 1 and abs(other_position_y - self.y) <= 1


class Narrower: # konuşmacı
    def __init__(self, x, y, conversations, is_speak = False):
        self.x = x
        self.y = y
        self.conversations = conversations
        self.is_speak = is_speak

    def can_speak(self):
        return not self.is_speak

    def speak(self):
        self.is_speak = True

class Asker(Narrower, YurumeAlgoritmasi):

    def savas(self):
        pass

class easteregg(Narrower,YurumeAlgoritmasi):
    def eastereggs(self):
        pass


class wall(Narrower,YurumeAlgoritmasi):
    def wall(self):
        pass

class Kral(Narrower, YurumeAlgoritmasi):
    pass

class border(Narrower,YurumeAlgoritmasi):
    def border(self):
        pass

class prenses(Narrower,YurumeAlgoritmasi):
    def princes(self):
        pass

class büyücü(Narrower,YurumeAlgoritmasi):
    def büyücü(self):
        pass

class ilters(Narrower,YurumeAlgoritmasi):
    def ilters(self):
        pass

class invisbility(Narrower,YurumeAlgoritmasi):
    def invisbility(self):
        pass

height, width = 50, 100

def show():
    for y in range(len(liste)):
        for x in range(len(liste[y])):
            try:
                if liste[y][x] == 'X':
                    screen.addch(y,x, liste[y][x], curses.color_pair(1) | curses.A_BOLD  | curses.A_BLINK)
                elif liste[y][x] == '∆':
                    screen.addch(y, x, liste[y][x], curses.color_pair(2) | curses.A_BOLD)
                elif liste[y][x]== 'E':
                    screen.addch(y, x, liste[y][x], curses.color_pair(4) | curses.A_BOLD)
                elif liste[y][x] == '|':
                    screen.addch(y, x, liste[y][x], curses.color_pair(5))
                elif liste[y][x] == '案':
                    screen.addch(y, x, liste[y][x], curses.color_pair(6) | curses.A_BOLD|curses.A_BLINK)
                elif liste[y][x] == '大':
                    screen.addch(y, x, liste[y][x], curses.color_pair(7) | curses.A_BOLD)
                elif liste[y][x] == '<':
                    screen.addch(y, x, liste[y][x], curses.color_pair(8) | curses.A_BOLD)
                else:
                    screen.addch(y, x, liste[y][x])
            except:
                pass
def create_screen():
    global liste
    liste = [['*' if y> 0 else ' ' for _ in range(width)] for y in range(height)]


def add_person(x, y):
    global liste

    liste[y][x] = '∆'
    liste[y][x+1] = ' '
    liste[y][x -1] = ' '

def add_enemy(x, y):
    global liste
    if y < len(liste):
        liste[y][x] = 'X'
        liste[y][x+1] = ' '
        liste[y][x-1] = ' '

def add_büyücü(büyücü):
    global liste
    x,y= büyücü.x,büyücü.y
    if y < len(liste):
        liste[y][x]='㍭'
        liste[y][x+1]=''
        liste[y][x-1]=''

def add_wall(wall):
    global liste
    x,y= wall.x,wall.y
    if y < len(liste):
        liste[y][x]='|'
        liste[y][x+1]=' '
        liste[y][x-1]=' '

def add_border(border):
    global liste
    x,y= border.x,border.y
    if y < len(liste):
        liste[y][x] = '<'
        liste[y][x + 1] = ''
        liste[y][x - 1] = ''


def add_prenses(prenses):
    global liste
    x,y= prenses.x,prenses.y
    if y < len(liste):
        liste[y][x] = '大'
        liste[y][x + 1] = ''
        liste[y][x - 1] = ''


def add_ilters(ilters):
    global liste
    x,y = ilters.x,ilters.y
    if y < len(liste):
        liste[y][x]='Ğ'
        liste[y][x+1]=''
        liste[y][x-1]=''


def add_asker(asker):
    global liste
    x,y = asker.x, asker.y
    if y < len(liste):
        liste[y][x] = '案'
        liste[y][x + 1] = ''
        liste[y][x - 1] = ''

def add_kral(Kral):
    global liste
    x,y = Kral.x , Kral.y
    if y < len(liste):
        liste[y][x]= 'Q'
        liste[y][x + 1] = ''
        liste[y][x - 1] = ''

def add_invisbility(invisbility):
    global liste
    x,y=invisbility.x,invisbility.y
    if y < len(liste):
        liste[y][x]='*'
        liste[y][x + 1] = '*'
        liste[y][x - 1] = '*'


def add_easteregs(easteregg):
    global liste
    x,y=easteregg.x,easteregg.y
    if y < len(liste):
        liste[y][x]='E'
        liste[y][x + 1] = ''
        liste[y][x - 1] = ''



try:
    invisbility_positions=[
        invisbility(6,30,['TUZAK YARALANDIN']),
        invisbility(30, 47, ['BÜYÜ YETENEKLERİN HİÇ İYİ DEĞİL BÜYÜCÜYÜ ZİYARET ETMELİSİN'])
    ]

    asker_positions=[
        Asker(96,45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),

        Asker(98, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(94    , 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(92, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(90, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(88, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(86, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(84, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(82, 45, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(82, 49, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),
        Asker(82, 47, [
            'MUHAFIZ:DUR! iceri giremessin',
            'WİTCHER:Krala beni Ilters\'ın gönderdiğini ilet',
            'MUHAFIZ:Burada bekle Kral\'a soralım(muhafız krala haber vermeye gider)',
            'MUHAFIZ:Kral seni Tahtına bekliyor iceri gir'
        ]),

    ] # 1.parametre x 2. parametre y 3. parametre konuştu mu bool 4. parametre de konuşmalar

    prenses_positions=[
        prenses(14,5, [
            'Prenses\'e ulaştın',
            'WITCHER:Merhaba sizi kurtarmak için babanız tarafından gönderildim',
            'Prenses:Yola tuzaklar kurduklarını duydum buradan çıkarken dikkatli olmalıyız',
            'WITCHER:Merak etmeyin sizi babanıza ulaştırıcam'
        ]),



    ]

    wall_positions=[
        wall(5, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(3, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(6, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(8, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(10, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(12, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(15, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(18, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(19, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(10, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(12, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(14, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(16, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(18, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(20, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(8, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(6, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(4, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(2, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 23, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 20, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 17, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 19, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 18, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 21, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),

        #büyücü
        wall(82, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(85, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(88, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(91, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(93, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(95, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(98, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
    wall(82, 28, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(85, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(88, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(91, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(93, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(95, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(98, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(83, 35, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(82, 29, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(82, 30, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(82, 31, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        #KÖY2
        wall(1,40,[
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(2, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(4, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(6, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),

        wall(3,40,[
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(5, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(7, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(9, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(11, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(13, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(15, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(17, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(19, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(3, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(5, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(7, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(9, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(11, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(13, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(14, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(16, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(18, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(20, 49, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 46, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 48, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 44, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(1, 43, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 42, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        #SAĞ
        wall(1, 45, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 45, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 43, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 41, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 48, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 41, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 50, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),wall(20, 45, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(20, 44, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),
        wall(1, 40, [
            'SADECE KAPIDAN ÇIKILABİLİR'
        ]),

    ]

    border_positions=  [
        border(50,20,['SINIR']),
        border(50,19,['SINIR']),
        border(50, 18, ['SINIR']),
        border(50, 17, ['SINIR']),
        border(50, 16, ['SINIR']),
        border(50, 14, ['SINIR']),
        border(50, 13, ['SINIR']),
        border(50, 12, ['SINIR']),
        border(50, 11, ['SINIR']),
        border(50, 10, ['SINIR']),
        border(50, 23, ['SINIR']),
        border(50, 22, ['SINIR']),
        border(50, 21, ['SINIR']),
        border(50, 9, ['SINIR']),
        border(50, 15, ['SINIR']),
        border(50, 24, ['SINIR']),
        border(50, 25, ['SINIR']),
        border(50, 26, ['SINIR']),
        border(50, 27, ['SINIR']),
        border(50, 28, ['SINIR']),
        border(50, 29, ['SINIR']),
        border(50, 30, ['SINIR']),
        border(50, 31, ['SINIR']),
        border(50, 32, ['SINIR']),
        border(50, 35, ['SINIR']),
        border(50, 36, ['SINIR']),
        border(50, 37, ['SINIR']),
        border(50, 38, ['SINIR']),
        border(50, 39, ['SINIR']),
        border(50, 40, ['SINIR']),
        border(50, 41, ['SINIR']),
        border(50, 42, ['SINIR']),
        border(50, 43, ['SINIR']),
        border(50, 44, ['SINIR']),
        border(50, 45, ['SINIR']),
        border(50, 46, ['SINIR']),
        border(50, 47, ['SINIR']),
        border(50, 48, ['SINIR']),
        border(50, 49, ['SINIR']),











        ]


    ilters_positions=[
        ilters(8,20,['ILTERS:MERHABA EVLAT',
                     'WITCHER:Büyücü beni sizden öküzgözünü almam için gönderdi',
                     'ILTERS:Maalesef evlat onu geçen hafta kralın hasta karısı için verdim']),

    ]

    kral_positions=[
        Kral(90,47,['KRAL:Buraya neden geldin',
                    'WİTCHER:Efendim İlters\'ın size vermiş olduğu öküzgözünü almak için',
                    'Kral:Sana onu bir şart ile veririm kızımı cadıların elinden kurtarırsan',
                    'WİTCHER:Kızını size getiricem'])
    ]


    büyücü_positions=[
        büyücü(95,30,['Büyücüye ulastın ondan büyü yetenegini artırmasını isteyebilirsin(Büyü yeteneğini artırmak için[B] Yola devam etmek için [D]',
                      'BüYÜCÜ:Senin büyü yetenegini artırmamı istiyor isen sana vericegim görevleri yapmalısın (Görev yapmak icin [@] Yola devam etmek için [F]',
                      'BÜYÜCÜ:Aferin evlat sana vericeğim görev RAGNOR kasabasından ILTERS\'ı bulman onu bulup ondan öküzgözünü al ve bana getir'])
    ]
    easteregg_positions=[
        easteregg(98,23,['Aradıgın seytansaplagi.site de saklı....']),
        easteregg(98, 1, ['TEBRİKLER!! burayı bulmayı başardın, ama asıl aradığın şey benim koordinatımın tam zıttının 4 ün karesi üstünde ']),
        easteregg(1, 37, ['evlat bu kadar merak iyi degil ama alıcağın sey, ahh! neydi unuttum belki karşı şehirdeki ikiizim hatırlıyordur'])
    ]
    büyü_yeteneği= 200
    enerji=100
    person_x = 10
    person_y = 42
    enemy_positions = [(3, 2),(3,5),(3,8),(9,8),(15,8),(21,8),(27,8),(33,8),(38,8),(44,8),(50,8),(56,8),(62,8),(68,8),(74,8),(80,8),(86,8),(92,8),(98,8),(9,2),(15,2),(21,2),(27,2),(27,5),(17,5),(12,5),(15,4),(15,6),(98,3),(98,7),(98,6),(86,5),(86,3),(86,5),(86,7)]

    while True:
        create_screen()

        add_person(person_x, person_y)

        for easteregg in   easteregg_positions:
            add_easteregs(easteregg)
        for invisbility in invisbility_positions:
            add_invisbility(invisbility)
        for border in border_positions:
            add_border(border)

        for wall in wall_positions:
            add_wall(wall)

        for asker in asker_positions:
            add_asker(asker)

        for prenses in prenses_positions:
            add_prenses(prenses)

        for büyücü in büyücü_positions:
            add_büyücü(büyücü)

        for ilters in ilters_positions:
            add_ilters(ilters)

        for Kral in  kral_positions:
            add_kral(Kral)
        for x, y in enemy_positions:
            add_enemy(x, y)
        show()
        screen.refresh()
        curses.napms(100)
        for büyücü in büyücü_positions:
            if büyücü.isNear(person_x,person_y) and büyücü.can_speak():
                for conv in büyücü.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(2000)
                büyücü.speak()
                break

        for border in border_positions:
            if border.isNear(person_x,person_y) and border.can_speak():
                for conv in border.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(0)
                border.speak()
                break
        for prenses in prenses_positions:
            if prenses.isNear(person_x,person_y) and prenses.can_speak():
                for conv in prenses.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(2000)
                prenses.speak()
                break
        for Kral in kral_positions:
            if Kral.isNear(person_x,person_y)and Kral.can_speak():
                for conv in Kral.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(2000)
                Kral.speak()
                break
        # asker kodları
        for wall in wall_positions:
            if wall.isNear(person_x,person_y) and wall.can_speak():
                for conv in wall.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(0)
                wall.speak()
                break



        for asker in asker_positions:

            if asker.isNear(person_x, person_y) and asker.can_speak():
                for conv in asker.conversations:
                    screen.addstr(0,0,conv)
                    screen.refresh()
                    curses.napms(2000)
                asker.speak()
                break

        for ilters in ilters_positions:
            if ilters.isNear(person_x,person_y) and ilters.can_speak():
                for conv in ilters.conversations:
                    screen.addstr(0, 0, conv)
                    screen.refresh()
                    curses.napms(2000)
                ilters.speak()
                break

        for easteregg in  easteregg_positions:
            if easteregg.isNear(person_x,person_y) and easteregg.can_speak():
                for conv in easteregg.conversations:
                    screen.addstr(0, 0, conv)
                    screen.refresh()
                    curses.napms(4000)
                easteregg.speak()
                break


        for invisbility in invisbility_positions:
            if invisbility.isNear(person_x,person_y) and invisbility.can_speak():
                for conv in invisbility.conversations:
                    screen.addstr(0, 0, conv)
                    screen.refresh()
                    curses.napms(2000)
                invisbility.speak()
                break

        is_enemy_killed = False
        for enemy in enemy_positions:
            x,y = enemy
            if abs(person_x - x) <= 1 and abs(person_y - y) <= 1:
                screen.addstr(0, 0, "Düşmanla karşılaştın [S]avaş yada [K]aç ?")
                fight_or_flee = screen.getch()

                if fight_or_flee in (ord('s'), ord('S')):
                    screen.addstr(0, 0, "[K]ılıç saldırısı veya [B]üyü" + (' ' * 100))
                    weapon=screen.getch()
                    if weapon in (ord('K'),ord('k')):
                        screen.addstr(0,0,"Kılıç saldırısı başladı"+(' ' * 100))
                        screen.refresh()
                        curses.napms(1500)
                        screen.addstr(0,0,"Düşmanı yendin"+(' ' * 100))
                        enemy_positions.remove(enemy)
                        is_enemy_killed = True
                    if weapon in (ord("B"),ord("b")):
                        screen.addstr(0, 0, "Yapmak istediğin büyüyü seç [A]lev veya [B]uz büyüsü " + (' '*100))
                        magic=screen.getch()
                        if magic in (ord('A'),ord('a')):
                            screen.addstr(0,0, "alev topu yağmuru başladı"+(' ' * 100))
                            screen.refresh()
                            curses.napms(1500)
                            screen.addstr(0,0,("Düşmanı yaktın")+(' ' * 100))
                            is_enemy_killed = True
                            enemy_positions.remove(enemy)
                        if magic in (ord('b'),ord('B')):
                            screen.addstr(0,0,"Düşmana buz saldırısı başladı"+(' ' * 100))
                            screen.refresh()
                            curses.napms(1300)
                            screen.addstr(0,0,"Düşman dondu onu [Ö]ldür yada [K]aç ")



                elif fight_or_flee in (ord('k'), ord('K')):
                    screen.addstr(0, 0, "Kaçılıyor..." + (' '*100))
                    curses.napms(1000)

        if is_enemy_killed:
            continue

        ch = screen.getch()
        if ch == curses.KEY_LEFT:
            person_x -= 1
        elif ch == curses.KEY_RIGHT:
            person_x += 1
        elif ch == curses.KEY_UP:
            person_y -= 1
        elif ch == curses.KEY_DOWN:
            person_y += 1
        elif ch == 127 or ch == 27:
            break

except Exception as e:
    with open('hata.txt', 'w') as wfile:
        print(e, e.args, file=wfile)
finally:
    curses.endwin()
