#!/usr/bin/env python3

from typing_extensions import Literal
from cyclopts import App
from sh import gum  # type: ignore

app = App()

# Define choices as tuples first
DIFFICULTY_OPTIONS = ("easy", "medium", "hard")
TOPIC_OPTIONS = ("math", "vocab")

# Use the tuples in type hints
DifficultyType = Literal[DIFFICULTY_OPTIONS[0], DIFFICULTY_OPTIONS[1], DIFFICULTY_OPTIONS[2]]
TopicType = Literal[TOPIC_OPTIONS[0], TOPIC_OPTIONS[1]]

easy_question_count = 10
medium_question_count = easy_question_count * 2
hard_question_count = medium_question_count * 2

@app.default
def main(
    difficulty: DifficultyType | None = None,
    topic: TopicType | None = None,
    num_questions: int | None = None,
):
    if difficulty is None:
        difficulty = gum.choose(list(DIFFICULTY_OPTIONS))

    if topic is None:
        topic = gum.choose(list(TOPIC_OPTIONS))
    
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

