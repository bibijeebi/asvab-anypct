#!/usr/bin/env python3

from cyclopts import App

app = App()

# ASVAB topics and theitupleresponding questions
# TOPICS: dict[str, list[tuple[str, str]]] = {
#     "Word Knowledge": [
#         ("Synonym for 'benevolent':", "Kind"),
#         ("Antonym for 'verbose':", "Concise"),
#         ("Definition of 'arduous':", "Difficult or demanding"),
#     ],
#     "Arithmetic Reasoning": [
#         ("If a car travels 60 miles per hour, how far will it go in 2.5 hours?", "150 miles"),
#         ("If 3 pens cost $4.50, how much do 7 pens cost?", "$10.50"),
#         ("What is 15% of 80?", "12"),
#     ],
#     "Mathematics Knowledge": [
#         ("What is the square root of 144?", "12"),
#         ("Solve for x: 3x + 7 = 22", "5"),
#         ("What is the area of a circle with radius 5?", "78.54"),
#     ],
# }

# class TopicButton(Button):
#     def __init__(self, topic: str):
#         super().__init__(topic, classes="topic")
#         self.topic = topic

# class QuestionScreen(Screen):
#     def __init__(self, topic: str):
#         super().__init__()
#         self.topic = topic
#         self.questions = TOPICS[topic]
#         self.current_idx = 0
#         self.correct = 0
#         self.total = len(self.questions)

#     def compose(self) -> ComposeResult:
#         yield Container(
#             Static(f"Topic: {self.topic}", id="topic-header"),
#             Static(self.questions[0][0], id="question"),
#             Button("Show Answer", id="show-answer"),
#             Button("Next Question", id="next-question"),
#             Button("Back to Topics", id="back"),
#         )

#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         if event.button.id == "show-answer":
#             question = self.questions[self.current_idx]
#             self.query_one("#question").update(
#                 f"Q: {question[0]}\nA: {question[1]}"
#             )
#         elif event.button.id == "next-question":
#             self.current_idx = (self.current_idx + 1) % len(self.questions)
#             self.query_one("#question").update(self.questions[self.current_idx][0])
#         elif event.button.id == "back":
#             self.app.pop_screen()

# class ASVABTrainer(App):
#     CSS = """
#     Screen {
#         align: center middle;
#     }

#     .topic {
#         width: 100%;
#         margin: 1;
#     }

#     #topic-header {
#         text-align: center;
#         padding: 1;
#     }

#     #question {
#         text-align: center;
#         padding: 2;
#         min-height: 3;
#     }

#     Button {
#         margin: 1;
#     }
#     """

#     def compose(self) -> ComposeResult:
#         yield Header(show_clock=True)
#         yield Container(
#             Static("Select an ASVAB Topic to Study:", classes="header"),
#             *(TopicButton(topic) for topic in TOPICS.keys()),
#         )
#         yield Footer()

#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         if isinstance(event.button, TopicButton):
#             self.push_screen(QuestionScreen(event.button.topic))

@app.default
def main():
    # app = ASVABTrainer()
    pass

if __name__ == "__main__":
    app()