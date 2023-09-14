import re
import os
import sys

def replace_copyright(copyright_message, path_to_file, types, new_types):
    regex = re.compile("(#\sBEGIN\sCOPYRIGHT)((.|\n)*)(#\sEND\sCOPYRIGHT)")
    
    with open(copyright_message, "r", encoding="UTF-8") as b:
        content = b.read()

    if os.path.isdir(path_to_file):    

        dir_replacement = os.listdir(path_to_file)
        for files in dir_replacement:

            new_path_to_file = path_to_file + "/" + files
            with open(new_path_to_file, "r", encoding="UTF-8") as f:
                replacement = f.read()
            if regex.search(replacement) and re.search(types, new_path_to_file):
                new_path_to_file = re.sub(f"{types}$", new_types, new_path_to_file )
                with open(new_path_to_file , "w", encoding="UTF-8") as f:
                    f.write(regex.sub(content, replacement))

            
    else:
        with open(path_to_file, "r", encoding="UTF-8") as f:
            replacement = f.read()
        if regex.search(replacement) and re.search(types, path_to_file):
                new_path_to_file = re.sub(f"{types}$", new_types, path_to_file)
                with open(new_path_to_file , "w", encoding="UTF-8") as f:
                    f.write(regex.sub(content, replacement))

def main():
    from_user = sys.argv
    if len(from_user) == 7 and from_user[3] == "-c" and from_user[5] == "-u":
        replace_copyright(from_user[1],from_user[2], from_user[4], from_user[6])
    
    
if __name__ == "__main__":
    main()
    