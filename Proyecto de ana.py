import tkinter as tk
from tkinter import messagebox

# Preguntas y respuestas del juego
preguntas = [
    {
        "pregunta": "¿Cuál es la ley de De Morgan para conjuntos?",
        "opciones": [
            "A ∪ B = B ∪ A",        # Incorrecto
            "A ∩ B = B ∩ A",        # Incorrecto
            "¬(A ∪ B) = ¬A ∩ ¬B",   # Correcto
            "A - B = A ∩ ¬B"        # Incorrecto
        ],
        "respuesta": 2  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es una regla de inferencia válida?",
        "opciones": [
            "A ∧ B → A",            # Correcto
            "A → A ∧ B",            # Incorrecto
            "A ∨ B → A",            # Incorrecto
            "A ∨ B → ¬A"            # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la absorción para conjuntos?",
        "opciones": [
            "A ∪ (A ∩ B) = A",      # Incorrecto
            "A ∩ (A ∪ B) = B",      # Incorrecto
            "A ∩ (A ∪ B) = A",      # Correcto
            "A ∪ (A ∩ B) = B"       # Incorrecto
        ],
        "respuesta": 2  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la identidad para la unión?",
        "opciones": [
            "A ∪ ∅ = A",            # Correcto
            "A ∩ ∅ = A",            # Incorrecto
            "A ∪ A' = A",           # Incorrecto
            "A ∪ A = ∅"             # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la identidad para la intersección?",
        "opciones": [
            "A ∩ A = A",            # Correcto
            "A ∪ ∅ = A",            # Incorrecto
            "A ∩ ∅ = A",            # Incorrecto
            "A ∩ A' = A"            # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley del complemento para la unión?",
        "opciones": [
            "A ∪ A' = U",           # Correcto
            "A ∩ A' = U",           # Incorrecto
            "A ∪ A = U",            # Incorrecto
            "A ∪ A' = ∅"            # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley del complemento para la intersección?",
        "opciones": [
            "A ∩ A' = ∅",           # Correcto
            "A ∩ A' = A",           # Incorrecto
            "A ∪ A' = ∅",           # Incorrecto
            "A ∩ A' = U"            # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la doble negación?",
        "opciones": [
            "¬(¬A) = A",            # Correcto
            "¬A ∪ ¬A = A",          # Incorrecto
            "¬A ∩ ¬A = A",          # Incorrecto
            "¬(A ∪ B) = A"          # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la idempotencia para la unión?",
        "opciones": [
            "A ∪ A = A",            # Correcto
            "A ∪ A = U",            # Incorrecto
            "A ∪ A = ∅",            # Incorrecto
            "A ∩ A = U"             # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la idempotencia para la intersección?",
        "opciones": [
            "A ∩ A = A",            # Correcto
            "A ∩ A = U",            # Incorrecto
            "A ∩ A = ∅",            # Incorrecto
            "A ∪ A = ∅"             # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la distribución de la unión sobre la intersección?",
        "opciones": [
            "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)", # Correcto
            "A ∪ (B ∩ C) = (A ∩ B) ∪ (A ∩ C)", # Incorrecto
            "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)", # Incorrecto
            "A ∩ (B ∩ C) = (A ∩ B) ∩ (A ∩ C)"  # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Cuál es la ley de la distribución de la intersección sobre la unión?",
        "opciones": [
            "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)", # Correcto
            "A ∩ (B ∪ C) = (A ∪ B) ∩ (A ∪ C)", # Incorrecto
            "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)", # Incorrecto
            "A ∪ (B ∪ C) = (A ∪ B) ∪ (A ∪ C)"  # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Qué significa modus ponens?",
        "opciones": [
            "Si P entonces Q; P; por lo tanto, Q", # Correcto
            "Si P entonces Q; Q; por lo tanto, P", # Incorrecto
            "Si P entonces Q; ¬Q; por lo tanto, ¬P", # Incorrecto
            "Si P entonces Q; ¬P; por lo tanto, ¬Q"  # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    },
    {
        "pregunta": "¿Qué significa modus tollens?",
        "opciones": [
            "Si P entonces Q; ¬Q; por lo tanto, ¬P", # Correcto
            "Si P entonces Q; Q; por lo tanto, P",   # Incorrecto
            "Si P entonces Q; ¬P; por lo tanto, ¬Q", # Incorrecto
            "Si P entonces Q; P; por lo tanto, Q"    # Incorrecto
        ],
        "respuesta": 0  # Índice de la respuesta correcta
    }
]

# Inicializar puntaje
puntaje = 0
pregunta_actual = 0

# Función para verificar la respuesta
def verificar_respuesta():
    global puntaje, pregunta_actual
    seleccion = var.get()
    if seleccion == preguntas[pregunta_actual]["respuesta"]:
        puntaje += 1
    pregunta_actual += 1
    if pregunta_actual < len(preguntas):
        mostrar_pregunta()
    else:
        messagebox.showinfo("Resultado", f"Tu puntaje es: {puntaje}/{len(preguntas)}")
        root.destroy()

# Función para mostrar la pregunta actual
def mostrar_pregunta():
    pregunta_label.config(text=preguntas[pregunta_actual]["pregunta"])
    for i in range(4):
        opciones[i].config(text=preguntas[pregunta_actual]["opciones"][i])

# Configuración de la ventana principal
root = tk.Tk()
root.title("Juego de Matemáticas: Leyes de Conjuntos y Reglas de Inferencia")

pregunta_label = tk.Label(root, text="", wraplength=400, justify="center")
pregunta_label.pack(pady=20)

var = tk.IntVar()

opciones = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=var, value=i)
    rb.pack(anchor="w")
    opciones.append(rb)

boton = tk.Button(root, text="Responder", command=verificar_respuesta)
boton.pack(pady=20)

mostrar_pregunta()

root.mainloop()
