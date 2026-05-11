import os
from pathlib import Path

def scan_documents(directory_name):
    """
    Locates all .txt files within the specified directory.
    Calculates path relative to the script's grandparent directory.
    """
    # Define the base path (moving up two levels from this script)
    base_path = Path(__file__).parent.parent / directory_name
    
    # Safety check: create the directory if it does not exist
    if not base_path.exists():
        base_path.mkdir(parents=True, exist_ok=True)
        return []
    
    # Return a list of all text files found
    return list(base_path.glob('*.txt'))

def read_file_content(file_path):
    """Reads and returns the string content of a given file path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e: 
        return f"Error reading file: {e}"    

def get_keyword_frequency(text_content, keyword):
    """
    Calculates the number of occurrences of a keyword within the text.
    Performs a case-insensitive search.
    """
    # Normalize both content and keyword to lowercase for consistency
    content_normalized = text_content.lower()
    keyword_normalized = keyword.lower()
    
    # Count exact matches
    return content_normalized.count(keyword_normalized)

if __name__ == "__main__":
    print("--- ZENITH LOADER | DOCUMENT ANALYSER ---")
    
    # 1. Directory selection
    target_dir = input("Enter directory name to scan (e.g., 'data'): ")
    files = scan_documents(target_dir)

    if not files:
        print(f"Error: No files found in '{target_dir}'.")
    else:
        # 2. Display file list
        print(f"\nFound {len(files)} file(s):")
        for index, path in enumerate(files):
            print(f"[{index}] {path.name}")
        
        # 3. User selec
        try:
            selection = int(input("\nSelect a file index to analyze: "))
            
            if 0 <= selection < len(files):
                selected_file = files[selection]
                content = read_file_content(selected_file)
                
                # 4. Keyword analysis
                search_query = input(f"Enter keyword to search in '{selected_file.name}': ")
                occurrences = get_keyword_frequency(content, search_query)
                
                if occurrences > 0:
                    print(f"\nMatch found: The word '{search_query}' appears {occurrences} time(s).")
                else:
                    print(f"\nNo matches: The word '{search_query}' was not found in this document.")
                
                # 5. Optional display
                toggle_view = input("\nView full document content? (y/n): ")
                if toggle_view.lower() == 'y':
                    print(f"\n--- DOCUMENT CONTENT ---\n{content}")
                    
            else:
                print("Error: Invalid selection. Please choose a number from the list.")
        except ValueError:
            print("Input Error: Please enter a numeric value.")

    print("\n--- SESSION TERMINATED ---")
