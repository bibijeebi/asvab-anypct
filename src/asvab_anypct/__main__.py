#!/usr/bin/env python3

import random
import sys
import json
from typing import List, Dict, Tuple
from pathlib import Path

def load_vocab_bank() -> Dict[str, str]:
    """Load vocabulary from JSON file."""
    try:
        # Get the directory where the script is located
        script_dir = Path(__file__).parent
        json_path = script_dir / 'vocab_bank.json'
        
        with open(json_path, 'r') as file:
            data = json.load(file)
            # Flatten the dictionary structure
            vocab_bank = {}
            for section in data.values():
                vocab_bank.update(section)
            return vocab_bank
    except FileNotFoundError:
        print("Error: vocab_bank.json file not found!")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in vocab_bank.json!")
        sys.exit(1)

def get_random_words(count: int, vocab_bank: Dict[str, str]) -> List[Tuple[str, str]]:
    """Get a random selection of words and their definitions."""
    return random.sample(list(vocab_bank.items()), count)

def generate_choices(correct_word: str, vocab_bank: Dict[str, str]) -> List[str]:
    """Generate a list of 4 choices including the correct word."""
    choices = [correct_word]
    wrong_choices = random.sample([word for word in vocab_bank.keys() 
                                 if word != correct_word], 3)
    choices.extend(wrong_choices)
    random.shuffle(choices)
    return choices

def run_quiz(word_count: int, vocab_bank: Dict[str, str]) -> Tuple[int, int, List[Dict]]:
    """Run the vocabulary quiz and return score, total, and missed questions."""
    words = get_random_words(word_count, vocab_bank)
    correct = 0
    missed_questions = []
    
    print("\nVocabulary Quiz")
    print("---------------")
    print("For each definition, choose the correct word.\n")
    
    for question_num, (word, definition) in enumerate(words, 1):
        print(f"\nQuestion {question_num}:")
        print(f"What word means: '{definition}'?")
        
        choices = generate_choices(word, vocab_bank)
        
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")
        
        while True:
            try:
                answer = int(input("\nEnter your choice (1-4): "))
                if 1 <= answer <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        user_answer = choices[answer - 1]
        if user_answer == word:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct word was: {word}")
            missed_questions.append({
                'question_num': question_num,
                'definition': definition,
                'correct_word': word,
                'user_answer': user_answer
            })
        
    return correct, word_count, missed_questions

def display_quiz_results(correct: int, total: int, missed_questions: List[Dict]):
    """Display the quiz results and missed questions."""
    percentage = (correct / total) * 100
    
    print("\n=== Quiz Results ===")
    print(f"Score: {correct} out of {total} correct ({percentage:.1f}%)")
    
    if missed_questions:
        print(f"\nYou missed {len(missed_questions)} questions:")
        print("\nMissed Questions Review:")
        print("------------------------")
        for missed in missed_questions:
            print(f"\nQuestion {missed['question_num']}:")
            print(f"Definition: '{missed['definition']}'")
            print(f"Your answer: {missed['user_answer']}")
            print(f"Correct answer: {missed['correct_word']}")
    else:
        print("\nPerfect score! You didn't miss any questions!")
    
    print("\nOverall Performance:")
    if percentage >= 90:
        print("Excellent work!")
    elif percentage >= 70:
        print("Good job! Keep practicing!")
    else:
        print("Keep studying! You'll improve!")

def get_user_choice() -> int:
    """Get and validate user's difficulty choice."""
    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def play_again() -> bool:
    """Ask if user wants to play again."""
    while True:
        print("\nWhat would you like to do?")
        print("1. Try Again")
        print("2. Quit")
        try:
            choice = int(input("\nEnter your choice (1-2): "))
            if choice == 1:
                return True
            elif choice == 2:
                return False
            print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    # Load vocabulary bank at startup
    vocab_bank = load_vocab_bank()
    
    while True:
        print("\nWelcome to the ASVAB Vocabulary Practice!")
        print("Choose difficulty:")
        print("1. Easy (10 words)")
        print("2. Medium (20 words)")
        print("3. Hard (30 words)")
        
        choice = get_user_choice()
        
        word_counts = {
            1: 10,  # Easy
            2: 20,  # Medium
            3: 30   # Hard
        }
        
        difficulty_names = {
            1: "Easy",
            2: "Medium",
            3: "Hard"
        }
        
        print(f"\nStarting {difficulty_names[choice]} difficulty quiz...")
        correct, total, missed_questions = run_quiz(word_counts[choice], vocab_bank)
        display_quiz_results(correct, total, missed_questions)
        
        if not play_again():
            print("\nThanks for playing! Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()

