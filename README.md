<div align="center">
  <h1>Literary AI Proofreading & Copydesk Engine 🚀</h1>
  <p>
    <img src="https://img.shields.io/badge/Projeto_Real-99Freelas-00b853?style=for-the-badge&logo=freelancer&logoColor=white" alt="99Freelas" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini" />
    <img src="https://img.shields.io/badge/NLP_Prompting-8E44AD?style=for-the-badge&logo=openai&logoColor=white" alt="NLP Prompting" />
    <img src="https://img.shields.io/badge/Docx_Automation-00A4EF?style=for-the-badge&logo=microsoftword&logoColor=white" alt="Word Automation" />
  </p>
  <h3>Pipeline automatizado de revisão ortográfica, gramatical e copidesque literário utilizando LLMs (Gemini 2.5 Flash) com rastreabilidade total de alterações.</h3>
</div>

<br>

> [!CAUTION]
> **🚨 ALERTA DE SECOP (SEGURANÇA DE OPERAÇÕES):**
> As credenciais de API da Google GenAI devem ser configuradas exclusivamente via arquivo `.env`. Nunca faça commit de chaves brutas em código.

## 📊 1. Visão Geral e Escopo Técnico
O **Literary AI Proofreading Engine** é uma plataforma baseada em Python e engenharia avançada de prompts desenvolvida para realizar copidesque literário e revisão de provas em manuscritos de ficção de até 30.000 palavras. A solução integra a nova SDK oficial do `google-genai` com o modelo `gemini-2.5-flash`, empregando um algoritmo de segmentação semântica stateless que divide a obra em blocos contextuais otimizados sem perder a fluidez ou corromper a voz do autor.

No mercado editorial e autopublicação (Amazon KDP, editoras independentes), a revisão manual de um manuscrito desse porte exige dias de trabalho intensivo. O sistema automatiza esse processo em questão de minutos, gerando o documento final devidamente formatado em `.docx` acompanhado de um relatório detalhado de auditoria de alterações e um script de validação de integridade por cruzamento de dados.

## 💼 2. Business Intelligence & Contexto do Cliente
* 🎯 **O Gargalo (A Dor Original):** A autora necessitava de uma revisão ortográfica, gramatical e de pontuação literária para um romance infantojuvenil finalizado (29.262 palavras). O desafio crítico consistia em corrigir erros da norma-padrão e alinhar a complexa pontuação de diálogos (travessões e incisos do narrador) sem alterar o enredo, a voz dos personagens ou criar alucinações de texto.
* 💡 **A Solução Estratégica (O Valor Entregue):** Foi criada uma esteira de processamento que aplica diretrizes de engenharia de prompt estritas com "Regras de Ouro" para pontuação literária. Além de entregar o manuscrito revisado pronto para publicação, o sistema produz um laudo técnico em Word (`Relatorio_de_Revisao_Sarah.docx`) mapeando cada trecho original e sua respectiva correção, agregando transparência e valor comercial ao serviço prestado.

## 🏛️ 3. Arquitetura do Sistema e Fluxo de Dados

```mermaid
flowchart TD
    subgraph Input ["Manuscrito de Entrada"]
        A["romance_original.docx (29k palavras)"]
    end

    subgraph Parser ["Chunking Semântico & Preparação"]
        B["Leitor de Blocos (2,500 palavras/bloco)"]
        C["Instrução de Sistema com Regra de Ouro (Diálogos)"]
    end

    subgraph AI_Engine ["Engine LLM Stateless (Gemini 2.5 Flash)"]
        D["Processamento em Lote com Retry Exponencial"]
        E["Parsers de Saída: TEXTO REVISADO vs LOG DE ALTERAÇÕES"]
    end

    subgraph QA ["Homologação & Geração de Artefatos"]
        F["romance_revisado_final.docx"]
        G["log_de_alteracoes_Sarah.txt"]
        H["Script de Homologação (Cruzamento de Strings)"]
        I["Relatorio_de_Revisao_Sarah.docx (Formatado)"]
    end

    A --> B
    B & C --> D
    D --> E
    E --> F & G
    G --> H & I
    F --> H

🛠️ 4. Stack Tecnológica e Engenharia
Core / Engine: Python 3.11+, Google GenAI SDK (google-genai), modelo gemini-2.5-flash.
Data, Cache & Storage: python-docx (Manipulação e formatação estruturada de documentos Office Open XML).
Mensageria & Assincronismo: Sessões de chamadas stateless com controle de backoff e limite de requisições.
Security & Network: Isolamento de chaves via variáveis de ambiente (python-dotenv), tratamento contra vazamento de dados.
⚙️ 5. Auditoria de Destaques Técnicos (A "Assinatura" do Dev)
Engenharia de Prompt Literária com "Regra de Ouro" para Incisos: Especificação formal para pontuação de diálogos literários, instruindo a IA a discernir quando o narrador interrompe frases contínuas ou divididas (ex: diferenciar vírgula e ponto final antes do segundo travessão).
Pipeline de Parseamento Duplo com Tags Delimitadoras: Estruturação da resposta do LLM em blocos determinísticos (=== TEXTO REVISADO === e === LOG DE ALTERACOES ===), garantindo a separação automática entre o corpo do texto e os metadados de auditoria.
Motor de Homologação e Integridade Automatizado (homologacao.py): Algoritmo de verificação cruzada que varre o relatório de alterações e valida via pattern matching se as correções reportadas pela IA realmente constam no documento Word finalizado.
🚀 6. Guia de Setup e Deploy (Padrão 12-Factor)
Dependências Mínimas: Python 3.10+, conexão de rede com a API da Google Cloud.
Variáveis de Ambiente: Crie o arquivo .env na raiz do projeto com base no .env.example:
env


GEMINI_API_KEY=sua_chave_api_aqui
Ambiente Docker / Containerização:
bash


docker build -t literary-revision-ai .
docker run --env-file .env -v $(pwd):/app literary-revision-ai
Execução Bare Metal:
bash


python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install google-genai python-docx python-dotenv
python corrigindo.py
python homologacao.py
python "gerar relatorio.py"
📂 7. Árvore de Diretórios (Arquitetura Refatorada)
text


repo-literary-revision-ai/
├── .env.example                       # Modelo seguro para configuração de chaves de API
├── .gitignore                         # Exclusão de arquivos temporários, ambientes virtuais e .env
├── README.md                          # Documentação técnica e comercial padrão Agência Premium
├── docs/                              # Documentação e briefings
│   └── briefing_original.txt          # Requisitos originais do cliente 99Freelas
├── src/                               # Scripts de automação e revisão
│   ├── corrigindo.py                  # Engine principal de integração com Gemini 2.5 Flash
│   ├── auditoria.py                   # Módulo de verificação estrutural de capítulos
│   ├── homologacao.py                 # Script de auditoria e validação cruzada de integridade
│   ├── gerar_relatorio.py             # Gerador de relatórios executivos em Word (.docx)
│   └── listar.py                      # Utilitário de inspeção de arquivos
└── 00-BACKLOG-NAO-CATEGORIZADO/       # Rascunhos e logs temporários
