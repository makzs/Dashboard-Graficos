from matplotlib import pyplot as plt


# eixo X
dias = [1,5,10,15,20,25,30]
# eixo Y
# Temperaturas Maximas
temp_max = [28,29,26,23,20,25,27]
# Temperaturas Minimas
temp_min = [20,22,21,19,17,20,23]

# adiciona um titulo ao grafico
plt.title('Temperaturas Maximas e Minimas')
plt.xlabel('Data')
plt.ylabel('Temperatura')

# Cria um grafico simples de dois eixos
plt.plot(dias, temp_max)
plt.plot(dias, temp_min)

# legendas
plt.legend(['Temp Max', 'Temp Min'])
# grid
plt.grid(True)

# metodo que mostra o grafico
plt.show()