import numpy as np
import matplotlib.pyplot as plt

#POTENCIAL
V0 = 100
#LADO DO CUBO  
a = 1   

#GRADE 
n_pontos = 200
y_vec = np.linspace(0, a, n_pontos)
z_vec = np.linspace(0, a, n_pontos)
Y, Z = np.meshgrid(y_vec, z_vec)

#X FIXADO EM a/2
X_fixo = a / 2.0

#INICIALIZAÇÃO
func_potencial = np.zeros_like(Y)

#TRUNCAMENTO COM OS 5 PRIMEIROS TERMOS
termos = [(1,1), (1,3), (3,1), (3,3), (1,5)]

#CÁLCULO DA SÉRIE DE FOURIER SENO
for n, m in termos:
    #ARGUMENTO senh
    arg_senh = np.pi * np.sqrt(n**2 + m**2) / a
    
    #FUNÇÕES X(x),Y(y),Z(z)
    termo_x = np.sin(n * np.pi * X_fixo / a)
    termo_y = np.sin(m * np.pi * Y / a)
    termo_z = np.sinh(arg_senh * Z) / np.sinh(arg_senh * a)
    
    #ACUMULADOR DO POTENCIAL
    func_potencial += (16 * V0 / (np.pi**2 * n * m)) * termo_x * termo_y * termo_z

plt.figure(figsize=(9,7))

#MAPA DE CALOR
mapa = plt.contourf(Y, Z, V, levels=100, cmap='magma')

#BARRA LATERAL
cbar = plt.colorbar(mapa)
cbar.set_label('Potencial Elétrico', fontsize=12, rotation=270, labelpad=20)

#EIXOS E TÍTULOS
plt.title('Mapa de Calor do Potencial no Centro do Cubo \n($x = a/2$)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Eixo Y', fontsize=12)
plt.ylabel('Eixo Z', fontsize=12)

plt.xlim(0, a)
plt.ylim(0, a)
plt.grid(True, linestyle=':', alpha=0.6, color='white')

plt.show()
