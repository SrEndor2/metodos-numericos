import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

def evaluar_funcion(func_str, val):
    f = sp.sympify(func_str)
    return float(f.evalf(subs={x: val}))

def newton_raphson(func_str, x0, tol, max_iter):
    f = sp.sympify(func_str)
    f_prime = sp.diff(f, x)
    for _ in range(max_iter):
        f_x0 = f.evalf(subs={x: x0})
        f_prime_x0 = f_prime.evalf(subs={x: x0})
        if f_prime_x0 == 0:
            return None
        x1 = x0 - f_x0 / f_prime_x0
        if abs(x1 - x0) < tol:
            return float(x1)
        x0 = x1
    return float(x1)

def falsa_posicion(func_str, a, b, tol, max_iter):
    f = sp.sympify(func_str)
    fa = f.evalf(subs={x: a})
    fb = f.evalf(subs={x: b})
    if fa * fb > 0:
        return None
    for _ in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f.evalf(subs={x: c})
        if abs(fc) < tol:
            return float(c)
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return float(c)

def biseccion(func_str, a, b, tol, max_iter):
    f = sp.sympify(func_str)
    fa = f.evalf(subs={x: a})
    fb = f.evalf(subs={x: b})
    if fa * fb > 0:
        return None
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f.evalf(subs={x: c})
        if abs(fc) < tol or abs(b - a) < tol:
            return float(c)
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return float(c)

def graficar_funcion(func_str, raiz=None):
    f = sp.lambdify(x, sp.sympify(func_str), "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    plt.figure()
    plt.axhline(0, color='gray', linestyle='--')
    plt.plot(x_vals, y_vals, label=f'f(x) = {func_str}')
    if raiz is not None:
        plt.plot(raiz, f(raiz), 'ro', label=f'Raíz ≈ {raiz:.5f}')
    plt.title("Gráfica de la función")
    plt.legend()
    plt.grid(True)
    plt.show()

def calcular_raiz():
    func_str = funcion_entry.get()
    metodo = metodo_var.get()
    tol = float(tolerancia_entry.get())
    max_iter = int(iteraciones_entry.get())

    try:
        if metodo == "Newton-Raphson":
            x0 = float(x0_entry.get())
            raiz = newton_raphson(func_str, x0, tol, max_iter)
        elif metodo == "Falsa Posición":
            a = float(a_entry.get())
            b = float(b_entry.get())
            raiz = falsa_posicion(func_str, a, b, tol, max_iter)
        elif metodo == "Bisección":
            a = float(a_entry.get())
            b = float(b_entry.get())
            raiz = biseccion(func_str, a, b, tol, max_iter)
        else:
            raise ValueError("Método no válido")

        if raiz is None:
            messagebox.showerror("Error", "No se encontró una raíz válida.")
        else:
            resultado_var.set(f"Raíz aproximada: {raiz:.6f}")
            graficar_funcion(func_str, raiz)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def actualizar_campos(*args):
    metodo = metodo_var.get()
    if metodo == "Newton-Raphson":
        x0_entry.grid(row=5, column=1)
        a_entry.grid_remove()
        b_entry.grid_remove()
        x0_label.grid(row=5, column=0)
        a_label.grid_remove()
        b_label.grid_remove()
    else:
        x0_entry.grid_remove()
        x0_label.grid_remove()
        a_label.grid(row=5, column=0)
        a_entry.grid(row=5, column=1)
        b_label.grid(row=6, column=0)
        b_entry.grid(row=6, column=1)

# Interfaz Tkinter
root = tk.Tk()
root.title("Métodos de Raíces")

# Función
tk.Label(root, text="f(x):").grid(row=0, column=0)
funcion_entry = tk.Entry(root, width=30)
funcion_entry.grid(row=0, column=1)

# Método
tk.Label(root, text="Método:").grid(row=1, column=0)
metodo_var = tk.StringVar()
metodo_menu = ttk.Combobox(root, textvariable=metodo_var, state="readonly")
metodo_menu['values'] = ("Newton-Raphson", "Falsa Posición", "Bisección")
metodo_menu.current(0)
metodo_menu.grid(row=1, column=1)
metodo_var.trace_add('write', actualizar_campos)

# Tolerancia
tk.Label(root, text="Tolerancia:").grid(row=2, column=0)
tolerancia_entry = tk.Entry(root)
tolerancia_entry.grid(row=2, column=1)
tolerancia_entry.insert(0, "0.0001")

# Iteraciones
tk.Label(root, text="Máx. Iteraciones:").grid(row=3, column=0)
iteraciones_entry = tk.Entry(root)
iteraciones_entry.grid(row=3, column=1)
iteraciones_entry.insert(0, "50")

# Campos dinámicos
x0_label = tk.Label(root, text="x0:")
x0_entry = tk.Entry(root)
a_label = tk.Label(root, text="a:")
a_entry = tk.Entry(root)
b_label = tk.Label(root, text="b:")
b_entry = tk.Entry(root)

# Botón
tk.Button(root, text="Calcular Raíz", command=calcular_raiz).grid(row=7, columnspan=2, pady=10)

# Resultado
resultado_var = tk.StringVar()
tk.Label(root, textvariable=resultado_var, font=("Arial", 12, "bold")).grid(row=8, columnspan=2)

# Inicializa campos
actualizar_campos()

root.mainloop()
