valor_parcela = float(input("Informe o valor da parcela mensal: "))
quantidade_parcelas = int(input("Informe à quantidade de parcelas: "))
valor_compra = valor_parcela * quantidade_parcelas
print(f"O valor da compra é: {valor_compra:,.2f}")

# Para informar o valor da parcela mensal, use o "." ao invés da ",".

'''Porque o Python só entende um valor quebrado, exemplo(550,00) se informar à 
ele dessa maneira (550.00). Ele usa o "." como ","     '''