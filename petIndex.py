import petsBd
import usersBd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#===========JANELA===========#
janela = Tk()
janela.title("Sistema de Registro de Pets 0.1")
janela.geometry("800x600")
janela.configure(background="black")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="./images/logon.ico")

#===========Importando imagens===========#
logo = PhotoImage(file="./images/logo.png")
bg = PhotoImage(file="./images/bg.png")

#===========FRAMES===========#
frame = Frame(janela, width="800", height="600", bg="gray", relief="raise")
frame.pack(side="top")

bgLabel = Label(frame, image=bg, bg="gray") 
bgLabel.place(x="0", y="0")

#==============WIDGETS=================#
userEntry = ttk.Entry(frame, width="30")
userEntry.insert(0, "Usuário")
userEntry.configure(state=DISABLED)
userEntry.place(x="285", y="270")

passEntry = ttk.Entry(frame, width="30")
passEntry.insert(0, "Senha")
passEntry.configure(state=DISABLED)
passEntry.place(x="285", y="300")

def loginclick(event):
    userEntry.configure(state=NORMAL)
    userEntry.delete(0, END)
    userEntry.unbind('<Button-1>', login_click_id)
    janela.attributes("-alpha", 1)
    
def passclick(event):
    passEntry.configure(state=NORMAL, show="•")
    passEntry.delete(0, END)
    passEntry.unbind('<Button-1>', pass_click_id)
    janela.attributes("-alpha", 1)
    
login_click_id = userEntry.bind('<Button-1>', loginclick)
pass_click_id = passEntry.bind('<Button-1>', passclick)

#============REGISTRAR USUARIO==================#

def registrarUser():
    regBtn.place(x="5000")
    loginBtn.place(x="5000")

    emailEntry = ttk.Entry(frame, width="30")
    emailEntry.insert(0,"E-mail")
    emailEntry.configure(state=DISABLED)
    emailEntry.place(x="285", y="240")
    def emailclick(event):
        emailEntry.configure(state=NORMAL)
        emailEntry.delete(0, END)
        emailEntry.unbind('<Button-1>', email_click_id)
        janela.attributes("-alpha", 1)

    email_click_id = emailEntry.bind('<Button-1>', emailclick)

    def registrarBd():
        email = emailEntry.get()
        user = userEntry.get()
        senha = passEntry.get()

        if (email == "" or user == "" or senha == ""):
            messagebox.showerror(title="SRP - Error", message="Preencha todos os campos.")
        else:
            usersBd.cursor.execute("""
                INSERT INTO Users(Email, User, Senha) VALUES(?, ?, ?)
            """, (email, user, senha))
            usersBd.conn.commit()
            messagebox.showinfo(title="SRP - Info", message="Usuário registrado com sucesso!")
    
    reg_to_bd_Btn = Button(frame, text="Registrar", width="20", command=registrarBd)
    reg_to_bd_Btn.place(x="300", y="335")

    def voltar():
        emailEntry.place(x="5000")
        reg_to_bd_Btn.place(x="5000")
        loginBtn.place(x="300")
        regBtn.place(x="300")
        voltarBtn.place(x="5000")
        userEntry.delete(0, END)
        passEntry.delete(0, END)

    voltarBtn = Button(frame, text="Voltar", width="20", command=voltar)
    voltarBtn.place(x="300", y="365")
    
#===========LOGAR==============#
def loginVerificar():
    userLogin = userEntry.get()
    passLogin = passEntry.get()
    usersBd.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? AND Senha = ?
    """, (userLogin, passLogin))
    verificar = usersBd.cursor.fetchone()
    try:
        if(userLogin in verificar and passLogin in verificar):
            messagebox.showinfo(title="SRP - Info", message="Bem-vindo ao Sistema de Registro de Pets!")
        else:
            pass
    except:
        messagebox.showerror(title="SRP - Error", message="Senha ou Usuário incorreto, tente novamente.")

    loginBtn.place(x="5000")
    regBtn.place(x="5000")
    userEntry.place(x="5000")
    passEntry.place(x="5000")


#===========BOTOES===============#
regBtn = Button(frame, text="Registrar Usuário", width="20", command=registrarUser)
regBtn.place(x="300", y="365")

loginBtn = Button(frame, text="Entrar", width="20", command=loginVerificar)
loginBtn.place(x="300", y="335")




"""def registrarPet():
    nomeR = nome.get()
    tipoR = tipo.get()
    racaR = raca.get()
    sexoR = sexo.get()
    nomeDR = nomeDono.get()
    telDR = telDono.get()
    
    if nomeR == "" or tipoR == "" or racaR == "" or sexoR == "" or nomeDR == "" or telDR == "":
        print("Preencha todos os campos!!!")
    else:
        petsBd.cursor.execute("""
        #INSERT INTO Pets (nomeR, tipoR, racaR, sexoR, nomeDR, telDR) VALUE (?, ?, ?, ?, ?, ?)
        """, (nomeR, tipoR, racaR, sexoR, nomeDR, telDR))
        petsBd.conn.commit()
    print("CADASTRO CONCLUIDO COM SUCESSO!")"""

janela.mainloop()