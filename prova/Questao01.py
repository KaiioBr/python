import customtkinter as ctk

# Configuração inicial do tema e modo de aparência
ctk.set_appearance_mode("dark")  # Modo escuro conforme a imagem
ctk.set_default_color_theme("blue")  # Tema azul para os botões e detalhes

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Cálculo de Imposto de REnda")
        self.geometry("400x460")
        self.resizable(False, False)

        # ----------------------------------------------------
        # TÍTULO PRINCIPAL E SUBTÍTULO
        # ----------------------------------------------------
        self.lbl_title = ctk.CTkLabel(
            self, 
            text="Cálculo de Imposto de REnda", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.lbl_title.pack(pady=(20, 0))

        # ----------------------------------------------------
        # CAMPOS DE ENTRADA (FORMULÁRIO)
        # ----------------------------------------------------
        self.frame_inputs = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_inputs.pack(padx=20, fill="x")

        # Campo: Nome do Funcionário
        self.lbl_nome = ctk.CTkLabel(
            self.frame_inputs, 
            text="Nome do Funcionário:", 
            font=ctk.CTkFont(size=14)
        )
        self.lbl_nome.pack(anchor="w")

        self.entry_nome = ctk.CTkEntry(
            self.frame_inputs, 
            placeholder_text="Digite o nome do funcionário", 
            height=35
        )
        self.entry_nome.pack(fill="x", pady=(0, 15))

        # Campo: Salário Bruto
        self.lbl_salario = ctk.CTkLabel(
            self.frame_inputs, 
            text="Salário Bruto (R$):", 
            font=ctk.CTkFont(size=14)
        )
        self.lbl_salario.pack(anchor="w")

        self.entry_salario = ctk.CTkEntry(
            self.frame_inputs, 
            placeholder_text="Digite o salário bruto", 
            height=35
        )
        self.entry_salario.pack(fill="x", pady=(0, 20))

        # ----------------------------------------------------
        # BOTÃO DE CÁLCULO
        # ----------------------------------------------------
        self.btn_calcular = ctk.CTkButton(
            self, 
            text="CALCULAR IMPOSTO", 
            font=ctk.CTkFont(size=14, weight="bold"), 
            height=40, 
            command=self.calcular_imposto
        )
        self.btn_calcular.pack(padx=20, fill="x", pady=(0, 20))

        # ----------------------------------------------------
        # PAINEL DE RESULTADO (SALÁRIO LÍQUIDO)
        # ----------------------------------------------------
        self.frame_resultado = ctk.CTkFrame(self, corner_radius=8)
        self.frame_resultado.pack(padx=20, fill="x", pady=(0, 20))

        self.lbl_res_titulo = ctk.CTkLabel(
            self.frame_resultado, 
            text="Salário Líquido:", 
            font=ctk.CTkFont(size=16)
        )
        self.lbl_res_titulo.pack(pady=(15, 5))

        self.lbl_resultado = ctk.CTkLabel(
            self.frame_resultado, 
            text="R$ 0,00", 
            font=ctk.CTkFont(size=28, weight="bold"), 
            text_color="#22c55e"  # Verde destacado
        )
        self.lbl_resultado.pack(pady=(0, 15))

    # ----------------------------------------------------
    # LÓGICA DE CÁLCULO
    # ----------------------------------------------------
    def calcular_imposto(self):
        try:
            # Obtém o valor digitado e faz tratamentos (ex: troca vírgula por ponto)
            salario_str = self.entry_salario.get().strip().replace(".", "").replace(",", ".")
            salario_bruto = float(salario_str)

            # Aplicação das regras de desconto
            if salario_bruto <= 2112.00:
                taxa_desconto = 0.0  # Isento
            elif salario_bruto <= 2826.65:
                taxa_desconto = 0.075  # 7,5%
            else:
                taxa_desconto = 0.15  # 15%

            # Cálculo do salário líquido
            salario_liquido = salario_bruto * (1 - taxa_desconto)

            # Formatação no formato da moeda brasileira (R$ X.XXX,XX)
            resultado_formatado = f"R$ {salario_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            
            # Atualiza o label com o valor calculado e garante a cor verde
            self.lbl_resultado.configure(text=resultado_formatado, text_color="#22c55e")

        except ValueError:
            # Tratamento caso o usuário digite letras ou caracteres inválidos
            self.lbl_resultado.configure(text="Valor Inválido", text_color="#ef4444")


if __name__ == "__main__":
    app = App()
    app.mainloop()