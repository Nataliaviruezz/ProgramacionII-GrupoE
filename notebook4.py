#importacion de librerías
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
#"crear ventana principal"
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Libro pacientes y doctores")
ventanaPrincipal.geometry("900x900")

#crear contenedores notebook(pestañas)
pestañas=ttk.Notebook(ventanaPrincipal)
#crear frames(uno por pestañas)
frame_pacientes=ttk.Frame(pestañas)
#agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")

#mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")

#Fnción para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    if len (limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len (limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio      
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year- fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#funcion guardar en archivo
def guardar_en_archivo():
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(
                f"{paciente['Nombre']}|"
                f"{paciente['Fecha de nacimiento']}|"
                f"{paciente['Edad']}|"
                f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|"
                f"{paciente['Tipo de seguro']}|{paciente['Centro médico']}\n"
            )
#funcion cargar desde archivo paciente
def cargar_desde_archivo_pacientes():
   try:
       with open("paciente.txt", "r", encoding="utf-8") as archivo:
           paciente_data.clear()
           for linea in archivo:
               datos = linea.strip().split("|")
               if len(datos) == 7:
                   paciente = {
                       "Nombre": datos[0],
                       "Fecha de Nacimiento": datos[1],
                       "Edad": datos[2],
                       "Género": datos[3],
                       "Grupo Sanguíneo": datos[4],
                       "Tipo de Seguro": datos[5],
                       "Centro Médico": datos[6]
                   }
                   paciente_data.append(paciente)
       cargar_treeview()
   except FileNotFoundError:
       open("paciente.txt","w",encoding="utf-8").close()
#def eliminar pacinte
def eliminar_paciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", f"¿Está seguro de eliminar el paciente'{treeview.item(id_item,'values')[0]}'?"):
           del paciente_data[indice]
           guardar_en_archivo()  # Guardar los cambios en el archivo
           cargar_treeview()
           messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente.")
    else:  # este else es del if seleccionado
       messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
    return
     
#Lista de pacientes (inicialmente vacía)
paciente_data=[]
#función pra registrar paciente
def registrarPaciente():
    #crear un diccionario con los datos ingresados
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Grupo Sanguineo":entryGrupoSanguineo.get(),
        "Tipo de seguro":tipo_seguro.get(),
        "Centro médico":centro_medico.get()
        
    }
    #agregar a la lista
    paciente_data.append(paciente)
    #linea modificada
    guardar_en_archivo()
    #Cargar el treeview
    cargar_treeview()
    
   
def cargar_treeview(): 
    #limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de seguro"],
                item["Centro médico"]
            )
        )
#nombre
labelNombreP=tk.Label(frame_pacientes,text="Nombre")
labelNombreP.grid(row=0,column=0,sticky="w",padx=5,pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")


#fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de nacimiento:")
labelFechaN.grid(row=1,column=0,sticky="w",padx=5,pady=5)
#llamando ala funcion de enmascarar fecha
validacion_fecha=ventanaPrincipal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w") 


#edad(readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadVar=tk.StringVar()
edad=tk.Entry(frame_pacientes,state="readonly",textvariable=edadVar)
edad.grid(row=2,column=1,sticky="w",padx=5,pady=5)

#genero(radio button)
labelGenero=tk.Label(frame_pacientes,text="Genero")
labelGenero.grid(row=3,column=0,sticky="w",padx=5,pady=5)
genero=tk.StringVar()
genero.set("Maculino")#valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Mascuino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,sticky="w",padx=5,pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes,text="femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,pady=5,sticky="w")

#Grupo Sanguíneo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo sanguíneo")
labelGrupoSanguineo.grid(row=5,column=0,sticky="w",padx=5,pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,sticky="w",padx=5,pady=5)

#tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de seguro")
labelTipoSeguro.grid(row=6,column=0,sticky="w",padx=5,pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público")#valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Público","Privado","Ninguno"],textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6,column=1,sticky="w",padx=5,pady=5)

#centro medico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud")
labelCentroMedico.grid(row=7,column=0,sticky="w",padx=5,pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital central")#valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital central","Centro Sur","Clínica Norte"],textvariable=centro_medico)
comboCentroMedico.grid(row=7,column=1,sticky="w",padx=5,pady=5)

#frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8,column=0,columnspan=2,padx=5,pady=5,sticky="w")

#botomn registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=8,column=0,padx=5,pady=5)
btn_registrar.configure(bg="#48FF68",fg="white")

#boton eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command=eliminar_paciente)
btn_eliminar.grid(row=8,column=1,padx=5)
btn_eliminar.configure(bg="#FF0014",fg="white")

#CREAR TREEVIEW PARA MOSTRAR PACIENTES
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM"),show="headings")
#DEFINIR ENCABEZADOS
treeview.heading("Nombre",text="Nombre completo")
treeview.heading("FechaN",text="Fecha de nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Genero")
treeview.heading("GrupoS",text="Grupo Sanguíneo")
treeview.heading("TipoS",text="Tipo seguro")
treeview.heading("CentroM",text="Centro Médico")

#definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=60,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120)

#ubicar treeview en cuadrícula
treeview.grid(row=9,column=0,columnspan=2,pady=10,sticky="nsew")
#scrobal vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
scroll_y.grid(row=9,column=2,sticky="ns")
#LISTA DE DOCTORES(INICIALMENTE VACIA)
doctor_data=[]
#FUNCION PARA REGISTRAR PACIENTE
def registrarDoctor():
#crear un diccionario con los datos ingresados
    doctor = {
        "Nombre": nombreD.get(),
        "Especialidad": especialidad.get(),
        "Edad": spinEdadD.get(),
        "Telefono": telefonoD.get(),
        }
    #AGREGAR PACIENTE A LA LISTA
    doctor_data.append(doctor)
    #CARGAR AL TREEVIEW
    cargar_treeview()
def cargar_treeview():
    #Limpiear el treeview
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    #Insertar cada paciente 
    for i, item in enumerate(doctor_data):
        treeviewD.insert(
            "", "end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Telefono"]
            )
        )
    
#------------DOCTORES-------------------
#CREAR FRAMES(UNO POR PESTAÑAS)
frame_doctores=ttk.Frame(pestañas)
#aGREGAR PESTAÑAS AL NOTEBOOK
pestañas.add(frame_doctores, text="Doctores")
#MOSTRAR LAS PESTAÑAS EN LA VENTANA
pestañas.pack(expand=True, fill="both")

#------------DOCTORES-------------------
#-----------WIDGETS------------
#TITULO
labelTitulo=tk.Label(frame_doctores, text="Registro de Doctores")
labelTitulo.grid(row=0, column=0, sticky="w", pady=10, padx=120)
#Nombre
labelNombreD=tk.Label(frame_doctores, text="Nombre Completo:")
labelNombreD.grid(row=1, column=0, sticky="w", pady=10, padx=5)
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=1, column=1, sticky="w", pady=10, padx=5)
#ESPECIALIDAD
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad:")
labelEspecialidad.grid(row=2, column=0, sticky="w", padx=5, pady=10)
especialidad=tk.StringVar()
especialidad.set("Neurologia")
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia","Cardiologia","Pediatria", "Traumatologia"], textvariable=especialidad)
comboEspecialidad.grid(row=2, column=1, sticky="w", padx=5, pady=10)
#EDAD 
labelEdadD=tk.Label(frame_doctores, text="Edad:")
labelEdadD.grid(row=3, column=0, padx=5, pady=10, sticky="w")
spinEdadD=ttk.Spinbox(frame_doctores, from_=0, to=99)
spinEdadD.grid(row=3, column=1, padx=5, pady=10, sticky="w")
#TELEFONO
labelTelefono=tk.Label(frame_doctores, text="Telefono:")
labelTelefono.grid(row=4, column=0, sticky="w", pady=10, padx=5)
telefonoD=tk.Entry(frame_doctores)
telefonoD.grid(row=4, column=1, sticky="w", pady=10, padx=5)
#FRAME PARA LOS BOTONES
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")
#BOTON REGISTRAR
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarDoctor, bg="green", fg="white")
btn_registrar.grid(row=5, column=0, padx=5)
#BOTON ELIMINAR
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="", bg="red", fg="white")
btn_eliminar.grid(row=5, column=1, padx=5)
#CREAR TREEVIEW PARA MOSTRAR DOCTORES
treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeviewD.heading("Nombre", text="Nombre Completo")
treeviewD.heading("Especialidad", text="Especialidad")
treeviewD.heading("Edad", text="Edad")
treeviewD.heading("Telefono", text="Telefono")
#DEFINIR ANCHOS DE COLUMNAS
treeviewD.column("Nombre", width=120) 
treeviewD.column("Especialidad", width=120) 
treeviewD.column("Edad", width=50, anchor="center") 
treeviewD.column("Telefono", width=60, anchor="center") 
treeviewD.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
#SCROLBAR VERTICAL
scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeviewD.yview)
scroll_y.grid(row=6, column=2, sticky="nsew")


cargar_desde_archivo_pacientes()#cargar datos desde el archivo al iniciar la aplicacion
ventanaPrincipal.mainloop()