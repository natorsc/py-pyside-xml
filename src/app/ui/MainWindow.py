# -*- coding: utf-8 -*-
"""."""

from PySide6 import QtWidgets

from app.uic.Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, **kwargs):
        super(MainWindow, self).__init__(parent=parent)
        self.application = kwargs.get('application')

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self) -> None:
        text = self.ui.line_edit.text()
        if text.strip():
            self.ui.label.setText(text)
        else:
            self.ui.label.setText(self.tr('The text field is empty.'))


if __name__ == '__main__':
    raise Exception('[!] Run the main.py file [!]')
