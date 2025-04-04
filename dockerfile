# Estágio de construção
FROM python:3.11-slim as builder

WORKDIR /app

# Instalar dependências de construção
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro para aproveitar cache de camadas
COPY requirements.txt .

# Instalar dependências
RUN pip install --user -r requirements.txt

# Estágio final
FROM python:3.11-slim

WORKDIR /app

# Copiar dependências instaladas do estágio builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Garantir que scripts na pasta .local sejam encontrados
ENV PATH=/root/.local/bin:$PATH

# Verificação de saúde
HEALTHCHECK --interval=30s --timeout=3s \
    CMD python -c "from hello import hello_world; print(hello_world())" || exit 1

# Metadados
LABEL maintainer="fernando.nereu@gmail.com"
LABEL version="1.0"
LABEL description="Aplicação Hello World para testes de CI/CD"

# Porta exposta (se aplicável)
# EXPOSE 8000

# Comando padrão
CMD ["python", "hello.py", "--test"]