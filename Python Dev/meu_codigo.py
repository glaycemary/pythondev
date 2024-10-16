# instalar o flet
# import flet

# Hashzap
# tela inicia 
    # título
    # botao de iniciar chat
        # quando clicar no botão
        # abrir um popup/modal/alerta para entrar no chat
            # título: bem vido ao hashzap  (Bem vindo ao Projetando)
            # Caixa de texto: escreva seu nome
            # botão entrar no chat
                # quando clicar no botão
                    # sumir com o título
                    # sumir com botão iniciar chat
                        # carregar o chat
                        # carregar o campo de enviar mensagem: "digite sua mensagem"
                        # carregar botão enviar
                            # quando clicar no botão enviar
                            # vai enviar a mensagem
                            # limpar a caixa de mensagem
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


# produto = {
#     "nome": "iphone",
#     "preço": 6500,
#     "quantidade": 150    
# }

# produto["quantidade"]


import flet as ft

# criar uma função principal para rodar o seu aplicativo
    # def nome_da_funcao(parametro):    o que a função vai fazer
def main(pagina):
    # titulo
    titulo = ft.Text("Projetando")
    
    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao Projetando")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup=ft.ElevatedButton("Entrar no chat")
    popup = ft.AlertDialog(title= titulo_popup, content= caixa_nome, actions= [botao_popup])

   


    # botao inial
    # sempre que o evento de click no botão ocorre um parametro de evento de click
    def abrir_popup(evento):
        # colocar popup na tela
        pagina.dialog = popup
        popup.open= True
        # atualizar a tela e o usuário enchergar a informação    (pagina.update())
        pagina.update()
        #dizer o que vai acontecer se o usuário clicar no botão.
        
    botao = ft.ElevatedButton("Iniciar Chat", on_click= abrir_popup)
        
    # colocar elementos na página
    pagina.add(titulo)
    pagina.add(botao)

#executar função com flet
# PARAMETRO PARA NAVEGADOR  (ft.WEB_BROWSER)

ft.app(main, view = ft.WebView)
