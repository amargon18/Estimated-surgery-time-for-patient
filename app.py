# CONSTRUCCIÓN APLICACIÓN DE ESCRITORIO
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import json

#-------------------------------------- FUNCIONES ------------------------------------------
ventana_secundaria = None

campos_de_entrada = []
campos = ['main_procedure', 'main_condition', 'secondary_procedure',
       'character_of_intervention', 'health_service', 'asa_score', 'gender',
       'age', 'weight', 'height', 'comorbidity', 'anesthesia_local',
       'anesthesia_sedation', 'anesthesia_plexus_block',
       'anesthesia_intradural', 'anesthesia_epidural', 'anesthesia_general',
       'cleaning_time', 'recovery_time']
def abrir_ventana_secundaria():
    global ventana_secundaria
    ventana_secundaria = tk.Toplevel(app)
    ventana_secundaria.title("Insertar datos")
    marco_formulario = tk.Frame(ventana_secundaria)
    marco_formulario.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    for i in range(19):
        label = tk.Label(marco_formulario, text=f"{campos[i]}:")
        row = i // 10  # Divide en dos columnas (0-7 en la columna 0, 8-14 en la columna 1)
        label.grid(row=i % 10, column=row * 2, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(marco_formulario)
        entry.grid(row=i % 10, column=row * 2 + 1, padx=10, pady=5, sticky=tk.EW)
        campos_de_entrada.append(entry)
    
    # Botón para enviar el formulario
    boton_enviar = tk.Button(ventana_secundaria, text="Enviar", command=lambda: enviar_formulario())
    boton_enviar.pack(pady=10, padx=20)
    ventana_secundaria.update_idletasks()
    ventana_secundaria.geometry("+%d+%d" % ((ventana_secundaria.winfo_screenwidth() - ventana_secundaria.winfo_reqwidth()) / 2,
                                             (ventana_secundaria.winfo_screenheight() - ventana_secundaria.winfo_reqheight()) / 2))


def enviar_formulario():
    global ventana_secundaria
    global campos_de_entrada
    datos = {}

    for i, entrada in enumerate(campos_de_entrada):
        nombre_campo = campos[i]
        valor = entrada.get()  # Obtener el valor como una cadena
        # Verificar si el nombre del campo no es 'surgery_length_of_duration' y convertir a flotante si es necesario
        try:
            valor = float(valor)
        except ValueError:
            pass  # Si la conversión a flotante falla, mantener el valor como cadena
        datos[nombre_campo] = valor

    ventana_secundaria.destroy()
    campos_de_entrada = []
    crearJSON(datos)

def crearJSON(diccionario):
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        nuevo_diccionario[clave] = valor
    print(nuevo_diccionario)
    realizarPeticion(nuevo_diccionario)

def realizarPeticion(json1):
    response = requests.post("http://localhost:8080/nuevaPrediccion", json=json1)
    prediction = response.json()
    crear_etiqueta(prediction[0])

def crear_etiqueta(valor):
    texto_etiqueta ="La duración de la cirugía será de {} minutos".format(valor)
    etiqueta = tk.Label(app, text=texto_etiqueta)
    # Empacar la etiqueta en la ventana
    etiqueta.pack()


#-------------------------------------- RESTO DEL CÓDIGO ------------------------------------------


app = tk.Tk()
app.geometry("1420x1200")
app.title("Tiempo estimación cirugía")


ruta_imagen = "quirofano.jpg"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((app.winfo_screenwidth(), app.winfo_screenheight()), Image.ANTIALIAS)
imagen_fondo = ImageTk.PhotoImage(imagen)


# Crear un Label para mostrar la imagen de fondo
label_fondo = tk.Label(app, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)


s = ttk.Style()
s.configure(
    "MyButton.TButton",
    #background="-transparentcolor", 
    borderwidth=0,
    font=("Times", 20),
    
)

boton = ttk.Button(app, text="Insertar Datos", command=abrir_ventana_secundaria,  style="MyButton.TButton")
boton.place(x=620, y=220)




app.mainloop()