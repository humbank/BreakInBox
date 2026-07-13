from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QFont, QFontDatabase
import threading
import sys
from rooms import Room
from comm import *
from esps import *



class Game():
    def __init__(self, app):

        self.app = app
        
        self.loader = QUiLoader()
        self.ui_file = QFile("./ui/new_start.ui")

        if not self.ui_file.open(QFile.ReadOnly):
            print("Cannot open UI")
            sys.exit(1)
        
        
        self.fonts = ["October Crow", "digital-7"]
        
        self.test_room = Room("Test Room", 2, ["This is a test romm", "This is thbe end of the test rookm"], {"hint1":"test", "hint2":"test2"})
        self.laser_room = Room("Laser Room", 1, ["Can you connect the laser and the diode?"], {"hint1":"x degree"}, total_time=180, required_deletes=["pb_submit", "stacked_puzzle_content"])
        self.comm_test_room = Room("Led test", 1, ["Led test"], ["no"], 1000)

        self.rooms = {"Test Room":self.test_room, "Laser Room":self.laser_room, "Led test": self.comm_test_room}



        self.current_room_nbr = 1
        self.current_room = None

        self.time_remaining = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)
        
        self.window = self.loader.load(self.ui_file)
        self.ui_file.close()

        self.window.setWindowIcon(QIcon("UI/assets/icons/app_icon.jpeg"))

        self.window.stackedWidget.setCurrentWidget(self.window.page_start)

        self.window.show()

        self.setup()


    def setup(self):
        self.load_fonts(self.fonts)

        self.populate_rooms(self.rooms)
        self.start_screen()
        self.menu_screen()
        self.admin_screen()

        threading.Thread(target=read, daemon=True).start()




    def start_screen(self):
        self.window.pb_start_no.clicked.connect(lambda: QApplication.quit())
        self.window.pb_start_yes.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_menu))

    def menu_screen(self):
        self.window.pb_admin_menu.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_admin))
        self.window.pb_back_menu.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_start))
        self.window.lst_menu.itemClicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_puzzle))
        self.window.lst_menu.itemClicked.connect(self.room_item_clicked)

    def admin_screen(self):
        self.window.pb_back_admin.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_menu))

    def puzzle_screen(self):
        self.window.pb_puzzle_back.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_menu))
        self.window.lbl_puzzle_nbr.setText(f'{self.current_room_nbr}/{self.current_room.room_total}')
        self.window.lbl_puzzle_descr.setText(self.current_room.descriptions[self.current_room_nbr-1])

        self.window.pb_led1_on.clicked.connect(lambda: ESP().one.led_on())
        self.window.pb_led1_off.clicked.connect(lambda: ESP().one.led_off())
        self.window.pb_led2_on.clicked.connect(lambda: ESP().two.led_on())
        self.window.pb_led2_off.clicked.connect(lambda: ESP().two.led_off())

        for name in self.current_room.required_deletes:
            widget = getattr(self.window, name, None)
            if widget is not None:
                widget.deleteLater()
        

    def update_countdown(self):
        self.window.lbl_countdown_puzzle.setText(self.format_time(self.time_remaining))
        self.time_remaining -= 1

        if self.time_remaining < 0:
            self.timer.stop()



    def format_time(self, seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02}:{secs:02}"



    def populate_rooms(self, rooms):
        for Room in rooms.values():
            self.window.lst_menu.addItem(Room.name)


    def load_fonts(self, fonts):
        #self.added_fonts = []

        for font in fonts:
            font_id = QFontDatabase.addApplicationFont(f"./assets/fonts/{font}.ttf")

            if font_id == -1:
                print("Failed to load font!")
            else:
                family = QFontDatabase.applicationFontFamilies(font_id)[0]
                #self.added_fonts.append(QFont(family))


    ########################################
    #         HELPER FUNCTIONS              
    ########################################
    def room_item_clicked(self, item):
        self.current_room = self.rooms[item.text()]
        self.time_remaining = self.current_room.total_time
        self.timer.start(1000)
        self.update_countdown()
        self.puzzle_screen()
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game(app)
    sys.exit(app.exec())