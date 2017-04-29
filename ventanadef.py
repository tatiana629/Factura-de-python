from tkinter import *



ventana=Tk()
ventana.geometry("350x170+200+200")
ventana.title("acceso")
usuario=Label(text="Usuario:",fg="pink",font=("Baskerville Old Face",15)).grid(row=0,column=0,sticky=W)
password=Label(text="Contraseña:", fg="blue",font("Baskerville Old Face",15)).grid(row=1,column=0)
entradauser=StringVar()

entradapass=StringVar()
textoUser=Entry(ventana,textvariable=entradauser,
                width=30).grid(row=0,column=2)
textopassword=Entry(ventana,textvariable=entradapass,
                    show=("*"),width=30).grid(row=1,column=2)
botoningresar=Button(ventana,text="Ingresar",font=("Cooper Black",12),width=10).place(x=20,y=80)
botonsalir=Button(ventana,text="salir",font=("Cooper Black",12),width=10,command=quit).place(x=150,y=80)
ventana.mainloop()


