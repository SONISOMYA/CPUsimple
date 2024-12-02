# CPU Simulator

## Overview

This **CPU Simulator** is a simple representation of how a CPU (Central Processing Unit) executes instructions. The simulator models a basic CPU with operations like addition, subtraction, and loading/storing values in registers. It demonstrates the core principles of **Computer Organization and Architecture (COA)**, such as the instruction cycle, registers, and arithmetic logic unit (ALU).

## Features

- **Instruction Cycle**: Simulates the basic CPU cycle: **Fetch → Decode → Execute**.
- **Register Management**: Emulates CPU registers to store temporary values.
- **Arithmetic Operations**: Performs operations like addition and subtraction.
- **Visualization**: Optionally visualizes the changes in register values after each cycle.
- **Configurable Program**: You can define a list of instructions in a `program.txt` file.

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

//To install dependencies, use the following:
pip install -r requirements.txt



