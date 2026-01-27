import argparse
import sys
from src import random_dir

def main():
    parser = argparse.ArgumentParser(description="Generate random directories and files.")
    parser.add_argument("-n", type=int, required=True, help="Number of files to generate")
    
    args = parser.parse_args()
    
    try:
        random_dir.create_files(args.n)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
