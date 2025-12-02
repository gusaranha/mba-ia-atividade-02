"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""

import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"  ✅ {len(df)} linhas carregadas")
        return df
    except FileNotFoundError:
        print(f"  ❌ Arquivo não encontrado: {caminho_arquivo}")
        return None


def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print_header("EXPLORAÇÃO DOS DADOS")
    print(f"Shape: {df.shape}")
    print(f"Linhas (clientes): {df.shape[0]:,}")
    print(f"Colunas (características): {df.shape[1]}")
    print()
    print("Detalhamento das colunas:")
    print(df.dtypes)
    print()
    print("5 primeiros clientes:")
    print(df.head())
    print()


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print_header("DISTRIBUIÇÃO DO TARGET")
    print(df[coluna_target].value_counts())
    print(df[coluna_target].value_counts(normalize=True))
    print()

def print_header(header_text):
    print()
    print("=" * 50)
    print(header_text)
    print("=" * 50)
    print()

# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
