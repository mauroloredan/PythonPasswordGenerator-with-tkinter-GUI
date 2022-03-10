from tkinter import *
import random

#list to pick up characters for the password
spc = ['@','#','$','%','&','(',')','[',']','.',',','-','_']
numeri = [0,1,2,3,4,5,6,7,8,9]
upperChar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerChar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def passwordGenerator():
    pg = Tk()
    pg.geometry("540x400")
    pg.title("Random Password Generator")
    pg.resizable(0,0)
    spacer1 = Label(pg, text="  ")
    titolo = Label(pg, text="Choose the lenght for the password and click on Generate.")
    spacer2 = Label(pg, text=" ")
    spacer1.grid(row=0, column=0, columnspan=2)
    titolo.grid(row=1, column=0, columnspan=2)
    spacer2.grid(row=2, column=0, columnspan=2)

    #generate the password
    def generaPsw():
        passwordGenerataText = ""
        global generated
        generated = ""
        choice_lst = []
        length = int(lungo.get())

        for i in range(length):			
            special = random.choice(spc)
            number = random.choice(numeri)
            maiuscole = random.choice(upperChar)
            minuscole = random.choice(lowerChar)
            choice_lst.append(special)
            choice_lst.append(number)
            choice_lst.append(maiuscole)
            choice_lst.append(minuscole)
            choice = random.choice(choice_lst)
            generated += str(choice)
		
        passwordGenerata.delete(0, END)
        passwordGenerataText = generated		
        passwordGenerata.insert(END, passwordGenerataText)

    #clear all fields
    def clear():
        lungo.delete(0,END)
        passwordGenerata.delete(0,END)
        name.delete(0, END)

    #save the password
    def save():
        nomePsw = name.get()
        f = open("psw.txt", "a")
        f.write("\n" + nomePsw + " : " + generated)


    #lenght
    lunghezza = Label(pg, text="Lenght:", justify='left')
    lungo = Entry(pg, width=30, justify='center')

    #buttons
    genera = Button(pg, text="Generate", padx=40, pady=5, command=generaPsw)
    cancella = Button(pg, text="Clear", fg="red", padx=40, pady=5, command=clear)
    salva = Button(pg, text="Save", padx=40, pady=5, command=save)

    #show the password
    spacer3 = Label(pg, text=" ")
    global passwordGenerataText
    passwordGenerataText = StringVar()
    global passwordGenerata
    passwordGenerata = Entry(pg, text=" ", width=30, justify="center", bg="lightgreen")

    #save the password
    spacer4 =Label(pg, text=" ")
    nomina = Label(pg, text="Choose a name for the password: ")
    nome = Label(pg, text="Name :", justify='left')
    name = Entry(pg, width=30)
    tip = Label(pg, text="* password will be saved in \'psw.txt\'", fg="red")

    #put things on screen
    lunghezza.grid(row=3, column=0)
    lungo.grid(row=3, column=1)
    genera.grid(row=5, column=0)
    cancella.grid(row=5, column=1)
    spacer3.grid(row=6, column=0, columnspan=2)
    passwordGenerata.grid(row=7, column=0, columnspan=2)  
    spacer4.grid(row=8, column=0, columnspan=2)
    nomina.grid(row=9, column=0, columnspan=2)
    nome.grid(row=10, column=0)
    name.grid(row=10, column=1)
    salva.grid(row=11, column=1)
    tip.grid(row=12, column=0, columnspan=2)

    pg.mainloop()

if __name__ == '__main__':
    	passwordGenerator()
