#!/usr/bin/env python3

from typing_extensions import Literal
from cyclopts import App
from sh import gum

app = App()

difficulty_choices = Literal["easy", "medium", "hard"]
topic_choices = Literal["math", "vocab"]

easy_question_count = 10
medium_question_count = easy_question_count * 2
hard_question_count = medium_question_count * 2

@app.default
def main(
    difficulty: difficulty_choices | None = None,
    topic: Literal["math", "vocab"] | None = None,
    num_questions: int | None = None,
):
    if difficulty is None:
        # print("Choose difficulty: easy, medium, hard")
        # difficulty = input("> ")
        difficulty = gum.choose(list(difficulty_choices.__args__))

    if topic is None:
        # print("Choose topic: math, vocab")
        # topic = input("> ")
        topic = gum.choose(list(topic_choices.__args__))
    
    if num_questions is None:
        num_questions = gum.choose(list(range(1, 101)))
    
    if difficulty == "easy":
        num_questions = easy_question_count
    elif difficulty == "medium":
        num_questions = medium_question_count
    elif difficulty == "hard":
        num_questions = hard_question_count

    print(f"Quizzing {topic} with {num_questions} questions of difficulty {difficulty}")

if __name__ == "__main__":
    app()

