from selenium import webdriver

# Inicio
def before_all(context):     #Antes de tudo
    # Declara o selenium e instaciar como navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/vinic/PycharmProjects/ fts132_blazedemo/drivers/chrome/96/chromedriver.exe')

    #Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de tudo')

# Fim
def after_all(context):    #Depois de tud

    # Desligar / Destruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de tudo')