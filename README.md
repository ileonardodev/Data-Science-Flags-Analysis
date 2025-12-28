# 🌍 Análise de Bandeiras com Data Science & Machine Learning

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Lib](https://img.shields.io/badge/Lib-Scikit--Learn-orange)
![Lib](https://img.shields.io/badge/Lib-Streamlit-red)

## 📌 Sobre o Projeto

Este projeto utiliza **Ciência de Dados** e **Machine Learning** para analisar padrões em bandeiras de países e prever a religião predominante com base em características visuais (cores, formas geométricas, presença de símbolos).

O sistema percorre um pipeline completo de dados:
1.  **ETL:** Extração e limpeza de dados brutos (`flags.csv`).
2.  **Modelagem:** Treinamento de modelos **Decision Tree** e **Random Forest**.
3.  **Engenharia:** Exportação das previsões para banco de dados SQL (`SQLite`).
4.  **Visualização:** Apresentação dos resultados em um Dashboard interativo via **Streamlit**.

---

## 📸 Dashboard (Demonstração)

<img width="1358" height="618" alt="Captura de tela de 2025-12-27 22-01-50" src="https://github.com/user-attachments/assets/0da6bfee-7594-4e65-9780-967c6f858082" />



> O Dashboard exibe a acurácia do modelo em tempo real e permite auditar onde o algoritmo acertou ou errou.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Análise de Dados:** Pandas, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Banco de Dados:** SQLite (via SQLAlchemy)
* **Web Dashboard:** Streamlit
* **IDE:** PyCharm Professional no Ubuntu Linux

---

## 📂 Estrutura do Projeto

* `flags.py`: Script principal contendo a Classe `AnalisadorDeBandeiras`. Realiza o carregamento, limpeza, treinamento do modelo e exportação SQL.
* `dashboard.py`: Aplicação web que lê o banco SQL e gera a interface visual.
* `dados/flags.csv`: Dataset original utilizado para treino e teste.
* `bandeiras_db.db`: Banco de dados SQLite gerado automaticamente com as previsões.

---

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/ileonardodev/Data-Science-Flags-Analysis.git](https://github.com/ileonardodev/Data-Science-Flags-Analysis.git)
