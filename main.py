import argparse
import sys
from src import random_dir

def main():
    parser = argparse.ArgumentParser(description="Generate random directories and files.")
    parser.add_argument("-n", type=int, help="Number of files to generate")
    parser.add_argument("-s", type=str, help="Search keyword")
    
    args = parser.parse_args()
    
    if args.n is None and args.s is None:
        parser.print_help()
        sys.exit(1)
    
    # Use try-except to catch any errors during file operations.
    try:
        if args.n:
            random_dir.create_files(args.n)
        
        if args.s:
            from src import search
            search.search_files(args.s)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
