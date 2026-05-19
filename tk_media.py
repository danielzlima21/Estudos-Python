import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Média Alunos')
app.geometry('300x300')

def ver_media():
    try:
        nome = campo_nome.get()
        nota1 = float(campo_nota1.get())
        nota2 = float(campo_nota2.get())
        nota = nota1 + nota2
        media = nota / 2
        if media >= 7:
            resultado_media.configure(text=f'{nome}, aprovado com média: {media}', text_color='green')
        else:
            resultado_media.configure(text=f'{nome}, reprovado com média: {media}', text_color='red')
    except ValueError:
        resultado_media.configure(text='Digite apenas números', text_color='red')

label_nome = ctk.CTkLabel(app, text='Nome')
label_nome.pack(pady=5)
campo_nome = ctk.CTkEntry(app, placeholder_text='Digite o nome')
campo_nome.pack(pady=5)

label_nota1 = ctk.CTkLabel(app, text='Nota 1')
label_nota1.pack(pady=5)
campo_nota1 = ctk.CTkEntry(app, placeholder_text='Digite a nota 1')
campo_nota1.pack(pady=5)

label_nota2 = ctk.CTkLabel(app, text='Nota 2')
label_nota2.pack(pady=5)
campo_nota2 = ctk.CTkEntry(app, placeholder_text='Digite a nota 2')
campo_nota2.pack(pady=5)

botao_media = ctk.CTkButton(app, text='Ver Média', command=ver_media)
botao_media.pack(pady=5)
resultado_media = ctk.CTkLabel(app, text='')
resultado_media.pack(pady=10)

app.mainloop()