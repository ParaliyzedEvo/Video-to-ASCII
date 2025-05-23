#Chatgpt helped me with what libraries to import for the project to work and started to work off of that
import time
import platform
import os
import random

#Path list to choose which converted video you want to play in the console
#List to store the different paths
path_list = ['frames','frames2']

#Function including a name for the procedure, a parameter, squencing, selection, iteration
def play_ascii_video(folder_path='', fps=0):
    
    """Description: This code plays an ASCII video by reading frames from a specified folder for a certain duration by the user specifying how many times they want to repeat.
    
    Args:
        folder_path (str): The path to the folder containing ASCII frame files.
        fps (int): The frames per second for playback (must be greater than 0).
    """
    
    #Check if the folder exists (Chatgpt helped me by adding this for error handling)
    if not os.path.exists(folder_path):
        print(f'Error: Folder "{folder_path}" does not exist.')
        return

    #Sort files in the folder to ensure frame order
    frame_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')])
    
    if not frame_files:
        print('No ASCII frame files found in the specified folder.')
        return
    
    clear_command = 'cls' if platform.system() == 'Windows' else 'clear'

    for frame_file in frame_files:
        with open(os.path.join(folder_path, frame_file), 'r') as f:
            ascii_frame = f.read()
            os.system(clear_command) #Clear the console
            print(ascii_frame)
            #Chatgpt helped me how to specify the fps
            time.sleep(1 / fps) #Adjust for desired frame rate

#Chatgpt optimized the inputs for the code to help me validate the inputs
#User Input:

#Validate the loop input
while True:
    try:
        loop = int(input('How many times do you want the video to loop? (0 for random) '))
        if loop > 0:
            print(f'Video will be looped {loop} times.')
            break
        elif loop == 0:
            loop = random.randint(1,10)
            print(f'Video will be looped {loop} times.')
            break
        else:
            print('Error: Loop must be greater than 0.')
    except ValueError:
        print('Error: Please enter a valid integer.')

while True:
    try:
        path_num = int(input('Enter 1 or 2 for path selection (0 for random): '))
        if path_num in [1, 2]:
            path = path_list[path_num - 1]
            print(f'Path {path_num} was chosen.')
            break
        elif path_num == 0:  # Random path
            path_num = random.randint(1, 2)
            path = path_list[path_num - 1]
            print(f'Path {path_num} was chosen.')
            break
        else:
            print('Error: Please enter 1, 2, or 0.')
    except ValueError:
        print('Error: Please enter a valid integer.')

# Optimized FPS selection
while True:
    try:
        num = int(input('How much fps do you want the video to be? (0 for random): '))
        if num > 0:
            print(f'Video will be {num} fps.')
            break
        elif num == 0:  # Random FPS
            num = random.randint(1, 270)
            print(f'Video will be {num} fps.')
            break
        else:
            print('Error: FPS must be greater than 0.')
    except ValueError:
        print('Error: Please enter a valid integer.')
    

#Call the playback function with specific parameters
for i in range(loop):
    play_ascii_video(folder_path = path,fps=num) #Puts all three inputs into the designated slots into the loop and into parameters