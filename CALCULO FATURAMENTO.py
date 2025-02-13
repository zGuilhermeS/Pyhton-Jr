import pandas as pd #IMPORT ARQUIVO

def calcular_faturamento(arquivo_csv):#IMPORT ARQUIVO
    df = pd.read_csv(arquivo_csv)
    df['faturamento'] = df['quantidade'] * df['preco_unitario'] # CALCULO
    faturamento_por_produto = df.groupby('produto')['faturamento'].sum() #CALCULO
    produto_max = faturamento_por_produto.idxmax() #VALOR MAX
    produto_min = faturamento_por_produto.idxmin() #VALOR MIN
    return faturamento_por_produto, produto_max, produto_min # RETORNO