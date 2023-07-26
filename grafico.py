from matplotlib import pyplot
import numpy as np

eixoX_Grafico1 = [10,20,30,40]
eixoY_Grafico1 = [5,10,15,20]
fig, Grafico1 = pyplot.subplots()
Grafico1.plot(eixoX_Grafico1,eixoY_Grafico1)
pyplot.show()

# DADOS

x = [3,22,7,48]
y = [13,4,90,160]

# CRIAR UMA FIGURA E UM EIXO

fig, ax = pyplot.subplots()
#PLOTAR OS GRAFÍCOS COM PERSONALIZAÇÃO

ax.plot(x,y, color = 'green' , linestyle = '--' , marker = 'o', label = 'casas')



# ADICIONAR RÓTULOS E TÍTULOS 

ax.set_xlabel('Quantidade de Casas')
ax.set_ylabel('Quantidades de Pessoas')
ax.set_title('Censo de Presença')

# INCLUIR UMA LEGENDA

ax.legend()

#MOSTRAR O GRAFÍCO

pyplot.show()





# OUTROS GRAFICOS

rotulos = ['maças','banana','uva','gelatina','FIGOS']
valores = [ 9,2,6,8,14]

fig, ax = pyplot.subplots()

ax.barh(rotulos,valores)


ax.set_xlabel('Frutas')
ax.set_ylabel('PREÇO')
ax.set_title('Media dos precosnde frutas ')

pyplot.show()


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


rotulos = [ 'banana', ' maça', 'cacau', 'baunilha','abacaxi']
tamanho = [25, 30,20,25,27]
cores = ['blue', 'orange', 'green','red','yellow']

fig, ax = pyplot.subplots()

ax.pie(tamanho,labels=rotulos,colors=cores, autopct='%1.1f%%')


ax.set_title('GRAFICO DE FRUTAS')

pyplot.show()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Dados (cotações diárias das ações)
dias = list(range(1, 13))
vale5 = [82.2, 79.2, 84.0, 86.4, 84.8, 87.2, 88.8, 92.0, 89.6, 92.8, 95.2, 93.6]
unip6 = [75.0, 73.2, 75.6, 77.4, 78.2, 76.8, 78.0, 81.0, 82.2, 83.6, 83.4, 82.2]
bbas3 = [28.3, 27.9, 28.5, 29.2, 29.0, 29.4, 29.7, 30.1, 29.8, 30.2, 30.5, 30.3]

# Criar figura e eixos
fig, ax = pyplot.subplots()

# Plotar os dados
ax.plot(dias, vale5, label='VALE5')
ax.plot(dias, unip6, label='UNIP6')
ax.plot(dias, bbas3, label='BBAS3')

# Mostrar os rótulos dos eixos e a legenda do gráfico
ax.set_xlabel('Dia')
ax.set_ylabel('Preço (R$)')
ax.legend()

# Exibir o gráfico pronto
pyplot.show()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Gerar um conjunto de dados aleatórios
np.random.seed(123)
x = np.random.normal(0, 1, 50)
y = np.random.normal(0, 1, 50)

# Criar figura e eixo
fig, ax = pyplot.subplots()

# Criar o gráfico de dispersão
ax.scatter(x, y)

# Inserir rótulos de dados e título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatterplot')

# Exibir o gráfico
pyplot.show()