import os
import random
import textwrap
import shutil
import datetime
from lorem_text import lorem


def inject_symbols(text):
    # Randomly injects numbers and symbols into the text between characters
    chars = list(text)
    symbols_numbers = ["0","1","2","3","4","5","6","7","8","9","!","@",
    "#","$","%","^","&","*","(",")","-","_","+","=","[","]","{","}",
    "|","\\","<",">",",",".","/","?","`","~"]
    
    # Random 0% to 25% of length of text insertions
    num_insertions = random.randint(0, len(chars) // 4)
    
    for _ in range(num_insertions):
        position = random.randint(0, len(chars))
        char_to_insert = random.choice(symbols_numbers)
        chars.insert(position, char_to_insert)
        
    return "".join(chars)

def generate_random_content():
    # Generates random content using lorem-text (1-1000 words)
    # then injects symbols/numbers
    num_words = random.randint(1, 1000)
    raw_text = lorem.words(num_words)
    return inject_symbols(raw_text)

def generate_random_title():
    num_words = random.randint(1, 10)
    return lorem.words(num_words).title()

def generate_random_datetime():
    # Date and time: randomly generate date and time
    # within the last 100 years
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(days=365*100)
    random_seconds = random.randint(0, int((end_time - start_time).total_seconds()))
    random_date = start_time + datetime.timedelta(seconds=random_seconds)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

def generate_page_number():
    # Page number: randomly generated page number
    return random.randint(1, 500)

def generate_random_name():
    # Generates a random filename/dirname using lorem-text (1 word)
    return lorem.words(1).replace(" ", "").lower()

def create_files(n, output_dir="output"):
    # Generates n files with random content in random directories (0-3 levels deep)
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
        body_content = generate_random_content()
        word_count = len(body_content.split())
        title = generate_random_title()
        date_time = generate_random_datetime()
        page_num = generate_page_number()
        
        metadata = (
            f"Title: {title}\n"
            f"Date and time: {date_time}\n"
            f"Page number: {page_num}\n"
            f"Word count: {word_count}\n\n"
        )
        
        wrapped_text = textwrap.fill(body_content, width=80)
        final_content = metadata + wrapped_text
        
        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"{file_path}")

    print(f"Generated {n} files in '{output_dir}'.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate random directories and files.")
    parser.add_argument("-n", type=int, required=True, help="Number of files to generate")
    parser.add_argument("-d", "--dir", type=str, default="output", help="Target directory (default: output)")
    args = parser.parse_args()
    create_files(args.n, output_dir=args.dir)
