ETL Series – Desafio Santander DIO

Bem-vindo ao repositório ETL Series, desenvolvido como parte do Desafio Santander Bootcamp – Ciência de Dados com Python (DIO).
Este projeto demonstra a construção de um pipeline ETL completo, totalmente automatizado, limpo e estruturado, com foco em boas práticas de engenharia de dados.

📌 📚 Visão Geral do Projeto

O objetivo deste projeto é:

Extrair dados brutos de séries televisivas (arquivo JSON fornecido no desafio);

Transformar os dados, realizando limpeza, padronização, normalização e enriquecimento;

Carregar (Load) o resultado em um arquivo final tabular estruturado (CSV);

Tudo isso utilizando Python, pandas e um fluxo ETL organizado em módulos.

O projeto foi construído com foco em:

✔️ Organização profissional
✔️ Tratamento de dados robusto
✔️ Código limpo e extensível
✔️ Estrutura adequada para deploy e integrações futuras


🧱 Estrutura do Repositório
ETL_Series/
│
├── __pycache__/             # Arquivos de cache gerados automaticamente pelo Python
│
├── Data/                    # Pasta contendo os dados brutos e/ou processados
│
├── extract.py               # Módulo responsável pela etapa de Extração (Extract)
├── load.py                  # Módulo responsável pela etapa de Carregamento (Load)
├── main.py                  # Script principal que orquestra todo o pipeline ETL
├── README.md                # Documentação do projeto
├── requirements.txt         # Lista de dependências Python do projeto
├── series.db                # Banco de dados SQLite com dados das séries
└── transform.py             # Módulo responsável pela etapa de Transformação (Transform)


🚀 Tecnologias Utilizadas

Python 3.10+

pandas

JSON

Virtualenv / venv

Git + GitHub

🔄 Pipeline ETL
🟨 1. Extract

Leitura do arquivo JSON contendo as séries.

Validação de estrutura e campos essenciais.

Conversão inicial para DataFrame.

🟦 2. Transform

Processos aplicados:

Limpeza de colunas

Padronização de nomes

Conversão de tipos de dados

Explosão de listas

Normalização de texto

Remoção de registros inválidos

Enriquecimento dos dados (ex.: cálculo de métricas)

🟩 3. Load

Exportação final para CSV organizado em /data/processed

Logs de execução

Garantia de idempotência do pipeline

▶️ Como Executar o Projeto
1. Clone o repositório
git clone https://github.com/henriquemorilha/etl_series_desafio_santander_dio.git

2. Navegue para a pasta principal
cd etl_series_desafio_santander_dio

3. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

4. Instale as dependências
pip install -r requirements.txt

5. Execute o pipeline
python main.py


Após a execução, os arquivos processados estarão em:

data/processed/

📊 Exemplo do Resultado Final
nome_da_serie	genero	ano_lancamento	avaliacao
Breaking Bad	Drama	2008	9.5
Dark	Sci-Fi	2017	8.8
📈 Melhorias Futuras

Integração com banco de dados (PostgreSQL ou MongoDB)

Orquestração com Apache Airflow

Visualização em dashboards

Automação CI/CD

Deploy como API ETL usando FastAPI

🏆 Sobre o Desafio

Este projeto faz parte do Santander Bootcamp (DIO) e tem como objetivo consolidar conhecimentos em:

✔️ Manipulação de dados
✔️ Arquitetura ETL
✔️ Boas práticas de engenharia de dados
✔️ Estruturação de projetos Python

👨‍💻 Autor

Henrique Morilha
🔗 GitHub: @henriquemorilha

Sugerir melhorias

Mandar pull requests

Se este projeto te ajudou, deixe uma estrelinha ⭐ no repositório!
