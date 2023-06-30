import schedule
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def jobJarvis():
    execJarvis()

def execJarvis():
    import webbrowser
    url="link do Site onte você bate ponto"

    bateuPonto = outra_funcao()
    print(bateuPonto)
    if bateuPonto == 'Sim':
        webbrowser.open(url)

def exibir_popup():
    popup = tk.Tk()
    popup.geometry('300x50')
    popup.title("Olá! Eu me chamo Jarvis")

    def clicar_sim():
        resposta.set("Sim")
        popup.destroy()

    def clicar_nao():
        resposta.set("Não")
        popup.destroy()

    pergunta_label = tk.Label(popup, text="Você quer bater seu ponto agora?")
    pergunta_label.pack()

    sim_button = tk.Button(popup, text="Sim Bater Ponto", command=clicar_sim)
    sim_button.pack(side=tk.LEFT)

    nao_button = tk.Button(popup, text="Não, vou bater depois", command=clicar_nao)
    nao_button.pack(side=tk.RIGHT)

    resposta = tk.StringVar()

    popup.mainloop()

    return resposta.get()

def outra_funcao():
    resultado = exibir_popup()
    return resultado

schedule.every().day.at("09:00").do(jobJarvis)
schedule.every().day.at("12:00").do(jobJarvis)
schedule.every().day.at("13:00").do(jobJarvis)
schedule.every().day.at("18:00").do(jobJarvis)

while True:
    schedule.run_pending()
    time.sleep(1)






