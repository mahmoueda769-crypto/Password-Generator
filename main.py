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

MIN_LENGTH = 6
MAX_LENGTH = 64

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
        length_row.add_widget(Label(
            text=f"Length ({MIN_LENGTH}–{MAX_LENGTH}):",
            font_size='15sp',
            size_hint_x=0.5
        ))
        self.length_input = TextInput(
            text="16",
            multiline=False,
            input_filter='int',
            font_size='18sp',
            size_hint_x=0.5
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

        # Validation error label
        self.error_label = Label(
            text="",
            font_size='13sp',
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=28
        )
        layout.add_widget(self.error_label)

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
            font_size='13sp',
            color=(0.3, 0.9, 0.5, 1),
            size_hint_y=None,
            height=28
        )
        layout.add_widget(self.status_label)

        return layout

    def _checkbox_row(self, label_text):
        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        chk = CheckBox(active=True, size_hint_x=0.15)
        row.add_widget(chk)
        row.add_widget(Label(text=label_text, font_size='15sp', size_hint_x=0.85))
        return chk, row

    def _validate_length(self):
        """
        Validates the length input.
        Returns the integer length on success, or None on failure.
        Sets self.error_label with a descriptive message on failure.
        """
        raw = self.length_input.text.strip()

        if not raw:
            self.error_label.text = "⚠ Please enter a password length."
            return None

        if not raw.isdigit():
            self.error_label.text = "⚠ Length must be a whole number."
            return None

        length = int(raw)

        if length < MIN_LENGTH:
            self.error_label.text = (
                f"⚠ Length {length} is too short — minimum is {MIN_LENGTH}."
            )
            return None

        if length > MAX_LENGTH:
            self.error_label.text = (
                f"⚠ Length {length} is too long — maximum is {MAX_LENGTH}."
            )
            return None

        self.error_label.text = ""
        return length

    def generate_password(self, _instance):
        self.status_label.text = ""

        length = self._validate_length()
        if length is None:
            self.result_input.text = "Fix the error above and try again."
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
            self.error_label.text = "⚠ Select at least one character type."
            self.result_input.text = "Fix the error above and try again."
            return

        remaining = [random.choice(pool) for _ in range(length - len(guaranteed))]
        all_chars = guaranteed + remaining
        random.shuffle(all_chars)

        self.result_input.text = "".join(all_chars)

    def copy_password(self, _instance):
        PLACEHOLDERS = {
            "Tap Generate…",
            "Fix the error above and try again.",
            ""
        }
        pwd = self.result_input.text
        if pwd not in PLACEHOLDERS:
            Clipboard.copy(pwd)
            self.status_label.text = "✓ Copied to clipboard!"
            self.error_label.text = ""
        else:
            self.status_label.text = "Generate a password first."


if __name__ == '__main__':
    PasswordGeneratorApp().run()
