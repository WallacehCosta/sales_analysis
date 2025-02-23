# Sales Analyzer

O **Sales Analyzer** é um sistema inteligente de análise de vendas que combina um backend robusto em FastAPI, um frontend dinâmico em React e bancos de dados PostgreSQL e MongoDB. Ele permite visualizar dados de vendas, gerar relatórios detalhados e prever tendências utilizando Machine Learning.

## Tecnologias Utilizadas

- **Backend**: FastAPI
- **Frontend**: React.js
- **Banco de Dados**: PostgreSQL (dados estruturados) e MongoDB (dados não estruturados)
- **Machine Learning**: Scikit-Learn, TensorFlow, PyCaret
- **Visualização de Dados**: Recharts (React) + Dash/Streamlit (opcional)
- **Autenticação**: OAuth2 com JWT
- **Containerização**: Docker

## Como Rodar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados.
- Git (opcional, para clonar o repositório).

### Passos para Execução

1. **Clone o repositório** (se necessário):
   ```bash
   git clone https://github.com/WallacehCosta/sales-analyzer.git
   cd sales-analyzer
   ```

2. **Crie o arquivo `.env`**:
   - Copie o conteúdo do arquivo `.env.example` para `.env`.
   - Ajuste as variáveis de ambiente, se necessário.

3. **Suba os containers**:
   ```bash
   docker-compose up --build
   ```

4. **Acesse o sistema**:
   - **Frontend**: `http://localhost:3000`
   - **Backend (API)**: `http://localhost:8000`

## Estrutura do Projeto

```
Sales Analyzer/
│── backend/                         # Backend com FastAPI
│   ├── app/                          # Código principal
│   │   ├── models/                   # Modelos do banco de dados
│   │   ├── routes/                   # Endpoints da API
│   │   ├── services/                 # Lógica de negócio
│   │   ├── utils/                    # Funções auxiliares
│   │   ├── main.py                   # Arquivo principal da API
│   ├── tests/                        # Testes automatizados
│   ├── Dockerfile                    # Dockerfile do backend
│   ├── requirements.txt              # Dependências do backend
│
│── frontend/                         # Frontend com React.js
│   ├── public/                       # Arquivos estáticos
│   ├── src/                          # Código fonte
│   │   ├── components/               # Componentes reutilizáveis
│   │   ├── pages/                    # Páginas do sistema
│   │   ├── services/                 # Comunicação com API
│   │   ├── hooks/                    # Hooks customizados
│   │   ├── styles/                   # Estilos (CSS/Tailwind)
│   │   ├── App.js                    # Componente principal
│   │   ├── index.js                  # Entrada do React
│   ├── package.json                  # Dependências do frontend
│
│── database/                         # Configuração dos bancos de dados
│   ├── init.sql                       # Scripts de inicialização do PostgreSQL
│
│── docker-compose.yml                 # Configuração dos containers
│── .env.example                        # Exemplo de variáveis de ambiente
│── README.md                           # Documentação do projeto
```

## Variáveis de Ambiente

As principais variáveis de ambiente estão no arquivo `.env` e incluem:

- Configuração do PostgreSQL e MongoDB.
- Chave secreta para autenticação JWT.
- URL da API para o frontend.

## Testes

Para rodar os testes automatizados:

1. Acesse o container do backend:
   ```bash
   docker exec -it sales_analyzer_backend bash
   ```

2. Execute os testes:
   ```bash
   pytest tests/
   ```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```
4. Faça push para a branch:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

### Próximos Passos:

1. **Criar os Dockerfiles** para backend e frontend.
2. **Rodar os containers** com `docker-compose up --build`.
3. **Testar o sistema** acessando `http://localhost:3000`.

Qualquer dúvida entre em contato pelo email: **_holandawallacecosta@gmail.com_**

