
# Import the sleep function from time library
# sleep function allows the process to be paused for certain period of time
from time import sleep

# Defining the main function
def main():

    # Starting a loop that runs forever
    while True:

        # Opening a try block
        # Try, Except are used to catch exceptions when running our program
        # Here, we use a Try, Except block to detect a keyboard interrupt, this allows our application to close when typing Ctrl+C in the CLI terminal
        try:

            # Printing an informative statement
            print ('This is the main thread')

            # Pausing execution for 1/2 a second
            sleep(0.5)

        # Catching the keyboard interrupt
        except KeyboardInterrupt:
            # This section is excuted only if we press Ctrl+C in the CLI terminal

            # Printing an informative message that the thread will close
            print('Main thread exited, goodbye :D')

            # Exiting from the loop
            break

# This section runs the function main when launching the code from the CLI
if __name__ == '__main__':
    main()
