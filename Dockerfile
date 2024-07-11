# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar apenas os arquivos de dependências do Poetry para cache
COPY pyproject.toml poetry.lock* /app/

# Install other dependencies
RUN apt-get update && apt-get install -y gcc

# Instalar Poetry
RUN pip install poetry

# Instalar dependências do projeto
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copiar o restante do código do aplicativo
COPY . /app

# Executar alembic para criar o banco de dados
#RUN alembic upgrade head

# Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
