import pygame
import sys
import psutil
import threading
import time

from mainmenu import main_menu
from text_adventure import game_loop

# Initialize Pygame
pygame.init()

# Global variable to control music playback
is_game_paused = False

# Music playback function
def play_music():
    pygame.mixer.music.load('your_music_file.mp3')
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    global is_game_paused

    while True:
        if is_game_paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        time.sleep(1)  # Sleep to prevent high CPU usage

# Function to calculate and display CPU usage
def calculate_cpu_usage(initial_cpu_times):
    # ... existing function code ...

def main():
    # Start the music thread
    music_thread = threading.Thread(target=play_music, daemon=True)
    music_thread.start()

    global is_game_paused

    while True:
        menu_result = main_menu()

        if menu_result == "start":
            # Start recording CPU usage
            initial_cpu_times = psutil.cpu_times(percpu=True)

            # Run the game loop
            is_game_paused = False  # Ensure music is playing
            game_loop()

            # Calculate and display CPU usage
            calculate_cpu_usage(initial_cpu_times)

        elif menu_result == "quit":
            break

if __name__ == "__main__":
    initial_CPU = psutil.cpu_times()
    initial_process_CPU = psutil.Process().cpu_times()
    start_time = time.time()

    main()

    # Collect CPU usage data
    end_time = time.time()
    final_CPU = psutil.cpu_times()
    final_process_cpu = psutil.Process().cpu_times()

    total_cpu_time = sum(final_CPU) - sum(initial_CPU)
    process_cpu_time = (final_process_cpu.user - initial_process_CPU.user) + \
                        (final_process_cpu.system - initial_process_CPU.system)
    cpu_usage_percentage = (process_cpu_time / total_cpu_time) * 100
    print(f"CPU usage percentage:  {cpu_usage_percentage:2f}%")
    print(f"Completion time: {end_time - start_time}")
