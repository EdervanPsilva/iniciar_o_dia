import pyautogui as py
import time
import os
import webbrowser

def iniciar_o_dia():
    time.sleep(2)  # Aguarda 2 segundos para o usuário se preparar
    
    py.press('win')  # Pressiona a tecla Windows
    py.write('chrome')  # Digita 'chrome' para abrir o navegador
    py.press('enter')  # Pressiona Enter para abrir o Chrome

    py.sleep(1)  # Aguarda o navegador abrir
    webbrowser.open('https://cmaa-smartmanufactory.atlassian.net/jira/people/63c69e352c6573abb08cd4d0/boards/17?assignee=63c6dd0eb1262586707a4723')  # Abre sprint do jira
    py.sleep(1)  # Aguarda o link ser digitado
    py.hotkey('ctrl', 't')  # Abre uma nova aba
    py.write('https://app.powerbi.com/')  # Abre o Power BI web
    py.press('enter')  # Pressiona Enter para abrir o link

    py.sleep(1)  # Aguarda o Power BI abrir
    py.press('win')  # Pressiona a tecla Windows
    py.write('teams')  # Digita 'teams' para abrir o Microsoft Teams
    py.press('enter')  # Pressiona Enter para abrir o Teams


    py.sleep(1)  # Aguarda o Teams abrir
    py.press('win')  # Pressiona a tecla Windows
    py.write('outlook')  # Digita 'outlook' para abrir o Microsoft  
    py.press('enter')  # Pressiona Enter para abrir o Outlook

    py.sleep(1)  # Aguarda o Outlook abrir
    py.press('win')  # Pressiona a tecla Windows
    py.write('whatsapp')  # Digita 'whatsapp' para abrir o WhatsApp
    py.press('enter')  # Pressiona Enter para abrir o WhatsApp 

    py.sleep(1)  # Aguarda o WhatsApp abrir
    py.press('win')  # Pressiona a tecla Windows   
    py.write('maria')  # Digita 'maria' para abrir o aplicativo
    py.press('enter')  # Pressiona Enter para abrir o aplicativo
    

if __name__ == "__main__":
    iniciar_o_dia()
