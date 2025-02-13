FROM python:3.9 # Usa a imagem oficial do Python 3.9 como base
WORKDIR /app # Define o diretório de trabalho dentro do contêiner
COPY requirements.txt .
RUN pip install -r requirements.txt  # Instala as dependências listadas no requirements.txt
COPY . .
CMD ["python", "app.py"] # Define o comando padrão para rodar o aplicativo