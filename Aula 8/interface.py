import customtkinter as ctk
from tkinter import messagebox 
ctk.set_appearance_mode('dark')

# funções

def viagem ():
    try:
        d = int (km.get())
        c = int (consumo.get())
        p = float (preco.get())
            
            #realizar o calculo
            
        valor_final = (d/c)*p
            
        resultado.configure(text=f'O valor final é R$ {valor_final:.2f}')    
    except :
        messagebox.showerror('ERRO', 'Por favor, preencha todos os campos corretamente!')
            
    
        

           
janela = ctk.CTk()
janela.geometry('650x400')
janela.title('App Viagem')

ctk.CTkLabel(janela,
             text='APP VIAGEM',
             text_color='white',
             font=('Roboto', 34)).pack(pady=20)

km = ctk.CTkEntry(janela,
                     width=350,
                     height=35,
                     placeholder_text='Digite a distância da viagem (km)',
                     border_width=1,
                     border_color='white',
                     )
km.pack(pady=10)

consumo = ctk.CTkEntry(janela,
                     width=350,
                     height=35,
                     placeholder_text='Digite o consumo do seu veículo',
                     border_width=1,
                     border_color='white',
                     )
consumo.pack(pady=10)

preco = ctk.CTkEntry(janela,
                     width=350,
                     height=35,
                     placeholder_text='Digite o preço atual do combustível',
                     border_width=1,
                     border_color='white',
                     )
preco.pack(pady=10)


botao = ctk.CTkButton(janela,
                      text='Calcular gasto',
                      fg_color='white',
                      text_color='black',
                      width=150,
                      height=35,
                      command=viagem)

botao.pack(pady=35)


resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('Verdana0', 30),
                         text_color='yellow')
resultado.pack(pady=10)
janela.mainloop()