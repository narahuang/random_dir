import os
import random
import textwrap
import shutil
from lorem_text import lorem


def inject_symbols(text):
    # Randomly injects numbers and symbols into the text between characters.
    chars = list(text)
    symbols_numbers = ["0","1","2","3","4","5","6","7","8","9","!","@",
    "#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}",
    "|","\\","<",">",",",".","/","?","`","~"]
    
    # Random 0% to 25% of length of text insertions.
    num_insertions = random.randint(0, len(chars) // 4)
    
    for _ in range(num_insertions):
        position = random.randint(0, len(chars))
        char_to_insert = random.choice(symbols_numbers)
        chars.insert(position, char_to_insert)
        
    return "".join(chars)

def generate_random_content():
    # Generates random content using lorem-text (1-1000 words)
    # then injects symbols/numbers.
    num_words = random.randint(1, 1000)
    raw_text = lorem.words(num_words)
    return inject_symbols(raw_text)

def generate_random_name():
    # Generates a random filename/dirname using lorem-text (1 word).
    return lorem.words(1).replace(" ", "").lower()

def create_files(n, output_dir="output"):
    # Generates n files with random content in random directories (0-3 levels deep).
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    for _ in range(n):
        # Determine depth: 0 to 3
        depth = random.randint(0, 3)
        current_path = output_dir
        
        # Build directory path
        for _ in range(depth):
            dir_name = generate_random_name()
            current_path = os.path.join(current_path, dir_name)
        
        # Ensure the directory exists
        os.makedirs(current_path, exist_ok=True)
        
        # Generate filename
        filename = generate_random_name() + ".txt"
        file_path = os.path.join(current_path, filename)
        
        # Generate content
        content = generate_random_content()
        wrapped_text = textwrap.fill(content, width=80)
        
        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(wrapped_text)
        print(f"{file_path}")

    print(f"Generated {n} files in '{output_dir}'.")
