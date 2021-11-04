import tkinter
from cacherbase6 import decodeMessage, CacherMessage
from tkinter import *
from tkinter import messagebox


def Decoder():
    root = Tk()
    root.title("Programme pour décoder le texte caché dans un texte")

    tx = Text(root, width=100, height=5)
    tx.pack()

    l = Label(root, text="Message codé : ")

    def valider():
        letexte = tx.get("1.0", END)
        decodee = decodeMessage(letexte)
        print(decodee)
        l.config(text="Message codé : " + decodee)

    b = Button(root, text="Décoder", command=valider)
    b.pack()

    

    l.pack()

    def backmenu():
        root.destroy()
        menu()
    b3 = Button(root, text="Revenir au menu", command=backmenu)
    b3.pack()


    root.mainloop()

def Coder():
    
    root = Tk()
    root.title("Programme pour coder du texte caché dans un texte")

    l1 = Label(root, text="Mettre un message ici :")
    l1.pack()

    tx = Text(root, width=100, height=5)
    tx.pack()

    l2 = Label(root, text="Mettre un message à cacher dans le premier message ici :")
    l2.pack()

    tx2 = Text(root, width=50, height=5)
    tx2.pack()

    l3 = Label(root, text="")
    l3.pack()

    

    def valider():
        original = tx.get("1.0", END)
        cahche = tx2.get("1.0", END)
        messagecache = CacherMessage(original, cahche)
        if "Erreur ! Le message original est trop court ! Il a besoin de" in messagecache or "est trop loin dans la table UTF-8" in messagecache:
            l3.config(text=messagecache)
        else :
            tx2.destroy()
            l2.destroy()
            l3.destroy()
            l1.config(text="Le message " + cahche + "\na été caché dans le texte original!")
            tx.delete(1.0,END)
            tx.insert(1.0, messagecache)
            tx.configure(state="disabled")
            root.clipboard_clear()
            root.clipboard_append(tx.get(1.0, END)[:-1])
            messagebox.showinfo("Programme python", "Le message a été copié dans le presse papier !")
            

    b = Button(root, text="Coder !", command=valider)
    b.pack()

    def reset():
        root.destroy()
        Coder()

    b2 = Button(root, text="Reset", command=reset)
    b2.pack()

    def backmenu():
        root.destroy()
        menu()
    b3 = Button(root, text="Revenir au menu", command=backmenu)
    b3.pack()

    


    root.mainloop()

def menu():
    root = Tk()
    def launchcoder():
        root.destroy()
        Coder()
    b1 = Button(root, text="CODER UN TEXTE", command=launchcoder)
    b1.pack()

    def launchdecode():
        root.destroy()
        Decoder()
    b2 = Button(root, text="DECODER UN TEXTE", command=launchdecode)
    b2.pack()

    root.mainloop()

menu()