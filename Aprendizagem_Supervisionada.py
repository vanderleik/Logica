# Regressão Logística
"""
Vamos usar o dataset iris, que possui dados de flores para 3 categorias.
Nosso modelo deverá receber dados das flores e prever a qual das 3 categorias a flor pertence.

Aqui o dataset:
https://archive.ics.uci.edu/ml/datasets/Iris
"""
# Pacotes para computação e matemática
import numpy as np
import math

# Classe para a função de Ativação Sigmoide
# Quando estudamos econometria, especialmente o modelo Logit,
# vemos essa função que é capaz de criar aquele gráfico com uma linha tangenciando
# o limite inferior, perto de zero, e o limite superior do gráfico, perto de 1, em um
# formato de S.
class Sigmoide():
    def __call__(self, x):
        return 1 / (1 + np.exp(-x))

# Algoritmo de Machine Learning - Regressão Logística
class RegressaoLogistica():
    # Construtor da Classe - define os atributos
    def __init__(self, learning_rate = .1, gradient_descent = True):
        self.param = None
        self.learning_rate = learning_rate
        self.gradient_descent = gradient_descent
        self.sigmoid = Sigmoide()
    # Inicializa os parâmetros
    def _inicializa_parametros(self, X):
        n_features = np.shape(X)[1]
        limit = 1 / math.sqrt(n_features)
        self.param = np.random.uniform(-limit, limit, (n_features,))
    # Converte uma matriz x para diagonal a fim de realizar os cálculos
    def make_diagonal(x):
        m = np.zeros((len(x), len(x)))
        for i in range(len(m[0])):
            m[i, i] = x[i]
        return m
    # Função para o treinamento
    # Aqui está o coração do algoritmo, suas operações matemáticas
    # Usamos o gradiente descendente a fim de encontrar o melhor valor dos
    # coeficientes, aquilo que o modelo aprende no treinamento
    def treinamento(self, X, y, n_iterations = 4000):
        self._inicializa_parametros(X)
        for i in range(n_iterations):
            y_pred = self.sigmoid(X.dot(self.param))
            if self.gradient_descent:
                self.param -= self.learning_rate * -(y - y_pred).dot(X)
            else:
                diag_gradient = make_diagonal(self.sigmoid.gradient(X.dot(self.param)))
                self.param = np.linalg.pinv(X.T.dot(diag_gradient).dot(X)).dot(X.T).dot(diag_gradient.dot(X).dot(self.param) + y - y_pred)
    # Método para previsão com o modelo
    def previsao(self, X):
        y_pred = np.round(self.sigmoid(X.dot(self.param))).astype(int)
        return y_pred

# Pacotes
from sklearn.datasets import load_iris
import numpy as np

# Função para normalizar os dados
def normaliza_dados(X, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(X, order, axis))
    l2[l2 == 0] = 1
    return X / np.expand_dims(l2, axis)

# Função para randomizar os dados
def randomiza_dados(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]

# Função para calcular a acurácia
def calcula_acuracia(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy

# Função para dividir os dados em treino e teste
def train_test_split(X, y, test_size=0.5, shuffle=True, seed=None):
    if shuffle:
        X, y = randomiza_dados(X, y, seed)
    split_i = len(y) - int(len(y) // (1 / test_size))
    X_train, X_test = X[:split_i], X[split_i:]
    y_train, y_test = y[:split_i], y[split_i:]
    return X_train, X_test, y_train, y_test

# Função para execução do programa
def main():
    # Carregar os dados
    data = load_iris()
    # Normalizar os dados de entrada
    X = normaliza_dados(data.data[data.target != 0])
    # Carregar os dados de saída
    y = data.target[data.target != 0]
    y[y == 1] = 0
    y[y == 2] = 1
    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, seed=1)
    # Definir o modelo
    modelo = RegressaoLogistica(gradient_descent=True)
    # Treinar o algoritmo e criar o modelo
    modelo.treinamento(X_train, y_train)
    # Usar o modelo treinado para fazer previsões
    y_pred = modelo.previsao(X_test)
    # Calcular a acurácia comparando valores previstos com valores observados
    acuracia = calcula_acuracia(y_test, y_pred)
    # Imprime a acurácia do modelo
    print ("Acurácia do Modelo:", acuracia)

# Executa o programa
if __name__ == "__main__":
    main()