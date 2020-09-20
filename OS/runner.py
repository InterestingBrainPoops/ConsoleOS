# Deprecated as of now but can be modified to run the game file if you have both Games and ConsoleOS in the same folder.
# One thing that needs to be done is to make it non-game specific and probably make a shell script witch is called 
import os
os.system("cd ../TestFiles/Snake && pip install -r requirements.txt && cd dist && pong.exe")