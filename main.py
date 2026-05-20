import random
import string
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard

Window.size = (360, 640)


class PasswordGeneratorApp(App):
    def build(self):
        self.title = "مولد كلمات المرور"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title_label = Label(
            text="Password Generator",
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title_label)

        input_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=50,
            spacing=10
        )
        self.len_label = Label(
            text="طول الكلمة:",
            font_size='16sp',
            size_hint_x=0.4
        )
        self.length_input = TextInput(
            text="12",
            multiline=False,
            input_filter='int',
            font_size='18sp',
            size_hint_x=0.6
        )
        input_layout.add_widget(self.len_label)
        input_layout.add_widget(self.length_input)
        layout.add_widget(input_layout)

        self.uppercase_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=40
        )
        self.uppercase_chk = CheckBox(active=True, size_hint_x=0.2)
        uppercase_lbl = Label(text="أحرف كبيرة (A-Z)", size_hint_x=0.8)
        self.uppercase_box.add_widget(self.uppercase_chk)
        self.uppercase_box.add_widget(uppercase_lbl)
        layout.add_widget(self.uppercase_box)

        self.lowercase_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=40
        )
        self.lowercase_chk = CheckBox(active=True, size_hint_x=0.2)
        lowercase_lbl = Label(text="أحرف صغيرة (a-z)", size_hint_x=0.8)
        self.lowercase_box.add_widget(self.lowercase_chk)
        self.lowercase_box.add_widget(lowercase_lbl)
        layout.add_widget(self.lowercase_box)

        self.numbers_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=40
        )
        self.numbers_chk = CheckBox(active=True, size_hint_x=0.2)
        numbers_lbl = Label(text="أرقام (0-9)", size_hint_x=0.8)
        self.numbers_box.add_widget(self.numbers_chk)
        self.numbers_box.add_widget(numbers_lbl)
        layout.add_widget(self.numbers_box)

        self.symbols_box = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=40
        )
        self.symbols_chk = CheckBox(active=True, size_hint_x=0.2)
        symbols_lbl = Label(text="رموز خاصة (!@#$)", size_hint_x=0.8)
        self.symbols_box.add_widget(self.symbols_chk)
        self.symbols_box.add_widget(symbols_lbl)
        layout.add_widget(self.symbols_box)

        self.result_input = TextInput(
            text="اضغط توليد...",
            readonly=True,
            font_size='18sp',
            halign='center',
            size_hint_y=None,
            height=60
        )
        layout.add_widget(self.result_input)

        generate_btn = Button(
            text="توليد كلمة مرور قوية",
            font_size='20sp',
            background_color=(0.1, 0.6, 0.4, 1),
            size_hint_y=None,
            height=50
        )
        generate_btn.bind(on_press=self.generate_password)
        layout.add_widget(generate_btn)

        copy_btn = Button(
            text="نسخ كلمة المرور",
            font_size='18sp',
            background_color=(0.2, 0.4, 0.8, 1),
            size_hint_y=None,
            height=50
        )
        copy_btn.bind(on_press=self.copy_password)
        layout.add_widget(copy_btn)

        self.status_label = Label(
            text="",
            font_size='14sp',
            size_hint_y=None,
            height=30,
            color=(0.2, 0.9, 0.5, 1)
        )
        layout.add_widget(self.status_label)

        return layout

    def generate_password(self, instance):
        try:
            length = int(self.length_input.text)
            if length < 4:
                self.result_input.text = "قصير جداً! (الأقل 4)"
                return
        except ValueError:
            self.result_input.text = "أدخل رقم صحيح!"
            return

        characters = ""
        guaranteed = []

        if self.uppercase_chk.active:
            characters += string.ascii_uppercase
            guaranteed.append(random.choice(string.ascii_uppercase))
        if self.lowercase_chk.active:
            characters += string.ascii_lowercase
            guaranteed.append(random.choice(string.ascii_lowercase))
        if self.numbers_chk.active:
            characters += string.digits
            guaranteed.append(random.choice(string.digits))
        if self.symbols_chk.active:
            characters += string.punctuation
            guaranteed.append(random.choice(string.punctuation))

        if not characters:
            self.result_input.text = "اختر نوع واحد على الأقل!"
            return

        remaining = [random.choice(characters) for _ in range(length - len(guaranteed))]
        all_chars = guaranteed + remaining
        random.shuffle(all_chars)

        self.result_input.text = "".join(all_chars)
        self.status_label.text = ""

    def copy_password(self, instance):
        pwd = self.result_input.text
        if pwd and pwd not in ("اضغط توليد...", "قصير جداً! (الأقل 4)", "أدخل رقم صحيح!", "اختر نوع واحد على الأقل!"):
            Clipboard.copy(pwd)
            self.status_label.text = "تم النسخ!"
        else:
            self.status_label.text = "لا توجد كلمة مرور للنسخ"


if __name__ == '__main__':
    PasswordGeneratorApp().run()
