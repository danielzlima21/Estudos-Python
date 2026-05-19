import customtkinter as ctk

ctk.set_appearance_mode('dark')

def mudar():
    label_aluno_nome.configure(text='Mudou')

def salvar_aluno():
    nome = campo_aluno_nome.get()
    try:
        nota1 = float(campo_aluno_nota1.get())
        nota2 = float(campo_aluno_nota2.get())

        if nota1 < 0 or nota2 < 0:
            resultado_salvar_aluno.configure(text='Nota não pode ser menor que zero', text_color='red')
        else:
            resultado_salvar_aluno.configure(text=f'{nome} adicionado ao banco de alunos', text_color='green')
    except ValueError:
        resultado_salvar_aluno.configure(text='Digite apenas números', text_color='red')

app = ctk.CTk()
app.title('Banco de Alunos')
app.geometry('500x500')

label_aluno_nome = ctk.CTkLabel(app, text='Nome do aluno', font=('Arial', 20))
label_aluno_nome.pack(pady=10)
campo_aluno_nome = ctk.CTkEntry(app, placeholder_text='Digite:')
campo_aluno_nome.pack(pady=10)

label_aluno_nota1 = ctk.CTkLabel(app, text='Nota 1')
label_aluno_nota1.pack(pady=10)
campo_aluno_nota1 = ctk.CTkEntry(app, placeholder_text='Digite:')
campo_aluno_nota1.pack(pady=10)

label_aluno_nota2 = ctk.CTkLabel(app, text='Nota 2')
label_aluno_nota2.pack(pady=10)
campo_aluno_nota2 = ctk.CTkEntry(app, placeholder_text='Digite:')
campo_aluno_nota2.pack(pady=10)

botao_salvar_aluno = ctk.CTkButton(app, text='Salvar aluno', command=salvar_aluno, hover_color='green', corner_radius=10)
botao_salvar_aluno.pack(pady=10)

botao_titulo = ctk.CTkButton(app, text='mudar titulo', command=mudar)
botao_titulo.pack(pady=10)

resultado_salvar_aluno = ctk.CTkLabel(app, text='')
resultado_salvar_aluno.pack(pady=10)


app.mainloop()
