
# Importing the threading module
# This module allows for creating and managing multi-threaded applications
import threading
from time import sleep

# An event is an object that allows communicating boolean values between threads
# The stop_event is a boolean event that indicates whether a user stopped the main thread or not
stop_event = threading.Event()

# A variable that indicates how many sub-threads will be launched
thread_count = 9

# Defining a function that will be used to create threads later on
# The function accepts the thread_number as an argument
def thread_worker(thread_number: int):

    # Using the globally defined stop_event
    global stop_event

    # Start a loop that runs as long as the stop_event is not set to true
    while not stop_event.is_set():

        # Print an informative message indicating the thread number
        print (f'This is thread no. {thread_number}')

        # Pause the function for certain period of time
        sleep(0.2 * thread_number)

    # This will be executed when the loop is exited (when the stop_event is set to true)
    print(F'Thread {thread_number} exited, goodbye :D')

# Defining the main function
def main():
    # Print an informative message, indicating that this is the main thread
    print ('This is the main thread')

    # Defining an empty list of threads
    # The list will be used to store threads to later make sure they exit
    threads = []

    # Run a loop that generates the desired number of threads
    for i in range(1, thread_count + 1):
        # A thread is created with the function thread_worker as the function, and pass the first argument (thread_number) as the current loop index (i)
        thread = threading.Thread(
            target=thread_worker,
            args=(i,)
        )
        
        # Start the thread
        # This create a thread that runs in parallel with the main thread 
        thread.start()

        # Add the thread to the list of threads
        threads.append(thread)


    # Starting a loop that runs forever
    while True:
        # Opening a try block
        # Try, Except are used to catch exceptions when running our program
        # Here, we use a Try, Except block to detect a keyboard interrupt, this allows our application to close when typing Ctrl+C in the CLI terminal
        try:
            # Pause the main thread for 1 second
            sleep(1)
        
        # Catching the keyboard interrupt
        except KeyboardInterrupt:

            # Setting the stop event to inform the threads to stop working
            stop_event.set()

            # Looping over the thread list to make sure they all complete execution and exit
            for t in threads:
                t.join()
            
            # Print an informative message that the main thread has exited
            print('Main thread exited, goodbye :D')

            # Exiting from the loop
            break

# This section runs the function main when launching the code from the CLI
if __name__ == '__main__':
    main()
