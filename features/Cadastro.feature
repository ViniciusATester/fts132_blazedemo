@Cadastro
Feature: Cadastro do Usuario
  Scenario: Cadastro com Sucesso
    Given  que acesso o site Blazedemo
    When clico em home
    And clico em Register
    Then vejo o formulario de cadastro
    When preencho "<nome>" "<empresa>" "<email>" "<senha>" "<confirma_senha>"
    And clico no botao Register
    Then exibe a confirmacao do cadastro