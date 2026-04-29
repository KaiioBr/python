import customtkinter as ctk
from tkinter import messagebox 

# Configuração da aparência
ctk.set_appearance_mode('light')

# Função de cálculo e classificação
def calcular_imc():
    try:
        # Pega os valores e substitui vírgula por ponto
        p = float(peso.get().replace(',', '.'))
        a = float(altura.get().replace(',', '.'))
            
        # Realiza o cálculo do IMC (Peso / Altura²)
        imc = p / (a ** 2)
            
        # Atualiza a label do número formatando para 1 casa decimal
        resultado_valor.configure(text=f'{imc:.1f}')  
        
        # Lógica de Classificação do IMC
        if imc < 18.5:
            situacao = "Abaixo do peso"
            cor = "#e67e22" # Laranja
        elif 18.5 <= imc < 24.9:
            situacao = "Peso normal"
            cor = "#27ae60" # Verde
        elif 25 <= imc < 29.9:
            situacao = "Sobrepeso"
            cor = "#f39c12" # Laranja mais forte
        elif 30 <= imc < 34.9:
            situacao = "Obesidade Grau I"
            cor = "#d35400" # Laranja escuro
        elif 35 <= imc < 39.9:
            situacao = "Obesidade Grau II"
            cor = "#c0392b" # Vermelho
        else:
            situacao = "Obesidade Grau III (Mórbida)"
            cor = "#900c3f" # Vermelho escuro/Vinho
            
        # Atualiza a label da situação com o texto e a cor correspondente
        resultado_situacao.configure(text=situacao, text_color=cor)

    except ValueError:
        messagebox.showerror('ERRO', 'Por favor, preencha todos os campos corretamente com números!')

# Criação da janela principal
janela = ctk.CTk()
janela.geometry('450x580') # Aumentei um pouco a altura para caber a nova label
janela.title('Calculadora de IMC')
janela.configure(fg_color='#f4f7fc') 

# --- TÍTULOS ---
ctk.CTkLabel(janela,
             text='Calculadora de IMC',
             text_color='#0c326f',
             font=('Arial', 32, 'bold')).pack(pady=(30, 5))

ctk.CTkLabel(janela,
             text='Descubra seu índice de massa corporal',
             text_color='#7a8394',
             font=('Arial', 14)).pack(pady=(0, 20))


# --- FRAME PRINCIPAL (Cartão Branco) ---
frame_inputs = ctk.CTkFrame(janela, fg_color='white', corner_radius=15, border_width=1, border_color='#e2e6ea')
frame_inputs.pack(pady=10, padx=30, fill='x')

ctk.CTkLabel(frame_inputs, 
             text='Peso (kg)', 
             text_color='#0c326f', 
             font=('Arial', 14, 'bold')).pack(anchor='w', padx=20, pady=(20, 5))

peso = ctk.CTkEntry(frame_inputs,
                    height=40,
                    placeholder_text='Ex: 70.5',
                    placeholder_text_color='#b0b6c4',
                    fg_color='white',
                    text_color='black',
                    border_width=1,
                    border_color='#ced4da')
peso.pack(fill='x', padx=20, pady=(0, 15))

ctk.CTkLabel(frame_inputs, 
             text='Altura (m)', 
             text_color='#0c326f', 
             font=('Arial', 14, 'bold')).pack(anchor='w', padx=20, pady=(5, 5))

altura = ctk.CTkEntry(frame_inputs,
                      height=40,
                      placeholder_text='Ex: 1.75',
                      placeholder_text_color='#b0b6c4',
                      fg_color='white',
                      text_color='black',
                      border_width=1,
                      border_color='#ced4da')
altura.pack(fill='x', padx=20, pady=(0, 25))

botao = ctk.CTkButton(frame_inputs,
                      text='Calcular IMC',
                      fg_color='#10419c',
                      hover_color='#0c326f',
                      text_color='white',
                      font=('Arial', 16, 'bold'),
                      height=45,
                      corner_radius=8,
                      command=calcular_imc)
botao.pack(fill='x', padx=20, pady=(0, 20))


# --- FRAME RESULTADO (Cartão Inferior) ---
frame_resultado = ctk.CTkFrame(janela, fg_color='#eef2fb', corner_radius=15, border_width=1, border_color='#dce4f2')
frame_resultado.pack(pady=10, padx=30, fill='x')

ctk.CTkLabel(frame_resultado, 
             text='Seu IMC', 
             text_color='#10419c', 
             font=('Arial', 14, 'bold')).pack(pady=(15, 0))

# Label do número do IMC
resultado_valor = ctk.CTkLabel(frame_resultado,
                               text='- -',
                               text_color='#10419c',
                               font=('Arial', 30, 'bold'))
resultado_valor.pack(pady=(0, 0))

# Nova Label para mostrar a situação (Magro, Normal, Obeso...)
resultado_situacao = ctk.CTkLabel(frame_resultado,
                                  text='',
                                  font=('Arial', 16, 'bold'))
resultado_situacao.pack(pady=(0, 15))

# Executa o App
janela.mainloop()