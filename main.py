
import pandas as pd
from pandasgui import show

#passo zero - entender o problema - leia o read me

#primeiro passo - tratar e coletar dados com o pandas
#obs - precisamos de uma ferramenta para visualizar os dados - pandasGUI,jupyter notebook
  
df = pd.read_csv("relatorio_descongelamento_filial7.csv");

#show(df);

primeiras_informacoes= df.head;

print(primeiras_informacoes);
 
df.info();

#df["Data_retirada"] = pd.to_datetime(df["Data_retirada"]);

print(df.describe());

print(df.isnull().sum());

data_especifica = "2025-05-19";

#df_filtrando_data = df[df["Data_Retirada"] == data_especifica];

inicio = "2025-06-15";

fim = "2025-06-20";

#df_periodo = df[(df["Data_Retirada"] >= inicio) & (df["Data_Retirada"] <= fim)];

df_filtrado = df[
    (df["Data_Retirada"] == "2025-06-19") &
    (df["SKU"].isin(["SKU_03", "SKU_05"])) &
    (df["Idade_Lote_Descongelado"] <= 2)
]

#proximo passo - entender o comportamento dos skus - qual o total de quilos
#retirados ate agora para cada produto
#qual sku tem maior volume movimentado
#onde pode estar o maior risco de perda

#total de kg retirado por sku
print(df.groupby("SKU")["Kg_Retirar_Hoje"].sum())


#total de kg em descongelamento por sku
print(df.groupby("SKU")["Kg_Descongelando"].sum());

df.groupby("SKU")["Kg_Descongelando"].sum();

df.groupby("SKU")["Kg_Disponivel_Hoje"].sum()


sum_e_medias = df.groupby("SKU").agg({
    "Kg_Retirar_Hoje" : ["sum", "mean"],
    "Kg_Descongelando": ["sum","mean"],
   "Kg_Disponivel_Hoje" : ["sum","mean"],
   "Idade_Lote_Descongelado" : ["mean","max"], 
})
#show(sum_e_medias);



#deteccao de skus com riscos de vencimento
#a gente vai partir de um pre suposto que nossa tabela nao tem a data de validade

validade = {
      "SKU_01": 3,
    "SKU_02": 3,
    "SKU_03": 3,
    "SKU_04": 3,
    "SKU_05": 3,
    "SKU_06": 5,
    "SKU_07": 5,
    "SKU_08": 5,
    "SKU_09": 5,
    "SKU_10": 5
}

vencimento  = df["Validade_Max"] = df["SKU"].map(validade);
#show(vencimento)
 
show(df);

#criando uma coluna de risco vencimento e aplicando aquela regra ali
df["Risco_Vencimento"] = df["Idade_Lote_Descongelado"] >= (df["Validade_Max"] - 1);

df_risco = df[df["Risco_Vencimento"]];



df_risco.to_csv("skus_em_risco.csv", index = False);


show(df_risco)
#criar um scripting
#exportando arquivo csv
df.to_csv("relatorio_diario.csv", index = False);