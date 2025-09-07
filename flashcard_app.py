import json
import os
import random

FILE = "flashcards.json"


def load_flashcards():
    """Load flashcards from JSON file."""
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_flashcards(flashcards):
    """Save flashcards to JSON file."""
    with open(FILE, "w") as f:
        json.dump(flashcards, f, indent=4)


def add_flashcard():
    """Add a new flashcard."""
    question = input("Enter question: ").strip()
    answer = input("Enter answer: ").strip()
    flashcards = load_flashcards()
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)
    print("[+] Flashcard added!")


def view_flashcards():
    """View all flashcards."""
    flashcards = load_flashcards()
    if not flashcards:
        print("[!] No flashcards available.")
        return
    print("\n--- All Flashcards ---")
    for i, card in enumerate(flashcards, 1):
        print(f"{i}. Q: {card['question']} | A: {card['answer']}")
    print("-----------------------\n")


def quiz():
    """Quiz mode: show random questions and check answers."""
    flashcards = load_flashcards()
    if not flashcards:
        print("[!] No flashcards available.")
        return

    print("\n--- Quiz Mode ---")
    random.shuffle(flashcards)
    for card in flashcards:
        print(f"\nQ: {card['question']}")
        input("Press Enter to see the answer...")
        print(f"A: {card['answer']}")
    print("\n[+] Quiz finished!\n")


def main():
    while True:
        print("Flashcard App")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Quiz Mode")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            view_flashcards()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
