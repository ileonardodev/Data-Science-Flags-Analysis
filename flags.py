import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Importação nova para SQL
from sqlalchemy import create_engine


class AnalisadorDeBandeiras:
    def __init__(self, caminho_arquivo):
        print("📥 Carregando dados...")
        self.df = pd.read_csv(caminho_arquivo)
        self.df.columns = self.df.columns.str.lower()
        print(f"✅ Dados carregados! {self.df.shape[0]} países.")

    def filtrar_por_continente(self, continente_id):
        return self.df[self.df['landmass'] == continente_id]

    def contar_cores_medias(self):
        return self.df['colors'].mean()

    def grafico_distribuicao_cores(self):
        print("📊 Gerando gráfico...")
        plt.figure(figsize=(10, 6))
        sns.countplot(x='colors', data=self.df, palette='viridis', hue='colors', legend=False)
        plt.title("Distribuição: Quantas cores as bandeiras costumam ter?")
        plt.show()

    def prever_religiao_floresta(self):
        print("\n🌲 --- Treinando Floresta para Análise ---")
        colunas_dicas = ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange',
                         'circles', 'crosses', 'saltires', 'quarters', 'sunstars',
                         'crescent', 'triangle']
        X = self.df[colunas_dicas]
        y = self.df['religion']

        # Treinamos com TUDO agora, pois queremos usar o modelo para exportar resultados
        # (Em um cenário real, salvaríamos o modelo treinado separadamente)
        self.modelo_floresta = RandomForestClassifier(n_estimators=100, random_state=42)
        self.modelo_floresta.fit(X, y)
        print("✅ Modelo interno atualizado.")

    # --- NOVO MÉTODO: EXPORTAR PARA SQL ---
    def exportar_resultados_sql(self, nome_banco="bandeiras_db.db"):
        print(f"\n💾 Exportando previsões para SQL ({nome_banco})...")

        # 1. Garante que o modelo existe
        if not hasattr(self, 'modelo_floresta'):
            self.prever_religiao_floresta()

        # 2. Faz a previsão para TODOS os países
        colunas_dicas = ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange',
                         'circles', 'crosses', 'saltires', 'quarters', 'sunstars',
                         'crescent', 'triangle']

        # Cria uma cópia para não sujar o original
        df_export = self.df[['name', 'religion']].copy()
        df_export['religiao_prevista'] = self.modelo_floresta.predict(self.df[colunas_dicas])

        # Adiciona uma coluna para verificar se acertou (1 = Sim, 0 = Não)
        df_export['acertou'] = (df_export['religion'] == df_export['religiao_prevista']).astype(int)

        # 3. Conecta com o Banco SQL (SQLite cria o arquivo sozinho)
        # 'sqlite:///nome_do_arquivo.db' é a String de Conexão
        motor_sql = create_engine(f'sqlite:///{nome_banco}')

        # 4. Escreve a tabela (to_sql é MÁGICO)
        # if_exists='replace' -> Se a tabela já existir, apaga e cria de novo
        df_export.to_sql('relatorios_previsao', con=motor_sql, if_exists='replace', index=False)

        print("✅ Sucesso! Tabela 'relatorios_previsao' criada no banco SQL.")
        print(f"📂 Verifique o arquivo '{nome_banco}' na pasta do seu projeto.")


# --- ÁREA DE TESTES ---
analisador = AnalisadorDeBandeiras("dados/flags.csv")

# Gera o arquivo .db
analisador.exportar_resultados_sql()