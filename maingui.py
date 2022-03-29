import pandas as pd
import csv
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import pickle


class ShowImage(QMainWindow) :
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('gui.ui', self)
        self.pushButton_input.clicked.connect(self.inputdata)
        self.pushButton_result.clicked.connect(self.predict)
        self.pushButton_reset.clicked.connect(self.resetdata)
        desired_width = 320
        pd.set_option('display.width', desired_width)
        pd.set_option('display.max_columns', 21)


    def inputdata(self):
        c1 = '1'
        c2 = self.textEdit.toPlainText()
        c3 = self.textEdit_2.toPlainText()
        c4 = self.textEdit_3.toPlainText()
        c5 = self.textEdit_4.toPlainText()
        c6 = self.textEdit_5.toPlainText()
        c7 = self.textEdit_6.toPlainText()
        c8 = self.textEdit_7.toPlainText()
        c9 = self.textEdit_8.toPlainText()
        c10 = self.textEdit_9.toPlainText()
        c11 = self.textEdit_10.toPlainText()
        c12 = self.textEdit_11.toPlainText()
        c13 = self.textEdit_12.toPlainText()
        c14 = self.textEdit_13.toPlainText()
        c15 = self.textEdit_14.toPlainText()
        c16 = self.textEdit_15.toPlainText()
        c17 = self.textEdit_16.toPlainText()
        c18 = self.textEdit_17.toPlainText()


        with open('maketest.csv', 'w', newline='') as f:
            fieldnames = ['id', 'battery_power', 'blue', 'dual_sim', 'fc',
                          'four_g', 'int_memory', 'm_dep', 'n_cores', 'pc',
                          'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time',
                          'three_g', 'wifi']
            writter = csv.DictWriter(f, fieldnames=fieldnames)

            writter.writeheader()
            writter.writerow({'id': c1, 'battery_power': c2, 'blue': c3, 'dual_sim': c4, 'fc': c5,
                              'four_g': c6, 'int_memory': c7, 'm_dep': c8, 'n_cores': c9, 'pc': c10,
                              'px_height': c11, 'px_width': c12, 'ram': c13, 'sc_h': c14, 'sc_w': c15,
                              'talk_time': c16, 'three_g': c17, 'wifi': c18})

        data = pd.read_csv("maketest.csv")

        print('Data Uji Berhasil di Input \n Silahkan Tekan Tombol Prediksi')


    def predict(self):
        # Memuat Model
        filename = 'phoneModel.pkl'
        model_load = pickle.load(open(filename, 'rb'))

        # Prediksi Data Testing
        print('Proses Prediksi Harga Handphone')
        test_data = pd.read_csv("maketest.csv")
        print('Data Uji')
        print(test_data.head(1))
        test_data = test_data.drop('id', axis=1)
        print(test_data.head(1))
        predicted_price_range = model_load.predict(test_data)
        print('')
        print('Hasil Prediksi')
        print(predicted_price_range)
        test_data['price_range'] = predicted_price_range
        print(test_data.head(1))

        self.textEdit_result.setText(str(predicted_price_range))


    def resetdata(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.textEdit_6.clear()
        self.textEdit_7.clear()
        self.textEdit_8.clear()
        self.textEdit_9.clear()
        self.textEdit_10.clear()
        self.textEdit_11.clear()
        self.textEdit_12.clear()
        self.textEdit_13.clear()
        self.textEdit_14.clear()
        self.textEdit_15.clear()
        self.textEdit_16.clear()
        self.textEdit_17.clear()
        self.textEdit_result.clear()


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = ShowImage()
    Window.setWindowTitle("Prediksi Harga Handphone")
    Window.show()
    sys.exit(app.exec_())