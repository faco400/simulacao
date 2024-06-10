# Como executar localmente backend

A partir do diretório backend:

1. instale as dependências:

```terminal
pip install -r requirements.txt
```

2. Inicialize o serviço do Mysql no seu sistema operacional. Lembre-se de criar a base de dados no MySQL se já não estiver criada.

3. Cria o .env a partir do template e substitua de acordo com suas credenciais

4. Execute o seguinte comando:
```terminal
uvicorn api.main:api --reload --port 8081 --host 0.0.0.0
```

Com isso você estará rodando o servidor na porta local 8081. **Em caso de erro verifique se porta está livre**

Para testar as requisições acesse http://localhost:8081/docs ou utilize ferramentas como [Insomnia](https://insomnia.rest/download)