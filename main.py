import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Caminho para o arquivo CSV
arquivo_csv = "./archive/matchinfo.csv"

# Lendo o arquivo CSV
df = pd.read_csv(arquivo_csv, sep=';')


colunas_desejadas = [
    "League", "Year", "blueTeamTag","bResult","rResult","redTeamTag", "blueTopChamp",
    "blueJungleChamp", "blueMiddleChamp",
    "blueADCChamp", "blueSupportChamp",
   "redTopChamp", "redJungleChamp",
    "redMiddleChamp", "redADCChamp",
    "redSupportChamp"
]

# Extraindo as colunas especificadas
dados = df[colunas_desejadas]

# Criando o DataFrame Pandas
novo_df = pd.DataFrame(dados)

coluna = {
    'League':'Liga',
    'Year':'Ano',
    'blueTeamTag':'Time_Azul',
    'bResult':'Vitoria_Azul',
    'rResult':'Vitoria_Vermemlho',
    'redTeamTag':'Time_Vermelho',
    'blueTopChamp':'Top_Azul',
    'blueJungleChamp':'Jungle_Azul',
    'blueMiddleChamp':'Mid_Azul',
    'blueADCChamp':'Adc_Azul',
    'blueSupportChamp':'Sup_Azul',
    'redTopChamp':'Top_Vermelho',
    'redJungleChamp':'Jungle_Vermelho',
    'redMiddleChamp':'Mid_Vermelho',
    'redADCChamp':'Adc_Vermelho',
    'redSupportChamp':'Sup_Vermelho',
}
novo_df.rename(columns=coluna, inplace=True)

df_atual = novo_df[(novo_df['Ano'] >= 2016) & (novo_df['Ano'] <= 2018)]
print(df_atual)


coluna_champs = [
    "Liga",
    "Top_Azul",
    "Jungle_Azul",
    "Mid_Azul",
    "Adc_Azul",
    "Sup_Azul",
    "Top_Vermelho",
    "Jungle_Vermelho",
    "Mid_Vermelho",
    "Adc_Vermelho",
    "Sup_Vermelho",
]

novo_df_champs = df_atual[coluna_champs]
print(novo_df_champs)

champions = novo_df_champs.values.flatten()  # Flatten para um único array
contagem_champions = pd.Series(champions).value_counts()

# Selecionar os 10 campeões mais escolhidos
top_10_champions = contagem_champions.head(10)

plt.figure(figsize=(10, 6))
top_10_champions.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 Campeões Mais Escolhidos no Competitivo em todas as Ligas \n Entre 2016 a 2018", fontsize=14)
plt.xlabel("Campeões", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.xticks(rotation=45, ha="right")  # Girar os nomes para facilitar leitura
plt.grid(axis="y", linestyle="--", alpha=0.7)
for index, value in enumerate(top_10_champions):
    plt.text(index, value + 0.5, str(value), ha="center", fontsize=10)

plt.tight_layout()

# Exibir o gráfico
plt.show()

#Analise global do campeos mais escolhidos 2016 a 2018

coluna_champs_liga = [
    "Liga",
    "Top_Azul",
    "Jungle_Azul",
    "Mid_Azul",
    "Adc_Azul",
    "Sup_Azul",
    "Top_Vermelho",
    "Jungle_Vermelho",
    "Mid_Vermelho",
    "Adc_Vermelho",
    "Sup_Vermelho",
]

# Selecionar apenas as colunas mencionadas
novo_df_liga = novo_df[coluna_champs_liga]
print(novo_df_liga)

# Filtrar os dados para a liga "CBLol"
df_cblol = novo_df_liga[novo_df_liga["Liga"] == "CBLoL"]
print(df_cblol)


# Contar o número de vezes que cada campeão aparece
todos_champions_cblol = df_cblol.iloc[:, 1:].values.flatten()  # Ignorar a coluna "Liga"
contagem_champions_cblol = pd.Series(todos_champions_cblol).value_counts()

# Selecionar os 10 campeões mais escolhidos
top_10_champions_cblol = contagem_champions_cblol.head(10)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
bars = top_10_champions_cblol.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 Campeões Mais Escolhidos na Liga CBLol\n Entre 2016 a 2018", fontsize=14)
plt.xlabel("Campeões", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Adicionar os valores no topo das barras
for index, value in enumerate(top_10_champions_cblol):
    plt.text(index, value + 0.5, str(value), ha="center", fontsize=10)

plt.tight_layout()
plt.show()
#analise do Campeonato Brasileiro de League of Legends(CBLoL) do campeos mais escolhidos entre 2016 a 2018

df_cblol = df_atual[df_atual["Liga"] == "CBLoL"]


# 3.0 Agrupar por ano e somar as vitórias para cada lado
vitorias_por_ano = df_cblol.groupby('Ano')[['Vitoria_Azul', 'Vitoria_Vermemlho']].sum()

# Calcular o total de vitórias e porcentagens
vitorias_por_ano['Total'] = vitorias_por_ano['Vitoria_Azul'] + vitorias_por_ano['Vitoria_Vermemlho']
vitorias_por_ano['Pct_Azul'] = (vitorias_por_ano['Vitoria_Azul'] / vitorias_por_ano['Total']) * 100
vitorias_por_ano['Pct_Vermelho'] = (vitorias_por_ano['Vitoria_Vermemlho'] / vitorias_por_ano['Total']) * 100

# Configuração dos eixos e larguras
anos = vitorias_por_ano.index
indice = np.arange(len(anos))
largura = 0.35

# Criar a figura do gráfico
plt.figure(figsize=(12, 6))

# Barras para vitórias do lado azul
barras_azul = plt.bar(
    indice - largura / 2,
    vitorias_por_ano['Vitoria_Azul'],
    largura,
    label="Vitórias Time Azul",
    color='blue'
)

# Barras para vitórias do lado vermelho
barras_vermelho = plt.bar(
    indice + largura / 2,
    vitorias_por_ano['Vitoria_Vermemlho'],
    largura,
    label="Vitórias Time Vermelho",
    color='red'
)

# Adicionar rótulos de quantidade e porcentagem nas barras
for i, barra in enumerate(barras_azul):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height() + 1,
        f"{int(barra.get_height())}\n({vitorias_por_ano['Pct_Azul'].iloc[i]:.1f}%)",
        ha='center',
        va='bottom',
        fontsize=10,
        color='blue'
    )

for i, barra in enumerate(barras_vermelho):
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height() + 1,
        f"{int(barra.get_height())}\n({vitorias_por_ano['Pct_Vermelho'].iloc[i]:.1f}%)",
        ha='center',
        va='bottom',
        fontsize=10,
        color='red'
    )

# Configurações do gráfico
plt.title("Vitórias do Time Azul e Vermelho no CBLoL (2016-2018)", fontsize=16)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Quantidade de Vitórias", fontsize=12)
plt.xticks(indice, anos)  # Adiciona os anos como rótulos no eixo X
plt.legend(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar layout e exibir o gráfico
plt.tight_layout()
plt.show()


#3.1 qual os 5 times com mais vitoria
vitorias_azul = df_cblol[df_cblol['Vitoria_Azul'] == 1].groupby('Time_Azul').size()

vitorias_vermelho = df_cblol[df_cblol['Vitoria_Vermemlho'] == 1].groupby('Time_Vermelho').size()

vitorias_totais = vitorias_azul.add(vitorias_vermelho, fill_value=0)

vitorias_totais_top5 = vitorias_totais.sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))
plt.bar(vitorias_totais_top5.index, vitorias_totais_top5.values, color='skyblue')

plt.title("Top 5 Times com Mais Vitórias no CBLoL (2016-2018)", fontsize=16)
plt.xlabel("Times", fontsize=12)
plt.ylabel("Quantidade de Vitórias", fontsize=12)
plt.xticks(rotation=45, ha='right')

for i, valor in enumerate(vitorias_totais_top5.values):
    plt.text(i, valor + 0.1, str(int(valor)), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

#3.1 a diferença de vitoria da ITZ de acordo com o lado que ela jogou
df_itz_cblol = df_cblol[((df_cblol['Time_Azul'] == 'ITZ') | (df_cblol['Time_Vermelho'] == 'ITZ')) & (df_cblol['Liga'] == 'CBLoL')]

vitorias_azul_itz_2016 = df_itz_cblol[(df_itz_cblol['Vitoria_Azul'] == 1) & (df_itz_cblol['Time_Azul'] == 'ITZ') & (df_itz_cblol['Ano'] == 2016)].shape[0]
vitorias_vermelho_itz_2016 = df_itz_cblol[(df_itz_cblol['Vitoria_Vermemlho'] == 1) & (df_itz_cblol['Time_Vermelho'] == 'ITZ') & (df_itz_cblol['Ano'] == 2016)].shape[0]

vitorias_azul_itz_2017 = df_itz_cblol[(df_itz_cblol['Vitoria_Azul'] == 1) & (df_itz_cblol['Time_Azul'] == 'ITZ') & (df_itz_cblol['Ano'] == 2017)].shape[0]
vitorias_vermelho_itz_2017 = df_itz_cblol[(df_itz_cblol['Vitoria_Vermemlho'] == 1) & (df_itz_cblol['Time_Vermelho'] == 'ITZ') & (df_itz_cblol['Ano'] == 2017)].shape[0]

vitorias_azul_itz_2018 = df_itz_cblol[(df_itz_cblol['Vitoria_Azul'] == 1) & (df_itz_cblol['Time_Azul'] == 'ITZ') & (df_itz_cblol['Ano'] == 2018)].shape[0]
vitorias_vermelho_itz_2018 = df_itz_cblol[(df_itz_cblol['Vitoria_Vermemlho'] == 1) & (df_itz_cblol['Time_Vermelho'] == 'ITZ') & (df_itz_cblol['Ano'] == 2018)].shape[0]

anos = ['2016', '2017', '2018']
vitorias_azul = [vitorias_azul_itz_2016, vitorias_azul_itz_2017, vitorias_azul_itz_2018]
vitorias_vermelho = [vitorias_vermelho_itz_2016, vitorias_vermelho_itz_2017, vitorias_vermelho_itz_2018]

plt.figure(figsize=(10, 6))

plt.plot(anos, vitorias_azul, marker='o', label='Vitórias no Azul', color='skyblue', linestyle='-', linewidth=2, markersize=8)
plt.plot(anos, vitorias_vermelho, marker='o', label='Vitórias no Vermelho', color='salmon', linestyle='-', linewidth=2, markersize=8)

plt.title("Vitórias da ITZ por Ano e Lado na Liga CBLoL (2016-2018)", fontsize=16)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Quantidade de Vitórias", fontsize=12)

plt.legend()

for i in range(len(anos)):
    plt.text(anos[i], vitorias_azul[i] + 0.2, str(vitorias_azul[i]), ha='center', va='bottom', fontsize=12)
    plt.text(anos[i], vitorias_vermelho[i] + 0.2, str(vitorias_vermelho[i]), ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()

# 4 os campeos mais escolhidos pela ITZ

escolhas_campeoes = pd.concat([
    df_itz_cblol['Top_Azul'],
    df_itz_cblol['Jungle_Azul'],
    df_itz_cblol['Mid_Azul'],
    df_itz_cblol['Adc_Azul'],
    df_itz_cblol['Sup_Azul'],
    df_itz_cblol['Top_Vermelho'],
    df_itz_cblol['Jungle_Vermelho'],
    df_itz_cblol['Mid_Vermelho'],
    df_itz_cblol['Adc_Vermelho'],
    df_itz_cblol['Sup_Vermelho']
]).value_counts()

top_10_campeoes = escolhas_campeoes.head(10)

fig, ax = plt.subplots(figsize=(12, 6))
top_10_campeoes.plot(kind='bar', color='purple', alpha=0.7, ax=ax)

ax.set_title('Top 10 Campeões Mais Escolhidos pela ITZ', fontsize=16)
ax.set_xlabel('Campeões', fontsize=12)
ax.set_ylabel('Número de Escolhas', fontsize=12)
ax.bar_label(ax.containers[0], fontsize=10)

plt.tight_layout()

plt.show()