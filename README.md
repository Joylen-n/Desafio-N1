# Desafio Nível 1 — PDV com Descontos e Bônus (Python)

## O que o código faz
Este script implementa a lógica de um sistema de Ponto de Venda (PDV) que calcula descontos progressivos baseados na idade do cliente e no valor da compra. Além das regras obrigatórias, esta versão inclui todos os bônus opcionais: descontos extras por quantidade de itens, sistema de cupom de fidelidade, um recibo detalhado exibido no terminal a cada transação e a exportação automática de um arquivo `.txt` contendo o relatório final e o histórico do dia.

## Como ele faz
1. O programa inicia um loop infinito recebendo o valor da compra, idade do cliente, quantidade de itens e um possível cupom. O loop encerra se o valor inserido for `0`.
2. Utiliza a estrutura `if` acompanhada de `continue` para validar e impedir a entrada de valores ou idades negativas.
3. Aplica os descontos de forma sequencial e cumulativa sobre a variável `valor_atual`:
   - **Regra 1:** Desconto de 20% se a idade for igual ou superior a 65 anos.
   - **Regra 2:** Desconto extra de 10% se o valor (já abatido pela idade) for estritamente maior que 100 reais.
   - **Bônus 1:** Desconto de 5% se a quantidade de itens comprados for maior que 3.
   - **Bônus 2:** Desconto de 10% se o usuário digitar o cupom `"FIDELIDADE10"`.
4. Exibe um painel de "Resumo da compra", mostrando o valor original, informando quais porcentagens foram aplicadas, o total economizado e o valor final a ser pago.
5. Salva o valor final na lista de `compras` usando `.append()` e acumula os totais de faturamento e de descontos concedidos.
6. Ao encerrar o loop, exibe no console o balanço total.
7. Utiliza a função `open("resumo.txt", "w")` e um laço `for` na lista para criar e gravar o histórico detalhado de compras em um arquivo de texto físico.

## Como rodar
Para executar o programa, abra o terminal na pasta do projeto e digite o comando:
`python pdv.py`

## Tabela de exemplos (Casos de Teste base)

| #  | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|:--:|:----------:|:-----:|:--------------:|:--------------:|:--------------------:|
| 1  | 50.00      | 30    | 0%             | 0%             | R$ 50.00             |
| 2  | 100.00     | 30    | 0%             | 0%             | R$ 100.00            |
| 3  | 80.00      | 65    | 20%            | 0%             | R$ 64.00             |
| 4  | 100.00     | 70    | 20%            | 0%             | R$ 80.00             |
| 5  | 125.00     | 70    | 20%            | 0%             | R$ 100.00            |
| 6  | 200.00     | 30    | 0%             | 10%            | R$ 180.00            |
| 7  | 101.00     | 30    | 0%             | 10%            | R$ 90.90             |
| 8  | 200.00     | 65    | 20%            | 10%            | R$ 144.00            |
| 9  | 1000.00    | 80    | 20%            | 10%            | R$ 720.00            |
| 10 | 200.00     | 64    | 0%             | 10%            | R$ 180.00            |

## Tabela de exemplos (Casos de Teste com Bônus)

| # | Valor (R$) | Idade | Qtd | Cupom        | Desc. Idade | Desc. Valor | Desc. Qtd | Desc. Cupom | Valor final esperado |
|:-:|:----------:|:-----:|:---:|:-------------|:-----------:|:-----------:|:---------:|:-----------:|:--------------------:|
| 1 | 100.00     | 30    | 4   | Nenhum       | 0%          | 0%          | 5%        | 0%          | R$ 95.00             |
| 2 | 100.00     | 30    | 2   | FIDELIDADE10 | 0%          | 0%          | 0%        | 10%         | R$ 90.00             |
| 3 | 200.00     | 65    | 5   | Nenhum       | 20%         | 10%         | 5%        | 0%          | R$ 136.80            |
| 4 | 125.00     | 70    | 2   | FIDELIDADE10 | 20%         | 0%          | 0%        | 10%         | R$ 90.00             |
| 5 | 200.00     | 70    | 5   | FIDELIDADE10 | 20%         | 10%         | 5%        | 10%         | R$ 123.12            |