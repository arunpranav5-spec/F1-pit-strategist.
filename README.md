# F1-pit-strategist.
# F1 Pit Stop Strategist

A lightweight, text-based Python application that simulates an F1 team strategy desk to determine optimal pit stop windows based on tire compounds.

## Features
- Dynamic Input Parsing:** Accepts compound choices directly from the race engineer.
- Tire Degradation Logic:** Maps specific stint lengths to Soft, Medium, and Hard compounds.
- Error Handling:** Built-in boundary checks to handle invalid or unsupported tire configurations gracefully.

## Architecture & Logic
The program initializes a fixed race state (`total_laps`), evaluates user inputs using conditional branching (`if/elif/else`), and calculates the remaining tire life safely before outputting execution commands.

## How to Run
Ensure you have Python 3.x installed on your environment. Run the script via the terminal:
`python3 pit_stop.py`
