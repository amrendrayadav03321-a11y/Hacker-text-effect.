import time
import sys
import random
import os

# Colors
MATRIX_GREEN = '\033[38;5;46m'
DEEP_GREEN = '\033[38;5;22m'
BOLD = '\033[1m'
RESET = '\033[0m'


def hacker_decrypt(text):
    for char in text:
        for _ in range(2):
            glitch = random.choice("!@#$%^&*()<>[]/\\|")
            sys.stdout.write(f"{DEEP_GREEN}{glitch}{RESET}")
            sys.stdout.flush()
            time.sleep(0.015)
            sys.stdout.write('\b')

        sys.stdout.write(f"{MATRIX_GREEN}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.06)


def run_viral_hacker_code():
    os.system('cls' if os.name == 'nt' else 'clear')

    intro_lines = [
        "[SYSTEM] Initializing....",
        "[ACCESS] Loading emotions....",
        "[MEMORY] Searching Heart ❤️...."
    ]

    for line in intro_lines:
        print(f"{DEEP_GREEN}{line}{RESET}")
        time.sleep(0.8)

    print("\n")

    lyrics = [
        "Hum pyar karne wale",
        "Duniya se na darne wale..",
        "Duniya se na darne wale",
        "Pyar karne walon ko",
        "Yeh duniya kyun jalati hai?",
        "Jo khud jalte hain unko",
        "Yeh duniya kyun darati hai?"
    ]

    for line in lyrics:
        sys.stdout.write(f"{DEEP_GREEN}{RESET}")
        hacker_decrypt(line)
        print("\n")
        time.sleep(0.7)

    print(
        f"\n{BOLD}{MATRIX_GREEN}[PROCESS COMPLETED SUCCESSFULLY]{RESET}"
    )


if __name__ == "__main__":
    run_viral_hacker_code()