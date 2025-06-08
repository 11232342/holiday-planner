from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 30, 711, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItems(["საქართველო", "იტალია", "ესპანეთი", "საბერძნეთი", "საფრანგეთი"])

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 120, 711, 41))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItems(["მუზეუმი", "სანაპირო", "ეკლესია/მონასტრები", "სხვადასხვა ღირშესანიშნაობები"])

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 711, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 300, 711, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 350, 711, 41))
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 400, 711, 151))
        self.textBrowser.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 101, 21))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 95, 191, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 185, 211, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 276, 171, 20))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.flagLabel = QtWidgets.QLabel(self.centralwidget)
        self.flagLabel.setGeometry(QtCore.QRect(640, 440, 100, 60))
        self.flagLabel.setMinimumSize(QtCore.QSize(100, 60))
        self.flagLabel.setText("")
        self.flagLabel.setObjectName("flagLabel")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.recommend_tour)
        self.comboBox.currentIndexChanged.connect(self.update_flag)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Holiday Planner"))
        self.pushButton.setText(_translate("MainWindow", "ძებნა"))
        self.label.setText(_translate("MainWindow", "ქვეყანა"))
        self.label_2.setText(_translate("MainWindow", "სასურველი აქტივობები"))
        self.label_3.setText(_translate("MainWindow", "ხანგრძლივობა(დღეები)"))
        self.label_4.setText(_translate("MainWindow", "ბიუჯეტი(ლარი)"))

    def update_flag(self):
        country = self.comboBox.currentText()
        if not country:
            self.flagLabel.clear()
            return
        image_path = os.path.join("flags", f"{country}.png")
        if os.path.exists(image_path):
            pixmap = QtGui.QPixmap(image_path).scaled(100, 60, QtCore.Qt.KeepAspectRatio)
            self.flagLabel.setPixmap(pixmap)
        else:
            self.flagLabel.clear()

    def recommend_tour(self):
        country = self.comboBox.currentText()
        activity = self.comboBox_2.currentText()
        try:
            duration = int(self.lineEdit.text())
            budget = float(self.lineEdit_2.text())
        except ValueError:
            self.textBrowser.setText("გთხოვთ შეიყვანოთ სწორი რიცხვები ხანგრძლივობასა და ბიუჯეტში.")
            return

        recommendations = {
            "საქართველო": {
                "მუზეუმი": {"places": ["საქართველოს მუზეუმი", "ხელოვნების მუზეუმი"], "min_days": 2, "min_budget": 300},
                "სანაპირო": {"places": ["ბათუმის პლაჟი", "ქობულეთი"], "min_days": 3, "min_budget": 400},
                "ეკლესია/მონასტრები": {"places": ["გელათი", "მცხეთის სვეტიცხოველი"], "min_days": 2, "min_budget": 200},
                "სხვადასხვა ღირშესანიშნაობები": {"places": ["ნარიყალა", "ტფილისის ძველი უბანი"], "min_days": 2, "min_budget": 250},
            },
            "იტალია": {
                "მუზეუმი": {"places": ["ვატიკანის მუზეუმი", "ურბინოს გალერეა"], "min_days": 3, "min_budget": 1200},
                "სანაპირო": {"places": ["ამალფის სანაპირო", "სიცილია"], "min_days": 4, "min_budget": 1500},
                "ეკლესია/მონასტრები": {"places": ["რომის ტაძრები", "ფლორენციის ეკლესიები"], "min_days": 3, "min_budget": 1000},
                "სხვადასხვა ღირშესანიშნაობები": {"places": ["კოლიზეუმი", "ვენეცია"], "min_days": 4, "min_budget": 1400},
            },
            "ესპანეთი": {
                "მუზეუმი": {"places": ["პრადოს მუზეუმი", "სიურეალისტური მუზეუმი"], "min_days": 3, "min_budget": 1000},
                "სანაპირო": {"places": ["კოსტა ბრავა", "იბიცა"], "min_days": 5, "min_budget": 1600},
                "ეკლესია/მონასტრები": {"places": ["საგრადა ფამილია", "მონტსერატის მონასტერი"], "min_days": 3, "min_budget": 900},
                "სხვადასხვა ღირშესანიშნაობები": {"places": ["ბარსელონა", "მადრიდი"], "min_days": 4, "min_budget": 1100},
            },
            "საბერძნეთი": {
                "მუზეუმი": {"places": ["ათენის არქეოლოგიური მუზეუმი"], "min_days": 2, "min_budget": 800},
                "სანაპირო": {"places": ["სანტორინი", "მიკონოსი"], "min_days": 4, "min_budget": 1400},
                "ეკლესია/მონასტრები": {"places": ["მეტეორა", "ათონის მთა"], "min_days": 3, "min_budget": 1000},
                "სხვადასხვა ღირშესანიშნაობები": {"places": ["აკროპოლისი", "დელფოი"], "min_days": 3, "min_budget": 1200},
            },
            "საფრანგეთი": {
                "მუზეუმი": {"places": ["ლუვრი", "ორსეის მუზეუმი"], "min_days": 3, "min_budget": 1300},
                "სანაპირო": {"places": ["ნიცა", "კანი"], "min_days": 4, "min_budget": 1600},
                "ეკლესია/მონასტრები": {"places": ["ნოტრ დამი", "მონ-სენ-მიშელი"], "min_days": 3, "min_budget": 1200},
                "სხვადასხვა ღირშესანიშნაობები": {"places": ["პარიზი", "ვერსალი"], "min_days": 4, "min_budget": 1500},
            },
        }

        if not country or not activity:
            self.textBrowser.setText("გთხოვთ აირჩიოთ ორივე - ქვეყანა და აქტივობა.")
            return

        info = recommendations.get(country, {}).get(activity)
        if info:
            if duration < info["min_days"]:
                self.textBrowser.setText("სამწუხაროდ ვერ მოიძებნა შესაბამისი ტური. მიუთითეთ მეტი დღე.")
            elif budget < info["min_budget"]:
                self.textBrowser.setText("სამწუხაროდ ვერ მოიძებნა შესაბამისი ტური. ბიუჯეტი არ არის საკმარისი.")
            else:
                places = "\n- " + "\n- ".join(info["places"])
                self.textBrowser.setText(
                    f"🇨🇵 რეკომენდებული ტური {country}-ში ({activity}):\n"
                    f"{places}\n\n"
                    f"🔹 მინ. დღეები: {info['min_days']}, მინ. ბიუჯეტი: ₾{info['min_budget']}"
                )
        else:
            self.textBrowser.setText("სამწუხაროდ ვერ მოიძებნა შესაბამისი ტური. სცადეთ სხვა პარამეტრები.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


