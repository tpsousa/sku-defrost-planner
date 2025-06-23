

Desafio de Dimensionamento de Retiradas para Descongelamento (Filial 7)
Visão Geral do Problema:
Este projeto tem como objetivo criar uma solução de análise de dados para dimensionar, de forma eficiente, a quantidade de produtos a serem retirados dos freezers da Filial 7 do Grupo Mateus. O foco é garantir o abastecimento correto das gôndolas, evitando tanto a falta de estoque quanto o desperdício por vencimento.

O desafio consiste em definir, diariamente, quantos quilos de cada SKU devem ser retirados do freezer, levando em consideração:

Histórico de vendas anteriores

Validade de cada produto após o descongelamento

Lead time operacional de 2 dias (tempo entre retirada e disponibilidade)

Capacidade dos freezers da filial

Com base nesses parâmetros, é necessário gerar um relatório diário contendo:

Quantidade a ser retirada hoje

Quantidade atualmente em descongelamento (disponível amanhã)

Quantidade disponível para venda hoje

Idade (em dias) de cada lote atualmente descongelado

Detalhamento do Contexto Operacional
Ciclo de Descongelamento
O processo segue um fluxo fixo:

Dia 0: Produtos são retirados do freezer e colocados para descongelar.

Dia 1: Produtos continuam em processo de descongelamento.

Dia 2: Produtos estão prontos para venda.

Após o descongelamento, os produtos possuem uma validade limitada (por exemplo, entre 3 e 5 dias).

Caso não sejam vendidos dentro do prazo de validade, os produtos devem ser descartados, gerando prejuízo.

A solução proposta deve ser capaz de antecipar demandas e controlar os estoques descongelados para minimizar perdas e garantir o abastecimento.