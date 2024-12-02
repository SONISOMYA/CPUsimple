# CPU Simulator

## Overview

This **CPU Simulator** is a simple representation of how a CPU (Central Processing Unit) executes instructions. The simulator models a basic CPU with operations like addition, subtraction, and loading/storing values in registers. It demonstrates the core principles of **Computer Organization and Architecture (COA)**, such as the instruction cycle, registers, and arithmetic logic unit (ALU).

## Features

- **Instruction Cycle**: Simulates the basic CPU cycle: **Fetch → Decode → Execute**.
- **Register Management**: Emulates CPU registers to store temporary values.
- **Arithmetic Operations**: Performs operations like addition and subtraction.
- **Visualization**: Optionally visualizes the changes in register values after each cycle.
- **Configurable Program**: You can define a list of instructions in a `program.txt` file.

## Project Structure
CPUsimple/
│
├── cpu.py                 # Main CPU simulator logic
├── program.txt            # Instructions for the CPU to execute
├── venv/                  # Virtual environment for the project dependencies
├── requirements.txt       # Python dependencies
├── README.md              # This file


## How to Run the Project

1. Clone the repository or download the files to your machine.
2. Install dependencies:
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # For macOS/Linux
     .\venv\Scripts\activate   # For Windows
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```
3. Create a `program.txt` file in the same directory with the instructions you want to run.
4. Run the simulator:
```bash
python cpu.py

How It Works

	1.	Fetching Instructions: Each instruction is fetched from the program.txt file.
	2.	Decoding: The instruction is decoded to determine what action the CPU needs to take (e.g., addition, subtraction).
	3.	Executing: The CPU performs the operation on the specified registers and stores the result.
	4.	Register Updates: The values in the registers are updated based on the executed operation.

Dependencies

	•	Python 3.x
	•	Required Python packages are listed in requirements.txt.

To install dependencies, use the following:
pip install -r requirements.txt



