# импорт необходимых библиотек и модулей
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

# базовая конструкция для запуска программы
class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(
            self): # тк я наследовалась от класса QMainWindow мне необходимо вызвать два конструктора (для класса CurrencyConv, второй для унаследования класса)
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_Ui()

 # поменяем название и иконку приложения
    def init_Ui(self):
        self.setWindowTitle('CurrencyConverter')
        self.setWindowIcon(QIcon('exchanging.png'))

        # сделаем подсказки в объектах лайн эдит(куда вписывать запрашиваемую информацию ввода)
        self.ui.input_currency.setPlaceholderText('from the currency:')
        self.ui.input_amount.setPlaceholderText('I have:')
        self.ui.output_currency.setPlaceholderText('to currency:')
        self.ui.pushButton.clicked.connect(self.converter)

        # создадим функцию, в которой будет выполняться конвертация денежных средств

    def converter(self):
        c = CurrencyConverter()
        c.convert(1, 'USD', 'EUR')  # нужно для корректной работы библиотеки
        print(c.currencies)
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())
        if input_currency in c.currencies:
            if output_currency in c.currencies:
                if input_amount > 0:
                    output_amount = round(c.convert(input_amount, '%s' % input_currency, '%s' % output_currency), 2)
                    self.ui.output_amount.setText(str(output_amount))
                else:
                    self.ui.output_amount.setText('Enter another number')
            else:
                self.ui.output_amount.setText('The second currency is not supported')
        else:
            self.ui.output_amount.setText('The first currency is not supported')


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

    # вызовем основной цикл обработки события и вызможность выхода из него
sys.exit(app.exec())