from tkinter import *

color_botones = '#ACE38A'

def f_boton_c():
    display1.delete(0, 'end')
    display2.delete(0, 'end')

def mostrar_boton(boton):
    display2.insert(END, boton)

def mostrar_igual():
    operacion = display2.get()
    resultado = str(eval(operacion))
    display1.delete(0, 'end')
    display2.delete(0, 'end')
    display1.insert(0, resultado)

def borrar_display():
    valores = display2.get()
    valor_nuevo = valores[:-1]
    display2.delete(0, 'end')
    display2.insert(-1, valor_nuevo)

master = Tk()
master.config(bg='#9EFD9A')

marco = Frame(master, relief="groove", borderwidth=5)
marco.grid(row=0, column=0, columnspan=4, rowspan=2)

display1 = Entry(marco, width=30,justify=RIGHT, relief="flat", state='normal')
display1.grid(row=0, column=0, columnspan=4)

display2 = Entry(marco, width=30,justify=RIGHT, relief="flat", state='normal')
display2.grid(row=1, column=0, columnspan=4)

#------------------------------------------- Fila 1
boton_c = Button(master, text='C', bg=f'{color_botones}', fg='Red', font='bold', command= f_boton_c)
boton_c.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=5, pady=3)

boton_borrar = Button(master, text='←', bg=f'{color_botones}', command=borrar_display)
boton_borrar.grid(row=2, column=2, sticky=NSEW, padx=5, pady=3)

boton_dividir = Button(master, text='%', bg=f'{color_botones}', command=lambda:[mostrar_boton('/')])
boton_dividir.grid(row=2, column=3, sticky=NSEW, padx=5, pady=3)

#------------------------------------------- Fila 2
boton_siete = Button(master, text='7', bg=f'{color_botones}', command=lambda:[mostrar_boton('7')])
boton_siete.grid(row=3, column=0, sticky=NSEW, padx=5, pady=3)

boton_ocho = Button(master, text='8', bg=f'{color_botones}', command=lambda:[mostrar_boton('8')])
boton_ocho.grid(row=3, column=1, sticky=NSEW, padx=5, pady=3)

boton_nueve = Button(master, text='9', bg=f'{color_botones}', command=lambda:[mostrar_boton('9')])
boton_nueve.grid(row=3, column=2, sticky=NSEW, padx=5, pady=3)

boton_multiplicar = Button(master, text='X', bg=f'{color_botones}', command=lambda:[mostrar_boton('*')])
boton_multiplicar.grid(row=3, column=3, sticky=NSEW, padx=5, pady=3)

#------------------------------------------- Fila 3
boton_cuatro = Button(master, text='4', bg=f'{color_botones}', command=lambda:[mostrar_boton('4')])
boton_cuatro.grid(row=4, column=0, sticky=NSEW, padx=5, pady=3)

boton_cinco = Button(master, text='5', bg=f'{color_botones}', command=lambda:[mostrar_boton('5')])
boton_cinco.grid(row=4, column=1, sticky=NSEW, padx=5, pady=3)

boton_seis = Button(master, text='6', bg=f'{color_botones}', command=lambda:[mostrar_boton('6')])
boton_seis.grid(row=4, column=2, sticky=NSEW, padx=5, pady=3)

boton_restar = Button(master, text='-', bg=f'{color_botones}', command=lambda:[mostrar_boton('-')])
boton_restar.grid(row=4, column=3, sticky=NSEW, padx=5, pady=3)
#------------------------------------------- Fila 4
boton_uno = Button(master, text='1', bg=f'{color_botones}', command=lambda:[mostrar_boton('1')])
boton_uno.grid(row=5, column=0, sticky=NSEW, padx=5, pady=3)

boton_dos = Button(master, text='2', bg=f'{color_botones}', command=lambda:[mostrar_boton('2')])
boton_dos.grid(row=5, column=1, sticky=NSEW, padx=5, pady=3)

boton_tres = Button(master, text='3', bg=f'{color_botones}', command=lambda:[mostrar_boton('3')])
boton_tres.grid(row=5, column=2, sticky=NSEW, padx=5, pady=3)

boton_sumar = Button(master, text='+', bg=f'{color_botones}', command=lambda:[mostrar_boton('+')])
boton_sumar.grid(row=5, column=3, sticky=NSEW, padx=5, pady=3)
#------------------------------------------- Fila 5
boton_cero = Button(master, text='0', bg=f'{color_botones}', command=lambda:[mostrar_boton('0')])
boton_cero.grid(row=6, column=0, columnspan=2, sticky=NSEW, padx=5, pady=3)

boton_punto = Button(master, text='.', bg=f'{color_botones}', command=lambda:[mostrar_boton('.')])
boton_punto.grid(row=6, column=2, sticky=NSEW, padx=5, pady=3)

boton_igual = Button(master, text='=', bg=f'{color_botones}', command=mostrar_igual)
boton_igual.grid(row=6, column=3, sticky=NSEW, padx=5, pady=3)

master.mainloop()