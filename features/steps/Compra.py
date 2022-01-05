import time

from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# precisa sempre importar a classe environment (onde estão o Antes e depois do teste)
from features import environment

# método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # pode ser inclida outras ações
        )


@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')
    # time.sleep(15)

@when(u'seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)


    print('Passo 2 - Selecionou a cidade de origem ')

@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):

    # Mapeia o combo com as cidades de origem
    combo_destino = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_destino = Select(combo_destino)

    # Seleciona o elemento no combo
    objeto_destino.select_by_visible_text(destino)
    #time.sleep(5)
    print('Passo 3  - Acessou a cidade de destino ')

@when(u'clico no botao Find Flights')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 4 - Clico no botao Find Flights')
''''''
@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    # 3 principais motivos para um script de atumação não funcionar
    # - seletores e identificadores
    # - sincronismo
    # - programação exótica

    # assert context.driver.find_element(By.TAG_NAME, 'h3').text() == 'Flights from São Paolo to Rome: '
   # assert context.driver.find_element(By.XPATH, '/html/body/div[2]/h3').text() == 'Flights from São Paolo to Rome:'
    print('Passo 5 - Direcionado para a pagina de selecao de voos')

@when(u'seleciono o primeiro voo')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 6 - Seleciono o primeiro voo ')

@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
   # assert context.driver.find_element(By.XPATH, '/html/body/div[2]/p[6]').text() == 'Please submit the form below to purchase the flight.'
    print('Passo 7 - Sou direcionado para a pagina de pagamento')

@when(u'preencho os dados para o pagamento')
def step_impl(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('James Bond')
    print('Passo 8 - Preencho od dados para o pagamento')

@when(u'clico no botao Purchase Flight')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 9 - clico no botao Purchase Flight')

@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
   # assert context.driver.find_element(By.TAG_NAME, 'h1').text() == 'Thank you for your purchase today!'
    print('Passo 10 - Sou direcionado para a pagina de confirmacao ')

@when(u'seleciono de "{origem}" para "{destino}"')
def step_impl(context, origem, destino):
    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    # Mapeia o combo com as cidades de origem
    combo_destino = context.driver.find_element(By.NAME, 'toPort')

    # Cria um objeto para permitir selecionar as opções do combo
    objeto_destino = Select(combo_destino)

    # Seleciona o elemento no combo
    objeto_destino.select_by_visible_text(destino)

    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

    print('Passo 2c - Selecionou a cidade de origem e destino')
