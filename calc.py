import sys, re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy
)
from PyQt5.QtCore import Qt

# 허용된 문자만 받음
ALLOWED_PATTERN = re.compile(r'^[0-9+\-*/().% ]+$')

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("정세아 계산기")
        self.setMinimumWidth(320)
        self._build_ui()
        self._apply_style()

    def _build_ui(self):
        grid = QGridLayout(self)
        grid.setSpacing(6)

        # 디스플레이
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(False)   # 숫자/연산자 키보드 입력 허용
        self.display.setPlaceholderText("0")
        self.display.setFixedHeight(52)
        self.display.setTextMargins(8, 0, 8, 0)
        grid.addWidget(self.display, 0, 0, 1, 4)

        # 버튼
        buttons = [
            ("C",  1, 0), ("(",  1, 1), (")", 1, 2), ("←", 1, 3),
            ("7",  2, 0), ("8",  2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4",  3, 0), ("5",  3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1",  4, 0), ("2",  4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0",  5, 0), (".", 5, 1), ("%", 5, 2), ("+", 5, 3),
            ("=",  6, 0),
        ]

        for text, r, c in buttons:
            btn = QPushButton(text)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            if text == "=":
                grid.addWidget(btn, r, 0, 1, 4)
            else:
                grid.addWidget(btn, r, c)
            btn.clicked.connect(self.handle_button)

        # 엔터 입력 시 계산 실행
        self.display.returnPressed.connect(self.evaluate)
        # 이벤트 필터: Backspace만 처리
        self.display.installEventFilter(self)

    def _apply_style(self):
        self.setStyleSheet("""
            QWidget { background: #121317; color: #e9e9ee; }
            QLineEdit {
                background: #1a1c22; border: 1px solid #2a2d36; border-radius: 10px;
                font-size: 22px; padding: 6px 10px;
            }
            QPushButton {
                background: #232733; border: 1px solid #2f3342; border-radius: 12px;
                font-size: 18px; padding: 10px;
            }
            QPushButton:hover { background: #2a2f3d; }
            QPushButton:pressed { background: #1e2230; }
            QPushButton[text="="] {
                background: #5a6bff; border: 1px solid #4656d8; font-weight: 600;
            }
            QPushButton[text="/"], QPushButton[text="*"],
            QPushButton[text="-"], QPushButton[text="+"] {
                background: #2c3650;
            }
            QPushButton[text="C"], QPushButton[text="←"] {
                background: #3b2c36;
            }
        """)

    # 백스페이스만 동작
    def eventFilter(self, obj, event):
        if obj is self.display and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Backspace:
                self.backspace()
                return True
        return super().eventFilter(obj, event)

    def handle_button(self):
        text = self.sender().text()
        if text == "C":
            self.clear()
        elif text == "←":
            self.backspace()
        elif text == "=":
            self.evaluate()
        else:
            self.insert(text)

    def clear(self):
        self.display.clear()

    def backspace(self):
        s = self.display.text()
        self.display.setText(s[:-1])

    def insert(self, ch: str):
        self.display.insert(ch)

    def evaluate(self):
        expr = self.display.text().strip()
        if not expr:
            return
        if not ALLOWED_PATTERN.match(expr):
            self.display.setText("Error: Invalid input")
            return
        # 퍼센트 처리
        expr = re.sub(r'(\d+(\.\d+)?)\s*%', r'(\1/100)', expr)
        try:
            result = eval(expr, {"__builtins__": {}}, {})
        except ZeroDivisionError:
            self.display.setText("Error: Division by zero")
            return
        except Exception:
            self.display.setText("Error")
            return
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        self.display.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    sys.exit(app.exec_())
