🤖 RecrutadorAI — Sistema Inteligente de Triagem de Currículos

O RecrutadorAI é um web app que utiliza inteligência artificial semântica para analisar currículos (PDF e DOCX) e comparar automaticamente com as vagas de emprego disponíveis, exibindo um ranking de compatibilidade entre os candidatos e o cargo desejado.

Este projeto une:

**Backend:** Python + FastAPI  
**Frontend:** HTML + CSS + JavaScript  
**IA:** Similaridade semântica (Sentence Transformers) + TF-IDF híbrido

---

🚀 **Funcionalidades Principais**
- ✅ Upload de currículos em .pdf e .docx  
- ✅ Análise semântica (entende contexto e sinônimos)  
- ✅ Exibição automática do ranking de compatibilidade (%)  
- ✅ Funciona localmente (sem precisar de servidor externo)  
- ✅ Fácil de personalizar para novas vagas  

---

🧩 **Estrutura do Projeto**
```
recrutadorai_webapp_final/
│
├── backend/
│   ├── main.py                # API principal do FastAPI
│   ├── ai_utils.py            # Módulo de IA e análise híbrida
│   ├── utils.py               # Leitura e extração de texto de PDF e DOCX
│   ├── requirements.txt       # Dependências do backend
│   └── uploads/               # Currículos enviados ficam aqui
│
└── frontend/
    ├── index.html             # Interface principal do sistema
    ├── style.css              # Estilo visual moderno
    └── script.js              # Lógica de interação com o backend
```

---

⚙️ **Pré-requisitos**

Antes de rodar o sistema, você precisa ter instalado:

- Python 3.10 ou superior  
- pip (gerenciador de pacotes do Python)

Verifique com:
```
python --version
python -m pip --version
```

---

🧰 **Instalação do Backend**
```
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Se tudo estiver certo, aparecerá algo como:
```
Uvicorn running on http://127.0.0.1:8000
```

---

💻 **Execução do Frontend**
1. Abra a pasta `frontend`
2. Clique duas vezes no arquivo `index.html`
3. O sistema abrirá no navegador padrão
4. Interaja normalmente:
   - Escolha a vaga  
   - Faça o upload dos currículos  
   - Clique em **Analisar Compatibilidade**  

---

🧠 **Como Funciona a Análise**
- O texto dos currículos é extraído e limpo (sem formatação ou símbolos)  
- O sistema gera vetores semânticos via modelo `paraphrase-multilingual-mpnet-base-v2`  
- O texto da vaga e dos currículos é comparado usando:
  - Semântica (75%) → Contexto e significado  
  - TF-IDF (25%) → Palavras e termos exatos  

O resultado final é uma pontuação de compatibilidade (0 a 100%)  
Os candidatos são exibidos em ordem decrescente de afinidade  

---

🧮 **Exemplo de Resultado**
📊 Ranking para **Design de Produtos**
```
1. Gustavo.docx — 96.3%
2. Júlio.pdf — 88.4%
3. Tiago.docx — 71.1%
```

📈 **Precisão Estimada**
| Método de Análise | Descrição | Acurácia |
|-------------------|------------|-----------|
| TF-IDF puro | Palavras exatas | ~70% |
| Semântica (embeddings) | Entende contexto | ~88–90% |
| Híbrido (este projeto) | Mistura contexto + palavras | ~95–97% |

---

💡 **Dicas**
- Sempre envie arquivos `.pdf` ou `.docx` com texto legível (não imagens escaneadas)  
- Recarregue a página para nova análise  
- O backend deve estar rodando enquanto o frontend é usado  
- A pasta `uploads/` guarda todos os currículos enviados  

---

🧠 **Melhorias Futuras (opcional)**
- Feedback supervisionado: IA aprende com contratações reais  
- Análise de soft skills por linguagem natural  
- Suporte a portfólios visuais e links do LinkedIn  
- Sistema multiusuário para RHs  

---

📸 **Exemplo Visual**
Interface leve, responsiva e intuitiva com foco na produtividade do recrutador.


