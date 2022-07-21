import time
from simon.chat.pages import ChatPage
from selenium.webdriver.common.by import By
from simon.chats.pages import PanePage
from datetime import datetime







def enviarMSG(pagina_do_selenium,deveescrever):
    "=========================PART-1 ============================="

    """
    ele atualiza nessa parte a "home" dele 
    
    VEJA ABAIXO -> 
    """

    chat_page = ChatPage(pagina_do_selenium)  # atualiza para a "home work"


    "=============================PART -2 ========================================="

    """
    APÓS ENTRAMOS NO CHAT, IREMOS FAZER COM QUE ELE DIGITE A MENSAGEM SOLICITADA E ENVIE ELA PARA 
    O CLIENTE 
    
    VEJA ABAIXO O FUNCIONAMENTO ->
    """
    time.sleep(0.2) #esse 1 segundo é para evitar bugs da ferramenta do selenium

    write = chat_page.writer  # seleciona o campo de escrita

    write.send_msg(deveescrever)  # escreve no chat

    time.sleep(0.2) # espera para escrever a mensagem com tranquilidade

    #na linha baixo ele seleciona o botão de enviar e clica nele
    #pagina_do_selenium.find_element(By.CSS_SELECTOR, "#main footer ._2lMWa  ._1Ae7k button.p2rjqpw5 ").click()


def lerMensagem(quatidadesDeMsg,comunicador,pagina_do_selenium):
    "===================PART-1============================="
    """
    nesse primeira parte ele apenas atualiza a pagina para conversa
    """
    chat_page = ChatPage(pagina_do_selenium)

    "=======================PART -2==================================="
    """
    NESSE PART 2 PROCURA AS MENSAGENS E COLOCAR EM UMA LISTA E RETORNA.
    
    VEJA ABAIXO O EXEMPLO ->
    """

    #NA LINHA ABAIXO ELE PROCURA AS QUANTIDADE DE MENSAGENS QUE FOI PASSADA
    mensagne = chat_page.messages.newest(int(quatidadesDeMsg), filterby=comunicador)

    conjuntoMSG = [conversa.text for conversa in mensagne] #ADICIONA AS MENSAGENS EM UMA LISTA

    return conjuntoMSG

def fecharcall(pagina_do_selenium):
    pagina_do_selenium.find_element(By.XPATH,value='//*[@id="main"]/header/div[3]/div/div[2]/div/div').click() #CLICA NOS 3 PONTOS

    valorDentro = pagina_do_selenium.find_element(By.XPATH,value='/html/body/div[1]/div/span[4]/div/ul/div/div/li[3]/div[1]').text

    if valorDentro == "Fechar conversa":
        pagina_do_selenium.find_element(By.XPATH, value='/html/body/div[1]/div/span[4]/div/ul/div/div/li[3]/div[1]').click()

    else:
        pagina_do_selenium.find_element(By.XPATH, value='/html/body/div[1]/div/span[4]/div/ul/div/div/li[5]/div[1]').click()


def LerMensagensGeral(pagina_do_selenium,quantLidas):

    """
    NESSA FUNÇÃO APENAS PEGAMOS AS MENSAGENS DE MANEIRA GERAL, OU SEJA , SEM SE IMPORTAR SE É O BOT OU DO CLIENTE
    """
    chat_page=ChatPage(pagina_do_selenium)
    msgg=chat_page.messages.newest(quantLidas)

#

    return [mensagem.text for mensagem in msgg ]


def dataUltimaMsg(pagina_do_selenium):
    """
    ESSA FUNÇÃO PEGA O A DATA DA ULTIMA MENSAGEM ENVIADA
    COMPARA COM DATA DO DIA E VE SE A MENSAGEM É DE HOJE
    """

    chatpage = ChatPage(pagina_do_selenium) #SELECIONA A PARTE DO DA CONVERSA
    msg = chatpage.messages.newest() #PEGA A ULTIMA MENSAGEM
    dataBase=msg.date #RETORNA A ULTIMA A DATA DELa
    if dataBase.strftime("%Y/%m/%d") == datetime.today().strftime("%Y/%m/%d"): #faz um teste lógico de as datas coenciden
        return True
    else:
        return False



def executar(numerador,baseDados,pagina_do_selenium): #verificar se é a primeira mensagem
    """

    ESSA FUNÇÃO É PARA VEFICIFICAR SEA MENSAGEM É PRIMEIRA DA CONVERDA

    POIS COMO O BOT SE BASEIA EM LER AS MENSAGENS DELE PARA SABER ONDE A CONVERSA ESTÁ SE NÃO HOUVER NENHUMA CONVERSA
    """


    n1=''
    for valor in baseDados: #desepacota as mensagens do bot
        for messagem in LerMensagensGeral(pagina_do_selenium,numerador):#elepega as ultimas mensageens do para comparar
            if valor==messagem:#se tiver uma mensagem parecidada
                n1=True #ele retorna True
            else:
                pass
    return n1

def tirarNotificacao(pagina_do_selenium):

    """
    ESSA FUNÇÃO TEM COMO FINALIDADE TIRAR NOTIFICAÇÕES QUE PODEM TER AO WHATSAAP ABRIR ,NOTICIFAÇÕES PASSADAS

    """
    time.sleep(40) #TEMPO PARA O WHATSAPP SE ORGANIZAR
    pane_page = PanePage(pagina_do_selenium)  # entra pagina dos chats
    chats = pane_page.opened_chats  # recolhe todos os chats
    for chat in chats:
        time.sleep(0.6)
        if chat.has_notifications():
            pane_page=PanePage((pagina_do_selenium))
            pane_page.get_opened_chat(chat.name).click()
            fecharcall(pagina_do_selenium)



