import matplotlib.pyplot as plt

def visualize_cpu_state(cpu):
    
    fig, ax = plt.subplots()
    ax.set_title(f"CPU State - Cycle {cpu.cycle}")
    ax.bar(cpu.registers.keys(), cpu.registers.values(), color='blue', alpha=0.7, label="Registers")
    ax.set_ylabel('Value')

    ax2 = ax.twinx()
    ax2.plot(list(cpu.memory.memory.keys()), list(cpu.memory.memory.values()), color='red', label="Memory")
    ax2.set_ylabel('Memory Value')

    plt.legend(loc='upper left')
    plt.show()
