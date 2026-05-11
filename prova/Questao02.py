import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Comanda Digital de Restaurante")
app.geometry("450x500") 
app.resizable(False, False)

COR_ROXO = "#912bbc"        
COR_ROXO_HOVER = "#702094"  
COR_VERDE = "#22c55e"       
COR_BORDA = "#4b5563"

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def calcular_comanda():
    try:
        val_str = entry_valor.get().strip().replace(".", "").replace(",", ".")
        valor_consumido = float(val_str)
        qtd_pessoas = int(entry_pessoas.get().strip())

        if valor_consumido < 0:
            raise ValueError
        if qtd_pessoas <= 0:
            raise ZeroDivisionError

        taxa_servico = valor_consumido * 0.10
        valor_total = valor_consumido + taxa_servico
        valor_individual = valor_total / qtd_pessoas

        lbl_taxa_val.configure(text=formatar_moeda(taxa_servico))
        lbl_total_val.configure(text=formatar_moeda(valor_total))
        lbl_indiv_val.configure(text=formatar_moeda(valor_individual), text_color=COR_VERDE)
        lbl_rodape.configure(text="* Valores calculados automaticamente", text_color=COR_ROXO)

    except:
        lbl_indiv_val.configure(text="Erro", text_color="#ef4444")
        lbl_rodape.configure(text="Verifique os valores inseridos!", text_color="#ef4444")

lbl_titulo = ctk.CTkLabel(
    app, 
    text="Comanda Digital de Restaurante", 
    font=ctk.CTkFont(size=22, weight="bold"),
    text_color=COR_ROXO
)
lbl_titulo.pack(pady=(25, 20))

frame_dados = ctk.CTkFrame(
    app, 
    corner_radius=8, 
    border_width=1, 
    border_color=COR_BORDA
)
frame_dados.pack(padx=20, fill="x", pady=(0, 15))

lbl_dados_titulo = ctk.CTkLabel(
    frame_dados, 
    text="Dados da Conta", 
    font=ctk.CTkFont(size=14, weight="bold"),
    text_color=COR_ROXO
)
lbl_dados_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

lbl_valor = ctk.CTkLabel(frame_dados, text="Valor Consumido (R$):", font=ctk.CTkFont(size=13))
lbl_valor.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 10))

entry_valor = ctk.CTkEntry(
    frame_dados, 
    placeholder_text="Digite o valor consumido", 
    width=180,
    height=30
)
entry_valor.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 10))

lbl_pessoas = ctk.CTkLabel(frame_dados, text="Quantidade de Pessoas:", font=ctk.CTkFont(size=13))
lbl_pessoas.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

entry_pessoas = ctk.CTkEntry(
    frame_dados, 
    placeholder_text="Digite a quantidade de pessoas", 
    width=180,
    height=30
)
entry_pessoas.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 15))

frame_dados.grid_columnconfigure(0, weight=1)

btn_fechar = ctk.CTkButton(
    app, 
    text="FECHAR CONTA", 
    font=ctk.CTkFont(size=15, weight="bold"), 
    height=40,
    fg_color=COR_ROXO,
    hover_color=COR_ROXO_HOVER,
    text_color="white",
    command=calcular_comanda
)
btn_fechar.pack(padx=20, fill="x", pady=(0, 15))

frame_resumo = ctk.CTkFrame(
    app, 
    corner_radius=8, 
    border_width=1, 
    border_color=COR_BORDA
)
frame_resumo.pack(padx=20, fill="x", pady=(0, 10))

lbl_resumo_titulo = ctk.CTkLabel(
    frame_resumo, 
    text="Resumo da Conta", 
    font=ctk.CTkFont(size=14, weight="bold"),
    text_color=COR_VERDE
)
lbl_resumo_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

lbl_taxa_txt = ctk.CTkLabel(frame_resumo, text="Taxa de Serviço (10%):", font=ctk.CTkFont(size=13))
lbl_taxa_txt.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 5))

lbl_taxa_val = ctk.CTkLabel(
    frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=COR_VERDE
)
lbl_taxa_val.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 5))

lbl_total_txt = ctk.CTkLabel(frame_resumo, text="Valor Total:", font=ctk.CTkFont(size=13))
lbl_total_txt.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 10))

lbl_total_val = ctk.CTkLabel(
    frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=COR_VERDE
)
lbl_total_val.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 10))

linha_divisoria = ctk.CTkFrame(frame_resumo, height=1, fg_color=COR_BORDA)
linha_divisoria.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=(5, 10))

lbl_indiv_txt = ctk.CTkLabel(frame_resumo, text="Valor Individual (por pessoa):", font=ctk.CTkFont(size=13))
lbl_indiv_txt.grid(row=4, column=0, sticky="w", padx=15, pady=(0, 10))

lbl_indiv_val = ctk.CTkLabel(
    frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=22, weight="bold"), text_color=COR_VERDE
)
lbl_indiv_val.grid(row=4, column=1, sticky="e", padx=15, pady=(0, 10))

lbl_rodape = ctk.CTkLabel(
    frame_resumo, 
    text="* Valores calculados automaticamente", 
    font=ctk.CTkFont(size=11), 
    text_color=COR_ROXO
)
lbl_rodape.grid(row=5, column=0, columnspan=2, pady=(5, 10))

frame_resumo.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    app.mainloop()