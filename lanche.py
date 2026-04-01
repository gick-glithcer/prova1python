#Calcule o seu Lanche
total = 0
valor = -1

print("Bem vindo a Cantina da escola🏫")
print("Digite o Valor do seu Lanche:")

while valor <=0:
    
   valor = float(input("Digite o Valor do Lanche🍔:"))
   if valor > 0:
       total = total + valor
       print(f"Subtotal:R${total:.2f}")
   elif valor < 0:
       print("Preço Invalido❌")
print(f"Valor da Compra é:R${total:.2f}")
#--Samuel Henrique Das Chagas--