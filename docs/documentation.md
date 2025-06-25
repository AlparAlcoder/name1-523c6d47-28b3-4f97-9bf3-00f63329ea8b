# Documentação da API FastAPI

Este código implementa uma API simples usando o framework FastAPI. A API tem um endpoint POST que aceita um item e insere-o em uma base de dados SQLite.

## Classes e Funções

### Classe Item

A classe `Item` herda de `BaseModel` e tem as seguintes propriedades:

- `id` (int): O identificador do item.
- `name` (str): O nome do item.
- `price` (float): O preço do item.
- `is_offer` (bool, opcional): Se o item está em oferta ou não. Padrão é `None`.

### Função connect_db

A função `connect_db` estabelece uma conexão com uma base de dados SQLite e retorna a conexão e o cursor.

### Função close_db

A função `close_db` fecha o cursor e a conexão com a base de dados. Recebe como parâmetros:

- `conn`: A conexão com a base de dados.
- `cursor`: O cursor da base de dados.

### Endpoint /items/

O endpoint `/items/` recebe um `POST` que gera um novo item na base de dados. O item deve ser um objeto da classe `Item`.

## Exemplos de Uso

Para usar o endpoint `/items/`, você deve enviar um `POST` com um corpo JSON que representa um item. Por exemplo:

```json
{
    "id": 1,
    "name": "Item One",
    "price": 19.99,
    "is_offer": false
}
```

A resposta será:

```json
{
    "status": "Item added successfully"
}
```

## Notas Importantes

Este código não implementa manipulação de erros completas. Se ocorrer um erro na operação de banco de dados (como tentar adicionar um item com um ID que já existe), o código simplesmente retorna um erro 400 sem detalhes úteis.

## Dependências Necessárias

- FastAPI: Um framework moderno e rápido (alta performance) para construir APIs.
- Pydantic: Uma biblioteca para validação de dados.
- SQLite3: Uma biblioteca para trabalhar com o banco de dados SQLite.