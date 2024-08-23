from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Leitura de banco de dados/base de dados
df = pd.read_excel("Vendas.xlsx")

# Cria uma lista de opções de IDs de lojas
opcoes_lojas = list(df['ID Loja'].unique())
opcoes_lojas.append('Todas as lojas')

# Cria uma lista de opções de tipos de gráficos
tipos_graficos = ['Barras', 'Linhas', 'Pizza']

# Criação dos componentes da página
# Componentes HTML e componentes dcc (dash)
app.layout = html.Div(children=[
    html.H1(children='Faturamento da loja'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por loja: '),    

    html.Div(children='''
        Obs: esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),
    
    dcc.Dropdown(opcoes_lojas, value='Todas as lojas', id='Lista lojas', style={'margin-bottom': '20px'}),
    
    dcc.Dropdown(tipos_graficos, value='Barras', id='Tipo grafico', style={'margin-bottom': '20px'}),
    
    html.Div(id="texto"),

    dcc.Graph(
        id='grafico_quantidade_vendas'
    )
    
    
])

# Callback para atualizar o texto e o gráfico
@app.callback(
    [Output('texto', 'children'), Output('grafico_quantidade_vendas', 'figure')],
    [Input('Lista lojas', 'value'), Input('Tipo grafico', 'value')]
)
def update_output(loja_selecionada, tipo_grafico):
    # Atualiza o texto
    texto = f'Loja selecionada: {loja_selecionada}'
    
    # Filtra os dados conforme a loja selecionada
    if loja_selecionada == "Todas as lojas":
        dados_filtrados = df
    else:
        dados_filtrados = df[df['ID Loja'] == loja_selecionada]

    # Cria o gráfico conforme o tipo selecionado
    if tipo_grafico == 'Barras':
        fig = px.bar(dados_filtrados, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    elif tipo_grafico == 'Linhas':
        fig = px.line(dados_filtrados, x="Produto", y="Quantidade", color="ID Loja")
    elif tipo_grafico == 'Pizza':
        fig = px.pie(dados_filtrados, names="Produto", values="Quantidade")

    return texto, fig

if __name__ == '__main__':
    app.run_server(debug=True)
