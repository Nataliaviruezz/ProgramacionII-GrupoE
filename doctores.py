import tkinter as tk
from tkinter import ttk

# Función para registrar doctores
def registrar_doctor():
    nombre = entry_nombre.get()
    especialidad = combo_especialidad.get()
    experiencia = spin_experiencia.get()
    genero = genero_var.get()
    hospital = entry_hospital.get()
    if nombre and especialidad and hospital:

        # Insertar en la tabla
        tree.insert("", "end", values=(nombre, especialidad, experiencia, genero, hospital))

        # Limpiar campos
        entry_nombre.delete(0, tk.END)
        combo_especialidad.set("")
        spin_experiencia.delete(0, tk.END)
        spin_experiencia.insert(0, 0)
        genero_var.set("Masculino")
        entry_hospital.delete(0, tk.END)

# Ventana Principal
ventana_principal = tk.Tk()  
ventana_principal.title("Registro de Doctores")  
ventana_principal.geometry("700x400")  

# formulario de Registro
lbl_titulo = ttk.Label(ventana_principal, text="Registro de Doctores", font=("Arial", 12, "bold"))
lbl_titulo.pack(pady=10)
frame_form = ttk.Frame(ventana_principal)
frame_form.pack(pady=5)

# Nombre
ttk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_nombre = ttk.Entry(frame_form, width=25)
entry_nombre.grid(row=0, column=1)

# Especialidad
ttk.Label(frame_form, text="Especialidad:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
combo_especialidad = ttk.Combobox(frame_form, values=["Cardiología", "Pediatría", "Traumatología", "Neurología"], width=22)
combo_especialidad.grid(row=1, column=1)

# Años de experiencia
ttk.Label(frame_form, text="Años Experiencia:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
spin_experiencia = tk.Spinbox(frame_form, from_=0, to=50, width=5)
spin_experiencia.grid(row=2, column=1, sticky="w")

# género
ttk.Label(frame_form, text="Género:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
genero_var = tk.StringVar(value="Masculino")
rb_m = ttk.Radiobutton(frame_form, text="Masculino", variable=genero_var, value="Masculino")
rb_f = ttk.Radiobutton(frame_form, text="Femenino", variable=genero_var, value="Femenino")
rb_m.grid(row=3, column=1, sticky="w")
rb_f.grid(row=4, column=1, sticky="w")

#Hospital
ttk.Label(frame_form, text="Hospital:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_hospital = ttk.Entry(frame_form, width=25)
entry_hospital.grid(row=5, column=1)

# Botón registrar
btn_registrar = tk.Button(frame_form, text="Registrar", bg="green", fg="white", command=registrar_doctor)
btn_registrar.grid(row=6, columnspan=2, pady=10)

# Tabla de Doctores
columns = ("Nombre", "Especialidad", "Experiencia", "Género", "Hospital")
tree = ttk.Treeview(ventana_principal, columns=columns, show="headings", height=6)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.pack(fill="x", padx=10, pady=10)

ventana_principal.mainloop()
 
 