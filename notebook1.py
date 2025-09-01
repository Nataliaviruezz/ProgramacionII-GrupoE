#Importacion de librerias
import tkinter as tk 
from tkinter import ttk,messagebox

#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("700x900")

#Crear contenedor Notebook(pestañas)
pestañas=ttk.Notebook(ventana_principal)

#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)

#Agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")

#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")

#Crear frames (doctores)
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
 #
#titulo
titulo =tk.Label(frame_doctores,text="Registro de Doctores", font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0,padx=10, pady=10)
 

#nombre frame doctores
labelNombre=tk.Label(frame_doctores,text="Nombre:")
labelNombre.grid(row=1,column=0,sticky="w",pady=5,padx=5)
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=1,column=1,sticky="w",pady=5,padx=5)

#especialidades frame doctores
labelEspecialidades=tk.Label(frame_doctores,text="Especialidades:")
labelEspecialidades.grid(row=2,column=0,sticky="w",pady=5,padx=5)
Especialidades=tk.StringVar()
Especialidades.set("Neurologia")
Especialidades=ttk.Combobox(frame_doctores,values=["Neurologia","Cardiologia","Pediatria","Traumatologia"],textvariable=Especialidades)
Especialidades.grid(row=2,column=1,sticky="w",pady=5,padx=5)
#edad frame doctores
edadLabel=tk.Label(frame_doctores,text="Edad:")
edadLabel.grid(row=3,column=0,sticky="w",padx=5,pady=5)
spin=tk.Spinbox(frame_doctores,from_=1,to=99)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")
#telefono
labelTelefono=tk.Label(frame_doctores,text="Telefono:")
labelTelefono.grid(row=4,column=0,sticky="w",pady=5,padx=5)
telefono=tk.Entry(frame_doctores)
telefono.grid(row=4,column=1,sticky="w",pady=5,padx=5)
#Frame para los botones
btn_frame = tk.Frame(frame_doctores)
btn_frame.grid(row=5, column=0, columnspan=2, pady=5, sticky="w")

# Botón Registrar
btn_registrar = tk.Button(btn_frame,
text="Registrar", command="",bg="Green")
btn_registrar.grid(row=5, column=6, padx=5)

# Botón Eliminar
btn_eliminar = tk.Button(btn_frame,
text="Eliminar", command="",bg="Red")
btn_eliminar.grid(row=5, column=7, padx=5)
# Crear TreeView para mostrar pacientes
treeview = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")

# Definir encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Telefono")

#Definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("Especialidad", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Telefono", width=60, anchor="center")

#Ubicar el treeView en la cuadricula
treeview.grid(row=8,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=8,column=2,sticky="ns")

 

#nombres
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo:")
labelNombre.grid(row=0,column=0,sticky="w",pady=5,padx=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,sticky="w",pady=5,padx=5)

#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de nacimiento:")
labelFechaN.grid(row=0,column=0,sticky="w",pady=5,padx=5)
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,sticky="w",pady=5,padx=5)

#Edad
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,sticky="w",pady=5,padx=5)
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,sticky="w",pady=5,padx=5)

#GENERO
labelGenero=tk.Label(frame_pacientes,text="Genero:")
labelGenero.grid(row=3,column=0,sticky="w",pady=5,padx=5)
genero=tk.StringVar()
genero.set("Masculino")#valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,sticky="w",padx=5)

#Grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",pady=5,padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,sticky="w",pady=5,padx=5)

#Tipo seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5,column=0,sticky="w",pady=5,padx=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Publico","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5,column=1,sticky="w",pady=5,padx=5)

#centro medico
labelCentoMedico=tk.Label(frame_pacientes,text="Centro de Salud:")
labelCentoMedico.grid(row=6,column=0,sticky="w",pady=5,padx=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Centro Norte","Centro Sur"],textvariable=centro_medico)
comboCentroMedico.grid(row=6,column=1,sticky="w",pady=5,padx=5)

#Frame para los botones
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")

# Botón Registrar
btn_registrar = tk.Button(btn_frame,
text="Registrar", command="")
btn_registrar.grid(row=0, column=0, padx=5)

# Botón Eliminar
btn_eliminar = tk.Button(btn_frame,
text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)

# Crear TreeView para mostrar pacientes
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Genero", "GrupoS", "TipoS", "CentroM"), show="headings")

# Definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Médico")

#Definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)

#Ubicar el treeView en la cuadricula
treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7,column=2,sticky="ns")
ventana_principal.mainloop()

 