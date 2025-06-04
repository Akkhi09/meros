import requests, customtkinter

class Cotacao():
    def __init__(self, moeda_base, moeda_destino):
        self.moeda_base = moeda_base
        self.moeda_destino = moeda_destino
        self.url = f"https://economia.awesomeapi.com.br/json/last/{self.moeda_base}-{self.moeda_destino}"

    def obter_cotacao(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            data = resposta.json()
            par = self.moeda_base + self.moeda_destino
            valor = data[par]['bid']
            return valor
        else:
            raise Exception("Falha ao obter dados da API")

class My_app():
    def __init__(self):
        self.root = customtkinter.CTk()

    def base_config_root(self):
        self.root.geometry("360x420")
        self.root.title("cambiador de notas")
        self.root.iconbitmap("./assets/icon.ico")
        self.root.resizable(False, False)
        self.root.config(bg="#ffffff")

    def formulario(self, frame):
        self.label = customtkinter.CTkLabel(frame, text="Digite a moeda base e a de destino", text_color="#008F7A", font=("Arial", 18, "bold"), anchor="center")
        self.input1 = customtkinter.CTkEntry(frame, placeholder_text="exemplo: USD", width=200, height=30, font=("Arial", 14), text_color="#bebbbb", fg_color="#ffffff", border_color="#bebbbb", border_width=2)
        self.input2 = customtkinter.CTkEntry(frame, placeholder_text="exemplo: AOA", width=200, height=30, font=("Arial", 14), text_color="#bebbbb", fg_color="#ffffff", border_color="#bebbbb", border_width=2)
        self.button = customtkinter.CTkButton(
            frame, text="obter cotação", width=200, height=30,
            font=("Arial", 14), text_color="#008F7A",
            fg_color="#bebbbb", border_color="#008F7A", border_width=2,
            hover_color="#363535", command=self.buscar_cotacao  # Integração aqui!
        )
        self.frame_ = customtkinter.CTkFrame(frame, width=100, height=200, corner_radius=5, fg_color="#363535", border_color="#008F7A", border_width=2)
        self.resultado = customtkinter.CTkLabel(self.frame_, text="", text_color="#bebbbb", font=("Arial", 14), anchor="center")

        self.label.pack(pady=10)
        self.input1.pack(pady=10)
        self.input2.pack(pady=10)
        self.button.pack(pady=10)
        self.frame_.pack(pady=10, padx=10, fill="both", expand=True)
        self.resultado.pack(pady=10, padx=10, fill="both", expand=True)

    def buscar_cotacao(self):
        moeda_base = self.input1.get().upper()
        moeda_destino = self.input2.get().upper()

        if not moeda_base or not moeda_destino:
            self.resultado.configure(text="Por favor, preencha ambos os campos.")
            return

        try:
            cotacao = Cotacao(moeda_base, moeda_destino)
            valor = cotacao.obter_cotacao()
            self.resultado.configure(text=f"1 {moeda_base} = {valor} {moeda_destino}")
            self.input1.delete(0, 'end')
            self.input2.delete(0, 'end')
        except Exception as e:
            self.resultado.configure(text=f"Erro ao obter cotação:\n{e}")

    def frame_for_exibition(self):
        self.frame = customtkinter.CTkFrame(self.root, width=640, height=480, corner_radius=0)
        self.frame.pack_propagate(False)
        self.frame.pack(fill="both", expand=True)
        self.label = customtkinter.CTkLabel(self.frame, text="Bem vindo ao dolar para tudo!", text_color="#bebbbb", font=("Arial", 20, "bold"), anchor="center")
        self.label.pack()
        self.formulario(self.frame)

    def initial(self):
        self.base_config_root()
        self.frame_for_exibition()
        self.root.mainloop()
# Executando o app
if __name__ == "__main__":
    app = My_app()
    app.initial()
