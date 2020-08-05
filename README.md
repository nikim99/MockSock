# Mock Sock

Mock Sock is a virtual puppet theatre that will allow for the user to make 
shapes of the sock puppet with their hands and it will display the puppet on 
the screen. The sock design will be molded over their hand and displayed in 
2D on the screen. The user will have design options available such sock design, 
accessories, and background options. They can also add interactive objects 
such as balls, apple, or cars.

## How to run

Before running the program, open the MockSock.py folder and change the line
with the sys.path.insert to match the path to LeapSDK in your computer and 
add \lib/x86 or \lib/x64 based on the bit version of your python and computer. 
To run the program go into the command terminal and navigate to the folder 
which contains all the files and pictures. Then run the MockSock.py file to 
start the program. A tkinter window will pop up that displays the graphics. 
Make sure the leap motion is connected before starting. If the leap motion 
is connected the frame information will begin to print in the terminal. 

## Libraries Needed

Be sure to import Leap, sys, math, thread, pyaudio and shapely properly before
running. 

Leap can be installed from https://www.leapmotion.com/setup/desktop/windows/ 

Shapely can be installed from pip installing either 

- Shapely‑1.6.4.post1‑cp27‑cp27m‑win32.whl
- Shapely‑1.6.4.post1‑cp27‑cp27m‑win_amd64.whl

Based on which windows bit version you are on 

To install pyaudio pip install the following

	python -m pip install pyaudio
	
Sys, thread, and math should be built in libraries
