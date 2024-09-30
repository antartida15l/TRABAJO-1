import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def graficar_funcion():
    print("==========================================================")
    print(" Graficador de Funciones de una sola variable, FINESI ALE ")
    print("==========================================================")
    funcion = input("Función: f(x) = ")
    variable = input("Variable: ")
    x = sp.symbols(variable)
    intervalo = input(f"Intervalo [min, max] = : {variable}[")
    limites = intervalo.strip('[]').split(',')
    limite_inf = float(limites[0].strip())
    limite_sup  = float(limites[1].strip())
    funcion = sp.sympify(funcion)
    x_vals = np.linspace(limite_inf, limite_sup, 400)
    evaluar_funcion = sp.lambdify(x, funcion, "numpy")
    y_vals = evaluar_funcion(x_vals)
    y_max = np.max(y_vals)
    y_min = np.min(y_vals)
    x_max = x_vals[np.argmax(y_vals)]
    x_min = x_vals[np.argmin(y_vals)]

    df = pd.DataFrame({'x': x_vals, 'f(x)': y_vals})
    
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['f(x)'], color='purple')
    
    ax.plot(x_max, y_max, 'ro', label=f'Máximo en x={x_max:.2f}')
    ax.plot(x_min, y_min, 'bo', label=f'Mínimo en x={x_min:.2f}')
    
    ax.axhline(0, color='black',linewidth=1)  
    ax.axvline(0, color='black',linewidth=1) 
    ax.set_xlabel(variable)
    ax.set_ylabel(f'f({variable})')
    ax.set_title(f'Gráfica de f({variable}) = {funcion}')
    ax.grid(True, which='both')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.legend()

    print(f"Máximo aproximado en: x = {x_max:.2f}, f(x) = {y_max:.2f}")
    print(f"Mínimo aproximado en: x = {x_min:.2f}, f(x) = {y_min:.2f}")
    
    plt.show()

if __name__ == "__main__":
    graficar_funcion()
