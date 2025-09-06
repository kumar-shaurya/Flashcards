import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

import json
import os

DARK_BG = "#181A20"
DARK_CARD = "#23272F"
DARK_ACCENT = "#1F222A"
DARK_BTN = "#2F3136"
DARK_BTN_HOVER = "#40444B"
DARK_TEXT = "#F5F6FA"
DARK_TEXT_FAINT = "#A0A3B1"
DARK_ACCENT2 = "#7289DA"

class FlashcardApp(toga.App):
    def startup(self):

        self.load_cards()
        self.index = 0
        self.show_answer = False
        primary_screen = self.screens[0]
        screen_size = primary_screen.size
        self.is_main = True

        # Screen 1
        self.main_box = toga.Box(
            style=Pack(direction=COLUMN, alignment=CENTER, padding=0, background_color=DARK_BG, flex=1)
        )
        self.top_box = toga.Box(
            style=Pack(direction="row", alignment=CENTER, padding_top=30, padding_bottom=20, background_color=DARK_BG, width=screen_size.width)
        )
        self.bottom_box = toga.Box(
            style=Pack(direction=COLUMN, alignment=CENTER, padding=0, background_color=DARK_BG, flex=1, width=screen_size.width)
        )

        # Add question number label
        self.question_number_label = toga.Label(
            text=f"Q {self.index + 1} / {len(self.cards)}" if self.cards else "Q 0 / 0",
            style=Pack(
                color=DARK_TEXT_FAINT,
                font_size=18,
                padding_left=20,
                padding_right=20
            )
        )

        self.add_btn = toga.Button(
            "+",
            on_press=self.mode_change,
            style=Pack(
                padding_left=20, padding_right=20, padding_top=8, padding_bottom=8,
                background_color=DARK_ACCENT2,
                color=DARK_TEXT,
                font_size=28,
                margin_left=0,
                margin_right=0
            )
        )

        self.delete_btn = toga.Button(
            "DEL",
            on_press=self.delete_card,
            style=Pack(
                padding_left=20, padding_right=20, padding_top=8, padding_bottom=8,
                background_color=DARK_ACCENT2,
                color=DARK_TEXT,
                font_size=28,
                margin_left=0,
                margin_right=0
            )
        )

        self.lable_button = toga.Button(
            self.cards[self.index][0] if self.cards else "No cards available. Please add a new card.",
            on_press=self.show_answer_func,
            style=Pack(
                padding=30,
                color=DARK_TEXT,
                font_size=22,
                background_color=DARK_CARD,
                width=screen_size.width * 0.8,
                height=screen_size.height * 0.5,
                margin_top=30,
                margin_bottom=30
            )
        )

        # Navigation buttons
        self.prev_btn = toga.Button(
            "⟨",
            on_press=self.prev_card,
            style=Pack(
                padding_left=24, padding_right=24, padding_top=10, padding_bottom=10,
                background_color=DARK_BTN,
                color=DARK_TEXT,
                font_size=20,
                margin_right=20
            )
        )
        self.next_btn = toga.Button(
            "⟩",
            on_press=self.next_card,
            style=Pack(
                padding_left=24, padding_right=24, padding_top=10, padding_bottom=10,
                background_color=DARK_BTN,
                color=DARK_TEXT,
                font_size=20,
                margin_left=20
            )
        )

        self.nav_box = toga.Box(
            children=[self.prev_btn, self.next_btn],
            style=Pack(direction="row", alignment=CENTER, padding_top=10, padding_bottom=10)
        )

        # Screen 2 (Add Card)
        self.add_box = toga.Box(
            style=Pack(direction=COLUMN, alignment=CENTER, padding_top=40, background_color=DARK_BG, flex=1)
        )
        self.question_label = toga.Label(
            text="Enter Question:",
            style=Pack(padding=5, color=DARK_TEXT_FAINT, font_size=16)
        )
        self.question_input = toga.TextInput(
            style=Pack(
                padding=10, background_color=DARK_CARD, color=DARK_TEXT,
                font_size=16, width=screen_size.width * 0.7, margin_bottom=10
            )
        )
        self.answer_label = toga.Label(
            text="Enter Answer:",
            style=Pack(padding=5, color=DARK_TEXT_FAINT, font_size=16)
        )
        self.answer_input = toga.TextInput(
            style=Pack(
                padding=10, background_color=DARK_CARD, color=DARK_TEXT,
                font_size=16, width=screen_size.width * 0.7, margin_bottom=20
            )
        )
        self.save_btn = toga.Button(
            "Save",
            on_press=self.save_card,
            style=Pack(
                padding_left=30, padding_right=30, padding_top=12, padding_bottom=12,
                background_color=DARK_ACCENT2,
                color=DARK_TEXT,
                font_size=18,
                margin_bottom=10
            )
        )
        self.main_btn = toga.Button(
            "Back",
            on_press=self.mode_change,
            style=Pack(
                padding_left=30, padding_right=30, padding_top=12, padding_bottom=12,
                background_color=DARK_BTN,
                color=DARK_TEXT,
                font_size=18
            )
        )

        # Placing UI elements
        self.add_box.add(
            self.question_label,
            self.question_input,
            self.answer_label,
            self.answer_input,
            self.save_btn,
            self.main_btn
        )

        self.main_box.add(self.top_box, self.bottom_box)
        self.top_box.add(self.question_number_label, self.add_btn, self.delete_btn)
        self.bottom_box.add(self.lable_button, self.nav_box)

        self.main_window = toga.MainWindow(title="Flashcards")
        self.main_window.content = self.main_box
        self.main_window.show()

    def show_answer_func(self, widget):
        if self.show_answer:
            self.lable_button.text = self.cards[self.index][0]
            self.show_answer = False
        else:
            self.lable_button.text = self.cards[self.index][1]
            self.show_answer = True

    def prev_card(self, widget):
        if self.index > 0:
            self.index -= 1
            self.update_card()

    def next_card(self, widget):
        if self.index < len(self.cards) - 1:
            self.index += 1
            self.update_card()

    def update_card(self):
        self.lable_button.text = self.cards[self.index][0]
        self.show_answer = False
        self.question_number_label.text = f"Q {self.index + 1} / {len(self.cards)}"

    def mode_change(self, widget):
        if self.is_main:
            self.is_main = False
            self.main_window.content = self.add_box
            self.question_input.value = ""
            self.answer_input.value = ""
        else:
            self.is_main = True
            self.main_window.content = self.main_box
            self.index = 0
            self.update_card()

    def save_card(self, widget):
        question = self.question_input.value
        answer = self.answer_input.value
        if question and answer:
            self.cards.append((question, answer))
            self.question_input.value = ""
            self.answer_input.value = ""
            self.question_number_label.text = f"Q {self.index + 1} / {len(self.cards)}"
            self.dump_cards()

    def delete_card(self, widget):
        if self.cards:
            del self.cards[self.index]
            if len(self.cards) == 0:
                self.lable_button.text = "No cards available. Please add a new card."
                self.show_answer = False
                self.question_number_label.text = "Q 0 / 0"
            else:
                self.index = min(self.index, len(self.cards) - 1)
                self.update_card()
        self.dump_cards()
        
    def on_exit(self):
        self.dump_cards()
        return True

    def dump_cards(self):
        # Save as list of lists for JSON compatibility
        try:
            cards_to_save = [list(card) for card in self.cards]
            json_path = os.path.join(os.path.expanduser("~"), "cards.json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(cards_to_save, f)
        except IOError:
            print("Error: Could not save card data.")

    def load_cards(self):
        json_path = os.path.join(os.path.expanduser("~"), "cards.json")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                self.cards = [tuple(card) for card in loaded]
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist or is empty/corrupt, so use the default cards
            self.cards = [
                ("What is the capital of France?", "Paris"),
                ("Who wrote Harry Potter?", "J.K. Rowling"),
                ("Largest planet in Solar System?", "Jupiter"),
            ]
        except IOError:
            print("Error: Could not load card data.")
            self.cards = [
                ("What is the capital of France?", "Paris"),
                ("Who wrote Harry Potter?", "J.K. Rowling"),
                ("Largest planet in Solar System?", "Jupiter"),
            ]
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.cards = [
                ("What is the capital of France?", "Paris"),
                ("Who wrote Harry Potter?", "J.K. Rowling"),
                ("Largest planet in Solar System?", "Jupiter"),
            ]

def main():
    return FlashcardApp()