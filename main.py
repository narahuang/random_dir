import argparse
import sys
from src import random_dir
from src import search

def main():
    parser = argparse.ArgumentParser(description="Generate random directories and files.")
    parser.add_argument("-n", type=int, help="Number of files to generate")
    parser.add_argument("-s", type=str, help="Search keyword")
    parser.add_argument("-d", "--dir", type=str, default="output", help="Target directory (default: output)")
    
    args = parser.parse_args()
    
    if args.n is None and args.s is None:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.n:
            random_dir.create_files(args.n, output_dir=args.dir)
        
        if args.s:
            search.search_files(args.s, search_dir=args.dir)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
