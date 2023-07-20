import os
from pathlib import Path # import all the path functions
import shelve

print(f"\n{Path.home()} is the home directory")

print(f"\n{Path.cwd()} is the current working directory")

print(f"\n{Path('../').resolve()} is the parent folder of the cwd")

print(f"\n{Path('../PWAD').resolve()} is on the same level as the cwd")

print(f"\n{Path('./lorem.txt').resolve()} is a file in the cwd")

newdir = Path.cwd() / 'a' / 'new' / 'folder'

print(f"{Path.cwd() / 'a' / 'new' / 'folder'} is a path with 3 new folders")

Path(newdir).mkdir() # mkdir can only make one new folder at a time

os.makedirs(newdir) # makedirs from the os module can make multiple new directories

print(f'\nIt is {newdir.is_absolute()} that {newdir} is an absolute path')

print(f"\nIt is {Path('spam/bacon/eggs').is_absolute()} that {Path('spam/bacon/eggs')} is an absolute path")

print(f"\nThe absolute path of {Path('spam/bacon/eggs')} is {Path('spam/bacon/eggs').resolve()}")

file = Path('lorem.txt').resolve()

print(f"\n{file.anchor} is the anchor of {file}")

print(f"\n{file.parent} is the parent folder of {file}")

print(f"\n{file.parents[1]} is the parent folder of the parent folder of {file}")

print(f"\n{file.name} is the name of {file}")

print(f"\n{file.stem} is the stem of {file}")

print(f"\n{file.suffix} is the suffix of {file}")

print(f"\n{file.drive} is the drive of {file}")

print(f"\nThese are all the files in the cwd {list(Path.cwd().glob('*'))}")

print(f"\nThese are all the Python files in the cwd {list(Path.cwd().glob('*.py'))}")

print(f"\nIt is {newdir.exists()} that {newdir} exists")

print(f"\nIt is {newdir.is_file()} that {newdir} exists and is a file")

print(f"\nIt is {newdir.is_dir()} that {newdir} exists and is a directory")

with open(file, 'r') as f:
    print(f"\n{file} is now open to read")
    print(f"\nHere are the contents of {file}")
    lorem = f.read()
    print(lorem)


with open('ipsum.txt', 'w') as f:
    print(f"\nipsum.txt has been created and is now open to write")
    f.write(lorem)
    print(f"\nipsum.txt now contians the text from {file}")

with open('ipsum.txt', 'a') as f:
    print(f"\nipsum.txt is now open to append")
    f.write('\nappending and upending')
    print(f"\nipsum.txt now includes the text 'appending and upending' at the end")

with shelve.open('mydata') as shelfFile:
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['cats'] = cats

with shelve.open('mydata') as shelfFile:
    print(f"\nshelfFile['cats']")

