import time
import pyautogui
import sys
import argparse
from threading import Event

# Create an event for stopping the script
stop_event = Event()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Mouse mover to prevent screen timeout/sleep')
    parser.add_argument('-d', '--duration', type=int, default=15,
                       help='Duration of mouse movement in seconds (default: 15)')
    parser.add_argument('-p', '--pause', type=int, default=10,
                       help='Pause duration between movements in seconds (default: 10)')
    parser.add_argument('-s', '--start-y', type=int, default=20,
                       help='Starting Y position (default: 20)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Print settings without running the mouse mover')
    return parser.parse_args()

def move_mouse(start_y, duration):
    # Get the screen dimensions
    screen_height = pyautogui.size()[1]
    
    # Calculate the starting and ending positions
    start_pos = (0, start_y)
    end_pos = (0, screen_height // 2)
    
    # Move the mouse cursor from top-left to middle-left
    pyautogui.moveTo(*start_pos)
    pyautogui.moveTo(*end_pos, duration=duration)

def main():
    args = parse_arguments()
    
    if args.dry_run:
        print(f"Settings:")
        print(f"Movement duration: {args.duration} seconds")
        print(f"Pause duration: {args.pause} seconds")
        print(f"Start Y position: {args.start_y}")
        sys.exit(0)
    
    print(f"Running with:")
    print(f"- Movement duration: {args.duration} seconds")
    print(f"- Pause duration: {args.pause} seconds")
    print(f"- Start Y position: {args.start_y}")
    print("\nPress Ctrl+C to stop")
    
    try:
        while not stop_event.is_set():
            move_mouse(args.start_y, args.duration)
            # Sleep in small intervals to check for interrupt
            for _ in range(args.pause):
                if stop_event.is_set():
                    break
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping script...")
        stop_event.set()
        sys.exit(0)

if __name__ == "__main__":
    main()
