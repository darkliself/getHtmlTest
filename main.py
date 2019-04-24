import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import mainView # Это наш конвертированный файл дизайна
from webView import *



class Main(QtWidgets.QMainWindow, mainView.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        


        self.browser = AceWebView(self.gridLayout_2)



        ## Вызов сплиттера
        ##slitedPool = SectionSplitter()

        self.pushButton.clicked.connect(self.tmpShow)

    def SayHello(self, text):
        print(text)

    def tmpShow(self):
        self.browser.browserView.page().toHtml(self.SayHello)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Main()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()