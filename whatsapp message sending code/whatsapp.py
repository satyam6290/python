import pyautogui
import time

# Wait for the user to open WhatsApp Web
input('Press Enter once you have opened WhatsApp Web and selected the chat...')

# Specify the message to send
message = input('Enter the message to send: ')

# Specify the number of times to send the message
num_times = int(input('Enter the number of times to send the message: '))

# Pause for a few seconds before starting
time.sleep(5)

# Send the message multiple times
for _ in range(num_times):
    # Type the message and press Enter
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(0.5)  # Add a small delay between messages

