from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessa o site https://www.kabum.com.br/promocao/MENU_PCGAMER
driver = webdriver.Firefox()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

    

#extrair todos os títulos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")
# for titulo in titulos:
#     print(titulo.text)
    
# extrair todos os preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")
# for preco in precos:
#     print(preco.text)

#Criando a planilha
workbook = openpyxl.Workbook()
#Criando aa página 'produtos'
workbook.create_sheet('produtos')
# Seleciono a página produtos
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'
workbook.save('produtos.xlsx')


# inserir os títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

#Salvando dados na planilha
workbook.save('produtos.xlsx')

driver.close()

# como entregar para o cliente')