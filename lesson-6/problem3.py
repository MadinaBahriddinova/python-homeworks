import os
import string
from collections import Counter

FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def create_file():
    print("sample.txt does not exist. Please enter text to create it:")
    text = input("Enter text: ")
    with open(FILE_NAME, "w") as file:
        file.write(text)
    print("File created successfully.\n")

def count_words():
    if not os.path.exists(FILE_NAME):
        create_file()
    
    with open(FILE_NAME, "r") as file:
        text = file.read().lower()
    
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = text.split()
    
    word_count = Counter(words)
    
    total_words = sum(word_count.values())
    most_common_words = word_count.most_common(5)
    
    print("\nTotal words:", total_words)
    print("Top 5 most common words:")
    for word, count in most_common_words:
        print(f"{word} - {count} times")
    
    with open(REPORT_FILE, "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in most_common_words:
            report.write(f"{word} - {count}\n")
    
    print("\nWord count report saved to 'word_count_report.txt'.\n")

if __name__ == "__main__":
    count_words()
