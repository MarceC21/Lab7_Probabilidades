import numpy as np
import matplotlib.pyplot as plt

# Párametros de la simualción

np.random.seed(2026)

N = 100      # número total de estampas
S = 7        # estampas por sobre
R = 10000    # simulaciones

# función para simular la compra de sobres hasta completar el álbum

def simular_album(N, S):
    
    # set para las estampas que ya tenemos
    coleccion = set()
    
    sobres = 0
    repetidas = 0
    
    while len(coleccion) < N:
        
        # generar un sobre con S estampas distintas
        sobre = np.random.choice(range(N), size=S, replace=False)
        
        sobres += 1
        
        for estampa in sobre:
            
            if estampa in coleccion:
                repetidas += 1
            else:
                coleccion.add(estampa)
                
    return sobres, repetidas

# =========================================================
# ETAPA 1
# =========================================================

lista_sobres = []
lista_repetidas = []

for _ in range(R):
    
    sobres, repetidas = simular_album(N, S)
    
    lista_sobres.append(sobres)
    lista_repetidas.append(repetidas)

lista_sobres = np.array(lista_sobres)
lista_repetidas = np.array(lista_repetidas)

# Resultados etapa1 

media_sobres = np.mean(lista_sobres)
std_sobres = np.std(lista_sobres)

media_repetidas = np.mean(lista_repetidas)
std_repetidas = np.std(lista_repetidas)

prob_mas_30 = np.mean(lista_sobres > 30)

print("===== RESULTADOS ETAPA 1 =====")
print(f"Media de sobres: {media_sobres:.4f}")
print(f"Desviación estándar sobres: {std_sobres:.4f}")
print()
print(f"Media de repetidas: {media_repetidas:.4f}")
print(f"Desviación estándar repetidas: {std_repetidas:.4f}")
print()
print(f"Probabilidad de necesitar más de 30 sobres: {prob_mas_30:.4f}")

# Valor teórico esperado

H_N = np.sum(1 / np.arange(1, N + 1))

valor_teorico = (N / S) * H_N

print()
print("===== TEORÍA DEL COLECCIONISTA =====")
print(f"H_{N} = {H_N:.4f}")
print(f"Valor teórico esperado: {valor_teorico:.4f}")

# Mínimo teórico de sobres (redondeado hacia arriba)

minimo_teorico = np.ceil(N / S)

print(f"Mínimo teórico de sobres: {minimo_teorico}")

# Si aparece el mínimo teórico en las simulaciones

casos_minimos = np.sum(lista_sobres == minimo_teorico)

print(f"Cantidad de simulaciones con el mínimo teórico: {casos_minimos}")

# =========================================================
# HISTOGRAMA
# =========================================================

plt.figure(figsize=(10,6))

plt.hist(lista_sobres, bins=30)

plt.axvline(media_sobres,
            linestyle='dashed',
            color='red',        
            linewidth=2,
            label=f"Media = {media_sobres:.2f}")

plt.axvline(valor_teorico,
            linestyle='solid',
            color='green',
            linewidth=2,
            label=f"Teórico = {valor_teorico:.2f}")

plt.xlabel("Número de sobres")
plt.ylabel("Frecuencia")
plt.title("Distribución del número de sobres necesarios")

plt.legend()

plt.show()

# =========================================================
# ETAPA 2
# =========================================================

# Simular la compra de M sobres y calcular la probabilidad de completar el álbum
M_values = [20,25,30,35,40,45,50,60,70,80]

probabilidades = []

for M in M_values:
    
    exitos = 0
    
    for _ in range(R):
        
        coleccion = set()
        
        for _ in range(M):
            
            sobre = np.random.choice(range(N), size=S, replace=False)
            
            for estampa in sobre:
                coleccion.add(estampa)
                
        if len(coleccion) == N:
            exitos += 1
            
    prob = exitos / R
    
    probabilidades.append(prob)

# =========================================================
# RESULTADOS ETAPA 2
# =========================================================

print()
print("===== ETAPA 2 =====")

for M, p in zip(M_values, probabilidades):
    print(f"M = {M:2d} ---> P(completar) = {p:.4f}")

# =========================================================
# GRÁFICA
# =========================================================

plt.figure(figsize=(10,6))

plt.plot(M_values, probabilidades, marker='o')

plt.axhline(0.5,
            linestyle='dashed',
            linewidth=2,
            label='50%')

plt.xlabel("Número de sobres")
plt.ylabel("Probabilidad de completar álbum")
plt.title("Probabilidad de completar el álbum")

plt.legend()

plt.show()

# =========================================================
# PRIMER M CON P > 0.5 Y P > 0.9
# =========================================================

m_50 = None
m_90 = None

for M, p in zip(M_values, probabilidades):
    
    if m_50 is None and p > 0.5:
        m_50 = M
        
    if m_90 is None and p > 0.9:
        m_90 = M

print()
print(f"Primer M con probabilidad > 50%: {m_50}")
print(f"Primer M con probabilidad > 90%: {m_90}")

# =========================================================
# COTA TEÓRICA PARA M = 50
# =========================================================

M = 50

cota = N * np.exp(-(M*S)/N)

print()
print("===== COTA TEÓRICA =====")
print(f"Cota unión para M = 50: {cota:.6f}")