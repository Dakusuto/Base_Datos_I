from inspect import EndOfBlock
from sqlite3 import Cursor
from tkinter import*
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox

import mysql.connector
from mysqlx import Result, Row


estudiantes=mysql.connector.connect(host="localhost",user="root",
password="123456",database="newschema")
cursor=estudiantes.cursor()
def Vista(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("", "end", values=i)


def Consulta():
    q2=q.get()
    query="select* from datos_de_estudiante where identificacion Like '%"+q2+"%'or NombresE like' %"+q2+"%'"
    cursor.execute(query)
    rows=cursor.fetchall()
    Vista(rows)

def Restablecer():
    query="select* from datos_de_Estudiante "
    cursor.execute(query)
    rows=cursor.fetchall()
    Vista(rows)

def Agregar():
    if t1.get()=="" or t2.get()=="":
        messagebox.showerror("por favor", " intentelo de nuevo")
    else:
        estudiantes=mysql.connector.connect(host="localhost",user="root",
        password="123456",database="newschema")
        cursor=estudiantes.cursor()
        cursor.execute("insert into datos_de_estudiante values(%s,%s,%s,%s)", (

        t1.get(),
        t2.get(),
        t3.get(),
        t4.get(),
        ))

        estudiantes.commit()
        estudiantes.close()
        messagebox.showinfo("Datos ingresados","se agregaron correctamente")
        Mostrar()



def Mostrar():
    estudiantes=mysql.connector.connect(host="localhost",user="root",
    password="123456",database="newschema")
    cursor=estudiantes.cursor()
    cursor.execute ("select* from datos_de_estudiante") 
    result=cursor.fetchall()
    if len(result) !=0:
        trv.delete(*trv.get_children())
        for row in result:
            trv.insert("",END,values=row)
    estudiantes.commit()
    estudiantes.close()



def Limpiar():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)

root=Tk()

q=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()

root.title("Estudiantes")
root.geometry("850x500")
root.config(bg="red")
root.config(relief="groove")
root.config(cursor="spider")

frame1=LabelFrame(root,text="datos del estudiante ", font=("calibri",14))
frame2=LabelFrame(root,text="consulta ", font=("calibri",14))
frame3=LabelFrame(root,text="datos del estudiante ", font=("calibri",14))

frame1.pack(fill="both",expand="yes",padx=20,pady=15)
frame2.pack(fill="both",expand="yes",padx=20,pady=15)
frame3.pack(fill="both",expand="yes",padx=20,pady=15)

trv=ttk.Treeview(frame3,columns=(1,2,3,4),show="headings",height="10")
trv.pack()


trv.heading(1,text="cedula ")
trv.heading(2,text="nombres y apellidos")
trv.heading(3,text="fecha de nacimiento")
trv.heading(4,text="genero")

query="SELECT* from estudiantes"
cursor.execute(query)
rows=cursor.fetchall()
Vista(rows)


lbl1=Label(frame1,width=10,text="identificacion")
lbl1.grid(column=0,row=0,padx=5,pady=3)
ent1=Entry(frame1,textvariable=t1)
ent1.grid(column=1,row=0,padx=5,pady=3)

lbl2=Label(frame1,width=10,text="nombre")
lbl2.grid(column=0,row=1,padx=5,pady=3)
ent2=Entry(frame1,textvariable=t2)
ent2.grid(column=1,row=1,padx=5,pady=3)

lbl3=Label(frame1,width=10,text="fecha de nacimiento")
lbl3.grid(column=0,row=2,padx=5,pady=3)
ent3=Entry(frame1,textvariable=t3)
ent3.grid(column=1,row=2,padx=5,pady=3)

lbl4=Label(frame1,width=10,text="genero")
lbl4.grid(column=0,row=3,padx=5,pady=3)
ent4=Entry(frame1,textvariable=t4)
ent4.grid(column=1,row=3,padx=5,pady=3)

agregar_btn=Button(frame1,width=10,text="Agregar", command=Agregar)
agregar_btn.grid(column=0,row=4,padx=5,pady=3)


actualizar_btn=Button(frame1,width=10,text="Actualizar")
actualizar_btn.grid(column=1,row=4,padx=5,pady=3)

eliminar_btn=Button(frame1,width=10,text="Eliminar")
eliminar_btn.grid(column=2,row=4,padx=5,pady=3)

limpiar_btn=Button(frame1,width=10,text="limpiar",command=Limpiar)
limpiar_btn.grid(column=3,row=4,padx=5,pady=3)

vista_btn=Button(frame1,width=10,text="Mostrar", command=Mostrar)
vista_btn.grid(column=4,row=4,padx=5,pady=3)


lbl=Label(frame2,width=10,text="consulta")
lbl.pack(side=tk.LEFT,padx=10)
ent=Entry(frame2,textvariable=q)
ent.pack(side=tk.LEFT,padx=6)


bnt=Button(frame2,width=10,text="consulta ",command=Consulta)
bnt.pack(side=tk.LEFT,padx=6)

cbnt=Button(frame2,width=10,text="restablecer ",command=Restablecer)
cbnt.pack(side=tk.LEFT,padx=6)


root.mainloop()