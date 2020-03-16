import sys
import warnings

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

warnings.filterwarnings("ignore", category=DeprecationWarning)

font_size = 60


def create_fonts():
    # create custom font database and load custom font into it
    global fonts
    fonts = QFontDatabase()
    fonts.addApplicationFont("/fonts/LcdPhone.ttf")

    global lcd_font
    lcd_font = QFont("LCD Phone", font_size)


def create_colors():
    # Base = menu, widget background
    # Background = ???
    # Foreground = ???
    # Text = most text in windows and widgets
    # AlternateBase = ???
    # Window = window background
    # WindowText = text for widgets in window
    # Button = background of buttons, combobox etc.
    # ButtonText = foreground/text of buttons, combobox etc.
    # ToolTipText = text for tooltips
    # ToolTipBase = background of tooltips
    # BrightText = ???
    # Link = text which links to something
    # Highlight = highlight color (when hovering over widget)
    # HighlightText = highlight text color (when hovering over widget)

    # create color palettes
    global dark_palette
    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Base, QColor(15, 15, 20))
    dark_palette.setColor(QPalette.Background, QColor(6, 10, 23))
    dark_palette.setColor(QPalette.Foreground, QColor(10, 10, 10))
    dark_palette.setColor(QPalette.Text, QColor(220, 225, 230))
    dark_palette.setColor(QPalette.AlternateBase, QColor(5, 12, 19))
    dark_palette.setColor(QPalette.Window, QColor(20, 20, 25))
    dark_palette.setColor(QPalette.WindowText, QColor(220, 235, 235))
    dark_palette.setColor(QPalette.Button, QColor(15, 15, 20))
    dark_palette.setColor(QPalette.ButtonText, QColor(220, 230, 240))
    dark_palette.setColor(QPalette.ToolTipText, QColor(223, 233, 238))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(5, 15, 23))
    dark_palette.setColor(QPalette.BrightText, QColor(240, 250, 255))
    dark_palette.setColor(QPalette.Link, QColor(20, 50, 150))
    dark_palette.setColor(QPalette.Highlight, QColor(5, 5, 5))
    dark_palette.setColor(QPalette.HighlightedText, QColor(225, 230, 235))

    global light_palette
    light_palette = QPalette()

    light_palette.setColor(QPalette.Base, QColor(230, 240, 250))
    light_palette.setColor(QPalette.Background, QColor(230, 240, 250))
    light_palette.setColor(QPalette.Foreground, QColor(50, 50, 60))
    light_palette.setColor(QPalette.Text, QColor(20, 25, 30))
    light_palette.setColor(QPalette.AlternateBase, QColor(225, 235, 245))
    light_palette.setColor(QPalette.Window, QColor(230, 240, 250))
    light_palette.setColor(QPalette.WindowText, QColor(20, 25, 30))
    light_palette.setColor(QPalette.Button, QColor(225, 235, 245))
    light_palette.setColor(QPalette.ButtonText, QColor(20, 25, 30))
    light_palette.setColor(QPalette.ToolTipText, QColor(20, 25, 30))
    light_palette.setColor(QPalette.ToolTipBase, QColor(225, 235, 245))
    light_palette.setColor(QPalette.BrightText, QColor(10, 10, 15))
    light_palette.setColor(QPalette.Link, QColor(20, 50, 150))
    light_palette.setColor(QPalette.Highlight, QColor(240, 245, 250))
    light_palette.setColor(QPalette.HighlightedText, QColor(10, 10, 15))

    # global transparent_palette
    # transparent_palette = QPalette()
    # transparent_color = QColor(235, 245, 255, 250)
    #
    # transparent_palette.setColor(QPalette.Base, transparent_color)
    # transparent_palette.setColor(QPalette.Background, transparent_color)
    # transparent_palette.setColor(QPalette.Foreground, QColor(50, 50, 60))
    # transparent_palette.setColor(QPalette.Text, QColor(20, 25, 30))
    # transparent_palette.setColor(QPalette.AlternateBase, transparent_color)
    # transparent_palette.setColor(QPalette.Window, transparent_color)
    # transparent_palette.setColor(QPalette.WindowText, QColor(20, 25, 30))
    # transparent_palette.setColor(QPalette.Button, transparent_color)
    # transparent_palette.setColor(QPalette.ButtonText, QColor(20, 25, 30))
    # transparent_palette.setColor(QPalette.ToolTipText, QColor(20, 25, 30))
    # transparent_palette.setColor(QPalette.ToolTipBase, transparent_color)
    # transparent_palette.setColor(QPalette.BrightText, QColor(10, 10, 15))
    # transparent_palette.setColor(QPalette.Link, QColor(20, 50, 150))
    # transparent_palette.setColor(QPalette.Highlight, QColor(240, 245, 250))
    # transparent_palette.setColor(QPalette.HighlightedText, QColor(10, 10, 15))

    global current_palette
    current_palette = dark_palette


def apply_click(f_box, sl):
    sl_size = sl.value()
    font = f_box.currentFont()
    font.setPointSize(sl_size)
    DigitalClock.setFont(digital_clock, font)

    global font_size
    font_size = font.pointSize()


class OptionsWindow(QMainWindow):
    def __init__(self):
        super(OptionsWindow, self).__init__()

        self.setWindowTitle("Widget Options")
        self.setFixedSize(650, 450)
        self.setPalette(current_palette)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        # create options list
        self.options_list = QListWidget()
        self.options_list.setFixedWidth(150)
        self.options_list.insertItem(0, "Font")
        self.options_list.insertItem(1, "Color")

        self.font_settings = QWidget()
        self.color_settings = QWidget()

        self.show_font_settings()
        self.show_color_settings()

        # create a stacked widget, add font and color settings
        self.Stack = QStackedWidget()
        self.Stack.addWidget(self.font_settings)
        self.Stack.addWidget(self.color_settings)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setFixedWidth(150)
        self.cancel_button.clicked.connect(lambda: self.close())

        self.apply_button = QPushButton("Apply")
        self.apply_button.setFixedWidth(100)
        self.apply_button.clicked.connect(lambda: apply_click(font_box, font_size_slider))

        self.ok_button = QPushButton("OK")
        self.ok_button.setFixedWidth(75)
        self.ok_button.clicked.connect(lambda: self.ok_click())

        main_layout = QVBoxLayout()

        options_layout = QHBoxLayout()
        options_layout.addWidget(self.options_list)
        options_layout.addWidget(self.Stack)

        font_btn_layout = QGridLayout()

        font_btn_layout.addWidget(self.cancel_button, 0, 0, 0, 2)
        font_btn_layout.addWidget(self.apply_button, 0, 1)
        font_btn_layout.addWidget(self.ok_button, 0, 2)

        main_layout.addLayout(options_layout)
        main_layout.addLayout(font_btn_layout)

        self.main_widget.setLayout(main_layout)

        self.options_list.currentRowChanged.connect(self.display_settings)
        self.show()

    def ok_click(self):
        apply_click(font_box, font_size_slider)
        self.close()

    def show_font_settings(self):
        main_layout = QVBoxLayout()
        font_settings_layout = QVBoxLayout()

        font_label = QLabel("Choose Font:")

        global font_box
        font_box = QFontComboBox()
        font_box.setCurrentFont(DigitalClock.font(digital_clock))

        font_size_label = QLabel("Choose Font Size:")

        global font_size_slider
        font_size_slider = QSlider(Qt.Horizontal)
        font_size_slider.setMinimum(50)
        font_size_slider.setMaximum(80)
        font_size_slider.setValue(font_size)

        font_size_slider.setTickPosition(QSlider.TicksRight)
        font_size_slider.setTickInterval(5)
        font_size_slider.setSingleStep(1)

        font_settings_layout.addWidget(font_label)
        font_settings_layout.addWidget(font_box)
        font_settings_layout.addWidget(font_size_label)
        font_settings_layout.addWidget(font_size_slider)
        font_settings_layout.setAlignment(Qt.AlignTop)

        main_layout.addLayout(font_settings_layout)

        self.font_settings.setLayout(main_layout)

    def change_colors(self, c_b):
        c_item = c_b.currentItem()

        global current_palette
        if c_item.text() == "Default Dark":
            current_palette = dark_palette
        elif c_item.text() == "Light":
            current_palette = light_palette
        # elif c_item.text() == "Transparent":
        #     current_palette = transparent_palette
        #     make_transparent(self)

        self.setPalette(current_palette)
        DigitalClock.setPalette(digital_clock, current_palette)

    def show_color_settings(self):
        main_layout = QVBoxLayout()
        color_settings_layout = QVBoxLayout()

        global color_box
        color_box = QListWidget()

        default_dark_theme = QListWidgetItem("Default Dark")

        light_theme = QListWidgetItem("Light")

        # transparent_theme = QListWidgetItem("Transparent")

        color_box.insertItem(0, default_dark_theme)
        color_box.insertItem(1, light_theme)
        # color_box.insertItem(2, transparent_theme)

        color_box.clicked.connect(lambda: self.change_colors(color_box))

        color_settings_layout.addWidget(color_box)
        color_settings_layout.setAlignment(Qt.AlignTop)

        main_layout.addLayout(color_settings_layout)

        self.color_settings.setLayout(main_layout)

    def display_settings(self, i):
        self.Stack.setCurrentIndex(i)


class DigitalClock(QMainWindow):
    def __init__(self):
        super(DigitalClock, self).__init__()

        self.title = "Digital Clock Widget"

        self.main_layout = QHBoxLayout()
        self.main_widget = QWidget(self)

        # allow for custom context menu and connect context menu request to custom event function
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.context_menu_event)

        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle(self.title)
        self.setAutoFillBackground(True)

        self.setGeometry(100, 100, 0, 0)
        self.setMaximumSize(1, 1)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)

        create_fonts()
        create_colors()
        self._create_context_menu()
        self._create_clock()

        self.show()

        self.setFont(lcd_font)

        # set window color scheme to color palette
        global current_palette
        self.setPalette(current_palette)

    def _create_options_window(self):
        self.options_window = OptionsWindow()
        self.options_window.show()

    def _create_context_menu(self):
        # create context menu
        self.context_menu = QMenu(self)
        self.context_menu.setPalette(dark_palette)

        # create action and connect it to function
        self.color_action = QAction("Options", self)
        self.color_action.triggered.connect(self._create_options_window)

        # add action to context menu
        self.context_menu.addAction(self.color_action)

    def context_menu_event(self, event):
        # execute context menu at mouse position
        self.context_menu.exec_(self.mapToGlobal(event))

    def _create_clock(self):
        # create label for holding time
        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.clock)

        # create timer and connect to show_time function
        clock_timer = QTimer(self)
        clock_timer.timeout.connect(self.show_time)
        clock_timer.start(100)

    def show_time(self):
        # get current time and make it a string
        cur_time = QTime.currentTime()
        time_str = cur_time.toString('hh:mm:ss')

        # set clock text
        self.clock.setText(time_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    digital_clock = DigitalClock()
    digital_clock.show()

    sys.exit(app.exec_())
