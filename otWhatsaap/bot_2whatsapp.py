import time
from selenium import webdriver
from simon.accounts.pages import LoginPage
from simon.chats.pages import PanePage
from otWhatsaap.funcoes_e_Dados import bot
from otWhatsaap.funcoes_e_Dados import baseDados
from simon.chat.pages import ChatPage
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()

loginPage=LoginPage(driver)
loginPage.load()
time.sleep(7)



while True: #loop do cod
   """=============part 1 Log================"""

   """
      -> nessa primeira parte apenas  faço log na pagina do whatsaapp 
   """
   pane_page=PanePage(driver) #entra pagina dos chats
   chats=pane_page.opened_chats #recolhe todos os chats

   "===================part 2 interação  ============================"

   """
      -> nessa parte o bot procura novas mensagens  e acessa o numero chat do cliente 
   """

   for chat in chats: #tranformação para iteravel
      if chat.has_notifications(): #filtro pelo chats com notificação
         pane_page = PanePage(driver)  # SELECIONA O BLOCO COM OS CONTATOS
         pane_page.get_opened_chat(chat.name).click()  # seleciona o contato e clica nele


         def executar(numerador): #verificar se é a primeira mensagem
            n1=''
            for valor in baseDados.conversas:
               for messagem in bot.LerMensagensGeral(driver,numerador):
                  if valor==messagem:
                   n1=True
                  else:
                     pass
            return n1

         if executar(3):

            """==-=-=-=-=-=-=-=-=- PART 3 ATENDIMENTO =-=-=-=-=-=-=-=-=-"""

            """
              ->  NESSA PARTE O BOT DE FATO REALIZA O ATENDIMENTO
              ->  CONSEGUINDO AS SEGUINTES INFORMAÇÕES ( NOME , N° MESA, N° DA MUSICA,QUANT.PESSOAS) 
            
            """

            msgns = bot.lerMensagem(1, "myself", driver) #LÊ A ULTIMA MENSAGEM DELE MESMO

            try:
               baseDados.conversas.index(msgns[0]) #PROCURA PARA VER SE A ULTIMA MENSAGEM DELE, ESTÁ NO SEU BANCO DE DADOS

               if msgns == baseDados.conversas[len(baseDados.conversas)-1]:#VERIFICA SE A ULTIMA MENSAGEM DELE FOI DE DESPEDIDA
                  bot.enviarMSG(driver, baseDados.conversas[0])#CASO SEJA ELE ENVIA UM MENSAGEM DE ENTRADA
                  bot.fecharcall(driver)

               else:
                  ponto=baseDados.conversas.index(msgns[0]) #NO CASO SE NÃO INICIAR UMA CONVERSA
                  # ELE PESQUISA PARA VER EM QUE PONTO ELE ESTÁ DA CONVERSA

                  bot.enviarMSG(driver,baseDados.conversas[ponto+1]) #ENVIA A MENSAGEM POSTERIOR NA LISTA

                  bot.fecharcall(driver)
            except:
               bot.enviarMSG(driver, baseDados.conversas[0])#CASO ELA NÃO ESTEJA ELE ENVIA UM MENSAGEM DE ENTRADA
               bot.fecharcall(driver)
         else:
            bot.enviarMSG(driver, baseDados.conversas[0])
            bot.fecharcall(driver)

      else:
         pass