import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x300")

saldo = 1000000

simbolos = ["🍒", "💎", "🐬", "⭐", "🍀"]

label_saldo = ctk.CTkLabel(app, text=f"Saldo: {saldo}$", font=("Arial", 20))
label_saldo.pack(pady=10)

frame_slots = ctk.CTkFrame(app)
frame_slots.pack(pady=20)

slot1 = ctk.CTkLabel(frame_slots, text="❓", font=("Arial", 40))
slot1.grid(row=0, column=0, padx=10)

slot2 = ctk.CTkLabel(frame_slots, text="❓", font=("Arial", 40))
slot2.grid(row=0, column=1, padx=10)

slot3 = ctk.CTkLabel(frame_slots, text="❓", font=("Arial", 40))
slot3.grid(row=0, column=2, padx=10)

resultado_label = ctk.CTkLabel(app, text="", font=("Arial", 18))
resultado_label.pack(pady=10)


def girar():

    global saldo

    aposta = 10

    if saldo < aposta:
        resultado_label.configure(text="Saldo insuficiente", text_color="red")
        return

    saldo -= aposta

    r1 = random.choice(simbolos)
    r2 = random.choice(simbolos)
    r3 = random.choice(simbolos)

    slot1.configure(text=r1)
    slot2.configure(text=r2)
    slot3.configure(text=r3)

    if r1 == r2 == r3:
        ganho = 100
        saldo += ganho
        resultado_label.configure(
            text=f"JACKPOT +{ganho}$",
            text_color="green"
        )
    else:
        resultado_label.configure(
            text="Você perdeu",
            text_color="red"
        )

    label_saldo.configure(text=f"Saldo: {saldo}$")


botao = ctk.CTkButton(
    app,
    text="GIRAR",
    command=girar,
    height=50,
    font=("Arial", 20)
)

botao.pack(pady=20)

app.mainloop()