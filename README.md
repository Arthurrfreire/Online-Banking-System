## Sistema de Gerenciamento de Contas Bancárias com Herança

Este projeto Python demonstra um sistema básico de gerenciamento de contas bancárias que utiliza o conceito de herança para criar diferentes tipos de contas com funcionalidades específicas.

## Estrutura do Projeto

  * `account.py:` Arquivo Python contendo as classes Account e Savings_Account.
  
  * `README.md:` Este arquivo de documentação.

## Descrição das Classes

`Account`

* Representa uma conta bancária genérica.
* Atributos:
        * `name:` Nome do titular da conta.
        * `account_number:` Número da conta.
        * `balance:` Saldo da conta.
* Métodos:
        * `deposit(amount):` Deposita um valor (amount) na conta.
        * `withdraw(amount):` Saca um valor (amount) da conta, se houver saldo suficiente.

`Savings_Account`

* Herda da classe `Account`, representando uma conta poupança.
* Atributos (além dos herdados de `Account`):
        * `interest_rate:` Taxa de juros da conta poupança.
* Métodos (além dos herdados de `Account`):
        * `add_interest():` Adiciona juros ao saldo da conta, calculando-os com base na taxa de juros e no saldo atual.

# Exemplo de Uso

    Python

    # Criando uma conta corrente
    account1 = Account("John Doe", "123456", 1000)
    account1.deposit(500)
    account1.withdraw(200)
    # Criando uma conta poupança
    savings_account = Savings_Account("John Doe", "789012", 2000, 0.05)  # 5% de juros
    savings_account.deposit(1000)
    savings_account.add_interest()
    savings_account.withdraw(500)
    savings_account.withdraw(1000) 


## Observações

* Este é um exemplo simplificado, sem recursos como validação de dados ou persistência em um banco de dados.
  
* A classe `Savings_Account` demonstra como a herança pode ser usada para criar classes especializadas que reutilizam o código da classe base (`Account`) e adicionam funcionalidades específicas.

**Importante:** Este projeto é apenas para fins educacionais e demonstrativos. Não deve ser usado em um ambiente de produção real, pois não possui as medidas de segurança e robustez necessárias para lidar com operações financeiras reais.
