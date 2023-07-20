# import the time module
import time, playsound, os

print('What kind of tea?')
print('')

# define the countdown func.
def countdown(tea):
    print('')
    if tea == 'b':
        t = 300
    elif tea == 'g':
        t = 180
    elif tea == 'h':
        t = 420
    elif tea == 't':
        t = 5
    else:
        print('What kind of tea? ')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('~ Tea ready in', timer, "~", end="\r")
        time.sleep(1)
        t -= 1
      
    print('~ Tea is ready! ')
    cwd = os.getcwd()
    playsound.playsound(os.path.join(cwd, "WW_Aryll_Hoy1.wav"))
  
  
# input time in seconds
tea = input("""b for black
g for green
h for herbal

""")
  
# function call
countdown(tea)

input('')