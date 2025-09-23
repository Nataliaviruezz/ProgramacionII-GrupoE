# =====================================
# Registro de Doctores con Tkinter
# =====================================

import tkinter as tk 
from tkinter import ttk, messagebox
from datetime import datetime

# =====================================
# Funciones para manejo de archivo
# =====================================

def guardar_en_archivo():
    with open("registro_doctores.txt","w",encoding="utf-8") as archivo:
        for doctor in lista_doctores:
            archivo.write(
                f"{doctor['Nombre']}|"
                f"{doctor['Especialidad']}|"
                f"{doctor['Experiencia']}|"
                f"{doctor['Género']}|"
                f"{doctor['Hospital']}\n"
            )

def cargar_desde_archivo():
    try:
        with open("registro_doctores.txt", "r", encoding="utf-8") as archivo:
            lista_doctores.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 5:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Experiencia": datos[2],
                        "Género": datos[3],
                        "Hospital": datos[4]
                    }
                    lista_doctores.append(doctor)
        actualizar_tabla()
    except FileNotFoundError:
        open("registro_doctores.txt", "w", encoding="utf-8").close()


# =====================================
# Funciones principales
# =====================================

lista_doctores = []

def registrar_doctor():
    nuevo_doctor = {  
        "Nombre": entrada_nombre.get(),
        "Especialidad": seleccion_especialidad.get(),
        "Experiencia": entrada_experiencia.get(),
        "Género": seleccion_genero.get(),
        "Hospital": seleccion_hospital.get()
    }
    lista_doctores.append(nuevo_doctor)
    guardar_en_archivo()
    actualizar_tabla()

def actualizar_tabla():
    for fila in tabla_doctores.get_children():
        tabla_doctores.delete(fila)

    for i, doctor in enumerate(lista_doctores):
        tabla_doctores.insert(
            "", "end", iid=str(i),
            values=(
                doctor["Nombre"],
                doctor["Especialidad"],
                doctor["Experiencia"],
                doctor["Género"],
                doctor["Hospital"]
            )
        )


# =====================================
# Interfaz Gráfica
# =====================================

ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("600x600")
ventana.configure(bg="LightPink")  # <-- color rosa claro

# Título
titulo = tk.Label(ventana,text="Registro de Doctores", bg="LightPink")
titulo.grid(row=0,column=1,sticky="w",padx=5,pady=5)

# Nombre
tk.Label(ventana,text="Nombre Completo: ", bg="LightPink").grid(row=1,column=0,sticky="w",padx=5,pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=1,column=1,sticky="w",padx=5,pady=5)

# Especialidad
tk.Label(ventana,text="Especialidad: ", bg="LightPink").grid(row=2,column=0,sticky="w",padx=5,pady=5)
seleccion_especialidad = tk.StringVar(value="Pediatría")
combo_especialidad = ttk.Combobox(
    ventana, 
    values=["Pediatría","Neurología","Cardiología","Traumatología"],
    textvariable=seleccion_especialidad
)
combo_especialidad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

# Años de Experiencia
tk.Label(ventana,text="Años de Experiencia: ", bg="LightPink").grid(row=3,column=0,padx=5,pady=5,sticky="w")
entrada_experiencia = tk.Spinbox(ventana, from_=1, to=60)
entrada_experiencia.grid(row=3,column=1,padx=5,pady=5,sticky="w")

# Género
tk.Label(ventana,text="Género: ", bg="LightPink").grid(row=5,column=0,sticky="w",padx=5,pady=5)
seleccion_genero = tk.StringVar(value="Masculino")
ttk.Radiobutton(ventana,text="Masculino",variable=seleccion_genero,value="Masculino").grid(row=5,column=1,sticky="w",padx=5)
ttk.Radiobutton(ventana,text="Femenino",variable=seleccion_genero,value="Femenino").grid(row=6,column=1,sticky="w",padx=5)

# Hospital
tk.Label(ventana,text="Hospital: ", bg="LightPink").grid(row=7,column=0,sticky="w",padx=5,pady=5)
seleccion_hospital = tk.StringVar(value="Hospital Central")
combo_hospital = ttk.Combobox(
    ventana,
    values=["Hospital Central","Hospital Norte","Clínica Santa María","Clínica Vida"],
    textvariable=seleccion_hospital
)
combo_hospital.grid(row=7,column=1,sticky="w",padx=5,pady=5)

# Botón Registrar
frame_botones = tk.Frame(ventana, bg="LightPink")
frame_botones.grid(row=8,column=0,columnspan=2,pady=5,sticky="w")
btn_registrar = tk.Button(frame_botones,text="Registrar",command=registrar_doctor,bg="LightGreen")
btn_registrar.grid(row=8,column=0,padx=5)

# Tabla TreeView
tabla_doctores = ttk.Treeview(
    ventana,
    columns=("Nombre","Especialidad","Experiencia","Género","Hospital"),
    show="headings"
)
tabla_doctores.heading("Nombre",text="Nombre Completo")
tabla_doctores.heading("Especialidad",text="Especialidad")
tabla_doctores.heading("Experiencia",text="Años de Experiencia")
tabla_doctores.heading("Género",text="Género")
tabla_doctores.heading("Hospital",text="Hospital")

tabla_doctores.column("Nombre",width=120)
tabla_doctores.column("Especialidad",width=120)
tabla_doctores.column("Experiencia",width=120,anchor="center")
tabla_doctores.column("Género",width=120)
tabla_doctores.column("Hospital",width=120)

tabla_doctores.grid(row=9,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

cargar_desde_archivo()
actualizar_tabla()

ventana.mainloop()
