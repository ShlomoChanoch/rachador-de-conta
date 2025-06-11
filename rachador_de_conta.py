print("Rachador de Conta")

conta_inicial = float(input("Quanto deu a conta?\n"))
gorjeta = int(input("Vai pagar a gorjeta?\nNo Brasil, a gorjeta é sempre 10%.\nDigite 1 para Sim ou 2 para Não.\n"))
pessoas = int(input("Vai dividir entre quantas pessoas?\n"))

if gorjeta == 1:
	porcentagem_da_gorjeta = 10
	total_gorjeta = (porcentagem_da_gorjeta / 100) * conta_inicial
	total_conta = conta_inicial + total_gorjeta
	final_conta = total_conta / pessoas
	print(f"A conta deu R$ {total_conta:.2f}, dando R$ {final_conta:.2f} pra cada um.")
elif gorjeta == 2:
        porcentagem_da_gorjeta = 0
        final_conta = conta_inicial / pessoas
        print(f"A conta deu R$ {conta_inicial:.2f}, dando R$ {final_conta:.2f} pra cada um.")
else:
	print("Input inválido, por favor, diga se pagará a gorjeta.")


