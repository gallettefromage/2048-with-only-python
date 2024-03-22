from tkinter import *
import random
from tkinter import filedialog, colorchooser, simpledialog
import os
chemin_actuel = os.path.abspath(__file__)
fenetre = Tk()
fenetre.geometry("720x480")
fond = "light blue"
fenetre.config(bg = fond)
fenetre.title("2048")
fenetre.iconbitmap(chemin_actuel.replace("2048.py", "download.ico"))
largeur = fenetre.winfo_width()
hauteur = fenetre.winfo_height()

fichier1nom = ""
fichier2nom = ""
fichier3nom = ""
fichiernom = chemin_actuel.replace("2048.py", "nom.txt")
with open(fichiernom, "r") as f:
        contenunom = f.read()
        exec(contenunom)
print(f"{fichier1nom}\n{fichier2nom}\n{fichier3nom}")


score = 0
police = "Arial"

hauteur = fenetre.winfo_height()
largeur = fenetre.winfo_width()

compteurc = 0

scoreaffichage = Label(fenetre, text = f"Score : {score}", font = (police, "20"))
scoreaffichage.place(x = 0, y = 0)

grille = Canvas(fenetre, height = 400, width=400, bg = "grey")
grille.pack(expand=YES)
grille.create_rectangle(0, 0, 100, 100, fill="grey")
rectangle1 = grille.create_rectangle(0, 0, 100, 100, fill="grey")
grille.create_rectangle(100, 0, 200, 100, fill="grey")
rectangle2 = grille.create_rectangle(100, 0, 200, 100, fill="grey")
grille.create_rectangle(200, 0, 300, 100, fill="grey")
rectangle3 = grille.create_rectangle(200, 0, 300, 100, fill="grey")
grille.create_rectangle(300, 0, 400, 100, fill="grey")
rectangle4 = grille.create_rectangle(300, 0, 400, 100, fill="grey")

grille.create_rectangle(0, 100, 100, 200, fill="grey")
rectangle5 = grille.create_rectangle(0, 100, 100, 200, fill="grey")
grille.create_rectangle(100, 100, 200, 200, fill="grey")
rectangle6 = grille.create_rectangle(100, 100, 200, 200, fill="grey")
grille.create_rectangle(200, 100, 300, 200, fill="grey")
rectangle7 = grille.create_rectangle(200, 100, 300, 200, fill="grey")
grille.create_rectangle(300, 100, 400, 200, fill="grey")
rectangle8 = grille.create_rectangle(300, 100, 400, 200, fill="grey")

grille.create_rectangle(0, 200, 100, 300, fill="grey")
rectangle9 = grille.create_rectangle(0, 200, 100, 300, fill="grey")
grille.create_rectangle(100, 200, 200, 300, fill="grey")
rectangle10 = grille.create_rectangle(100, 200, 200, 300, fill="grey")
grille.create_rectangle(200, 200, 300, 300, fill="grey")
rectangle11 = grille.create_rectangle(200, 200, 300, 300, fill="grey")
grille.create_rectangle(300, 200, 400, 300, fill="grey")
rectangle12 = grille.create_rectangle(300, 200, 400, 300, fill="grey")

grille.create_rectangle(0, 300, 100, 400, fill="grey")
rectangle13 = grille.create_rectangle(0, 300, 100, 400, fill="grey")
grille.create_rectangle(100, 300, 200, 400, fill="grey")
rectangle14 = grille.create_rectangle(100, 300, 200, 400, fill="grey")
grille.create_rectangle(200, 300, 300, 400, fill="grey")
rectangle15 = grille.create_rectangle(200, 300, 300, 400, fill="grey")
grille.create_rectangle(300, 300, 400, 400, fill="grey")
rectangle16 = grille.create_rectangle(300, 300, 400, 400, fill="grey")



grille.create_text(50, 50, text = "", font= ("", "72"))
c1 = grille.create_text(50, 50, text = "", font= ("", "72"))
grille.create_text(150, 50, text = "", font= ("", "72"))
c2 = grille.create_text(150, 50, text = "", font= ("", "72"))
grille.create_text(250, 50, text = "", font= ("", "72"))
c3 = grille.create_text(250, 50, text = "", font= ("", "72"))
grille.create_text(350, 50, text = "", font= ("", "72"))
c4 = grille.create_text(350, 50, text = "", font= ("", "72"))

grille.create_text(50, 150, text = "", font= ("", "72"))
c5 = grille.create_text(50, 150, text = "", font= ("", "72"))
grille.create_text(150, 150, text = "", font= ("", "72"))
c6 = grille.create_text(150, 150, text = "", font= ("", "72"))
grille.create_text(250, 150, text = "", font= ("", "72"))
c7 = grille.create_text(250, 150, text = "", font= ("", "72"))
grille.create_text(350, 150, text = "", font= ("", "72"))
c8 = grille.create_text(350, 150, text = "", font= ("", "72"))

grille.create_text(50, 250, text = "", font= ("", "72"))
c9 = grille.create_text(50, 250, text = "", font= ("", "72"))
grille.create_text(150, 250, text = "", font= ("", "72"))
c10 = grille.create_text(150, 250, text = "", font= ("", "72"))
grille.create_text(250, 250, text = "", font= ("", "72"))
c11 = grille.create_text(250, 250, text = "", font= ("", "72"))
grille.create_text(350, 250, text = "", font= ("", "72"))
c12 = grille.create_text(350, 250, text = "", font= ("", "72"))

grille.create_text(50, 350, text = "", font= ("", "72"))
c13 = grille.create_text(50, 350, text = "", font= ("", "72"))
grille.create_text(150, 350, text = "", font= ("", "72"))
c14 = grille.create_text(150, 350, text = "", font= ("", "72"))
grille.create_text(250, 350, text = "", font= ("", "72"))
c15 = grille.create_text(250, 350, text = "", font= ("", "72"))
grille.create_text(350, 350, text = "", font= ("", "72"))
c16 = grille.create_text(350, 350, text = "", font= ("", "72"))





t1 = "40"

t2 = "40"
t3 = "40"
t4 = "30"
t5 = "25"


n2 = "#FDE5E0"
n4 = "#EBCBC5"
n8 = "#FFA86C"
n16 = "#FF9959"
n32 = "#FF7151"
n64 = "#FF4426"
n128 = "#FFFD7C"
n256 = "#FDFB56"
n512 = "#FCFA45"
n1024 = "#FBF933"
n2048 = "#FCF900"
n4096 = "#34322F"
n8192 = "#000000"
n16384 = "#3F4752"
n32768 = "#48586F"
n65536 = "#406EB0"
eve= ""
eve2 = ""
coef = 0
touche = False
compteur = 0
retours = [False for _ in range(65536)]
retourscore = [False for _ in range(65536)]

def retour():
    global retours, retourscore, score
    global grille
    global rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16

    x = 0
    a = 0
    while a == 0:
        
        if not retours[x]:
            a = 1
        if a == 1:
            retours[x] = [
                grille.itemcget(rectangle1, 'fill'),
                grille.itemcget(rectangle2, 'fill'),
                grille.itemcget(rectangle3, 'fill'),
                grille.itemcget(rectangle4, 'fill'),
                grille.itemcget(rectangle5, 'fill'),
                grille.itemcget(rectangle6, 'fill'),
                grille.itemcget(rectangle7, 'fill'),
                grille.itemcget(rectangle8, 'fill'),
                grille.itemcget(rectangle9, 'fill'),
                grille.itemcget(rectangle10, 'fill'),
                grille.itemcget(rectangle11, 'fill'),
                grille.itemcget(rectangle12, 'fill'),
                grille.itemcget(rectangle13, 'fill'),
                grille.itemcget(rectangle14, 'fill'),
                grille.itemcget(rectangle15, 'fill'),
                grille.itemcget(rectangle16, 'fill')
            ]
            
            retours[x] = retours[x]
            a = 1
        else:
            x += 1
    a = 0
    x = 0
    while a == 0:
        
        if not retourscore[x]:
            a = 1
        if a == 1:
            retourscore[x] = [score]
            
            retourscore[x] = retourscore[x]
            a = 1
        else:
            x += 1

def retourl2(event=None):
    global retours, retourscore
    global score
    global grille
    global scoreaffichage

    compteur = 0
    for i in range(65535, 0, -1):
        if retours[i]:
            g = retours[i-1]
            retours[i] = False
            
            score = int(str(retourscore[i - 1]).replace("[", "").replace("]", ""))
            retourscore[i] = False

            scoreaffichage.config(text=f"Score : {score}")

            for rectangle in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
                grille.itemconfig(rectangle, fill=g[compteur])
                compteur += 1
            break
    couleur()
    
boutonarriere = Button(fenetre, text = "retour", command= retourl2, font = (police, "20"))
boutonarriere.place(x= 0,y = 670)
fichier = chemin_actuel.replace("2048.py", "sauvegarde.txt")
with open(fichier, "r") as f:
        contenu = f.read()
        print(contenu)
fichier2 = chemin_actuel.replace("2048.py", "s2.txt")
fichier3 = chemin_actuel.replace("2048.py", "s3.txt")
def sauvegarder3():
    global fichier
    global score
    global police
    global t1
    global t2
    global t3
    global t4
    global t5
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16
    print(fichier3)
    liste = []
    liste.append(grille.itemcget(rectangle1, "fill"))
    liste.append(grille.itemcget(rectangle2, "fill"))
    liste.append(grille.itemcget(rectangle3, "fill"))
    liste.append(grille.itemcget(rectangle4, "fill"))
    liste.append(grille.itemcget(rectangle5, "fill"))
    liste.append(grille.itemcget(rectangle6, "fill"))
    liste.append(grille.itemcget(rectangle7, "fill"))
    liste.append(grille.itemcget(rectangle8, "fill"))
    liste.append(grille.itemcget(rectangle9, "fill"))
    liste.append(grille.itemcget(rectangle10, "fill"))
    liste.append(grille.itemcget(rectangle11, "fill"))
    liste.append(grille.itemcget(rectangle12, "fill"))
    liste.append(grille.itemcget(rectangle13, "fill"))
    liste.append(grille.itemcget(rectangle14, "fill"))
    liste.append(grille.itemcget(rectangle15, "fill"))
    liste.append(grille.itemcget(rectangle16, "fill"))
    with open(fichier3, "w") as f:
         f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = {liste}\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
def sauvegarder2():
    global fichier
    global score
    global police
    global t1
    global t2
    global t3
    global t4
    global t5
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16
    print(fichier2)
    liste = []
    liste.append(grille.itemcget(rectangle1, "fill"))
    liste.append(grille.itemcget(rectangle2, "fill"))
    liste.append(grille.itemcget(rectangle3, "fill"))
    liste.append(grille.itemcget(rectangle4, "fill"))
    liste.append(grille.itemcget(rectangle5, "fill"))
    liste.append(grille.itemcget(rectangle6, "fill"))
    liste.append(grille.itemcget(rectangle7, "fill"))
    liste.append(grille.itemcget(rectangle8, "fill"))
    liste.append(grille.itemcget(rectangle9, "fill"))
    liste.append(grille.itemcget(rectangle10, "fill"))
    liste.append(grille.itemcget(rectangle11, "fill"))
    liste.append(grille.itemcget(rectangle12, "fill"))
    liste.append(grille.itemcget(rectangle13, "fill"))
    liste.append(grille.itemcget(rectangle14, "fill"))
    liste.append(grille.itemcget(rectangle15, "fill"))
    liste.append(grille.itemcget(rectangle16, "fill"))
    with open(fichier2, "w") as f:
        f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = {liste}\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
def sauvegarder():
    global fichier
    global score
    global police
    global t1
    global t2
    global t3
    global t4
    global t5
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16
    print(fichier)
    liste = []
    liste.append(grille.itemcget(rectangle1, "fill"))
    liste.append(grille.itemcget(rectangle2, "fill"))
    liste.append(grille.itemcget(rectangle3, "fill"))
    liste.append(grille.itemcget(rectangle4, "fill"))
    liste.append(grille.itemcget(rectangle5, "fill"))
    liste.append(grille.itemcget(rectangle6, "fill"))
    liste.append(grille.itemcget(rectangle7, "fill"))
    liste.append(grille.itemcget(rectangle8, "fill"))
    liste.append(grille.itemcget(rectangle9, "fill"))
    liste.append(grille.itemcget(rectangle10, "fill"))
    liste.append(grille.itemcget(rectangle11, "fill"))
    liste.append(grille.itemcget(rectangle12, "fill"))
    liste.append(grille.itemcget(rectangle13, "fill"))
    liste.append(grille.itemcget(rectangle14, "fill"))
    liste.append(grille.itemcget(rectangle15, "fill"))
    liste.append(grille.itemcget(rectangle16, "fill"))
    print(u1)
    with open(fichier, "w") as f:
         f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = {liste}\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
class nouvelle_parti():
    
    def noivelle():
       
        global score
        global police
        global t1
        global t2
        global t3
        global t4
        global t5
        global n2
        global n4
        global n8
        global n16
        global n32
        global n64
        global n128
        global n256
        global n512 
        global n1024
        global n2048
        global n4096
        global n8192
        global n16384
        global n32768
        global n65536
        global fichier
        score = 0
        scoreaffichage.config(text = f"Score : {score}")
        compteur = 0
        g = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]
        for i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
            grille.itemconfig(i, fill = g[compteur])
            compteur += 1      
        couleur()
        antilag()
    def aucunfichier():      
        global score
        global police
        global t1
        global t2
        global t3
        global t4
        global t5
        global n2
        global n4
        global n8
        global n16
        global n32
        global n64
        global n128
        global n256
        global n512 
        global n1024
        global n2048
        global n4096
        global n8192
        global n16384
        global n32768
        global n65536
        global fichier
        t1 = "40"

        t2 = "40"
        t3 = "40"
        t4 = "30"
        t5 = "25"


        n2 = "#FDE5E0"
        n4 = "#EBCBC5"
        n8 = "#FFA86C"
        n16 = "#FF9959"
        n32 = "#FF7151"
        n64 = "#FF4426"
        n128 = "#FFFD7C"
        n256 = "#FDFB56"
        n512 = "#FCFA45"
        n1024 = "#FBF933"
        n2048 = "#FCF900"
        n4096 = "#34322F"
        n8192 = "#000000"
        n16384 = "#3F4752"
        n32768 = "#48586F"
        n65536 = "#406EB0"
        score = 0
        scoreaffichage.config(text = f"Score : {score}")
        police = "Arial"
        compteur = 0
        g = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]
        for i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
            grille.itemconfig(i, fill = g[compteur])
            compteur += 1      
        couleur()
        antilag()
    def nouvelle_parti1():
        global fichier, score, scoreaffichage
        verification = simpledialog.askstring("Sur", "Êtes vous sur de vouloir écraser cette sauvegarde.")
        if verification.lower() == "oui":
            chargé.chargé1
            score = 0
            scoreaffichage.config(text = f"Score : {score}")
            global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
            with open(fichier, "w") as f:
                f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
            scoreaffichage.config(text = f"Score : {score}")
            nouvelle_parti.noivelle()

    def nouvelle_parti2():
        global fichier2, score, scoreaffichage
        verification = simpledialog.askstring("Sur", "Êtes vous sur de vouloir écraser cette sauvegarde.")
        if verification.lower() == "oui":
            
            chargé.chargé2
            score = 0
            scoreaffichage.config(text = f"Score : {score}")
            global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
            with open(fichier2, "w") as f:
                f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
            scoreaffichage.config(text = f"Score : {score}")
            nouvelle_parti.noivelle()
            
    def nouvelle_parti3():
        global fichier3, score, scoreaffichage
        verification = simpledialog.askstring("Sur", "Êtes vous sur de vouloir écraser cette sauvegarde.")
        if verification.lower() == "oui":
            chargé.chargé3()
            score = 0
            scoreaffichage.config(text = f"Score : {score}")
            global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
            with open(fichier3, "w") as f:
                f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
            scoreaffichage.config(text = f"Score : {score}")
            nouvelle_parti.noivelle()


def action(event):
    global compteur
    compteur = 0
    global touche
    touche = True
    global coef
    global scoreaffichage
    global score
    global police
    global t1
    global t2
    global t3
    global t4
    global t5
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16
    global eve2
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    y = 0
    global eve
    global grille
    global retour1
    global modefacile
    liste1 = []
    liste1.append(grille.itemcget(rectangle1, "fill"))
    liste1.append(grille.itemcget(rectangle2, "fill"))
    liste1.append(grille.itemcget(rectangle3, "fill"))
    liste1.append(grille.itemcget(rectangle4, "fill"))
    liste1.append(grille.itemcget(rectangle5, "fill"))
    liste1.append(grille.itemcget(rectangle6, "fill"))
    liste1.append(grille.itemcget(rectangle7, "fill"))
    liste1.append(grille.itemcget(rectangle8, "fill"))
    liste1.append(grille.itemcget(rectangle9, "fill"))
    liste1.append(grille.itemcget(rectangle10, "fill"))
    liste1.append(grille.itemcget(rectangle11, "fill"))
    liste1.append(grille.itemcget(rectangle12, "fill"))
    liste1.append(grille.itemcget(rectangle13, "fill"))
    liste1.append(grille.itemcget(rectangle14, "fill"))
    liste1.append(grille.itemcget(rectangle15, "fill"))
    liste1.append(grille.itemcget(rectangle16, "fill"))
    eve = event.keysym
    eve2 = event.char

    if event.keysym == "Left":

        liste2 = [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]
    if event.keysym == "Right":

        liste2 = [rectangle4, rectangle3, rectangle2, rectangle1, rectangle8, rectangle7, rectangle6, rectangle5, rectangle12, rectangle11, rectangle10, rectangle9, rectangle16, rectangle15, rectangle14, rectangle13]
    if event.keysym == "Up":

        liste2 = [rectangle1, rectangle5, rectangle9, rectangle13, rectangle2, rectangle6, rectangle10, rectangle14, rectangle3, rectangle7, rectangle11, rectangle15, rectangle4, rectangle8, rectangle12, rectangle16]
    if event.keysym == "Down":

        liste2 = [rectangle13, rectangle9, rectangle5, rectangle1, rectangle14, rectangle10, rectangle6, rectangle2, rectangle15, rectangle11, rectangle7, rectangle3, rectangle16, rectangle12, rectangle8, rectangle4]
    g = 1
    compteur1 = -1
    compteur2 = -2
    compteur3 = -3
    transfo1 = 0
    transfo2 = 0
    if event.keysym == "Up" or event.keysym == "Down" or event.keysym == "Right" or event.keysym == "Left":
        for rec in liste2:
            rec2 =liste2[compteur1]
            rec3 =liste2[compteur2]
            rec4 =liste2[compteur3]
            compteur1 +=1
            compteur2 +=1
            compteur3 +=1 
            if g == 2 or g  == 6 or  g == 10 or g ==14:
               a, b, c = 1, 0, 0
               transfo1 = 0
            elif g == 3 or g  == 7 or  g == 11 or g ==15:
               b, a, c = 1, 0, 0
               transfo2 = 0
            elif g == 4 or g  == 8 or  g == 12 or g ==16:
               c, a, b = 1 ,0, 0
            else:
                a,b,c = 0,0,0


            if a == 1:
                
                if not grille.itemcget(rec, "fill") == "grey":
                    if not grille.itemcget(rec2, "fill") == "grey":
                        if grille.itemcget(rec, "fill") == grille.itemcget(rec2, "fill"):
                            if grille.itemcget(rec, "fill") == n2:
                                grille.itemconfig(rec2, fill= n4)
                                grille.itemconfig(rec, fill="grey")
                                score+=4
                            elif grille.itemcget(rec, "fill") == n4:
                                grille.itemconfig(rec2, fill=n8)
                                grille.itemconfig(rec, fill="grey")
                                score+=8
                            elif grille.itemcget(rec, "fill") == n8:
                                grille.itemconfig(rec2, fill= n16)
                                grille.itemconfig(rec, fill="grey")
                                score+=14
                            elif grille.itemcget(rec, "fill") == n16:
                                grille.itemconfig(rec2, fill=n32)
                                grille.itemconfig(rec, fill="grey")
                                score+=32
                            elif grille.itemcget(rec, "fill") == n32:
                                grille.itemconfig(rec2, fill=n64)
                                grille.itemconfig(rec, fill="grey")
                                score+=64
                            elif grille.itemcget(rec, "fill") == n64:
                                grille.itemconfig(rec2, fill=n128)
                                grille.itemconfig(rec, fill="grey")
                                score+=128
                            elif grille.itemcget(rec, "fill") == n128:
                                grille.itemconfig(rec2, fill=n256)
                                grille.itemconfig(rec, fill="grey")
                                score+=256
                            elif grille.itemcget(rec, "fill") == n256:
                                grille.itemconfig(rec2, fill=n512)
                                grille.itemconfig(rec, fill="grey")
                                score+=512
                            elif grille.itemcget(rec, "fill") == n512:
                                grille.itemconfig(rec2, fill=n1024)
                                grille.itemconfig(rec, fill="grey")
                                score+=1024
                            elif grille.itemcget(rec, "fill") == n1024:
                                grille.itemconfig(rec2, fill=n2048)
                                grille.itemconfig(rec, fill="grey")
                                score+=2048
                            elif grille.itemcget(rec, "fill") == n2048:
                                grille.itemconfig(rec2, fill=n4096)
                                grille.itemconfig(rec, fill="grey")
                                score+=4096
                            elif grille.itemcget(rec, "fill") == n4096:
                                grille.itemconfig(rec2, fill=n8192)
                                grille.itemconfig(rec, fill="grey")
                                score+=8192
                            elif grille.itemcget(rec, "fill") == n8192:
                                grille.itemconfig(rec2, fill=n16384)
                                grille.itemconfig(rec, fill="grey")
                                score+=16384
                            elif grille.itemcget(rec, "fill") == n16384:
                                grille.itemconfig(rec2, fill=n32768)
                                grille.itemconfig(rec, fill="grey")
                                score+=32768
                            elif grille.itemcget(rec, "fill") == n32768:
                                grille.itemconfig(rec2, fill=n65536)
                                grille.itemconfig(rec, fill="grey")
                                score+=65536
                            transfo1 = 1
                    else:
                        y = grille.itemcget(rec, "fill")
                        grille.itemconfig(rec2, fill = str(y))
                        grille.itemconfig(rec, fill = "grey")



            elif b == 1:
                
                if not grille.itemcget(rec, "fill") == "grey":
                     
                        if not grille.itemcget(rec2, "fill") == "grey":

                            if grille.itemcget(rec2, "fill") == grille.itemcget(rec, "fill"):

                                if grille.itemcget(rec, "fill") == n2:

                                    grille.itemconfig(rec2, fill=n4)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=4
                                elif grille.itemcget(rec, "fill") == n4:
                                    grille.itemconfig(rec2, fill=n8)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=8
                                elif grille.itemcget(rec, "fill") == n8:
                                    grille.itemconfig(rec2, fill=n16)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=16
                                elif grille.itemcget(rec, "fill") == n16:
                                    grille.itemconfig(rec2, fill=n32)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=32
                                elif grille.itemcget(rec, "fill") == n32:
                                    grille.itemconfig(rec2, fill=n64)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=64
                                elif grille.itemcget(rec, "fill") == n64:
                                    grille.itemconfig(rec2, fill=n128)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=128
                                elif grille.itemcget(rec, "fill") == n128:
                                    grille.itemconfig(rec2, fill=n256)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=256
                                elif grille.itemcget(rec, "fill") == n256:
                                    grille.itemconfig(rec2, fill=n512)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=512
                                elif grille.itemcget(rec, "fill") == n512:
                                    grille.itemconfig(rec2, fill=n1024)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=1024
                                elif grille.itemcget(rec, "fill") == n1024:
                                    grille.itemconfig(rec2, fill=n2048)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=2048
                                elif grille.itemcget(rec, "fill") == n2048:
                                    grille.itemconfig(rec2, fill=n4096)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=4096
                                elif grille.itemcget(rec, "fill") == n4096:
                                    grille.itemconfig(rec2, fill=n8192)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=8192
                                elif grille.itemcget(rec, "fill") == n8192:
                                    grille.itemconfig(rec2, fill=n16384)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=16384
                                elif grille.itemcget(rec, "fill") == n16384:
                                    grille.itemconfig(rec2, fill=n32768)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=32768
                                elif grille.itemcget(rec, "fill") == n32768:
                                    grille.itemconfig(rec2, fill=n65536)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=65536
                                transfo2 = 1

                        elif not grille.itemcget(rec3, "fill") == "grey":
                            if grille.itemcget(rec3, "fill") == grille.itemcget(rec, "fill") and transfo1 == 0:
                                if grille.itemcget(rec, "fill") == n2:
                                    grille.itemconfig(rec3, fill = n4)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4
                                elif grille.itemcget(rec, "fill") ==  n4:
                                    grille.itemconfig(rec3, fill = n8)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8
                                elif grille.itemcget(rec, "fill") ==  n8:
                                    grille.itemconfig(rec3, fill = n16)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16
                                elif grille.itemcget(rec, "fill") ==  n16:
                                    grille.itemconfig(rec3, fill = n32)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32
                                elif grille.itemcget(rec, "fill") ==  n32:
                                    grille.itemconfig(rec3, fill = n64)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=64
                                elif grille.itemcget(rec, "fill") ==  n64:
                                    grille.itemconfig(rec3, fill = n128)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=128
                                elif grille.itemcget(rec, "fill") ==  n128:
                                    grille.itemconfig(rec3, fill = n256)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=256
                                elif grille.itemcget(rec, "fill") ==  n256:
                                    grille.itemconfig(rec3, fill = n512)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=512
                                elif grille.itemcget(rec, "fill") ==  n512:
                                    grille.itemconfig(rec3, fill = n1024)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=1024
                                elif grille.itemcget(rec, "fill") ==  n1024:
                                    grille.itemconfig(rec3, fill = n2048)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=2048
                                elif grille.itemcget(rec, "fill") ==  n2048:
                                    grille.itemconfig(rec3, fill = n4096)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4096
                                elif grille.itemcget(rec, "fill") ==  n4096:
                                    grille.itemconfig(rec3, fill = n8192)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8192
                                elif grille.itemcget(rec, "fill") ==  n8192:
                                    grille.itemconfig(rec3, fill = n16384)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16384
                                elif grille.itemcget(rec, "fill") ==  n16384:
                                    grille.itemconfig(rec3, fill = n32768)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32768
                                elif grille.itemcget(rec, "fill") ==  n32768:
                                    score+=65536
                                    grille.itemconfig(rec3, fill = n65536)
                                    grille.itemconfig(rec, fill = "grey")
                                transfo1 = 1
                            else:
                                y = grille.itemcget(rec, "fill")
                                grille.itemconfig(rec2, fill = y)
                                grille.itemconfig(rec, fill = "grey")


                        else:
                            y = grille.itemcget(rec, "fill")
                            grille.itemconfig(rec3, fill = y)
                            grille.itemconfig(rec, fill = "grey")
            




            elif c ==1 :
                    if not grille.itemcget(rec, "fill") == "grey":
                        if not grille.itemcget(rec2, "fill") == "grey":
                            if grille.itemcget(rec2, "fill") == grille.itemcget(rec, "fill"):
                                if grille.itemcget(rec, "fill") == n2:
                                    grille.itemconfig(rec2, fill=n4)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=4
                                elif grille.itemcget(rec, "fill") == n4:
                                    grille.itemconfig(rec2, fill=n8)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=8
                                elif grille.itemcget(rec, "fill") == n8:
                                    grille.itemconfig(rec2, fill=n16)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=16
                                elif grille.itemcget(rec, "fill") == n16:
                                    grille.itemconfig(rec2, fill=n32)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=32
                                elif grille.itemcget(rec, "fill") == n32:
                                    grille.itemconfig(rec2, fill=n64)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=64
                                elif grille.itemcget(rec, "fill") == n64:
                                    grille.itemconfig(rec2, fill=n128)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=128
                                elif grille.itemcget(rec, "fill") == n128:
                                    grille.itemconfig(rec2, fill=n256)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=256
                                elif grille.itemcget(rec, "fill") == n256:
                                    grille.itemconfig(rec2, fill=n512)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=512
                                elif grille.itemcget(rec, "fill") == n512:
                                    grille.itemconfig(rec2, fill=n1024)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=1024
                                elif grille.itemcget(rec, "fill") == n1024:
                                    grille.itemconfig(rec2, fill=n2048)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=2048
                                elif grille.itemcget(rec, "fill") == n2048:
                                    grille.itemconfig(rec2, fill=n4096)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=4096
                                elif grille.itemcget(rec, "fill") == n4096:
                                    grille.itemconfig(rec2, fill=n8192)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=8192
                                elif grille.itemcget(rec, "fill") == n8192:
                                    grille.itemconfig(rec2, fill=n16384)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=16384
                                elif grille.itemcget(rec, "fill") == n16384:
                                    grille.itemconfig(rec2, fill=n32768)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=32768
                                elif grille.itemcget(rec, "fill") == n32768:
                                    grille.itemconfig(rec2, fill=n65536)
                                    grille.itemconfig(rec, fill="grey")
                                    score+=65536

                        elif not grille.itemcget(rec3, "fill") == "grey":
                            print(str(transfo2))
                            if grille.itemcget(rec3, "fill") == grille.itemcget(rec, "fill") and transfo2 == 0:
                                if grille.itemcget(rec, "fill") == n2:
                                    grille.itemconfig(rec3, fill = n4)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4
                                elif grille.itemcget(rec, "fill") ==  n4:
                                    grille.itemconfig(rec3, fill = n8)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8
                                elif grille.itemcget(rec, "fill") ==  n8:
                                    grille.itemconfig(rec3, fill = n16)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16
                                elif grille.itemcget(rec, "fill") ==  n16:
                                    grille.itemconfig(rec3, fill = n32)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32
                                elif grille.itemcget(rec, "fill") ==  n32:
                                    grille.itemconfig(rec3, fill = n64)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=64
                                elif grille.itemcget(rec, "fill") ==  n64:
                                    grille.itemconfig(rec3, fill = n128)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=128
                                elif grille.itemcget(rec, "fill") ==  n128:
                                    grille.itemconfig(rec3, fill = n256)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=256
                                elif grille.itemcget(rec, "fill") ==  n256:
                                    grille.itemconfig(rec3, fill = n512)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=512
                                elif grille.itemcget(rec, "fill") ==  n512:
                                    grille.itemconfig(rec3, fill = n1024)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=1024
                                elif grille.itemcget(rec, "fill") ==  n1024:
                                    grille.itemconfig(rec3, fill = n2048)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=2048
                                elif grille.itemcget(rec, "fill") ==  n2048:
                                    grille.itemconfig(rec3, fill = n4096)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4096
                                elif grille.itemcget(rec, "fill") ==  n4096:
                                    grille.itemconfig(rec3, fill = n8192)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8192
                                elif grille.itemcget(rec, "fill") ==  n8192:
                                    grille.itemconfig(rec3, fill = n16384)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16384
                                elif grille.itemcget(rec, "fill") ==  n16384:
                                    grille.itemconfig(rec3, fill = n32768)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32768
                                elif grille.itemcget(rec, "fill") ==  n32768:
                                    grille.itemconfig(rec3, fill = n65536)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=65536
                            else:
                                y = grille.itemcget(rec, "fill")
                                grille.itemconfig(rec2, fill = str(y))
                                grille.itemconfig(rec, fill = "grey")
                    
                        elif not grille.itemcget(rec4, "fill") == "grey":
                            if grille.itemcget(rec4, "fill") == grille.itemcget(rec, "fill")  and transfo1 == 0:
                                if grille.itemcget(rec, "fill") == n2:
                                    grille.itemconfig(rec4, fill = n4)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4
                                elif grille.itemcget(rec, "fill") ==  n4:
                                    grille.itemconfig(rec4, fill = n8)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8
                                elif grille.itemcget(rec, "fill") ==  n8:
                                    grille.itemconfig(rec4, fill = n16)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16
                                elif grille.itemcget(rec, "fill") ==  n16:
                                    grille.itemconfig(rec4, fill = n32)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32
                                elif grille.itemcget(rec, "fill") ==  n32:
                                    grille.itemconfig(rec4, fill = n64)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=64
                                elif grille.itemcget(rec, "fill") ==  n64:
                                    grille.itemconfig(rec4, fill = n128)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=128
                                elif grille.itemcget(rec, "fill") ==  n128:
                                    grille.itemconfig(rec4, fill = n256)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=256
                                elif grille.itemcget(rec, "fill") ==  n256:
                                    grille.itemconfig(rec4, fill = n512)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=512
                                elif grille.itemcget(rec, "fill") ==  n512:
                                    grille.itemconfig(rec4, fill = n1024)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=1024
                                elif grille.itemcget(rec, "fill") ==  n1024:
                                    grille.itemconfig(rec4, fill = n2048)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=2048
                                elif grille.itemcget(rec, "fill") ==  n2048:
                                    grille.itemconfig(rec4, fill = n4096)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=4096
                                elif grille.itemcget(rec, "fill") ==  n4096:
                                    grille.itemconfig(rec4, fill = n8192)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=8192
                                elif grille.itemcget(rec, "fill") ==  n8192:
                                    grille.itemconfig(rec4, fill = n16384)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=16384
                                elif grille.itemcget(rec, "fill") ==  n16384:
                                    grille.itemconfig(rec4, fill = n32768)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=32768
                                elif grille.itemcget(rec, "fill") ==  n32768:
                                    grille.itemconfig(rec4, fill = n65536)
                                    grille.itemconfig(rec, fill = "grey")
                                    score+=65536
                            else:
                                y = grille.itemcget(rec, "fill")
                                grille.itemconfig(rec3, fill = str(y))
                                grille.itemconfig(rec, fill = "grey")

                        else:
                            y = grille.itemcget(rec, "fill")
                            grille.itemconfig(rec4, fill = str(y))
                            grille.itemconfig(rec, fill = "grey")







            g+=1
        liste2 = []
        liste2.append(str(grille.itemcget(rectangle1, "fill")))
        liste2.append(grille.itemcget(rectangle2, "fill"))
        liste2.append(grille.itemcget(rectangle3, "fill"))
        liste2.append(grille.itemcget(rectangle4, "fill"))
        liste2.append(grille.itemcget(rectangle5, "fill"))
        liste2.append(grille.itemcget(rectangle6, "fill"))
        liste2.append(grille.itemcget(rectangle7, "fill"))
        liste2.append(grille.itemcget(rectangle8, "fill"))
        liste2.append(grille.itemcget(rectangle9, "fill"))
        liste2.append(grille.itemcget(rectangle10, "fill"))
        liste2.append(grille.itemcget(rectangle11, "fill"))
        liste2.append(grille.itemcget(rectangle12, "fill"))
        liste2.append(grille.itemcget(rectangle13, "fill"))
        liste2.append(grille.itemcget(rectangle14, "fill"))
        liste2.append(grille.itemcget(rectangle15, "fill"))
        liste2.append(grille.itemcget(rectangle16, "fill"))
        if not liste1 == liste2 or modefacile == 1 or liste2 == ['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey']:
            print("ebhfe")
            commencer()
            retour()
        print(liste1)
        print(liste2)
        scoreaffichage.config(text= f"Score : {score}")



















def commencer():
    global scoreaffichage
    global score
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global rectangle1
    global rectangle2
    global rectangle3
    global rectangle4
    global rectangle5
    global rectangle6
    global rectangle7
    global rectangle8
    global rectangle9
    global rectangle10
    global rectangle11
    global rectangle12
    global rectangle13
    global rectangle14
    global rectangle15
    global rectangle16
    r = 0
    r = random.randint(0, 15)
    liste = [rectangle4, rectangle3, rectangle2, rectangle1, rectangle8, rectangle7, rectangle6, rectangle5, rectangle12, rectangle11, rectangle10, rectangle9, rectangle16, rectangle15, rectangle14, rectangle13]
    if grille.itemcget(liste[r], "fill") == "grey":
        grille.itemconfig(liste[r], fill = n2)
    else:
        commencer()
    score += 2
    scoreaffichage.config(text= f"Score : {score}")
    couleur()


u1 = "black"#2
u2 = "black"#4
u3 = "black"#8
u4 = "black"#16
u5 = "black"#32
u6 = "black"#64
u7 = "black"#128
u8 = "black"#256
u9 = "black"#512
u10 = "black"#1024
u11 = "black"#2048
u12 = "white"#4096
u13 = "white"#8192
u14 = "white"#16 mille
u15 = "white"# 32 mille
u16 = "white"#65 mille

def couleur():
    global u1
    global u2
    global u3
    global u4
    global u5
    global u6
    global u7
    global u8
    global u9
    global u10
    global u11
    global u12
    global u13
    global u14
    global u15
    global u16
    global t1
    global t2
    global t3
    global t4
    global t5
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global rectangle1
    global rectangle2
    global rectangle3
    global rectangle4
    global rectangle5
    global rectangle6
    global rectangle7
    global rectangle8
    global rectangle9
    global rectangle10
    global rectangle11
    global rectangle12
    global rectangle13
    global rectangle14
    global rectangle15
    global rectangle16
    global touche
    global gz
    print(gz)
    touche = False
    compteur = 0
    for g in [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]:
        if compteur == 0:
            h = grille.itemcget(rectangle1,"fill")
        if compteur == 1:
            h = grille.itemcget(rectangle2,"fill")
        if compteur == 2:
            h = grille.itemcget(rectangle3,"fill")
        if compteur == 3:
            h = grille.itemcget(rectangle4,"fill")
        if compteur == 4:
            h = grille.itemcget(rectangle5,"fill")
        if compteur == 5:
            h = grille.itemcget(rectangle6,"fill")
        if compteur == 6:
            h = grille.itemcget(rectangle7,"fill")
        if compteur == 7:
            h = grille.itemcget(rectangle8,"fill")
        if compteur == 8:
            h = grille.itemcget(rectangle9,"fill")
        if compteur == 9:
            h = grille.itemcget(rectangle10,"fill")
        if compteur == 10:
            h = grille.itemcget(rectangle11,"fill")
        if compteur == 11:
            h = grille.itemcget(rectangle12,"fill")
        if compteur == 12:
            h = grille.itemcget(rectangle13,"fill")
        if compteur == 13:
            h = grille.itemcget(rectangle14,"fill")
        if compteur == 14:
            h = grille.itemcget(rectangle15,"fill")
        if compteur == 15:
            h = grille.itemcget(rectangle16,"fill")


        if h == "grey":
            grille.itemconfig(g, text = "", font = (police, t1))
        if h == n2:
            grille.itemconfig(g, text = "2", font = (police, t1), fill = u1)
        if h == n4:
            grille.itemconfig(g, text = "4", font = (police, t1),  fill = u2)
        if h == n8:
            grille.itemconfig(g, text = "8", font = (police, t1),  fill = u3)
        if h == n16:
            grille.itemconfig(g, text = "16", font = (police, t2),  fill = u4 )
        if h == n32:
            grille.itemconfig(g, text = "32", font = (police, t2),  fill = u5)
        if h == n64:
            grille.itemconfig(g, text = "64", font = (police, t2),  fill = u6)
        if h == n128:
            grille.itemconfig(g, text = "128", font = (police, t3),  fill = u7)
        if h == n256:
            grille.itemconfig(g, text = "256", font = (police, t3),  fill = u8)
        if h == n512:
            grille.itemconfig(g, text = "512", font = (police, t3),  fill = u9)
        if h == n1024:
            grille.itemconfig(g, text = "1024", font = (police, t4),  fill = u10)
        if h == n2048:
            grille.itemconfig(g, text = "2048", font = (police, t4),  fill = u11 )
        if h == n4096:
            grille.itemconfig(g, text = "4096", font = (police, t4),  fill = u12 )
        if h == n8192:
            grille.itemconfig(g, text = "8192", font = (police, t4),  fill = u13 )
        if h == n16384:
            grille.itemconfig(g, text = "16384", font = (police, t5),  fill = u14 )
        if h == n32768:
            grille.itemconfig(g, text = "32768", font = (police, t5),  fill = u15 )
        if h == n65536:
            grille.itemconfig(g, text = "65536", font = (police, t5),  fill = u16 )
        compteur +=1
    


textc = ""


l2 = False
l4 = False
l8 = False
l16 = False
l32 = False
l64 = False
l128 = False
l256 = False
l512 = False
l1024 = False
l2048 = False
l4000 = False
l8000 = False
l16000 = False
l32000 = False
l65000 = False
def autre():
    pass


endroitmenu = Frame(fenetre)
endroitmenu.place(x= 0, y = 36)
parti = Menubutton(endroitmenu, text = "Option", activebackground= "pink", bd = "2", relief = "raised", font = ('', "15"))
parti.grid(column= 0, row=0, padx = 0, pady= 0)

sousmenuoption = Menu(parti, tearoff= 0)
parti.config(menu = sousmenuoption)

def quitter_PERS():
    fenetre.attributes('-fullscreen', False)
    Endroit_personalisation.place_forget()
    endroitmenu_pers.lift()


Endroit_personalisation = Frame(fenetre, bg = "grey", width= 2000, height= 2000)
endroitmenu_pers = Frame(Endroit_personalisation)
endroitmenu_pers.place(x=0,y=0)
option_pers = Menubutton(endroitmenu_pers, text = "Personalisation : Fichier brut", bd = 2, relief= "raised", activebackground= "light green")
option_pers.grid(row = 0, column=0, padx= 0, pady=0)
menu_pers = Menu(option_pers, tearoff= 0)
option_pers.config(menu = menu_pers)
textfichier  = contenu
fichierbrute = Label(Endroit_personalisation, bg = "grey", fg = "white", font= ("", "15"), width= 1000, text = textfichier, anchor="w", justify="left")
fichierbrute.place(x=100, y=0)
def rei():
    global n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police
    global listecouleur
    listeconfigpers()
    couleurpers = [n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police]
    n2 = "#FDE5E0"
    n4 = "#EBCBC5"
    n8 = "#FFA86C"
    n16 = "#FF9959"
    n32 = "#FF7151"
    n64 = "#FF4426"
    n128 = "#FFFD7C"
    n256 = "#FDFB56"
    n512 = "#FCFA45"
    n1024 = "#FBF933"
    n2048 = "#FCF900"
    n4096 = "#34322F"
    n8192 = "#000000"
    n16384 = "#3F4752"
    n32768 = "#48586F"
    n65536 = "#406EB0"
    couleurrei = [n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police]
    compteur2 = 0
    for y in couleurpers:
     compteur = 0
     for i in listecouleur:
        if i == y:
            listecouleur[compteur]=couleurrei[compteur2]
        compteur +=1
     compteur2 +=1
    print(listecouleur)
    compteur = 0
    for i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
        grille.itemconfig(i, fill = listecouleur[compteur])
        compteur += 1
    couleur()
    bouton.config(bg = n2)
    bouton4.config(bg = n4)
    bouton8.config(bg = n8)
    bouton16.config(bg = n16)
    bouton32.config(bg = n32)
    bouton64.config(bg = n64)
    bouton128.config(bg = n128)
    bouton256.config(bg = n256)
    bouton512.config(bg = n512)
    bouton1024.config(bg = n1024)
    bouton2048.config(bg = n2048)
    bouton4092.config(bg = n4096)
    bouton8000.config(bg = n8192)
    bouton16000.config(bg = n16384)
    bouton32000.config(bg = n32768)
    bouton64000.config(bg = n65536)


listecouleur = []
def listeconfigpers():
    global listecouleur
    listecouleur = []
    listecouleur.append(grille.itemcget(rectangle1, "fill"))
    listecouleur.append(grille.itemcget(rectangle2, "fill"))
    listecouleur.append(grille.itemcget(rectangle3, "fill"))
    listecouleur.append(grille.itemcget(rectangle4, "fill"))
    listecouleur.append(grille.itemcget(rectangle5, "fill"))
    listecouleur.append(grille.itemcget(rectangle6, "fill"))
    listecouleur.append(grille.itemcget(rectangle7, "fill"))
    listecouleur.append(grille.itemcget(rectangle8, "fill"))
    listecouleur.append(grille.itemcget(rectangle9, "fill"))
    listecouleur.append(grille.itemcget(rectangle10, "fill"))
    listecouleur.append(grille.itemcget(rectangle11, "fill"))
    listecouleur.append(grille.itemcget(rectangle12, "fill"))
    listecouleur.append(grille.itemcget(rectangle13, "fill"))
    listecouleur.append(grille.itemcget(rectangle14, "fill"))
    listecouleur.append(grille.itemcget(rectangle15, "fill"))
    listecouleur.append(grille.itemcget(rectangle16, "fill"))


code_hex = "0"
couleuravant = "0"
def changement():
    global code_hex
    global couleuravant
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur" )
    compteur = 0
    for i in listecouleur:
        if i == couleuravant:
           listecouleur[compteur]= code_hex
        compteur +=1
    compteur = 0
    for i in retours:
            if not i == False:
                compteur2= 0
                listeretour = i
                for o in listeretour:
                    if o == couleuravant:
                        listeretour[compteur2] = code_hex
                    compteur2 +=1
                retours[compteur] = listeretour
                compteur +=1
    compteur = 0
    for i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
        grille.itemconfig(i, fill = listecouleur[compteur])
        compteur += 1
    couleur()
def choisir_couleur2():
    global grille
    global couleuravant
    global n2, u1
    couleuravant = n2
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton.config(bg = code_hex) 
        n2 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u1 = code_hex
        bouton.config(fg = u1)

def choisir_couleur4():
    global grille
    global couleuravant
    global n4
    global u2
    couleuravant = n4
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton4.config(bg = code_hex)
        n4 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u2 = code_hex
        bouton4.config(fg = u2)
def choisir_couleur8():
    global grille
    global couleuravant
    global n8
    global u3
    couleuravant = n8
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton8.config(bg = code_hex)
        n8 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u3 = code_hex
        bouton8.config(fg = u3)

def choisir_couleur16():
    global grille
    global couleuravant
    global n16
    global u4
    couleuravant = n16
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton16.config(bg = code_hex)
        n16 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u4 = code_hex
        bouton16.config(fg = u4)


def choisir_couleur32():
    global grille
    global couleuravant
    global n32
    global u5
    couleuravant = n32
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton32.config(bg = code_hex)
        n32 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u5 = code_hex
        bouton32.config(fg = u5)

def choisir_couleur64():
    global grille
    global couleuravant
    global n64
    global u6
    couleuravant = n64
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton64.config(bg = code_hex)
        n64 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u6 = code_hex
        bouton64.config(fg = u6)
def choisir_couleur128():
    global grille
    global couleuravant
    global n128
    global u7
    couleuravant = n128
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton128.config(bg = code_hex)
        n128 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u7 = code_hex
        bouton128.config(fg = u7)

def choisir_couleur256():
    global grille
    global couleuravant
    global n256
    global u8
    couleuravant = n256
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton256.config(bg = code_hex)
        n256 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u8 = code_hex
        bouton256.config(fg = u8)

def choisir_couleur512():
    global grille
    global couleuravant
    global n512
    global u9
    couleuravant = n512
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton512.config(bg = code_hex)
        n512 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u9 = code_hex
        bouton512.config(fg = u9)

def choisir_couleur1024():
    global grille
    global couleuravant
    global n1024
    global u10
    couleuravant = n1024
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton1024.config(bg = code_hex)
        n1024 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u10 = code_hex
        bouton1024.config(fg = u10)
def choisir_couleur2048():
    global grille
    global couleuravant
    global n2048
    global u11
    couleuravant = n2048
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton2048.config(bg = code_hex)
        n2048 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u11 = code_hex
        bouton2048.config(fg = u11)

def choisir_couleur4092():
    global grille
    global couleuravant
    global n4096
    global u12
    couleuravant = n4096
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton4092.config(bg = code_hex)
        n4096 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u12 = code_hex
        bouton4092.config(fg = u12)


def choisir_couleur8192():
    global grille
    global couleuravant
    global n8192,u13
    couleuravant = n8192
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton8000.config(bg = code_hex)
        n8192 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u13 = code_hex
        bouton8000.config(fg = u13)

def choisir_couleur1600():
    global grille
    global couleuravant
    global n16384,u14
    couleuravant = n16384
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton16000.config(bg = code_hex)
        n16384 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u14 = code_hex
        bouton16000.config(fg = u14)
def choisir_couleur32000():
    global grille
    global couleuravant
    global n32768,u15
    couleuravant = n32768
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton32000.config(bg = code_hex)
        n32768 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u15 = code_hex
        bouton32000.config(fg = u15)

def choisir_couleur65000():
    global grille
    global couleuravant
    global n65536,u16
    couleuravant = n65536
    listeconfigpers()
    global listecouleur
    global code_hex
    changement()
    if not code_hex == None:
        bouton64000.config(bg = code_hex)
        n65536 = code_hex
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None:
        u16 = code_hex
        bouton64000.config(fg = u16)

endroi_couleur = Frame(Endroit_personalisation, width= 400, height= 460, bg = "grey")
renisialiser = Button(endroi_couleur, text ="Réinitialisé", command = rei, font = (police, "20"))
renisialiser.place (x= 0,y=400)
bouton = Button(endroi_couleur, text="2", command=choisir_couleur2, bg = n2, width=5, height= 2, font =("", '25'), fg = u1)
bouton.place(x=0,y=0)
bouton4 = Button(endroi_couleur, text="4", command=choisir_couleur4, bg = n4,  width=5, height= 2, font =("", '25'), fg = u2)
bouton4.place(x=100,y=0)
bouton8 = Button(endroi_couleur, text="8", command=choisir_couleur8, bg = n8,  width=5, height= 2, font =("", '25'), fg = u3)
bouton8.place(x=200,y=0)
bouton16 = Button(endroi_couleur, text="16", command=choisir_couleur16, bg = n16,  width=5, height= 2, font =("", '25'), fg = u4)
bouton16.place(x=300,y=0)
bouton32 = Button(endroi_couleur, text="32", command=choisir_couleur32, bg = n32,  width=5, height= 2, font =("", '25'), fg = u5)
bouton32.place(x=00,y=100)
bouton64 = Button(endroi_couleur, text="64", command=choisir_couleur64, bg = n64, width=5, height= 2, font =("", '25'), fg = u6)
bouton64.place(x=100,y=100)
bouton128 = Button(endroi_couleur, text="128", command=choisir_couleur128, bg = n128, width=5, height= 2, font =("", '25'), fg = u7)
bouton128.place(x=200,y=100)
bouton256 = Button(endroi_couleur, text="256", command=choisir_couleur256, bg = n256, width=5, height= 2, font =("", '25'), fg = u8)
bouton256.place(x=300,y=100)


bouton512 = Button(endroi_couleur, text="512", command=choisir_couleur512, bg = n512,  width=5, height= 2, font =("", '25'), fg = u9)
bouton512.place(x=00,y=200)
bouton1024 = Button(endroi_couleur, text="1024", command=choisir_couleur1024, bg = n1024,  width=5, height= 2, font =("", '25'), fg = u10)
bouton1024.place(x=100,y=200)
bouton2048 = Button(endroi_couleur, text="2048", command=choisir_couleur2048, bg = n2048,  width=5, height= 2, font =("", '25'), fg = u11)
bouton2048.place(x=200,y=200)
bouton4092 = Button(endroi_couleur, text="4096", command=choisir_couleur4092, bg = n4096,  width=5, height= 2, font =("", '25'), fg = u12)
bouton4092.place(x=300,y=200)
bouton8000 = Button(endroi_couleur, text="8192", command=choisir_couleur8192, bg = n8192,  width=5, height= 2, font =("", '25'), fg = u13)
bouton8000.place(x=00,y=300)
bouton16000 = Button(endroi_couleur, text="16384", command=choisir_couleur1600, bg = n16384, width=5, height= 2, font =("", '25'), fg = u14)
bouton16000.place(x=100,y=300)
bouton32000 = Button(endroi_couleur, text="32768", command=choisir_couleur32000, bg = n32768, width=5, height= 2, font =("", '25'), fg = u15)
bouton32000.place(x=200,y=300)
bouton64000 = Button(endroi_couleur, text="65536", command=choisir_couleur65000, bg = n65536, width=5, height= 2, font =("", '25'), fg = u16)
bouton64000.place(x=300,y=300)

ln2 = ""
ln4 = ""
ln8 = ''
ln16 = ""
ln32 = ""
ln64 = ""
ln128 = ""
ln256 = ""
ln512 = ""
ln1024 = ""
ln2048 = ""
ln4096 = ""
ln8192 = ""
ln16384 = ""
ln32768 = ""
ln65536 = ""

class THEME:

    
    def noiretblanc():
        global chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128,ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        ln2 = "#ffffff"
        ln4 = "#e5e5e5"
        ln8 = "#cdcdcd"
        ln16 = "#c4c4c4"
        ln32 = "#b4b4b4"
        ln64 = "#a6a6a6"
        ln128 = "#959595"
        ln256 = "#868686"
        ln512 = "#7c7c7c"
        ln1024 = "#7a7a7a"
        ln2048 = "#707070"
        ln4096 = "#6a6a6a"
        ln8192 = "#585858"
        ln16384 = "#4e4e4e"
        ln32768 = "#353535"
        ln65536 = "#0a0a0a"
        THEME.modif()
        u16 = "white"
        u15 = "white"
        u14 = "white"
        u13 = "white"
        u12 = "white"
        u11 = "black"
        u10 = "black"
        u9 = "#080808"
        u8 = "black"
        u7 = "black"
        u6 = "black"
        u5 = "black"
        u1 = "black"
        u2 = "black"
        u3 = "black"
        u4 = "black"
        fond = "#c1c1c1"
        n2 = "#ffffff"
        n4 = "#e5e5e5"
        n8 = "#cdcdcd"
        n16 = "#c4c4c4"
        n32 = "#b4b4b4"
        n64 = "#a6a6a6"
        n128 = "#959595"
        n256 = "#868686"
        n512 = "#7c7c7c"
        n1024 = "#7a7a7a"
        n2048 = "#707070"
        n4096 = "#6a6a6a"
        n8192 = "#585858"
        n16384 = "#4e4e4e"
        n32768 = "#353535"
        n65536 = "#0a0a0a"
        police = "Castellar"
        couleur_pers()
        fenetre.config(bg = fond)
        Endroit_fondmodif.config(bg = fond)
    def rainbow():
        global chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128,ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        ln2 = "#80ff80"
        ln4 = "#80ff00"
        ln8 = "#00ff00"
        ln16 = "#008000"
        ln32 = "#ff8000"
        ln64 = "#ff8040"
        ln128 = "#ffff00"
        ln256 = "#ffff80"
        ln512 = "#ff8080"
        ln1024 = "#ff0000"
        ln2048 = "#d70000"
        ln4096 = "#800000"
        ln8192 = "#b900b9"
        ln16384 = "#ff00ff"
        ln32768 = "#ff55ff"
        ln65536 = "#ffa6ff"
        THEME.modif()      
        u16 = "#000000"
        u15 = "#000000"
        u14 = "#000000"
        u13 = "#000000"
        u12 = "#000000"
        u11 = "black"
        u10 = "black"
        u9 = "black"
        u8 = "black"
        u7 = "black"
        u6 = "black"
        u5 = "black"
        u1 = "black"
        u2 = "black"
        u3 = "black"
        u4 = "black"
        fond = "#ceed54"
        n2 = "#80ff80"
        n4 = "#80ff00"
        n8 = "#00ff00"
        n16 = "#008000"
        n32 = "#ff8000"
        n64 = "#ff8040"
        n128 = "#ffff00"
        n256 = "#ffff80"
        n512 = "#ff8080"
        n1024 = "#ff0000"
        n2048 = "#d70000"
        n4096 = "#800000"
        n8192 = "#b900b9"
        n16384 = "#ff00ff"
        n32768 = "#ff55ff"
        n65536 = "#ffa6ff"
        police = "French Script MT"
        couleur_pers()
        fenetre.config(bg = fond)
        Endroit_fondmodif.config(bg = fond)
    def desert():
        global chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128,ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        ln2 = "#ff9d6f"
        ln4 = "#ff915b"
        ln8 = "#ff854a"
        ln16 = "#ff7837"
        ln32 = "#ff6f28"
        ln64 = "#ff6215"
        ln128 = "#fb5200"
        ln256 = "#e14900"
        ln512 = "#d54500"
        ln1024 = "#ca4200"
        ln2048 = "#ae3800"
        ln4096 = "#973100"
        ln8192 = "#842b00"
        ln16384 = "#712400"
        ln32768 = "#5b1e00"
        ln65536 = "#421500"
        THEME.modif()
        u16 = "white"
        u15 = "white"
        u14 = "white"
        u13 = "#ffffff"
        u12 = "#000000"
        u11 = "black"
        u10 = "black"
        u9 = "black"
        u8 = "black"
        u7 = "black"
        u6 = "black"
        u5 = "black"
        u1 = "black"
        u2 = "black"
        u3 = "black"
        u4 = "black"
        fond = "#ff9d6f"
        n2 = "#ff9d6f"
        n4 = "#ff915b"
        n8 = "#ff854a"
        n16 = "#ff7837"
        n32 = "#ff6f28"
        n64 = "#ff6215"
        n128 = "#fb5200"
        n256 = "#e14900"
        n512 = "#d54500"
        n1024 = "#ca4200"
        n2048 = "#ae3800"
        n4096 = "#973100"
        n8192 = "#842b00"
        n16384 = "#712400"
        n32768 = "#5b1e00"
        n65536 = "#421500"
        police = "Algerian"
        couleur_pers()
        fenetre.config(bg = fond)
        Endroit_fondmodif.config(bg = fond)
    def sauvegardé():
        global chemin_actuel, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        fichierpers = chemin_actuel.replace("2048.py", "perso.txt")
        with open(fichierpers, "w") as f:
            f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"')
    def chargé():
        listeconfigpers()
        global listecouleur
        global chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128,ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        fichierpers = chemin_actuel.replace("2048.py", "perso.txt")
        
        dico = {'u16' : u16,'u15' : u15,'u14' : u14,'u13' : u13,'u12' : u12,'u11' : u11,'u10' : u10,'u9' : u9,'u8' : u8,'u7' : u7,'u6' : u6,'u5' : u5,'u4' : u4,'u3' : u3,'u2' : u2,'u1' : u1,'fond': fond, 'police':police,'t4':t4,'t3':t3,'t2':t2,'t1':t1,'n65536':n65536,'n32768':n32768,'n16384':n16384,'n8192':n8192,'n4096':n4096,'n2048':n2048,'n1024':n1024,'n512':n512,'n256':n256,'n128':n128,'n64':n64,'n8':n8,'n4':n4,'n16':n16,'n32':n32, 'couleur' : couleur, 'grille' : grille,'n2': n2, 'rectangle1': rectangle1, 'rectangle2': rectangle2, 'rectangle3': rectangle3, 'rectangle4': rectangle4, 'rectangle5': rectangle5, 'rectangle6': rectangle6, 'rectangle7': rectangle7, 'rectangle8': rectangle8, 'rectangle9': rectangle9, 'rectangle10': rectangle10, 'rectangle11': rectangle11, 'rectangle12': rectangle12, 'rectangle13': rectangle13, 'rectangle14': rectangle14, 'rectangle15': rectangle15, 'rectangle16': rectangle16}
        with open(fichierpers, "r") as f:
            contenu = f.read()
            exec(contenu, dico)
        ln2 = dico['n2']
        ln4 = dico['n4']
        ln8 = dico['n8']
        ln16 = dico['n16']
        ln32 = dico['n32']
        ln64 = dico['n64']
        ln128 = dico['n128']
        ln256 = dico['n256']
        ln512 = dico['n512']
        ln1024 = dico['n1024']
        ln2048 = dico['n2048']
        ln8192 = dico['n8192']
        ln16384 = dico['n16384']
        ln32768 = dico['n32768']
        ln65536 = dico['n65536']
        THEME.modif()
        n2 = dico['n2']
        n4 = dico['n4']
        n8 = dico['n8']
        n16 = dico['n16']
        n32 = dico['n32']
        n64 = dico['n64']
        n128 = dico['n128']
        n256 = dico['n256']
        n512 = dico['n512']
        n1024 = dico['n1024']
        n2048 = dico['n2048']
        n4096 = dico['n4096']
        n8192 = dico['n8192']
        n16384 = dico['n16384']
        n32768 = dico['n32768']
        n65536 = dico['n65536']
        t1 = dico['t1']
        t2 = dico['t2']
        t3 = dico['t3']
        t4 = dico['t4']
        fond = dico['fond']
        police = dico['police']
        u1 = dico['u1']
        u2 = dico['u2']
        u3 = dico['u3']
        u4 = dico['u4']
        u5 = dico['u5']
        u6 = dico['u6']
        u7 = dico['u7']
        u8 = dico['u8']
        u9 = dico['u9']
        u10 = dico['u10']
        u11 = dico['u11']
        u12 = dico['u12']
        u13 = dico['u13']
        u14 = dico['u14']
        u15 = dico['u15']
        u16 = dico['u16']
        fenetre.config(bg = fond)
        Endroit_fondmodif.config(bg = fond)
        couleur_pers()
        couleur()
    def apartir():
        global listecouleur, chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128, ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        rgb, code_hex = colorchooser.askcolor(title = "Couleur du block 2")
        sequence_couleurs = [rgb]
        if not rgb == None:
            listeconleurpers = []
            
            def assombrir_couleur(rgb, facteur):
                r, g, b = rgb
                r = max(int(r * facteur),0)
                g = max(int(g * facteur),0)
                b = max(int(b * facteur),0)
                return r, g, b
            

            for i in range (1, 16):
                facteur = 1 - (i * 0.06)
                couleur_assombrie = assombrir_couleur(rgb, facteur)
                sequence_couleurs.append(couleur_assombrie)
            for couleur in sequence_couleurs:
                    r, g ,b = couleur
                    code_hex = '#%02x%02x%02x' % (r, g ,b)
                    listeconleurpers.append(code_hex)
            print(listeconleurpers)
            ln2 = listeconleurpers[0]
            ln4 = listeconleurpers[1]
            ln8 = listeconleurpers[2]
            ln16 = listeconleurpers[3]
            ln32 = listeconleurpers[4]
            ln64 = listeconleurpers[5]
            ln128 = listeconleurpers[6]
            ln256 = listeconleurpers[7]
            ln512 = listeconleurpers[8]
            ln1024 = listeconleurpers[9]
            ln2048 = listeconleurpers[10]
            ln4096 = listeconleurpers[11]
            ln8192 = listeconleurpers[12]
            ln16384 = listeconleurpers[13]
            ln32768 = listeconleurpers[14]
            ln65536 = listeconleurpers[15]
            THEME.modif()
            n2 = listeconleurpers[0]
            n4 = listeconleurpers[1]
            n8 = listeconleurpers[2]
            n16 = listeconleurpers[3]
            n32 = listeconleurpers[4]
            n64 = listeconleurpers[5]
            n128 = listeconleurpers[6]
            n256 = listeconleurpers[7]
            n512 = listeconleurpers[8]
            n1024 = listeconleurpers[9]
            n2048 = listeconleurpers[10]
            n4096 = listeconleurpers[11]
            n8192 = listeconleurpers[12]
            n16384 = listeconleurpers[13]
            n32768 = listeconleurpers[14]
            n65536 = listeconleurpers[15]
            fond = listeconleurpers[2]
            u11= "white"
            u12 = "white"
            u13= "white"
            u14 = "white"
            u15 = "white"
            u16  ="white"
            couleur_pers()
            fenetre.config(bg = fond)
            Endroit_fondmodif.config(bg = fond)
    def modif():
        print("modif")
        global listecouleur,retour, chemin_actuel,ln2,ln4,ln8,ln16,ln32,ln64,ln128, ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        g = [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]
        compteur = 0  
        for i in g:
            rec = g[compteur]
            compteur+=1
            if grille.itemcget(rec, 'fill') == n2:
                grille.itemconfig(rec, fill = ln2)
            if grille.itemcget(i, 'fill') == n4:
                grille.itemconfig(i, fill = ln4)
            if grille.itemcget(i, 'fill') == n8:
                grille.itemconfig(i, fill = ln8)
            if grille.itemcget(i, 'fill') == n16:
                grille.itemconfig(i, fill = ln16)
            if grille.itemcget(i, 'fill') == n32:
                grille.itemconfig(i, fill = ln32)
            if grille.itemcget(i, 'fill') == n64:
                grille.itemconfig(i, fill = ln64)
            if grille.itemcget(i, 'fill') == n128:
                grille.itemconfig(i, fill = ln128)
            if grille.itemcget(i, 'fill') == n256:
                grille.itemconfig(i, fill = ln256)
            if grille.itemcget(i, 'fill') == n512:
                grille.itemconfig(i, fill = ln512)
            if grille.itemcget(i, 'fill') == n1024:
                grille.itemconfig(i, fill = ln1024)
            if grille.itemcget(i, 'fill') == n2048:
                grille.itemconfig(i, fill = ln2048)
            if grille.itemcget(i, 'fill') == n4096:
                grille.itemconfig(i, fill = ln4096)
            if grille.itemcget(i, 'fill') == n8192:
                grille.itemconfig(i, fill = ln8192)
            if grille.itemcget(i, 'fill') == n16384:
                grille.itemconfig(i, fill = ln16384)
            if grille.itemcget(i, 'fill') == n32768:
                grille.itemconfig(i, fill = ln32768)
            if grille.itemcget(i, 'fill') == n65536:
                grille.itemconfig(i, fill = ln65536)
            retourconfig()

def retourconfig():
        global retours, ln2,ln4,ln8,ln16,ln32,ln64,ln128, ln256,ln512,ln1024,ln2048,ln4096, ln8192,ln16384,ln32768,ln65536, u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        compteur = 0
        for i in retours:
            if not i == False:
                compteur2= 0
                listeretour = i
                for o in listeretour:
                    if o == n2:
                        listeretour[compteur2] = ln2
                    if o == n4:
                        listeretour[compteur2] = ln4
                    if o == n8:
                        listeretour[compteur2] = ln8
                    if o == n16:
                        listeretour[compteur2] = ln16
                    if o == n32:
                        listeretour[compteur2] = ln32
                    if o == n64:
                        listeretour[compteur2] = ln64
                    if o == n128:
                        listeretour[compteur2] = ln128
                    if o == n256:
                        listeretour[compteur2] = ln256
                    if o == n512:
                        listeretour[compteur2] = ln512
                    if o == n1024:
                        listeretour[compteur2] = ln1024
                    if o == n2048:
                        listeretour[compteur2] = ln2048
                    if o == n4096:
                        listeretour[compteur2] = ln4096
                    if o == n8192:
                        listeretour[compteur2] = ln8192
                    if o == n16384:
                        listeretour[compteur2] = ln16384
                    if o == n32768:
                        listeretour[compteur2] = ln32768
                    if o == n65536:
                        listeretour[compteur2] = ln65536
                    compteur2 +=1
                retours[compteur] = listeretour
                compteur +=1


Préset = Menu(option_pers, tearoff=0)
themesauv = Menu(option_pers, tearoff=0)
themesauv.add_command(label = "Sauvegarder", command = THEME.sauvegardé)
themesauv.add_separator()
themesauv.add_command(label = "Chargé", command = THEME.chargé)
Préset.add_cascade(label = "Thème personalisé", menu = themesauv)
Préset.add_separator()
Préset.add_command(label = "Noir et blanc", command = THEME.noiretblanc)
Préset.add_separator()
Préset.add_command(label = "Multicolor", command = THEME.rainbow)
Préset.add_separator()
Préset.add_command(label = "Désert", command = THEME.desert)
Préset.add_separator()
Préset.add_command( label = "A partir de la couleur du block 2", command = THEME.apartir)
menu_pers.add_cascade(menu=Préset, label = "Thème")
menu_pers.add_separator()

def couleur_pers():
    Endroit_fondmodif.place_forget()
    option_pers.config(text = "Personalisation : Couleurs")
    endroi_couleur.place(x= 100, y = 100)
    fichierbrute.place_forget()
    bouton.config(bg = n2, fg = u1, font = (police, '25'))
    bouton4.config(bg = n4, fg = u2, font = (police, '25'))
    bouton8.config(bg = n8, fg = u3, font = (police, '25'))
    bouton16.config(bg = n16, fg = u4, font = (police, '25'))
    bouton32.config(bg = n32, fg = u5, font = (police, '25'))
    bouton64.config(bg = n64, fg = u6, font = (police, '25'))
    bouton128.config(bg = n128, fg = u7, font = (police, '25'))
    bouton256.config(bg = n256, fg = u8, font = (police, '25'))
    bouton512.config(bg = n512, fg = u9, font = (police, '25'))
    bouton1024.config(bg = n1024, fg = u10, font = (police, '25'))
    bouton2048.config(bg = n2048, fg = u11, font = (police, '25'))
    bouton4092.config(bg = n4096, fg = u12, font = (police, '25'))
    bouton8000.config(bg = n8192, fg = u13, font = (police, '25'))
    bouton16000.config(bg = n16384, fg = u14, font = (police, '25'))
    bouton32000.config(bg = n32768, fg = u14, font = (police, '25'))
    bouton64000.config(bg = n65536, fg = u16, font = (police, '25'))

menu_pers.add_command(label = "Couleurs", activebackground= "light green", command=couleur_pers)
menu_pers.add_separator()

def fichier_pers():
    Endroit_fondmodif.place_forget()
    endroi_couleur.place_forget()
    option_pers.config(text = "Personalisation : Fichier brut")
    fichierbrute.place(x=100, y=100)

menu_pers.add_command(label = "Fichier brut", activebackground= "light green", command = fichier_pers)
menu_pers.add_separator()
def fond_pers():
    endroi_couleur.place_forget()
    option_pers.config(text = "Personalisation : Fond")
    fichierbrute.place_forget()
    Endroit_fondmodif.place(x= 300, y = 200)
def modifierfondpers():
    global fond
    x, code_hex = colorchooser.askcolor(title="Sélectionner une couleur")
    if not code_hex == None :
        fond = code_hex
        fenetre.config(bg = code_hex)
        Endroit_fondmodif.config(bg = code_hex)
Endroit_fondmodif = Frame(Endroit_personalisation, width= 720, height = 480 , bg = fond)
modifier_fond = Button(Endroit_fondmodif, font = ("", "25"), command = modifierfondpers, text = "Couleur")
modifier_fond.place(x=0, y=0)
menu_pers.add_command(label = "Fond", activebackground= "light green", command= fond_pers)
menu_pers.add_separator()
class POLICE():
    def maj():
        bouton.config(bg = n2, fg = u1, font = (police, '25'))
        bouton4.config(bg = n4, fg = u2, font = (police, '25'))
        bouton8.config(bg = n8, fg = u3, font = (police, '25'))
        bouton16.config(bg = n16, fg = u4, font = (police, '25'))
        bouton32.config(bg = n32, fg = u5, font = (police, '25'))
        bouton64.config(bg = n64, fg = u6, font = (police, '25'))
        bouton128.config(bg = n128, fg = u7, font = (police, '25'))
        bouton256.config(bg = n256, fg = u8, font = (police, '25'))
        bouton512.config(bg = n512, fg = u9, font = (police, '25'))
        bouton1024.config(bg = n1024, fg = u10, font = (police, '25'))
        bouton2048.config(bg = n2048, fg = u11, font = (police, '25'))
        bouton4092.config(bg = n4096, fg = u12, font = (police, '25'))
        bouton8000.config(bg = n8192, fg = u13, font = (police, '25'))
        bouton16000.config(bg = n16384, fg = u14, font = (police, '25'))
        bouton32000.config(bg = n32768, fg = u14, font = (police, '25'))
        bouton64000.config(bg = n65536, fg = u16, font = (police, '25'))
    def policechange():
        global police
        police = simpledialog.askstring("police", "Choisir une police")
        POLICE.maj()
    def Algerian():
        global police
        police = "Algerian"
        POLICE.maj()
    def BlackadderITC():
        global police
        police = "Blackadder ITC"
        POLICE.maj()
    def Castellar():
        global police
        police = "Castellar"
        POLICE.maj()
    def CooperBlack():
        global police
        police = "Cooper Black"
        POLICE.maj()
    def Chiller():
        global police
        police = "Chiller"
        POLICE.maj()
    def ComicSansMS():
        global police
        police = "Comic Sans MS"
        POLICE.maj()
    def FrenchScriptMT():
        global police
        police = "French Script MT"
        POLICE.maj()
    def Mistral():
        global police
        police = "Mistral"
        POLICE.maj()
    def rei():
        global police
        police = "Arial"
        POLICE.maj()
    def Jokerman():
        global police
        police = "Jokerman"
        POLICE.maj()
    def Symbol():
        global police
        police = "Symbol"
        POLICE.maj()
    def BookshelfSymbol7():
        global police
        police = "Bookshelf Symbol 7"
        POLICE.maj()
    def Elephant():
        global police
        police = "Elephant"
        POLICE.maj()
    def BodoniMTPosterCompressed():
        global police
        police = "Bodoni MT Poster Compressed"
        POLICE.maj()
        
        
menu_pers_police = Menu(menu_pers, tearoff=0)
menu_pers_police.add_command(label = "Choisir soit même", command= POLICE.policechange)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Réinitialisé", font = (""), command= POLICE.rei)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Algerian", font = ("Algerian"), command= POLICE.Algerian)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Bodoni MT Poster Compressed", font = ("Bodoni MT Poster Compressed", '15'), command= POLICE.BodoniMTPosterCompressed)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Blackadder ITC", font = ("Blackadder ITC", "15"), command= POLICE.BlackadderITC)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Castellar", font = ("Castellar"), command= POLICE.Castellar)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Chiller", font = ("Chiller"), command= POLICE.Chiller)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Comic Sans MS", font = ("Comic Sans MS", '15'), command= POLICE.ComicSansMS)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Cooper Black", font = ("Cooper Black", "15"), command= POLICE.CooperBlack)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Elephant", font = ("Elephant", "15"), command= POLICE.Elephant)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "French Script MT", font = ("French Script MT", '15'), command= POLICE.FrenchScriptMT)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Jokerman", font = ("Jokerman"), command= POLICE.Jokerman)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Mistral", font = ("Mistral"), command= POLICE.Mistral)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Symbol", font = ("Symbol"), command= POLICE.Symbol)
menu_pers_police.add_separator()
menu_pers_police.add_command(label = "Bookshelf Symbol 7", font = ("Bookshelf Symbol 7", "15"), command= POLICE.BookshelfSymbol7)


menu_pers.add_cascade(label = "Police", menu=menu_pers_police)

menu_pers.add_separator()


menu_pers.add_command(label = "Quitter", activebackground= "light green", command= quitter_PERS)


def antilag():
    global retours, retourscore
    retours = []
    retours = [False for _ in range(65536)]
    retourscore = []
    retourscore = [False for _ in range(65536)]


sous_menu_cote = Menu(parti, tearoff=0)
sous_menu_cote.add_command(label=fichier1nom, command = sauvegarder)
sous_menu_cote.add_separator()
sous_menu_cote.add_command(label=fichier2nom, command= sauvegarder2)
sous_menu_cote.add_separator()
sous_menu_cote.add_command(label=fichier3nom, command= sauvegarder3)
sousmenuoption.add_cascade(label="Sauvegarder", menu=sous_menu_cote)
gz = "550"
class chargé: 
    def chargé1():
        global score,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        global gz
        dico = {'score': score,'u16' : u16,'u15' : u15,'u14' : u14,'u13' : u13,'u12' : u12,'u11' : u11,'u10' : u10,'u9' : u9,'u8' : u8,'u7' : u7,'u6' : u6,'u5' : u5,'u4' : u4,'u3' : u3,'u2' : u2,'u1' : u1,'fond': fond, 'police':police,'t4':t4,'t3':t3,'t2':t2,'t1':t1,'n65536':n65536,'n32768':n32768,'n16384':n16384,'n8192':n8192,'n4096':n4096,'n2048':n2048,'n1024':n1024,'n512':n512,'n256':n256,'n128':n128,'n64':n64,'n8':n8,'n4':n4,'n16':n16,'n32':n32, 'couleur' : couleur, 'grille' : grille,'n2': n2, 'rectangle1': rectangle1, 'rectangle2': rectangle2, 'rectangle3': rectangle3, 'rectangle4': rectangle4, 'rectangle5': rectangle5, 'rectangle6': rectangle6, 'rectangle7': rectangle7, 'rectangle8': rectangle8, 'rectangle9': rectangle9, 'rectangle10': rectangle10, 'rectangle11': rectangle11, 'rectangle12': rectangle12, 'rectangle13': rectangle13, 'rectangle14': rectangle14, 'rectangle15': rectangle15, 'rectangle16': rectangle16}
        with open(fichier, "r") as f:
            contenu = f.read()
            exec(contenu, dico)
        n2 = dico['n2']
        n4 = dico['n4']
        n8 = dico['n8']
        n16 = dico['n16']
        n32 = dico['n32']
        n64 = dico['n64']
        n128 = dico['n128']
        n256 = dico['n256']
        n512 = dico['n512']
        n1024 = dico['n1024']
        n2048 = dico['n2048']
        n4096 = dico['n4096']
        n8192 = dico['n8192']
        n16384 = dico['n16384']
        n32768 = dico['n32768']
        n65536 = dico['n65536']
        t1 = dico['t1']
        t2 = dico['t2']
        t3 = dico['t3']
        t4 = dico['t4']
        fond = dico['fond']
        police = dico['police']
        u1 = dico['u1']
        u2 = dico['u2']
        u3 = dico['u3']
        u4 = dico['u4']
        u5 = dico['u5']
        u6 = dico['u6']
        u7 = dico['u7']
        u8 = dico['u8']
        u9 = dico['u9']
        u10 = dico['u10']
        u11 = dico['u11']
        u12 = dico['u12']
        u13 = dico['u13']
        u14 = dico['u14']
        u15 = dico['u15']
        u16 = dico['u16']
        score = dico['score']
        scoreaffichage.config(text = f"Score : {score}")
        fenetre.config(bg = fond)
        couleur()
        antilag()
    def chargé2():
        global score,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        dico = {'score': score,'u16' : u16,'u15' : u15,'u14' : u14,'u13' : u13,'u12' : u12,'u11' : u11,'u10' : u10,'u9' : u9,'u8' : u8,'u7' : u7,'u6' : u6,'u5' : u5,'u4' : u4,'u3' : u3,'u2' : u2,'u1' : u1,'fond': fond, 'police':police,'t4':t4,'t3':t3,'t2':t2,'t1':t1,'n65536':n65536,'n32768':n32768,'n16384':n16384,'n8192':n8192,'n4096':n4096,'n2048':n2048,'n1024':n1024,'n512':n512,'n256':n256,'n128':n128,'n64':n64,'n8':n8,'n4':n4,'n16':n16,'n32':n32, 'couleur' : couleur, 'grille' : grille,'n2': n2, 'rectangle1': rectangle1, 'rectangle2': rectangle2, 'rectangle3': rectangle3, 'rectangle4': rectangle4, 'rectangle5': rectangle5, 'rectangle6': rectangle6, 'rectangle7': rectangle7, 'rectangle8': rectangle8, 'rectangle9': rectangle9, 'rectangle10': rectangle10, 'rectangle11': rectangle11, 'rectangle12': rectangle12, 'rectangle13': rectangle13, 'rectangle14': rectangle14, 'rectangle15': rectangle15, 'rectangle16': rectangle16}
        with open(fichier2, "r") as f:
            contenu = f.read()
            exec(contenu, dico)
        n2 = dico['n2']
        n4 = dico['n4']
        n8 = dico['n8']
        n16 = dico['n16']
        n32 = dico['n32']
        n64 = dico['n64']
        n128 = dico['n128']
        n256 = dico['n256']
        n512 = dico['n512']
        n1024 = dico['n1024']
        n2048 = dico['n2048']
        n4096 = dico['n4096']
        n8192 = dico['n8192']
        n16384 = dico['n16384']
        n32768 = dico['n32768']
        n65536 = dico['n65536']
        t1 = dico['t1']
        t2 = dico['t2']
        t3 = dico['t3']
        t4 = dico['t4']
        fond = dico['fond']
        police = dico['police']
        u1 = dico['u1']
        u2 = dico['u2']
        u3 = dico['u3']
        u4 = dico['u4']
        u5 = dico['u5']
        u6 = dico['u6']
        u7 = dico['u7']
        u8 = dico['u8']
        u9 = dico['u9']
        u10 = dico['u10']
        u11 = dico['u11']
        u12 = dico['u12']
        u13 = dico['u13']
        u14 = dico['u14']
        u15 = dico['u15']
        u16 = dico['u16']
        score = dico['score']
        scoreaffichage.config(text = f"Score : {score}")
        fenetre.config(bg = fond)
        couleur()
        antilag()
    def chargé3():
        global score,u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16,n2, n4 ,n16,n32,n64,n128,n256,n512,n1024,n2048,n4096,n8192,n8,n16384,n32768,n65536,t1,t2,t3,t4,police, fond
        dico = {'score': score,'u16' : u16,'u15' : u15,'u14' : u14,'u13' : u13,'u12' : u12,'u11' : u11,'u10' : u10,'u9' : u9,'u8' : u8,'u7' : u7,'u6' : u6,'u5' : u5,'u4' : u4,'u3' : u3,'u2' : u2,'u1' : u1,'fond': fond, 'police':police,'t4':t4,'t3':t3,'t2':t2,'t1':t1,'n65536':n65536,'n32768':n32768,'n16384':n16384,'n8192':n8192,'n4096':n4096,'n2048':n2048,'n1024':n1024,'n512':n512,'n256':n256,'n128':n128,'n64':n64,'n8':n8,'n4':n4,'n16':n16,'n32':n32, 'couleur' : couleur, 'grille' : grille,'n2': n2, 'rectangle1': rectangle1, 'rectangle2': rectangle2, 'rectangle3': rectangle3, 'rectangle4': rectangle4, 'rectangle5': rectangle5, 'rectangle6': rectangle6, 'rectangle7': rectangle7, 'rectangle8': rectangle8, 'rectangle9': rectangle9, 'rectangle10': rectangle10, 'rectangle11': rectangle11, 'rectangle12': rectangle12, 'rectangle13': rectangle13, 'rectangle14': rectangle14, 'rectangle15': rectangle15, 'rectangle16': rectangle16}
        with open(fichier3, "r") as f:
            contenu = f.read()
            exec(contenu, dico)
        n2 = dico['n2']
        n2 = dico['n2']
        n4 = dico['n4']
        n8 = dico['n8']
        n16 = dico['n16']
        n32 = dico['n32']
        n64 = dico['n64']
        n128 = dico['n128']
        n256 = dico['n256']
        n512 = dico['n512']
        n1024 = dico['n1024']
        n2048 = dico['n2048']
        n4096 = dico['n4096']
        n8192 = dico['n8192']
        n16384 = dico['n16384']
        n32768 = dico['n32768']
        n65536 = dico['n65536']
        t1 = dico['t1']
        t2 = dico['t2']
        t3 = dico['t3']
        t4 = dico['t4']
        fond = dico['fond']
        police = dico['police']
        u1 = dico['u1']
        u2 = dico['u2']
        u3 = dico['u3']
        u4 = dico['u4']
        u5 = dico['u5']
        u6 = dico['u6']
        u7 = dico['u7']
        u8 = dico['u8']
        u9 = dico['u9']
        u10 = dico['u10']
        u11 = dico['u11']
        u12 = dico['u12']
        u13 = dico['u13']
        u14 = dico['u14']
        u15 = dico['u15']
        u16 = dico['u16']
        score = dico['score']
        scoreaffichage.config(text = f"Score : {score}")
        fenetre.config(bg = fond)
        couleur()
        antilag()

sous_menu_chargé = Menu(parti, tearoff= 0)
sous_menu_chargé.add_command(label = fichier1nom, command = chargé.chargé1)
sous_menu_chargé.add_separator()
sous_menu_chargé.add_command(label = fichier2nom, command = chargé.chargé2)
sous_menu_chargé.add_separator()
sous_menu_chargé.add_command(label = fichier3nom, command = chargé.chargé3)
sousmenuoption.add_separator()
sousmenuoption.add_cascade(label= "Chargé", menu = sous_menu_chargé)

sousmenuoption.add_separator()

sous_menu_nouvellepari  = Menu(parti, tearoff= 0)
sous_menu_nouvellepari.add_command(label = "Aucun fichier", command = nouvelle_parti.aucunfichier)
sous_menu_nouvellepari.add_separator()
sous_menu_nouvellepari.add_command(label = fichier1nom, command = nouvelle_parti.nouvelle_parti1)
sous_menu_nouvellepari.add_separator()
sous_menu_nouvellepari.add_command(label = fichier2nom, command = nouvelle_parti.nouvelle_parti2)
sous_menu_nouvellepari.add_separator()
sous_menu_nouvellepari.add_command(label = fichier3nom, command = nouvelle_parti.nouvelle_parti3)
sousmenuoption.add_cascade(label = "Nouvelle partie", menu = sous_menu_nouvellepari)

sousmenuoption.add_separator()

sous_menu_renomer = Menu(parti, tearoff = 0)
index_fichier2nom = sous_menu_nouvellepari.index(fichier3nom)

# Imprimez l'index
print("L'index de fichier2nom dans sous_menu_nouvellepari est :", index_fichier2nom)
def renomé1():
    global fichier1nom
    global sous_menu_nouvellepari
    fichier1nom = simpledialog.askstring("nom du fichier :", "nom du fichier :")
    sous_menu_renomer.entryconfig(0, label = fichier1nom)
    sous_menu_chargé.entryconfig(0, label = fichier1nom)
    sous_menu_cote.entryconfig(0, label = fichier1nom)
    sous_menu_nouvellepari.entryconfig(2, label = fichier1nom)            
sous_menu_renomer.add_command(label = fichier1nom, command = renomé1)
sous_menu_renomer.add_separator()
def renomé2():
    global fichier2nom
    fichier2nom = simpledialog.askstring("nom du fichier :", "nom du fichier :")
    sous_menu_renomer.entryconfig(2, label = fichier2nom)
    sous_menu_nouvellepari.entryconfig(4, label = fichier2nom)
    sous_menu_chargé.entryconfig(2, label = fichier2nom)
    sous_menu_cote.entryconfig(2, label = fichier2nom)
sous_menu_renomer.add_command(label = fichier2nom, command = renomé2)
sous_menu_renomer.add_separator()
def renomé3():
    global fichier3nom
    fichier3nom = simpledialog.askstring("nom du fichier :", "nom du fichier :")
    sous_menu_renomer.entryconfig(4, label = fichier3nom)
    sous_menu_nouvellepari.entryconfig(6, label = fichier3nom)
    sous_menu_chargé.entryconfig(4, label = fichier3nom)
    sous_menu_cote.entryconfig(4, label = fichier3nom)
sous_menu_renomer.add_command(label = fichier3nom, command = renomé3)
sousmenuoption.add_cascade(label = "Renomer", menu = sous_menu_renomer)



sousmenuoption.add_separator()

sousmenuoption.add_command(label = "Anti Bug", activebackground= "pink", command= antilag)
sousmenuoption.add_separator()





def personnalisation():
    global n2
    fenetre.attributes('-fullscreen', True)
    Endroit_personalisation.place(x=0,y=0)
    endroitmenu_pers.lift()
    couleur_pers()
    

sousmenuoption.add_command(label = "Personnnalisation", activebackground= "pink",command = personnalisation)
sousmenuoption.add_separator()
  
def réinitialisation():
    a = simpledialog.askstring("Sur","Sur?")
    if a.lower() == "oui":
       
        global score
        global police
        global t1
        global t2
        global t3
        global t4
        global t5
        global n2
        global n4
        global n8
        global n16
        global n32
        global n64
        global n128
        global n256
        global n512 
        global n1024
        global n2048
        global n4096
        global n8192
        global n16384
        global n32768
        global n65536
        global fichier
        global fichier2
        global fichier3
        global fichier1nom
        global fichier2nom
        global fichier3nom
        global u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15,u16
        score = 0
        u1 = "black"#2
        u2 = "black"#4
        u3 = "black"#8
        u4 = "black"#16
        u5 = "black"#32
        u6 = "black"#64
        u7 = "black"#128
        u8 = "black"#256
        u9 = "black"#512
        u10 = "black"#1024
        u11 = "black"#2048
        u12 = "white"#4096
        u13 = "white"#8192
        u14 = "white"#16 mille
        u15 = "white"# 32 mille
        u16 = "white"#65 mille
        t1 = "40"

        t2 = "40"
        t3 = "40"
        t4 = "30"
        t5 = "25"


        n2 = "#FDE5E0"
        n4 = "#EBCBC5"
        n8 = "#FFA86C"
        n16 = "#FF9959"
        n32 = "#FF7151"
        n64 = "#FF4426"
        n128 = "#FFFD7C"
        n256 = "#FDFB56"
        n512 = "#FCFA45"
        n1024 = "#FBF933"
        n2048 = "#FCF900"
        n4096 = "#34322F"
        n8192 = "#000000"
        n16384 = "#3F4752"
        n32768 = "#48586F"
        n65536 = "#406EB0"
        score = 0
        police = "Arial"
        compteur = 0
        g = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]
        for i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
            grille.itemconfig(i, fill = g[compteur])
            compteur += 1      
        couleur()
        with open (fichiernom, "w") as f:
            f.write(f"fichier1nom = 'Fichier 1'\nfichier2nom = 'Fichier 2'\nfichier3nom = 'Fichier 3'")
        with open(fichier, "w") as f:
            f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
        with open(fichier2, "w") as f:
            f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
        with open(fichier3, "w") as f:
            f.write(f'u16 = "{u16}"\nu15 = "{u15}"\nu14 = "{u14}"\nu13 = "{u13}"\nu12 = "{u12}"\nu11 = "{u11}"\nu10 = "{u10}"\nu9 = "{u9}"\nu8 = "{u8}"\nu7 = "{u7}"\nu6 = "{u6}"\nu5 = "{u5}"\nu1 = "{u1}"\nu2 = "{u2}"\nu3 = "{u3}"\nu4 = "{u4}"\nfond = "{fond}"\nt1 = "{t1}"\nt2 = "{t2}"\nt3 = "{t3}"\nt4 = "{t4}"\nt5 = "{t5}"\nn2 = "{n2}"\nn4 = "{n4}"\nn8 = "{n8}"\nn16 = "{n16}"\nn32 = "{n32}"\nn64 = "{n64}"\nn128 = "{n128}"\nn256 = "{n256}"\nn512 = "{n512}"\nn1024 = "{n1024}"\nn2048 = "{n2048}"\nn4096 = "{n4096}"\nn8192 = "{n8192}"\nn16384 = "{n16384}"\nn32768 = "{n32768}"\nn65536 = "{n65536}"\nscore = {score}\npolice = "{police}"\ncompteur = 0\ng = ["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"]\nfor i in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:\n        grille.itemconfig(i, fill = g[compteur])\n        compteur += 1\ncouleur()')
        fenetre.destroy()
sousmenuoption.add_command(label = "Réinitialisé", activebackground= "Red", command= réinitialisation)






def maj(event):
  try:
    global compteur
    global touche
    global coef
    global scoreaffichage
    global score
    global police
    global t1
    global t2
    global t3
    global t4
    global t5
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16
    global eve2
    global n2
    global n4
    global n8
    global n16
    global n32
    global n64
    global n128
    global n256
    global n512 
    global n1024
    global n2048
    global n4096
    global n8192
    global n16384
    global n32768
    global n65536
    global eve
    global grille
    largeur = fenetre.winfo_width()
    hauteur = fenetre.winfo_height()
    if largeur < hauteur:
        coef =  720/ largeur
    else:
        coef = 480/hauteur
    cor = (0, 0, (100/ coef), (100/ coef))
    grille.coords(rectangle1, cor)
    grille.tag_raise(rectangle1)
    cor = ((100 / coef), 0, (200/ coef), (100/ coef))
    grille.coords(rectangle2,  cor)
    grille.tag_raise(rectangle2)
    cor = ((200 / coef ), 0, (300/ coef ), (100/ coef ))
    grille.coords(rectangle3,  cor)
    grille.tag_raise(rectangle3)
    cor = ((300 / coef ), 0, (400/ coef ), (100/ coef ))
    grille.coords(rectangle4,  cor)
    grille.tag_raise(rectangle4)
    cor = (0, (100 / coef ), (100/ coef ), (200/ coef ))
    grille.coords(rectangle5,  cor)
    grille.tag_raise(rectangle5)
    cor = ((100 / coef ), (100 / coef ), (200/ coef ), (200/ coef ))
    grille.coords(rectangle6, cor)
    grille.tag_raise(rectangle6)
    cor = ((200 / coef ), (100 / coef ), (300/ coef ), (200/ coef ))
    grille.coords(rectangle7,  cor)
    grille.tag_raise(rectangle7)
    cor = ((300 / coef ), (100 / coef ), (400/ coef ), (200/ coef ))
    grille.coords(rectangle8,  cor)
    grille.tag_raise(rectangle8)


    cor = (0, (200 / coef ), (100/ coef ), (300/ coef))
    grille.coords(rectangle9,  cor)
    grille.tag_raise(rectangle9)
    cor = ((100 / coef ), (200 / coef ), (200/ coef), (300/ coef ))
    grille.coords(rectangle10,  cor)
    grille.tag_raise(rectangle10)
    cor = ((200 / coef ), (200 / coef ), (300/ coef ), (300/ coef))
    grille.coords(rectangle11,  cor)
    grille.tag_raise(rectangle11)
    cor = ((300 / coef ), (200 / coef ), (400/ coef), (300/ coef ))
    grille.coords(rectangle12,  cor)
    grille.tag_raise(rectangle12)
    cor = (0, (300 / coef ), (100/ coef ), (400/ coef ))
    grille.coords(rectangle13,  cor)
    grille.tag_raise(rectangle13)
    cor = ((100 / coef ), (300 / coef ), (200/ coef), (400/ coef ))
    grille.coords(rectangle14,  cor)
    grille.tag_raise(rectangle14)
    cor = ((200 / coef ), (300 / coef ), (300/ coef ), (400/ coef ))
    grille.coords(rectangle15,  cor)
    grille.tag_raise(rectangle15)
    cor = ((300 / coef ), (300 / coef ), (400/ coef ), (400/ coef ))
    grille.coords(rectangle16,  cor)
    grille.config(width=(400 / coef ), height=(400 / coef ))
    grille.tag_raise(rectangle16)


    grille.coords(c1,(50 / coef ), (50 / coef ) )
    grille.tag_raise(c1)
    grille.coords(c2,(150 / coef ), (50 / coef ) )
    grille.tag_raise(c2)
    grille.coords(c3,(250 / coef ), (50 / coef ) )
    grille.tag_raise(c3)
    grille.coords(c4,(350 / coef ), (50 / coef ) )
    grille.tag_raise(c4)
    grille.coords(c5,(50 / coef ), (150 / coef ) )
    grille.tag_raise(c5)
    grille.coords(c6,(150 / coef ), (150 / coef ) )
    grille.tag_raise(c6)
    grille.coords(c7,(250 / coef ), (150 / coef ) )
    grille.tag_raise(c7)
    grille.coords(c8,(350 / coef ), (150 / coef ) )
    grille.tag_raise(c8)
    grille.coords(c9,(50 / coef ), (250 / coef ) )
    grille.tag_raise(c9)
    grille.coords(c10,(150 / coef ), (250 / coef ) )
    grille.tag_raise(c10)
    grille.coords(c11,(250 / coef ), (250 / coef ) )
    grille.tag_raise(c11)
    grille.coords(c12,(350 / coef ), (250 / coef ) )
    grille.tag_raise(c12)
    grille.coords(c13,(50 / coef ), (350 / coef ) )
    grille.tag_raise(c13)
    grille.coords(c14,(150 / coef ), (350 / coef ) )
    grille.tag_raise(c14)
    grille.coords(c15,(250 / coef ), (350 / coef ) )
    grille.tag_raise(c15)
    grille.coords(c16,(350 / coef ), (350 / coef ) )
    grille.tag_raise(c16)

    t1 = str(int(40/coef//1))
    t2 = str(int(40/coef//1))
    t3 = str(int(40/coef//1))
    t4 = str(int(30/coef//1))
    t5 = str(int(25/coef//1))

    scoreaffichage.config(font = (police, str(int(20/coef//1))))
    boutonarriere.config(font = (police, str(int(20/coef//1))))
    boutonarriere.place(y= hauteur-(50/coef), x =0)
    endroitmenu.place(x= 0, y = 36/coef)
    parti.config(font = (police, str(int(15/coef//1))))
    endroitmenu_pers.lift()
    option_pers.lift()
    couleur()
  except:
      print("fin")

def fermer():
    global fichiernom,fichier1nom,fichier2nom,fichier3nom
    with open (fichiernom, "w") as f:
        f.write(f"fichier1nom = '{fichier1nom}'\nfichier2nom = '{fichier2nom}'\nfichier3nom = '{fichier3nom}'")
    print("t")
    fenetre.destroy()

sousmenuoption.add_separator()
sousmode = Menu(parti, tearoff=0)
modefacile = 0

def modesimple():
    global modefacile
    sousmenuoption.entryconfig(14, label = "Mode : simple")
    modefacile = 1
def modenormal():
    global modefacile
    sousmenuoption.entryconfig(14, label = "Mode : normal")
    modefacile = 0
sousmode.add_command(label="Simple", command = modesimple)
sousmode.add_separator()
sousmode.add_command(label="Normal", command = modenormal)
sousmenuoption.add_cascade(label="Mode : normal", menu=sousmode, activebackground= "grey")


def perspective():
    global retours, retourscore
    global score
    global grille
    global scoreaffichage
    facteur = simpledialog.askstring("Seconde", "Nombre de seconde entre chaque étape")
    facteur = facteur.replace(",", ".")
    try:
        facteur = float(facteur)
    except: 
        facteur = None
    if not facteur == None:
        compteur = 0
        for i in retours:    
            if retours[compteur]:
                g  = retours[compteur]
                print(g)
                print(retours[compteur])
                compteur2=0
                for rectangle in [rectangle1, rectangle2, rectangle3, rectangle4, rectangle5, rectangle6, rectangle7, rectangle8, rectangle9, rectangle10, rectangle11, rectangle12, rectangle13, rectangle14, rectangle15, rectangle16]:
                    grille.itemconfig(rectangle, fill=g[compteur2])
                    compteur2 += 1
            else:   break
            couleur()
            fenetre.update()
            fenetre.after(int((float(facteur)*1000)//1))
            compteur +=1

sousmenuoption.add_separator()
sousmenuoption.add_command(label = "Perspective", activebackground= "purple", command = perspective)
def retourl3(event):
    retourl2()

fenetre.protocol("WM_DELETE_WINDOW", fermer)
fenetre.bind('<Key>', action, autre)
fenetre.bind('<z>', retourl3)
fenetre.bind("<Configure>", maj)
fenetre.mainloop()

