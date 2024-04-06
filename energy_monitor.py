# Energy Monitor and Energy Monitor GUI
import sys
import smartpy as sp
import time
from tkinter import Tk, Label, Button, Entry, StringVar

# Energy Monitor

class EnergyMonitor:
    def __init__trait(self):
        self.energySupplied = sp.BigMap()
    


        class EnergyMonitor:
            def __init__(self):
                self.energySupplied = sp.BigMap()
                self.energyCreditsMinted = 0

            def supplyEnergy(self, params): 
                self.energySupplied[SmartPy.sender] = params.energy 

            def issueEnergyCredits(self, params):
                self.energySupplied[SmartPy.sender] += params.energy_credits
                self.energyCreditsMinted += params.energy_credits

            def countEnergyCreditsMintedPerSecond(self):
                start_time = time.time()
                while True:
                    time.sleep(30)
                    elapsed_time = time.time() - start_time
                    print(f"Energy credits minted per second: {self.energyCreditsMinted / elapsed_time}")

            def burnEnergyCredits(self, params):
                if self.energySupplied[SmartPy.sender] < params.energy_credits:
                    raise ValueError("Not enough energy credits to burn")
                self.energySupplied[sp.sender] -= params.energy_credits

            def getEnergyCreditValue(self):
                total_energy_supplied = sum(self.energySupplied.values())
                total_energy_credits = len(self.energySupplied)
                if total_energy_credits == 0:
                    return 0
                return total_energy_supplied / total_energy_credits
            
            if __name__ == "__main__":
                monitor = EnergyMonitor()
                print(monitor.getEnergyCreditValue())

# Energy Monitor GUI
class EnergyMonitorGUI:
    def __init__(self, monitor):
        self.monitor = monitor
        self.root = Tk()
        self.root.title("Energy Monitor GUI")

        self.energy_credits_label = Label(self.root, text="Energy Credits Issued")
        self.energy_credits_label.pack()

        self.energy_credits_value = StringVar()
        self.energy_credits_value.set(self.monitor.energyCreditsMinted)
        self.energy_credits_value_label = Label(self.root, textvariable=self.energy_credits_value)
        self.energy_credits_value_label.pack()

        self.issue_button = Button(self.root, text="Issue Energy Credits", command=self.issue_energy_credits)
        self.issue_button.pack()

        self.burn_button = Button(self.root, text="Burn Energy Credits", command=self.burn_energy_credits)
        self.burn_button.pack()

        self.root.mainloop()

    def issue_energy_credits(self):
        self.monitor.issueEnergyCredits({'energy_credits': 1})
        self.energy_credits_value.set(self.monitor.energyCreditsMinted)

    def burn_energy_credits(self):
        try:
            self.monitor.burnEnergyCredits({'energy_credits': 1})
            self.energy_credits_value.set(self.monitor.energyCreditsMinted)
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    monitor = EnergyMonitor()
    gui = EnergyMonitorGUI(monitor)
    

