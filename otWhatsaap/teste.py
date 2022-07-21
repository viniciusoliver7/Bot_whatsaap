import datetime
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

         print(bot.dataUltimaMsg(driver))
         print(datetime.datetime.today())
