import tkinter
import random
import math

tester = math.tau.real

# Instansier GUI
root = tkinter.Tk()

# Ændr baggrundsfarve/navn/størrelse i main vindue
root.configure(bg="white")
root.title("Min To-DO-Liste")
root.geometry("300x500")

# Tom liste
opgaver = []

# Liste til test
opgaver = ["Lave lektier", "Fis den af", "Slå Græs"]

# Funktionerne

def opdater_lb_opgaver():
    # Tøm listeboks lb_opgaver
    toem_lb_opgaver()

    # Opdater listeboks lb_opgaver
    for opgave in opgaver:
        lb_opgaver.insert("end", opgave)


def toem_lb_opgaver():
    lb_opgaver.delete(0, "end")


def tilfoej_opgave():
    # Fang input i tekstfeltet
    opgave = txt_input.get()

    # Inputvalidering
    if opgave != "":
        opgaver.append(opgave)
        opdater_lb_opgaver()
        txt_input.delete(0, "end")
    else:
        lbl_display["text"] = "Angiv venligst en opgave!"


def slet_alt():
    global opgaver
    opgaver = []
    opdater_lb_opgaver()


def slet():
    opgaven = lb_opgaver.get("active")
    if opgaven in opgaver:
        opgaver.remove(opgaven)
        opdater_lb_opgaver()
        lbl_display["text"] = f"{opgaven} er slettet!"
    else:
        lbl_display["text"] = "Markér venligst en opgave!"


def sort_stigende():
    opgaver.sort()
    opdater_lb_opgaver()


def sort_aftagende():
    opgaver.sort(reverse=True)
    opdater_lb_opgaver()


def tilfaeldig():
    lbl_display["text"] = random.choice(opgaver)


def antal():
    cnt = len(opgaver)
    lbl_display["text"] = f"Antal opgaver: {cnt}"


# Overskrift
lbl_title = tkinter.Label(root, text="To-do-liste", bg="white")
lbl_title.pack()

# Display linie
lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.pack()

# Input felt
txt_input = tkinter.Entry(root, width=15)
txt_input.pack()

# Knapper
btn_tilfoej_opgave = tkinter.Button(root, text="Tilføj opgave", fg="green", bg="white",
                                    command=tilfoej_opgave)
btn_tilfoej_opgave.pack()

btn_slet_alt = tkinter.Button(root, text="Slet alt", fg="orange", bg="white",
                                    command=slet_alt)
btn_slet_alt.pack()

btn_slet = tkinter.Button(root, text="Slet", fg="red", bg="white",
                                    command=slet)
btn_slet.pack()

btn_sort_stigende = tkinter.Button(root, text="Sorter stigende", fg="grey", bg="white",
                                   command=sort_stigende)
btn_sort_stigende.pack()

btn_sort_aftagende = tkinter.Button(root, text="Sorter aftagende", fg="grey", bg="white",
                                    command=sort_aftagende)
btn_sort_aftagende.pack()

btn_tilfaeldig = tkinter.Button(root, text="Vælg tilfældig", fg="grey", bg="white",
                                command=tilfaeldig)
btn_tilfaeldig.pack()

btn_antal_opgaver = tkinter.Button(root, text="Antal opgaver", fg="grey", bg="white",
                      command=antal)
btn_antal_opgaver.pack()

btn_afslut = tkinter.Button(root, text="Afslut", fg="white", bg="red",
                      command=root.destroy)
btn_afslut.pack()

# Listbox
lb_opgaver = tkinter.Listbox(root)
lb_opgaver.pack()

# Opdater indhold i listeboks lb_opgaver
opdater_lb_opgaver()

root.mainloop()
