# Variáveis

compras = []
total_bruto = 0.0
total_descontos = 0.0

print("---Bem-vindo ao PDV---")

while True:
    # Entrada do valor da compra
    valorCompra_input = float(input("Digite o valor da compra (ou 0 para finalizar): "))

    # Quebra do loop caso 0
    if valorCompra_input == 0:
        break

    # Caso digite valores negtivos 
    if valorCompra_input < 0:
        print("O valor não pode ser negativo!!! Tente novamente.")
        continue

    # Entrada da idade do cliente
    idade_input = int(input("Digite a idade do cliente: "))   
    
    # Caso a idade seja negativa
    if idade_input < 0:
        print("A idade não pode ser negativa!!! Tente novamente.")
        continue

    # Bonus
    qtd_itens_input = int(input("Digite a quantidade de itens: "))
    cupom = input("Digite o cupom de desconto (ou pressione Enter para ignorar): ")

    #Variavel para calcular os descontos
    valor_atual = valorCompra_input

    # Regra 1 - desconto por idade de 20% quando >= 65 anos
    if idade_input >= 65:
        valor_atual = valor_atual - (valor_atual * 0.2)

    # Regra 2 - desconto por valor da compra de 10% quando > 100 reais
    if valor_atual > 100:
        valor_atual = valor_atual - (valor_atual * 0.1)

    # Bonus 1 - desconto por quantidade de itens de 5% quando > 3 itens
    if qtd_itens_input > 3:
        valor_atual = valor_atual - (valor_atual * 0.05)

    # Bonus 2 - desconto de cupom de fidelidade de 10% quando o cupom for "FIDELIDADE10"
    if cupom == "FIDELIDADE10":
        valor_atual = valor_atual - (valor_atual * 0.1)

    # Cálculo do desconto total
    desconto_total_compra = valorCompra_input - valor_atual

    # ----------- Mostrar o resumo da compra -----------
    print("\nResumo da compra:")
    print(f"Valor Original: R$ {valorCompra_input:.2f}")

    # Verifica quais descontos foram ativados para mostrar as porcentagens
    if idade_input >= 65:
        print("- Desconto por Idade: 20% aplicado")

    # Lógica para checar se o valor (após o desconto de idade) passou de 100
    valor_apos_idade = valorCompra_input - (valorCompra_input * 0.20 if idade_input >= 65 else 0)
    if valor_apos_idade > 100:
        print("- Desconto por Valor: 10% extra aplicado")

    # Mostra no print se o desconto de quantidade foi ativado
    if qtd_itens_input > 3:
        print("- Desconto por Quantidade: 5% extra aplicado")

    # Mostra no print se o cupom foi ativado
    if cupom == "FIDELIDADE10":
        print("- Cupom de Fidelidade: 10% extra aplicado")

    # Mostra o total economizado e o valor final obrigatório
    print(f"Você economizou: R$ {desconto_total_compra:.2f}")
    print(f"Valor final: R$ {valor_atual:.2f}\n")
    #------------------------------------------------------

    # Salvar no histórico e acumular os totais
    compras.append(valor_atual)
    total_bruto += valorCompra_input
    total_descontos += desconto_total_compra

print("\n=== Resumo do dia ===")
print(f"Total de compras: {len(compras)}")
print(f"Total bruto: R${total_bruto:.2f}")
print(f"Total de descontos feitos: R${total_descontos:.2f}")
print(f"Total final: R${sum(compras):.2f}\n")

# Bonus de historico num ficheiro txt
arquivo = open("resumo.txt", "w")
arquivo.write(f"=== Resumo do dia ===\n")
arquivo.write(f"Total de compras: {len(compras)}\n")
arquivo.write(f"Total bruto: R${total_bruto:.2f}\n")
arquivo.write(f"Total de descontos feitos: R${total_descontos:.2f}\n")
arquivo.write(f"Total final: R${sum(compras):.2f}\n")
arquivo.write("--- Histórico de compras ---\n")

for i in range(len(compras)):
    arquivo.write(f"Compra {i + 1}: R${compras[i]:.2f}\n")
    
arquivo.close()
print("\nResumo do dia salvo em 'resumo.txt'.")
