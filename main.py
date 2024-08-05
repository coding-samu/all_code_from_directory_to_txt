import os

def write_file_content(root, file_path, content):
    with open("output.txt", "a") as file:
        file.write(f"{root}/{file_path}\n")
        file.write(content)
        file.write("\n\n")

def process_directory(root, ignore_extensions, ignore_directories, ignore_files):
    for dirpath, dirnames, filenames in os.walk(root):
        # Rimuovi le directory da ignorare dalla lista di dirnames
        dirnames[:] = [d for d in dirnames if d not in ignore_directories]
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_extension = os.path.splitext(filename)[1]
            if file_extension not in ignore_extensions and filename not in ignore_files:
                with open(file_path, "r") as file:
                    print(f"Processing file: {file_path}")
                    content = file.read()
                    write_file_content(root, file_path, content)

# Esempio di utilizzo
directory_path = "PATH"  # Path della cartella da analizzare
ignore_extensions = [".txt", ".md"]  # Estensioni dei file da ignorare
ignore_directories = [".git"]  # Nomi delle cartelle da ignorare
ignore_files = [".gitignore", "LICENSE"]  # Nomi dei file da ignorare

process_directory(directory_path, ignore_extensions, ignore_directories, ignore_files)