preco_atual = float(input("Digite o preço do produto: R$ "))


if preco_atual <= 50:
    novo_preco = preco_atual * 1.05 
else:
    novo_preco = preco_atual * 1.10 

print(f"O novo valor do produto é: R$ {novo_preco:.2f}")
