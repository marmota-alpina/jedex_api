# Jedex API

Esta é a documentação para configurar e executar a API Jedex utilizando Docker Compose.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Como usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/marmota-alpina/jedex_api.git
   cd jedex_api
   ```

2. **Crie e inicie os containers:**

   Execute o comando abaixo para criar e iniciar os containers definidos no arquivo `docker-compose.yml`.

   ```bash
   docker-compose up --build
   ```

   O comando acima fará o seguinte:
   - Construirá a imagem da API a partir do Dockerfile na raiz do projeto.
   - Criará e iniciará um container para a API com o nome `jedex_api`.
   - Criará e iniciará um container para o banco de dados PostgreSQL com o nome `jedex_postgres`.
   - Configurará uma rede interna para comunicação entre os containers.
   - Mapeará a porta 8000 do container da API para a porta 5001 da máquina host.
   - Mapeará a porta 5432 do container do PostgreSQL para a porta 5434 da máquina host.
   - Criará um volume Docker para persistir os dados do banco de dados.

3. **Acesse a API:**

   Após iniciar os containers, a API estará disponível em `http://localhost:5001`.

## Configuração dos Serviços

### API

- **Build:** O container da API é construído a partir do Dockerfile na raiz do projeto.
- **Container Name:** `jedex_api`
- **Ports:** A API está mapeada para a porta `5001` no host e `8000` no container.
- **Depends On:** A API depende do serviço `jedex_postgres`.
- **Environment Variables:**
  - `DATABASE_URL`: URL de conexão com o banco de dados PostgreSQL.

### PostgreSQL

- **Image:** `postgres:13`
- **Environment Variables:**
  - `POSTGRES_USER`: Nome do usuário do PostgreSQL (`jedex_user`).
  - `POSTGRES_PASSWORD`: Senha do usuário do PostgreSQL (`password`).
  - `POSTGRES_DB`: Nome do banco de dados (`jedex_db`).
- **Volumes:** Um volume Docker (`jedex_postgres_data`) é utilizado para persistir os dados do banco de dados.
- **Ports:** O PostgreSQL está mapeado para a porta `5434` no host e `5432` no container.

## Volumes

- `jedex_postgres_data`: Volume Docker para persistir os dados do banco de dados PostgreSQL.

## Parando os containers

Para parar e remover os containers, utilize o comando:

```bash
docker-compose down
```

## Contribuindo

Se você deseja contribuir com este projeto, por favor, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

---

Para quaisquer dúvidas ou problemas, sinta-se à vontade para abrir uma [issue](https://github.com/marmota-alpina/jedex_api/issues).


# Jedex API

Jedex API é uma aplicação desenvolvida com Flask para fornecer serviços relacionados ao cálculo de frete, gerenciamento de empresas e contratos. Este README fornece informações sobre como usar os endpoints disponíveis na API.

## Visão Geral

- **Versão da API**: 1.0.0
- **Documentação OpenAPI**: 3.1.0

## Endpoints

### Cálculo de Frete

#### `POST /api/v1/freight/`

Calcula o valor do frete com base nos dados fornecidos.

- **Tags**: Freight
- **Resumo**: Calcula o valor do frete
- **Request Body**: Necessário (JSON)
  - Schema: `FreightRequest`
- **Responses**:
  - `200`: Sucesso (Schema: `FreightResponse`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

### Gerenciamento de Empresas

#### `GET /api/v1/company/`

Obtém a lista de todas as empresas cadastradas.

- **Tags**: Company
- **Resumo**: Lê as empresas cadastradas
- **Responses**:
  - `200`: Sucesso (Array de `CompanyResponse`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `POST /api/v1/company/`

Cria uma nova empresa.

- **Tags**: Company
- **Resumo**: Cria uma nova empresa
- **Request Body**: Necessário (JSON)
  - Schema: `CompanyCreate`
- **Responses**:
  - `200`: Sucesso (Schema: `CompanyResponse`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `GET /api/v1/company/{company_id}`

Obtém detalhes de uma empresa específica.

- **Tags**: Company
- **Resumo**: Lê uma empresa específica
- **Path Parameters**:
  - `company_id` (string): ID da empresa
- **Responses**:
  - `200`: Sucesso (Schema: `CompanyResponse`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `PUT /api/v1/company/{company_id}`

Atualiza os dados de uma empresa específica.

- **Tags**: Company
- **Resumo**: Atualiza uma empresa específica
- **Path Parameters**:
  - `company_id` (string): ID da empresa
- **Request Body**: Necessário (JSON)
  - Schema: `CompanyUpdate`
- **Responses**:
  - `200`: Sucesso (Schema: `CompanyResponse`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `DELETE /api/v1/company/{company_id}`

Deleta uma empresa específica.

- **Tags**: Company
- **Resumo**: Deleta uma empresa específica
- **Path Parameters**:
  - `company_id` (string): ID da empresa
- **Responses**:
  - `200`: Sucesso (booleano)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

### Gerenciamento de Contratos

#### `GET /api/v1/contract/`

Obtém a lista de todos os contratos cadastrados.

- **Tags**: Contract
- **Resumo**: Obtém todos os contratos
- **Responses**:
  - `200`: Sucesso (Array de `Contract`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `POST /api/v1/contract/`

Cria um novo contrato.

- **Tags**: Contract
- **Resumo**: Cria um novo contrato
- **Request Body**: Necessário (JSON)
  - Schema: `ContractCreate`
- **Responses**:
  - `201`: Sucesso (Schema: `Contract`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `GET /api/v1/contract/{contract_id}`

Obtém detalhes de um contrato específico.

- **Tags**: Contract
- **Resumo**: Obtém um contrato específico
- **Path Parameters**:
  - `contract_id` (string): ID do contrato
- **Responses**:
  - `200`: Sucesso (Schema: `Contract`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `PUT /api/v1/contract/{contract_id}`

Atualiza os dados de um contrato específico.

- **Tags**: Contract
- **Resumo**: Atualiza um contrato específico
- **Path Parameters**:
  - `contract_id` (string): ID do contrato
- **Request Body**: Necessário (JSON)
  - Schema: `ContractUpdate`
- **Responses**:
  - `200`: Sucesso (Schema: `Contract`)
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

#### `DELETE /api/v1/contract/{contract_id}`

Deleta um contrato específico.

- **Tags**: Contract
- **Resumo**: Deleta um contrato específico
- **Path Parameters**:
  - `contract_id` (string): ID do contrato
- **Responses**:
  - `204`: Sucesso
  - `422`: Erro de Validação
  - `404`: Não Encontrado
  - `500`: Erro Interno do Servidor

### Root

#### `GET /`

Lê a raiz do serviço.

- **Resumo**: Lê a raiz do serviço
- **Responses**:
  - `200`: Sucesso

## Componentes de Esquemas

### CompanyCreate

```json
{
  "type": "object",
  "required": ["register_number", "name", "address", "city", "state", "postal_code", "phone", "email"],
  "properties": {
    "register_number": { "type": "string", "title": "Register Number" },
    "name": { "type": "string", "title": "Name" },
    "address": { "type": "string", "title": "Address" },
    "city": { "type": "string", "title": "City" },
    "state": { "type": "string", "title": "State" },
    "postal_code": { "type": "string", "title": "Postal Code" },
    "phone": { "type": "string", "title": "Phone" },
    "email": { "type": "string", "format": "email", "title": "Email" }
  },
  "title": "CompanyCreate"
}
```

### CompanyResponse

```json
{
  "type": "object",
  "required": ["register_number", "name", "address", "city", "state", "postal_code", "phone", "email", "id"],
  "properties": {
    "register_number": { "type": "string", "title": "Register Number" },
    "name": { "type": "string", "title": "Name" },
    "address": { "type": "string", "title": "Address" },
    "city": { "type": "string", "title": "City" },
    "state": { "type": "string", "title": "State" },
    "postal_code": { "type": "string", "title": "Postal Code" },
    "phone": { "type": "string", "title": "Phone" },
    "email": { "type": "string", "format": "email", "title": "Email" },
    "id": { "type": "string", "title": "Id" }
  },
  "title": "CompanyResponse"
}
```

### CompanyUpdate

```json
{
  "type": "object",
  "properties": {
    "register_number": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Register Number" },
    "name": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Name" },
    "address": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Address" },
    "city": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "City" },
    "state": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "State" },
    "postal_code": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Postal Code" },
    "phone": { "anyOf": [{ "type": "string" }, {

 "type": "null" }], "title": "Phone" },
    "email": { "anyOf": [{ "type": "string" }, { "type": "null" }], "format": "email", "title": "Email" }
  },
  "title": "CompanyUpdate"
}
```

### ContractCreate

```json
{
  "type": "object",
  "required": ["company_id", "contract_number", "start_date", "end_date"],
  "properties": {
    "company_id": { "type": "string", "title": "Company Id" },
    "contract_number": { "type": "string", "title": "Contract Number" },
    "start_date": { "type": "string", "format": "date", "title": "Start Date" },
    "end_date": { "type": "string", "format": "date", "title": "End Date" }
  },
  "title": "ContractCreate"
}
```

### ContractUpdate

```json
{
  "type": "object",
  "properties": {
    "company_id": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Company Id" },
    "contract_number": { "anyOf": [{ "type": "string" }, { "type": "null" }], "title": "Contract Number" },
    "start_date": { "anyOf": [{ "type": "string" }, { "type": "null" }], "format": "date", "title": "Start Date" },
    "end_date": { "anyOf": [{ "type": "string" }, { "type": "null" }], "format": "date", "title": "End Date" }
  },
  "title": "ContractUpdate"
}
```

### Contract

```json
{
  "type": "object",
  "required": ["company_id", "contract_number", "start_date", "end_date", "id"],
  "properties": {
    "company_id": { "type": "string", "title": "Company Id" },
    "contract_number": { "type": "string", "title": "Contract Number" },
    "start_date": { "type": "string", "format": "date", "title": "Start Date" },
    "end_date": { "type": "string", "format": "date", "title": "End Date" },
    "id": { "type": "string", "title": "Id" }
  },
  "title": "Contract"
}
```

### FreightRequest

```json
{
  "type": "object",
  "required": ["origin_postal_code", "destination_postal_code", "weight"],
  "properties": {
    "origin_postal_code": { "type": "string", "title": "Origin Postal Code" },
    "destination_postal_code": { "type": "string", "title": "Destination Postal Code" },
    "weight": { "type": "number", "title": "Weight" }
  },
  "title": "FreightRequest"
}
```

### FreightResponse

```json
{
  "type": "object",
  "required": ["value", "estimated_days"],
  "properties": {
    "value": { "type": "number", "title": "Value" },
    "estimated_days": { "type": "integer", "title": "Estimated Days" }
  },
  "title": "FreightResponse"
}
```