
import pandas as pd
from sqlalchemy import create_engine

def migrar_csv_para_postgres(caminho_csv, nome_tabela):
    # Ler o CSV
    df = pd.read_csv(caminho_csv);
    
    # Criar a engine de conexão (ajuste os dados abaixo para o seu banco)
    engine = create_engine('postgresql://postgres:8289@localhost:5432/sku_db')
    
    # Enviar para o banco (se já existir, substitui a tabela)
    df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
    
    print(f"Dados do arquivo {caminho_csv} migrados para a tabela '{nome_tabela}' com sucesso!")

if __name__ == "__main__":
    caminho_csv = 'C:/Users/tp776/OneDrive/PULSE/python/entendendo_oh_problema/data/relatorio_descongelamento_filial7.csv'      # caminho para o seu CSV
    nome_tabela = 'sku_db'        # nome da tabela no banco
    migrar_csv_para_postgres(caminho_csv, nome_tabela)
