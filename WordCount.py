import os
import glob
import sys

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            return len(content.split())
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def process_directory(directory_path):
    file_word_counts = {}
    for subdir, dirs, files in os.walk(directory_path):
        for file in glob.glob(os.path.join(subdir, '*.txt')):
            word_count = count_words_in_file(file)
            if word_count is not None:
                file_word_counts[file] = word_count
    return file_word_counts

def main(path):
    if os.path.isfile(path) and path.endswith('.txt'):
        print(f"{path}: {count_words_in_file(path)} words")
    elif os.path.isdir(path):
        file_word_counts = process_directory(path)
        sorted_files = sorted(file_word_counts.items(), key=lambda x: x[1])
        for file, count in sorted_files:
            print(f"{file}: {count} words")
    else:
        print("The path is neither a .txt file nor a directory.")

# Replace 'your_path_here' with your specific file or directory path
main_path = sys.argv[1]
main(main_path)

