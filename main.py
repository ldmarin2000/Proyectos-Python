from tkinter import *
from tkinter import ttk as ttk

# Ventana Princiapl
root = Tk()
root.title("Login Usuario")

# mainFrame
mainFrame = Frame(root)
mainFrame.pack()
mainFrame.config(width=480,height=320) #, bg="lightblue")

# Textos y Titulos
titulo=Label(mainFrame,text="Login de Usuario",font=("Arial",24))
titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

nombreLabel = Label(mainFrame,text="Usuario: ")
nombreLabel.grid(column=0,row=1)
passLabel= Label(mainFrame,text="Contraseña :")
passLabel.grid(column=0,row=2)

# Ebtradas de texto
nombreUsuario = StringVar()
nombreUsuario.set("Admin")
nombreEntry = Entry(mainFrame,textvariable=nombreUsuario)
nombreEntry.grid(column=1,row=1)

contraseñaUsuario = StringVar()
contraseñaUsuario.set("1234")
contraseñaEntry = Entry(mainFrame,textvariable=nombreUsuario,show="*")
contraseñaEntry.grid(column=1,row=2)

# Botones

iniciarSessionButton= ttk.Button(mainFrame,text="Inciar Sesion",)
iniciarSessionButton.grid(column=1,row=3,ipadx=5,ipady=5,padx=10,pady=10)

registrarButton= ttk.Button(mainFrame,text="Registrar Usuario")
registrarButton.grid(column=0,row=3,ipadx=5,ipady=5,padx=10,pady=10)



root.mainloop()