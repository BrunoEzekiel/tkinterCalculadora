import tkinter as tk

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    escolha = operacoes.get()

    if escolha == 'Soma':
        resultado = num1 + num2
    elif escolha == 'Subtração':
        resultado = num1 - num2
    elif escolha == 'Multiplicação':
        resultado = num1 * num2
    elif escolha == 'Divisão':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero!"
    else:
        resultado = "Escolha inválida."

    label_resultado.config(text=f"Resultado: {resultado}")

janela = tk.Tk()
janela.title("Calculadora")

label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_operacao = tk.Label(janela, text="Operação:")
label_operacao.grid(row=2, column=0, padx=10, pady=10)

operacoes = tk.StringVar()
operacoes.set('Soma') 
menu_operacoes = tk.OptionMenu(janela, operacoes, 'Soma', 'Subtração', 'Multiplicação', 'Divisão')
menu_operacoes.grid(row=2, column=1, padx=10, pady=10)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()
