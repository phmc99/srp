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

#===========IMAGENS===========#
logo = PhotoImage(file="./images/logo.png")
bg = PhotoImage(file="./images/bg.png")

#===========FRAMES===========#
frame = Frame(janela, width="800", height="600", bg="gray", relief="raise")
frame.pack(side="top")

bgLabel = Label(frame, image=bg, bg="gray") 
bgLabel.place(x="0", y="0")

#==============WIDGETS DA PAGINA=================#
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
    
    def voltar():
        emailEntry.place(x="5000")
        reg_to_bd_Btn.place(x="5000")
        loginBtn.place(x="300")
        regBtn.place(x="300")
        voltarBtn.place(x="5000")
        userEntry.delete(0, END)
        passEntry.delete(0, END)

#===========BOTOES DA PAGINA DE REGISTRO DO USER===========#
    reg_to_bd_Btn = Button(frame, text="Registrar", width="20", command=registrarBd)
    reg_to_bd_Btn.place(x="300", y="335")

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

#============WIDGETS DE REGISTRO DOS PETS=================#
    nomePetEntry = ttk.Entry(frame, width="30")
    nomePetEntry.insert(0,"Nome do Pet.")
    nomePetEntry.configure(state=DISABLED)
    nomePetEntry.place(x="285", y="240")

    tipoPetEntry = ttk.Entry(frame, width="30")
    tipoPetEntry.insert(0,"Tipo do pet. (Canino, felino, ...)")
    tipoPetEntry.configure(state=DISABLED)
    tipoPetEntry.place(x="285", y="265")

    racaPetEntry = ttk.Entry(frame, width="30")
    racaPetEntry.insert(0,"Raça do Pet ou nome popular.")
    racaPetEntry.configure(state=DISABLED)
    racaPetEntry.place(x="285", y="290")

    sexoPetEntry = ttk.Entry(frame, width="30")
    sexoPetEntry.insert(0,"Sexo do pet.")
    sexoPetEntry.configure(state=DISABLED)
    sexoPetEntry.place(x="285", y="315")

    donoPetEntry = ttk.Entry(frame, width="30")
    donoPetEntry.insert(0,"Nome do dono.")
    donoPetEntry.configure(state=DISABLED)
    donoPetEntry.place(x="285", y="340")

    teldonoPetEntry = ttk.Entry(frame, width="30")
    teldonoPetEntry.insert(0,"Telefone de contato do dono. (Apenas números)")
    teldonoPetEntry.configure(state=DISABLED)
    teldonoPetEntry.place(x="285", y="365")

    def nomepetclick(event):
        nomePetEntry.configure(state=NORMAL)
        nomePetEntry.delete(0, END)
        nomePetEntry.unbind('<Button-1>', nomepet_click_id)

    def tipopetclick(event):
        tipoPetEntry.configure(state=NORMAL)
        tipoPetEntry.delete(0, END)
        tipoPetEntry.unbind('<Button-1>', tipopet_click_id)

    def racapetclick(event):
        racaPetEntry.configure(state=NORMAL)
        racaPetEntry.delete(0, END)
        racaPetEntry.unbind('<Button-1>', racapet_click_id)

    def sexopetclick(event):
        sexoPetEntry.configure(state=NORMAL)
        sexoPetEntry.delete(0, END)
        sexoPetEntry.unbind('<Button-1>', sexopet_click_id)

    def donopetclick(event):
        donoPetEntry.configure(state=NORMAL)
        donoPetEntry.delete(0, END)
        donoPetEntry.unbind('<Button-1>', donopet_click_id)

    def teldonoclick(event):
        teldonoPetEntry.configure(state=NORMAL)
        teldonoPetEntry.delete(0, END)
        teldonoPetEntry.unbind('<Button-1>', teldono_click_id)
        
    nomepet_click_id = nomePetEntry.bind('<Button-1>', nomepetclick)
    tipopet_click_id = tipoPetEntry.bind('<Button-1>', tipopetclick)
    racapet_click_id = racaPetEntry.bind('<Button-1>', racapetclick)
    sexopet_click_id = sexoPetEntry.bind('<Button-1>', sexopetclick)
    donopet_click_id = donoPetEntry.bind('<Button-1>', donopetclick)
    teldono_click_id = teldonoPetEntry.bind('<Button-1>', teldonoclick)

#==================REGISTRAR O PET=====================#
    def registrarPet():
        nome = nomePetEntry.get()
        tipo = tipoPetEntry.get()
        raca = racaPetEntry.get()
        sexo = sexoPetEntry.get()
        dono = donoPetEntry.get()
        tel = teldonoPetEntry.get()
        
        if (nome == "" or tipo == "" or raca == "" or sexo == "" or dono == "" or tel == ""):
            messagebox.showerror(title="SRP - Errror", message="Preencha todos os campos.")
        else:
            petsBd.cursor.execute("""
            INSERT INTO Pets (Nome, Tipo, Raca, Sexo, Dono, TelDono) VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, tipo, raca, sexo, dono, tel))
            petsBd.conn.commit()
            messagebox.showinfo(title="SRP - Info", message="Pet cadastrado com sucesso.")

    regPetBtn = Button(frame, text="Registrar Pet", width="20", command=registrarPet)
    regPetBtn.place(x="300", y="400")

    def limparPet():
        nomePetEntry.delete(0, END)
        tipoPetEntry.delete(0, END)
        racaPetEntry.delete(0, END)
        sexoPetEntry.delete(0, END)
        donoPetEntry.delete(0, END)
        teldonoPetEntry.delete(0, END)

    limparPetBtn = Button(frame, text="Limpar", width="20", command=limparPet)
    limparPetBtn.place(x="300", y="430")
    
    

#===========BOTOES INICIO===============#
regBtn = Button(frame, text="Registrar Usuário", width="20", command=registrarUser)
regBtn.place(x="300", y="365")

loginBtn = Button(frame, text="Entrar", width="20", command=loginVerificar)
loginBtn.place(x="300", y="335")


janela.mainloop()


