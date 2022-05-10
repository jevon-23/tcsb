"""
Authors: 
    Student : Alexander Eichner
    Coach   : Jevon Jackson

A program that starts a uses a keyboard listener to run functionality based on a key that is
pressed.
"""
import threading
from pynput import keyboard

"""
A class meant to map threads to functions that can be toggled on / off to run in the 
background. 

Creates a new thread that runs FUNCTION if the user ENABLES the HOT_KEY.
    => Letter field serves no purpose other than for visual and concreteness. 
       B/c Everything runs based on a field in our class struct, the underlying structure
       does not use letter at all Hence => (b = hot_keys(counter, None)) && 
       (b = hot_keys(counter, 'c')) works equally the same. 


Example: To generate an instance:
    # Create a global function
    def func():
        print("hello world")

    # Create a new instance mapping that global function to a character being passed in
    a = hot_key(func, 'a')
    a.toggle_hot_key() # enable hot_key
    timer.sleep(10)    # Wait a little bit 
    a.toggle_hot_key   # disable hot_key
    
"""
stopped = False # Used to let hot_keys know when to exit (check run_thread / keyboard_listener)
class hot_keys:

    def __init__(self, function, letter):
        # Function mapped to this hotkey
        self.func = function 

        # Key that we map this hot_key to (unused throughout process, just for visual purpose)
        self.letter = letter

        # Is this hot key enabled
        self.enabled = False

        # Create a thread to execute desired functionality of toggle 
        self.thread = threading.Thread(target=self.run_thread, args=())
        self.thread.start()

    """Enables the hotkey for this key"""
    def toggle_hot_key(self):
        self.enabled ^= 1
        if (self.enabled):
            print(self.letter + " enabled")
        else:
            print(self.letter + " disabled")
    
    """Runs HOT_KEY'S function iff our listener is still running and our hotkey is enabled """
    def run_thread(self):
        global stopped
        while(not stopped):
            # While program still running, execute our function if key is enabled 
            if (self.enabled):
                self.func()
        return


x, y = 2, 3
def printVals():
    global x, y
    print("x = " + str(x))
    print("y = " + str(y))
    return

#functions for hot_keys
def bFunc():
    global x
    x += 1

def cFunc():
    global y
    y += 1


""" Create the hotkeys for this session"""
b = hot_keys(bFunc, 'b')
c = hot_keys(cFunc, 'c')

""" Start our keyboard listener """
def keyboard_listener():
    global stopped, x, y

    # Functionality executed once our listener receives a pressed key
    def on_press(key):
        try:
            print('key {0} pressed'.format(
                key.char))
            if (key.char == ('c')):
                # Toggle c on/ off
                c.toggle_hot_key()
            elif (key.char == ('b')):
                # Turn b on / off
                b.toggle_hot_key()
            elif (key.char == 'd'):
                printVals()
        except AttributeError:
            print('invalid {0} pressed'.format(
                key))

    # Functionality executed once our listener receives the relasing of an already pressed key
    def on_release(key):
        # Uncomment to see what key has been released 
        # print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    print("starting listener")
    # Create a new keyboard listener, and start it
    listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
    listener.start()

    # Main thread needs to wait for our listener to be finished running before exiting
    listener.join()
    print("Listener has finished; x = " + str(x) + " y = " + str(y))

    # Tell the rest of the threads to stop running
    stopped = True
    return

if __name__ == "__main__":
    keyboard_listener()
    print("Done!")
