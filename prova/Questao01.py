import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cálculo de Imposto de Renda")
app.geometry("400x460")
app.resizable(False, False)

def calcular_imposto():
    try:
        salario_str = entry_salario.get().strip().replace(".", "").replace(",", ".")
        salario_bruto = float(salario_str)

        if salario_bruto <= 2112.00:
            taxa_desconto = 0.0
        elif salario_bruto <= 2826.65:
            taxa_desconto = 0.075
        else:
            taxa_desconto = 0.15

        salario_liquido = salario_bruto * (1 - taxa_desconto)

        resultado_formatado = f"R$ {salario_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        lbl_resultado.configure(text=resultado_formatado, text_color="#22c55e")

    except ValueError:
        lbl_resultado.configure(text="Valor Inválido", text_color="#ef4444")

lbl_title = ctk.CTkLabel(
    app, 
    text="Cálculo de Imposto de Renda", 
    font=ctk.CTkFont(size=20, weight="bold")
)
lbl_title.pack(pady=(20, 0))

frame_inputs = ctk.CTkFrame(app, fg_color="transparent")
frame_inputs.pack(padx=20, fill="x")

lbl_nome = ctk.CTkLabel(
    frame_inputs, 
    text="Nome do Funcionário:", 
    font=ctk.CTkFont(size=14)
)
lbl_nome.pack(anchor="w")

entry_nome = ctk.CTkEntry(
    frame_inputs, 
    placeholder_text="Digite o nome do funcionário", 
    height=35
)
entry_nome.pack(fill="x", pady=(0, 15))

lbl_salario = ctk.CTkLabel(
    frame_inputs, 
    text="Salário Bruto (R$):", 
    font=ctk.CTkFont(size=14)
)
lbl_salario.pack(anchor="w")

entry_salario = ctk.CTkEntry(
    frame_inputs, 
    placeholder_text="Digite o salário bruto", 
    height=35
)
entry_salario.pack(fill="x", pady=(0, 20))

btn_calcular = ctk.CTkButton(
    app, 
    text="CALCULAR IMPOSTO", 
    font=ctk.CTkFont(size=14, weight="bold"), 
    height=40, 
    command=calcular_imposto
)
btn_calcular.pack(padx=20, fill="x", pady=(0, 20))

frame_resultado = ctk.CTkFrame(app, corner_radius=8)
frame_resultado.pack(padx=20, fill="x", pady=(0, 20))

lbl_res_titulo = ctk.CTkLabel(
    frame_resultado, 
    text="Salário Líquido:", 
    font=ctk.CTkFont(size=16)
)
lbl_res_titulo.pack(pady=(15, 5))

lbl_resultado = ctk.CTkLabel(
    frame_resultado, 
    text="R$ 0,00", 
    font=ctk.CTkFont(size=28, weight="bold"), 
    text_color="#22c55e"
)
lbl_resultado.pack(pady=(0, 15))

if __name__ == "__main__":
    app.mainloop()