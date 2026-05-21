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
from kivy.utils import platform

# Only resize window on desktop — ignored on Android/iOS
if platform not in ('android', 'ios'):
    Window.size = (360, 640)


class PasswordGeneratorApp(App):
    def build(self):
        self.title = "Password Generator"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=12)

        layout.add_widget(Label(
            text="Password Generator",
            font_size='22sp',
            bold=True,
            size_hint_y=None,
            height=48
        ))

        # Length row
        length_row = BoxLayout(orientation='horizontal', size_hint_y=None, height=48, spacing=10)
        length_row.add_widget(Label(text="Length:", font_size='16sp', size_hint_x=0.4))
        self.length_input = TextInput(
            text="16",
            multiline=False,
            input_filter='int',
            font_size='18sp',
            size_hint_x=0.6
        )
        length_row.add_widget(self.length_input)
        layout.add_widget(length_row)

        # Checkboxes
        self.uppercase_chk, uc_row = self._checkbox_row("Uppercase (A–Z)")
        self.lowercase_chk, lc_row = self._checkbox_row("Lowercase (a–z)")
        self.numbers_chk,   nb_row = self._checkbox_row("Numbers (0–9)")
        self.symbols_chk,   sy_row = self._checkbox_row("Symbols (!@#$)")

        for row in (uc_row, lc_row, nb_row, sy_row):
            layout.add_widget(row)

        # Output field
        self.result_input = TextInput(
            text="Tap Generate…",
            readonly=True,
            font_size='16sp',
            halign='center',
            size_hint_y=None,
            height=56
        )
        layout.add_widget(self.result_input)

        # Buttons
        gen_btn = Button(
            text="Generate Password",
            font_size='18sp',
            background_color=(0.1, 0.6, 0.4, 1),
            size_hint_y=None,
            height=52
        )
        gen_btn.bind(on_press=self.generate_password)
        layout.add_widget(gen_btn)

        copy_btn = Button(
            text="Copy to Clipboard",
            font_size='16sp',
            background_color=(0.2, 0.4, 0.8, 1),
            size_hint_y=None,
            height=48
        )
        copy_btn.bind(on_press=self.copy_password)
        layout.add_widget(copy_btn)

        self.status_label = Label(
            text="",
            font_size='14sp',
            size_hint_y=None,
            height=30,
            color=(0.3, 0.9, 0.5, 1)
        )
        layout.add_widget(self.status_label)

        return layout

    def _checkbox_row(self, label_text):
        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        chk = CheckBox(active=True, size_hint_x=0.15)
        row.add_widget(chk)
        row.add_widget(Label(text=label_text, font_size='15sp', size_hint_x=0.85))
        return chk, row

    def generate_password(self, _instance):
        try:
            length = int(self.length_input.text)
        except ValueError:
            self.result_input.text = "Enter a valid number!"
            return

        if length < 4:
            self.result_input.text = "Minimum length is 4!"
            return
        if length > 256:
            self.result_input.text = "Maximum length is 256!"
            return

        pool = ""
        guaranteed = []

        if self.uppercase_chk.active:
            pool += string.ascii_uppercase
            guaranteed.append(random.choice(string.ascii_uppercase))
        if self.lowercase_chk.active:
            pool += string.ascii_lowercase
            guaranteed.append(random.choice(string.ascii_lowercase))
        if self.numbers_chk.active:
            pool += string.digits
            guaranteed.append(random.choice(string.digits))
        if self.symbols_chk.active:
            pool += string.punctuation
            guaranteed.append(random.choice(string.punctuation))

        if not pool:
            self.result_input.text = "Select at least one type!"
            return

        remaining = [random.choice(pool) for _ in range(length - len(guaranteed))]
        all_chars = guaranteed + remaining
        random.shuffle(all_chars)

        self.result_input.text = "".join(all_chars)
        self.status_label.text = ""

    def copy_password(self, _instance):
        PLACEHOLDERS = {
            "Tap Generate…",
            "Enter a valid number!",
            "Minimum length is 4!",
            "Maximum length is 256!",
            "Select at least one type!",
            ""
        }
        pwd = self.result_input.text
        if pwd not in PLACEHOLDERS:
            Clipboard.copy(pwd)
            self.status_label.text = "Copied!"
        else:
            self.status_label.text = "Generate a password first."


if __name__ == '__main__':
    PasswordGeneratorApp().run()
