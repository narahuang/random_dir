import os

def search_files(keyword, search_dir="output"):
    if not os.path.exists(search_dir):
        print(f"Directory '{search_dir}' not found.")
        return

    results = []
    
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if not file.endswith(".txt"):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Case-insensitive check
                if keyword.lower() in content.lower():
                    lines = content.split('\n')
                    title = "N/A"
                    date_time = "N/A"
                    
                    for line in lines:
                        if line.startswith("Title: "):
                            title = line[len("Title: "):].strip()
                        elif line.startswith("Date and time: "):
                            date_time = line[len("Date and time: "):].strip()
                        
                        if title != "N/A" and date_time != "N/A":
                            break
                            
                    results.append({
                        "date_time": date_time,
                        "title": title,
                        "path": file_path
                    })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # Print table
    if not results:
        print(f"No files found containing keyword '{keyword}'.")
        return

    print(f"{'Date and Time':<25} | {'Title':<40} | {'Path'}")
    print("-" * 26 + "+" + "-" * 42 + "+" + "-" * 30)
    
    for res in results:
        title_display = (res['title'][:37] + '...') if len(res['title']) > 40 else res['title']
        print(f"{res['date_time']:<25} | {title_display:<40} | {res['path']}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Search for a keyword in directory.")
    parser.add_argument("-s", "--search", type=str, required=True, help="Search keyword")
    parser.add_argument("-d", "--dir", type=str, default="output", help="Directory to search in (default: output)")
    args = parser.parse_args()
    search_files(args.search, search_dir=args.dir)
