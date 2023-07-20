import easygui
import glob
import os
from pathlib import Path
import subprocess

# Converts .m4a files into mp3 files
def convert_to_mp3():
    input = easygui.diropenbox('Select the folder with the files you want to convert ')
    output = easygui.diropenbox('Select the destination folder ')
    for file in glob.glob(os.path.join(input, r'*.m4a')):
        stem = Path(file).stem
        des = os.path.join(output, f'{stem}.mp3')
        command = ['ffmpeg', '-i', f'{file}', f'{des}']
        print(f'Converting {stem} to mp3')
        subprocess.run(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

def main():
    convert_to_mp3()

if __name__ == "__main__":
    main()