import customtkinter as ctk

# Configuração inicial do tema e modo de aparência
ctk.set_appearance_mode("dark")

class ComandaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Comanda Digital de Restaurante")
        self.geometry("450x550")
        self.resizable(False, False)

        # Cores de Destaque
        self.COR_LARANJA = "#ff7f00"
        self.COR_LARANJA_HOVER = "#e06600"
        self.COR_VERDE = "#22c55e"
        self.COR_BORDA = "#4b5563"

        # ----------------------------------------------------
        # CABEÇALHO (ÍCONE E TÍTULO)
        # ----------------------------------------------------
        self.lbl_icone = ctk.CTkLabel(
            self, 
            text="🍽️", 
            font=ctk.CTkFont(size=40)
        )
        self.lbl_icone.pack(pady=(15, 0))

        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text="Comanda Digital de Restaurante", 
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.COR_LARANJA
        )
        self.lbl_titulo.pack(pady=(0, 15))

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

        # Título do Frame
        self.lbl_dados_titulo = ctk.CTkLabel(
            self.frame_dados, 
            text="Dados da Conta", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.COR_LARANJA
        )
        self.lbl_dados_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

        # Campo: Valor Consumido
        self.lbl_valor = ctk.CTkLabel(self.frame_dados, text="Valor Consumido (R$):", font=ctk.CTkFont(size=13))
        self.lbl_valor.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 10))

        self.entry_valor = ctk.CTkEntry(
            self.frame_dados, 
            placeholder_text="Digite o valor consumido", 
            width=180,
            height=30
        )
        self.entry_valor.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 10))

        # Campo: Quantidade de Pessoas
        self.lbl_pessoas = ctk.CTkLabel(self.frame_dados, text="Quantidade de Pessoas:", font=ctk.CTkFont(size=13))
        self.lbl_pessoas.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 15))

        self.entry_pessoas = ctk.CTkEntry(
            self.frame_dados, 
            placeholder_text="Digite a quantidade de pessoas", 
            width=180,
            height=30
        )
        self.entry_pessoas.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 15))

        # Configura o peso das colunas para alinhar perfeitamente à esquerda e direita
        self.frame_dados.grid_columnconfigure(0, weight=1)

        # ----------------------------------------------------
        # BOTÃO: FECHAR CONTA
        # ----------------------------------------------------
        self.btn_fechar = ctk.CTkButton(
            self, 
            text="🧾 FECHAR CONTA", 
            font=ctk.CTkFont(size=15, weight="bold"), 
            height=40,
            fg_color=self.COR_LARANJA,
            hover_color=self.COR_LARANJA_HOVER,
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

        # Título do Frame de Resumo
        self.lbl_resumo_titulo = ctk.CTkLabel(
            self.frame_resumo, 
            text="Resumo da Conta", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.COR_VERDE
        )
        self.lbl_resumo_titulo.grid(row=0, column=0, sticky="w", padx=15, pady=(10, 10))

        # Linha: Taxa de Serviço
        self.lbl_taxa_txt = ctk.CTkLabel(self.frame_resumo, text="Taxa de Serviço (10%):", font=ctk.CTkFont(size=13))
        self.lbl_taxa_txt.grid(row=1, column=0, sticky="w", padx=15, pady=(0, 5))

        self.lbl_taxa_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_taxa_val.grid(row=1, column=1, sticky="e", padx=15, pady=(0, 5))

        # Linha: Valor Total
        self.lbl_total_txt = ctk.CTkLabel(self.frame_resumo, text="Valor Total:", font=ctk.CTkFont(size=13))
        self.lbl_total_txt.grid(row=2, column=0, sticky="w", padx=15, pady=(0, 10))

        self.lbl_total_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=14, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_total_val.grid(row=2, column=1, sticky="e", padx=15, pady=(0, 10))

        # Linha Divisória (Separador visual)
        self.linha_divisoria = ctk.CTkFrame(self.frame_resumo, height=1, fg_color=self.COR_BORDA)
        self.linha_divisoria.grid(row=3, column=0, columnspan=2, sticky="ew", padx=15, pady=(5, 10))

        # Linha: Valor Individual (Destaque Final)
        self.lbl_indiv_txt = ctk.CTkLabel(self.frame_resumo, text="Valor Individual (por pessoa):", font=ctk.CTkFont(size=13))
        self.lbl_indiv_txt.grid(row=4, column=0, sticky="w", padx=15, pady=(0, 10))

        self.lbl_indiv_val = ctk.CTkLabel(
            self.frame_resumo, text="R$ 0,00", font=ctk.CTkFont(size=22, weight="bold"), text_color=self.COR_VERDE
        )
        self.lbl_indiv_val.grid(row=4, column=1, sticky="e", padx=15, pady=(0, 10))

        # Rodapé do Frame
        self.lbl_rodape = ctk.CTkLabel(
            self.frame_resumo, 
            text="* Valores calculados automaticamente", 
            font=ctk.CTkFont(size=11), 
            text_color=self.COR_LARANJA
        )
        self.lbl_rodape.grid(row=5, column=0, columnspan=2, pady=(5, 10))

        self.frame_resumo.grid_columnconfigure(0, weight=1)

    # ----------------------------------------------------
    # LÓGICA DE CÁLCULO E VALIDAÇÃO
    # ----------------------------------------------------
    def formatar_moeda(self, valor):
        """Formata um float para o padrão de moeda do Brasil (R$ X.XXX,XX)."""
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def calcular_comanda(self):
        try:
            # Captura e formatação dos dados de entrada
            val_str = self.entry_valor.get().strip().replace(".", "").replace(",", ".")
            valor_consumido = float(val_str)

            qtd_pessoas = int(self.entry_pessoas.get().strip())

            # Validações básicas de negócio
            if valor_consumido < 0:
                raise ValueError("O valor consumido não pode ser negativo.")
            if qtd_pessoas <= 0:
                raise ZeroDivisionError("A quantidade de pessoas deve ser maior que zero.")

            # Processamento dos cálculos
            taxa_servico = valor_consumido * 0.10
            valor_total = valor_consumido + taxa_servico
            valor_individual = valor_total / qtd_pessoas

            # Atualização da interface com os valores calculados
            self.lbl_taxa_val.configure(text=self.formatar_moeda(taxa_servico), text_color=self.COR_VERDE)
            self.lbl_total_val.configure(text=self.formatar_moeda(valor_total), text_color=self.COR_VERDE)
            self.lbl_indiv_val.configure(text=self.formatar_moeda(valor_individual), text_color=self.COR_VERDE)
            self.lbl_rodape.configure(text="* Valores calculados automaticamente", text_color=self.COR_LARANJA)

        except (ValueError, ZeroDivisionError):
            # Em caso de erro (texto no lugar de número, ou 0 pessoas), exibe alerta visual
            msg_erro = "Erro: Verifique os valores inseridos!"
            self.lbl_taxa_val.configure(text="---", text_color="#ef4444")
            self.lbl_total_val.configure(text="---", text_color="#ef4444")
            self.lbl_indiv_val.configure(text="R$ Erro", text_color="#ef4444")
            self.lbl_rodape.configure(text=msg_erro, text_color="#ef4444")


if __name__ == "__main__":
    app = ComandaApp()
    app.mainloop()