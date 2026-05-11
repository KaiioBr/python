import customtkinter as ctk

# Configuração inicial do tema e modo de aparência
ctk.set_appearance_mode("dark")

class ComandaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Comanda Digital de Restaurante")
        self.geometry("450x500") # Altura reduzida pois removemos o ícone
        self.resizable(False, False)

        # Paleta de Cores (Roxo)
        self.COR_ROXO = "#912bbc"        
        self.COR_ROXO_HOVER = "#702094"  
        self.COR_VERDE = "#22c55e"       
        self.COR_BORDA = "#4b5563"

        # ----------------------------------------------------
        # CABEÇALHO (APENAS TÍTULO)
        # ----------------------------------------------------
        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text="Comanda Digital de Restaurante", 
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=self.COR_ROXO
        )
        self.lbl_titulo.pack(pady=(25, 20)) # Aumentado o espaçamento superior (pady)

        # ----------------------------------------------------
        # FRAME 1: DADOS DA CONTA (ENTRADAS)
        # ----------------------------------------------------
        self.frame_dados = ctk.CTkFrame(
            self, 
            corner_radius=8, 
            border_width=1, 
            border_color=self.COR_BORDA
        )
        self.frame_dados.pack(padx=20, fill="x", pady=(0, 15))

        self.lbl_dados_titulo = ctk.CTkLabel(
            self.frame_dados, 
            text="Dados da Conta", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.COR_ROXO
        )
        self.lbl_dados_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

        self.lbl_valor = ctk.CTkLabel(self.frame_dados, text="Valor Consumido (R$):", font=ctk.CTkFont(size=13))
        self.lbl_valor.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 10))

        self.entry_valor = ctk.CTkEntry(
            self.frame_dados, 
            placeholder_text="Digite o valor consumido", 
            width=180,
            height=30
        )
        self.entry_valor.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 10))

        self.lbl_pessoas = ctk.CTkLabel(self.frame_dados, text="Quantidade de Pessoas:", font=ctk.CTkFont(size=13))
        self.lbl_pessoas.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

        self.entry_pessoas = ctk.CTkEntry(
            self.frame_dados, 
            placeholder_text="Digite a quantidade de pessoas", 
            width=180,
            height=30
        )
        self.entry_pessoas.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 15))

        self.frame_dados.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------
        # BOTÃO: FECHAR CONTA
        # ----------------------------------------------------
        self.btn_fechar = ctk.CTkButton(
            self, 
            text="FECHAR CONTA", 
            font=ctk.CTkFont(size=15, weight="bold"), 
            height=40,
            fg_color=self.COR_ROXO,
            hover_color=self.COR_ROXO_HOVER,
            text_color="white",
            command=self.calcular_comanda
        )
        self.btn_fechar.pack(padx=20, fill="x", pady=(0, 15))

        # ----------------------------------------------------
        # FRAME 2: RESUMO DA CONTA (SAÍDAS)
        # ----------------------------------------------------
        self.frame_resumo = ctk.CTkFrame(
            self, 
            corner_radius=8, 
            border_width=1, 
            border_color=self.COR_BORDA
        )
        self.frame_resumo.pack(padx=20, fill="x", pady=(0, 10))

        self.lbl_resumo_titulo = ctk.CTkLabel(
            self.frame_resumo, 
            text="Resumo da Conta", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.COR_VERDE
        )
        self.lbl_resumo_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

        self.lbl_taxa_txt = ctk.CTkLabel(self.frame_resumo, text="Taxa de Serviço (10%):", font=ctk.CTkFont(size=13))
        self.lbl_taxa_txt.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 5))

        self.lbl_taxa_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_taxa_val.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 5))

        self.lbl_total_txt = ctk.CTkLabel(self.frame_resumo, text="Valor Total:", font=ctk.CTkFont(size=13))
        self.lbl_total_txt.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 10))

        self.lbl_total_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_total_val.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 10))

        self.linha_divisoria = ctk.CTkFrame(self.frame_resumo, height=1, fg_color=self.COR_BORDA)
        self.linha_divisoria.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=(5, 10))

        self.lbl_indiv_txt = ctk.CTkLabel(self.frame_resumo, text="Valor Individual (por pessoa):", font=ctk.CTkFont(size=13))
        self.lbl_indiv_txt.grid(row=4, column=0, sticky="w", padx=15, pady=(0, 10))

        self.lbl_indiv_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=22, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_indiv_val.grid(row=4, column=1, sticky="e", padx=15, pady=(0, 10))

        self.lbl_rodape = ctk.CTkLabel(
            self.frame_resumo, 
            text="* Valores calculados automaticamente", 
            font=ctk.CTkFont(size=11), 
            text_color=self.COR_ROXO
        )
        self.lbl_rodape.grid(row=5, column=0, columnspan=2, pady=(5, 10))

        self.frame_resumo.grid_columnconfigure(0, weight=1)

    def formatar_moeda(self, valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def calcular_comanda(self):
        try:
            val_str = self.entry_valor.get().strip().replace(".", "").replace(",", ".")
            valor_consumido = float(val_str)
            qtd_pessoas = int(self.entry_pessoas.get().strip())

            if valor_consumido < 0:
                raise ValueError
            if qtd_pessoas <= 0:
                raise ZeroDivisionError

            taxa_servico = valor_consumido * 0.10
            valor_total = valor_consumido + taxa_servico
            valor_individual = valor_total / qtd_pessoas

            self.lbl_taxa_val.configure(text=self.formatar_moeda(taxa_servico))
            self.lbl_total_val.configure(text=self.formatar_moeda(valor_total))
            self.lbl_indiv_val.configure(text=self.formatar_moeda(valor_individual))
            self.lbl_rodape.configure(text="* Valores calculados automaticamente", text_color=self.COR_ROXO)

        except:
            self.lbl_indiv_val.configure(text="Erro", text_color="#ef4444")
            self.lbl_rodape.configure(text="Verifique os valores inseridos!", text_color="#ef4444")

if __name__ == "__main__":
    app = ComandaApp()
    app.mainloop()