import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QGridLayout
from PyQt5.QtCore import Qt
class Janela(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializando a tabela e o total
        self.table = PrettyTable(['Produto', 'Preço'])
        self.total = 0

        # Criando os widgets da interface
        self.label_produto = QLabel("Produto:", self)
        self.entrada_produto = QLineEdit(self)
        self.label_preco = QLabel("Preço:", self)
        self.entrada_preco = QLineEdit(self)
        self.botao_adicionar = QPushButton("Adicionar", self)
        self.tabela_widget = QTableWidget(0, 2, self)
        self.tabela_widget.setHorizontalHeaderLabels(["Produto", "Preço"])
        self.botao_salvar = QPushButton("Salvar", self)

        # Configurando a tabela
        self.tabela_widget.horizontalHeader().setStretchLastSection(True)
        self.tabela_widget.verticalHeader().setVisible(False)

        # Criando o layout
        layout = QGridLayout()
        layout.addWidget(self.label_produto, 0, 0)
        layout.addWidget(self.entrada_produto, 0, 1)
        layout.addWidget(self.label_preco, 1, 0)
        layout.addWidget(self.entrada_preco, 1, 1)
        layout.addWidget(self.botao_adicionar, 2, 0, 1, 2)
        layout.addWidget(self.tabela_widget, 3, 0, 1, 2)
        layout.addWidget(self.botao_salvar, 4, 0, 1, 2)
        self.setLayout(layout)

        # Conectando os sinais aos slots
        self.botao_adicionar.clicked.connect(self.adicionar_item)
        self.botao_salvar.clicked.connect(self.salvar_arquivo)

        # Definindo o título da janela e exibindo
        self.setWindowTitle("JU-Fio-de-Malha")
        self.show()

    # Função para adicionar um item à tabela
    def adicionar_item(self):
        # ... (código para adicionar item à tabela e calcular o total)
        # ... (atualizar a tabela)

    # Função para salvar o arquivo
    def salvar_arquivo(self):
        # ... (código para salvar o arquivo)
