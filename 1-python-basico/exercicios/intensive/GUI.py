from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.geometry("500x300")
janela.title("APP DE TESTES")
janela.eval('tk::PlaceWindow . center')
# janela.configure(background="#23F4C6")

usuario_bd = 'ian'
senha_bd = 'aaaa'

def prog():
    janela.destroy()
    novaJanela = Tk()
    novaJanela.geometry("1080x720")
    novaJanela.title("TELA INICIAL")
    novaJanela.eval('tk::PlaceWindow . center')

    Label(
        novaJanela,
        text="EM DESENVOLVIMENTO - AGUARDE",
        font=(
            'Helvetica', 28, "italic"
        ),
        foreground= "white",
        background="red",
        anchor=CENTER,
    ).place(
        x=0,
        y=0,
        width=1080,
        height=50
    )


    novaJanela.mainloop()

def user_verify():

    if usuario_bd == usuario.get() and senha_bd == senha.get():
        messagebox.showinfo('Sucesso', 'Bem-vindo(a), Você realizou seu login com sucesso! ;)')
        prog()
    else:
        messagebox.askretrycancel('Erro','Você digitou sua senha ou usuário incorretamente :(')


# messagebox.showinfo('information', 'Hi! You got a prompt.')
# messagebox.showerror('error', 'Something went wrong!')
# messagebox.showwarning('warning', 'accept T&C')
# messagebox.askquestion('Ask Question', 'Do you want to continue?')
# messagebox.askokcancel('Ok Cancel', 'Are You sure?')
# messagebox.askyesno('Yes|No', 'Do you want to proceed?')
# messagebox.askretrycancel('retry', 'Failed! want to try again?')


# CAMPO USUARIO
Label(
    janela,
    text="Usuário",
    anchor=W,
    font=(
        'Helvetica', 14, 'bold'
    ),
    # background="black",
    # foreground="white"
).place(
    x=150,
    y=15,
    width=200,
    height=50)

usuario = Entry(
    janela,
    font=(
        'Helvetica', 20, 'normal'
    )
)
usuario.place(
    x=150,
    y=55,
    width=200,
    height=40
)

# CAMPO SENHA

Label(
    janela,
    text="Senha",
    anchor=W,
    font=(
        'Helvetica', 14, 'bold'
    ),
    # background="black",
    # foreground="white"
).place(
    x=150,
    y=100,
    width=200,
    height=50)

senha = Entry(
    janela,
    font=(
        'Helvetica', 20, 'normal'
    ),
    show='*'
)
senha.place(
    x=150,
    y=140,
    width=200,
    height=40
)

# BOTÃO de login

Button(
    janela,
    text="Fazer Login",
    font=(
        'Helvetica', 14, 'bold'
    ),
    cursor="hand2",
    command=user_verify
).place(
    x=150,
    y=200,
    width=200,
    height=50
)

janela.mainloop()
