FROM python:3.13-slim

# Instala dependências Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Define o diretório de trabalho para onde está o main.py
WORKDIR /


# Comando padrão
CMD ["python", "main.py"]