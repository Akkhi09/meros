import requests, customtkinter

class My_app():
    def __init__(self):
        self.root = customtkinter.CTk()
    def base_config_root(self):
        self.root.geometry("500x480")
        self.root.title("cambiador de notas")
        self.root.iconbitmap("./assets/icon.ico")
        self.root.resizable(False, False)
        self.root.config(bg="#ffffff")
    def formulario(self, frame):
        #rotulo para o formulario
        self.label= customtkinter.CTkLabel(frame, text="Digite a moeda base e a de destino", text_color="#008F7A", font=("Arial", 18, "bold"), anchor="center")
        #primeiro input moeda base
        self.input1 = customtkinter.CTkEntry(frame, placeholder_text="exemplo: USD", width= 200, height= 30, font=("Arial", 14), text_color="#bebbbb", fg_color="#ffffff", border_color="#bebbbb", border_width=2)
        #segundo input moeda destino
        self.input2 = customtkinter.CTkEntry(frame, placeholder_text="exemplo: AOA", width= 200, height= 30, font=("Arial", 14), text_color="#bebbbb", fg_color="#ffffff", border_color="#bebbbb", border_width=2)
        #butão para obter a cotação
        self.button = customtkinter.CTkButton(frame,text="obter cotação", width= 200, height= 30, font=("Arial", 14), text_color="#008F7A", fg_color="#bebbbb", border_color="#008F7A", border_width=2, hover_color="#363535")
        
        self.frame_= customtkinter.CTkFrame(frame, width=100, height=200, corner_radius=5, fg_color="#363535",  border_color="#bebbbb", border_width=2)
        
        self.label.pack(pady=10)
        self.input1.pack(pady=10)
        self.input2.pack(pady=10)
        self.button.pack(pady=10)
        self.frame_.pack(pady=10, padx=10, fill="both", expand=True)
        
    def frame_for_exibition(self):
        self.frame = customtkinter.CTkFrame(self.root, width= 640, height= 480, corner_radius= 0)
        self.frame.pack_propagate(False)
        self.frame.pack(fill="both", expand=True)
        self.label = customtkinter.CTkLabel(self.frame, text="Bem vindo ao cotador do Akkhi", text_color="#bebbbb", font=("Arial", 20, "bold"), anchor="center")   
        ##chamando o formularios
        self.formulario(self.frame)
        self.label.pack()
    
        
    def initial(self):
        self.base_config_root()
        self.frame_for_exibition()
        self.root.mainloop()
        
class Cotacao():
    def __init__(self, moeda_base, moeda_destino):
        self.moeda_base = moeda_base
        self.moeda_destino = moeda_destino
        self.url= f"https://economia.awesomeapi.com.br/json/last/{self.moeda_base}-{self.moeda_destino}"
    def obter_cotacao(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            self.data = resposta.json()
            self.par = self.moeda_base + self.moeda_destino
        self.valor = self.data[self.par]['bid']
        print(self.valor)
# catador = Cotacao("USD", "AOA")
# catador.obter_cotacao()
if __name__== "__main__":
    app = My_app()
    app.initial()