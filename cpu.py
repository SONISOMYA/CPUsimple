from alu import ALU
from memory import Memory
from visualization import visualize_cpu_state

class CPU:
    def __init__(self):
        self.registers = {"R1": 0, "R2": 0} 
        self.memory = Memory()
        self.pc = 0 
        self.cycle = 0
        self.alu = ALU()

    def fetch(self):
        instruction = program_memory[self.pc]
        print(f"Cycle {self.cycle}: Fetching instruction {instruction}")
        return instruction

    def decode(self, instruction):
        opcode = instruction[:2] 
        operand1_index = int(instruction[2])  
        operand2_index = int(instruction[3])  

        
        operand1 = f"R{operand1_index + 1}"
        operand2 = f"R{operand2_index + 1}"
        
        print(f"Cycle {self.cycle}: Decoding instruction {opcode} with operands {operand1}, {operand2}")
        return opcode, operand1, operand2

    def execute(self, opcode, operand1, operand2):
        if opcode == "00":  # ADD
            result = self.alu.add(self.registers[operand1], self.registers[operand2])
        elif opcode == "01":  # SUB
            result = self.alu.subtract(self.registers[operand1], self.registers[operand2])
        elif opcode == "10":  # LOAD
            result = self.memory.load(self.registers[operand1])
        elif opcode == "11":  # STORE
            self.memory.store(self.registers[operand1], self.registers[operand2])
            result = None
        print(f"Cycle {self.cycle}: Executing {opcode} => Result: {result}")
        return result

    def run(self, program_memory):
        while self.pc < len(program_memory):
            self.cycle += 1
            instruction = self.fetch()
            opcode, operand1, operand2 = self.decode(instruction)
            result = self.execute(opcode, operand1, operand2)
            if result is not None:
                self.registers[operand1] = result
            self.pc += 1
            visualize_cpu_state(self)


program_memory = ["0010", "0110", "1001", "1110"]

cpu = CPU()
cpu.run(program_memory)
