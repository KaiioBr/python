import customtkinter as ctk
ctk.set_appearance_mode('dark')

# O erro estava aqui: removi as aspas de dentro de CTk()
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
                      height=35)

botao.pack(pady=35)

janela.mainloop()