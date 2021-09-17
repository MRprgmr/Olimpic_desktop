from PyQt5.QtGui import QIcon, QImage, QMovie, QPixmap
from PyQt5.QtWidgets import QComboBox, QDialog, QFileDialog, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem as ti
from PyQt5.QtCore import QSettings, QThread, Qt, pyqtSignal, pyqtSlot

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import xlwt

from Resources.Designs import main_window, server_dialog
from models import *

import requests

#Main window
class MainWindow(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #settings
        self.settings = QSettings('Olympiad_registration', 'Configs')

        #server address edit button
        self.set_but.clicked.connect(self.open_settings_edit)

        #set refresh button gif
        self.refr_gif = QMovie(':/mw_icons/refresh_gif.gif')
        self.refr_gif.start()
        self.refr_lab.setMovie(self.refr_gif)
        self.refr_lab.setVisible(False)
        self.refr_but.clicked.connect(self.refresh_olympiads)

        #table update data
        self.tw.setColumnHidden(0, True)
        self.tw.setColumnWidth(1, 260)
        self.tw.setColumnWidth(2, 260)
        self.tw.setColumnWidth(3, 180)
        self.update_table_data()
        self.del_but.clicked.connect(self.delete_button)
        self.clear_but.clicked.connect(self.delete_all)
        self.export_but.clicked.connect(self.export_as_excel)

        #set camera start and stop buttons
        self.stop_bot.setEnabled(False)
        self.start_but.clicked.connect(self.start_camera)
        self.stop_bot.clicked.connect(self.stop_camera)

        #set status panel
        self.correct_icon = QIcon(':/mw_icons/correct.png')
        self.incorrect_icon = QIcon(':/mw_icons/incorrect.png')
        self.status_info.setMovie(self.refr_gif)
        self.status_info.setVisible(False)
        self.status_info_icon.setVisible(False)
        self.status_text.setVisible(False)

    def export_as_excel(self):
        filename = QFileDialog.getSaveFileName(
                    self, 'Export as excel', '', "Excel (*.xls)")[0]
        if filename != "":
            wb = xlwt.Workbook()
            ws = wb.add_sheet('Registered users')
            ws.write(0, 0, "Ism Familiyasi")
            ws.write(0, 1, 'Sinfi')
            ws.write(0, 2, 'Telefon raqami')
            all_users = User.select()
            i = 1
            for user in all_users:
                ws.write(i, 0, f"{user.last_name} {user.first_name}")
                ws.write(i, 1, user.class_name)
                ws.write(i, 2, user.phone_number)
                i += 1
            wb.save(filename)

    def delete_all(self):
        ret = QMessageBox.question(self, 'Delete', "Are you sure to delete all data from from the list?", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if ret == QMessageBox.Yes:
            all = User.select()
            for item in all:
                item.delete_instance()
            self.update_table_data()

    def delete_button(self):
        if len(self.tw.selectedItems()) != 0:
            id = self.tw.item(self.tw.currentRow(), 0).text()
            ret = QMessageBox.question(self, 'Delete', "Are you sure to delete this user from the list?", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
            if ret == QMessageBox.Yes:
                User.get(User.id == int(id)).delete_instance()
                self.update_table_data()

    def update_table_data(self):
        users_data = User.select().order_by(User.last_name)
        self.tw.setRowCount(0)
        for user in users_data:
            rp = self.tw.rowCount()
            self.tw.insertRow(rp)
            self.tw.setItem(rp, 0, ti(str(user.id)))
            self.tw.setItem(rp, 1, ti(user.first_name))
            self.tw.setItem(rp, 2, ti(user.last_name))
            self.tw.setItem(rp, 3, ti(user.class_name))
            self.tw.setItem(rp, 4, ti(user.phone_number))
        self.label.setText(f"Total:          {self.tw.rowCount()}")

    def start_camera(self):
        if self.com_box.currentData() is not None:
            self.vth = VideoThread(self.com_box.currentData())
            self.vth.change_pixmap_signal.connect(self.update_image)
            self.vth.change_status_info.connect(self.chanche_status_info)
            self.vth.start()
            self.start_but.setEnabled(False)
            self.com_box.setEnabled(False)
            self.stop_bot.setEnabled(True) 
        else:
            QMessageBox.warning(self, "Error", "None of the olympiad hasn't been selected yet")

    def stop_camera(self):
        self.vth.stop()
        self.com_box.setEnabled(True)
        self.start_but.setEnabled(True)
        self.stop_bot.setEnabled(False)

    def hide_status_bar(self):
        self.status_info.setVisible(False)
        self.status_info_icon.setVisible(False)
        self.status_text.setVisible(False)

    @pyqtSlot(dict)
    def chanche_status_info(self, data):
        if data['status'] == 'checking':
            self.status_text.setText("Tekshirilmoqda")
            self.status_info.setVisible(True)
            self.status_text.setVisible(True)
            self.status_info_icon.setVisible(False)
        elif data['status'] == 'not_found':
            self.status_text.setText("Topilmadi")
            self.status_info_icon.setIcon(self.incorrect_icon)
            self.status_info.setVisible(False)
            self.status_info_icon.setVisible(True)
        elif data['status'] == 'wrong':
            QMessageBox.warning(self, "Error", "An error has occurred by server address or internet connection,\nplease make sure that your address is correct and you have\nstable internet connection.")
            self.status_info.setVisible(False)
            self.status_text.setVisible(False)
        elif data['status'] == 'accepted':
            self.status_text.setText("Qabul qilindi")
            self.status_info_icon.setIcon(self.correct_icon)
            self.status_info.setVisible(False)
            self.status_info_icon.setVisible(True)
            first_last_name = data['full_name'].split(' ')
            User.create(telegram_id=data['telegram_id'], first_name=first_last_name[1], last_name=first_last_name[0], class_name=data['class_name'], phone_number=data['phone_number'])
            self.update_table_data()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.cm.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(320, 240, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def open_settings_edit(self):
        self.settings_dialog = ServerDialog(self)
        self.settings_dialog.exec_()

    def refresh_olympiads(self):
        self.start_refresh_gif()
        self.olympiads_loader = Olympiads_thread(self.settings.value('server_address', str))
        self.olympiads_loader.data.connect(self.load_olympiads)
        self.olympiads_loader.start()

    def load_olympiads(self, data):
        if len(data) == 0:
            self.com_box.clear()
        elif data[0] == '505':
            QMessageBox.warning(self, "Error", "An error has occurred by server address or internet connection,\nplease make sure that your address is correct and you have\nstable internet connection.")
        else:
            self.com_box: QComboBox
            self.com_box.clear()
            for item in data:
                self.com_box.addItem(item['title'], item['id'])
        self.stop_refresh_gif()

    def start_refresh_gif(self):
        self.refr_but.setVisible(False)
        self.refr_lab.setVisible(True)
    
    def stop_refresh_gif(self):
        self.refr_but.setVisible(True)
        self.refr_lab.setVisible(False)

#Camera thread
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_status_info = pyqtSignal(dict)

    def __init__(self, olympiad_id):
        super().__init__()
        self._run_flag = True
        self.checking = True
        self.olympiad_id = olympiad_id

    def run(self):
        cap = cv2.VideoCapture(0)

        while self._run_flag:
            ret, cv_img = cap.read()

            if ret:
                qr_code = self.qr_decoder(cv_img)
                status = None
                if qr_code is not None:

                    points = qr_code.polygon
                    (x,y,w,h) = qr_code.rect
                    pts = np.array(points, np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(cv_img, [pts], True, (0, 255, 0), 4)

                    barcodeData = qr_code.data.decode("utf-8")

                    status = self.check_if_id(barcodeData)
                    if status == "exists":
                        text = "Ro'yxatga olingan"
                        color = (21, 232, 42)
                    elif status == "incorrect":
                        text = "Noto'g'ri"
                        color = (18, 109, 255)  
                    elif status == "to_check":
                        text = "Tekshirilmoqda"
                        color = (255, 0, 0)
                    cv2.putText(cv_img, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.7, color, 5)

                self.change_pixmap_signal.emit(cv_img)
                if self.checking and status == "to_check":
                    self.check_and_run(barcodeData.split('_')[1])
                    self.checking = False
        cap.release()
    
    def check_and_run(self, user_id):
        self.change_status_info.emit({
            'status': 'checking'
        })
        self.checker_thread = User_checker(self.olympiad_id, user_id)
        self.checker_thread.data.connect(self.change_status)
        self.checker_thread.run()

    @pyqtSlot(dict)
    def change_status(self, data):
        self.change_status_info.emit(data)
        self.checking = True

    def check_if_id(self, id):
        id = id.split('_')
        if len(id) == 2:
            if id[1].isdigit() and id[0] == 'id':
                usr = User.get_or_none(telegram_id=int(id[1]))
                if usr is not None:
                    return "exists"
                else:
                    return "to_check"
        return "incorrect"
            

    def qr_decoder(self, image):
        gray_img = cv2.cvtColor(image, 0)
        barcode = decode(gray_img)
        if len(barcode) == 0:
            return None
        else:
            return barcode[0]

    def stop(self):
        self._run_flag = False
        self.wait()

#user profile checker thread
class User_checker(QThread):
    data = pyqtSignal(dict)
    
    def __init__(self, olympiad_id, user_id):
        super(User_checker, self).__init__()
        self.settings = QSettings('Olympiad_registration', 'Configs')
        self.olympiad_id = olympiad_id
        self.user_id = user_id
    
    def run(self):
        try:
            PARAMS = {
                'olympiad_id': self.olympiad_id,
                'user_id': self.user_id
            }
            data = requests.get(url=f"{self.settings.value('server_address', str)}check_user/", params=PARAMS)
            self.data.emit(data.json())
        except:
            data = {
                'status': 'wrong',
            }
            self.data.emit(data)


#Olympiads loader thread
class Olympiads_thread(QThread):
    data = pyqtSignal(list)
 
    def __init__(self, url):
        super(Olympiads_thread, self).__init__()
        self.url = url
    
    def run(self):
        try:
            data = requests.get(self.url + 'get_olympiads')
            self.data.emit(data.json())
        except:
            self.data.emit(['505'])

# server address edit dialog
class ServerDialog(QDialog, server_dialog.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.settings = QSettings('Olympiad_registration', 'Configs')
        self.lineEdit.setText(self.settings.value('server_address', type=str))
        self.ok.clicked.connect(self.save)
        self.cancel.clicked.connect(self.close)
    
    def save(self):
        self.settings.setValue('server_address', self.lineEdit.text())
        self.accept()