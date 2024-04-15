import tkinter as tk
from tkinter import messagebox

#project by Azad Aliyev, Emre Alptekin and Sadiq Aliyev - 54850_54132_54741

def calculate_energy_consumption():
    try:
        area = float(area_entry.get())
        occupants = int(occupants_entry.get())
        heating_power = float(heating_power_entry.get())
        appliances_energy = float(appliances_energy_entry.get())
        insulation_quality = float(insulation_quality_entry.get())
        windows_area = float(windows_area_entry.get())
        window_type = window_type_var.get()
        external_temp = float(external_temp_entry.get())
        renewable_sources = float(renewable_sources_entry.get())
        wall_insulation = float(wall_insulation_entry.get())

        seasonal_adjustment = (1.2 + 0.8) / 2
        heating_adjustment = (external_temp + 15) / 35
        window_loss_factor = windows_area * (0.85 if window_type == 'double' else 1.2)

        heating_energy = (heating_power * area * seasonal_adjustment * heating_adjustment * (
                    1 - wall_insulation) * window_loss_factor)

        total_energy_consumption = (heating_energy + appliances_energy * 365) - renewable_sources * 365

        energy_per_person = total_energy_consumption / occupants

        energy_per_area_per_year = total_energy_consumption / (area * insulation_quality)

        result_label.config(text="Energy consumption: %.2f kWh/m^2 per year" % energy_per_area_per_year)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


root = tk.Tk()
root.title("Energy Consumption Calculator")

tk.Label(root, text="Area of the house (m^2):").grid(row=0, column=0, padx=5, pady=5)
area_entry = tk.Entry(root)
area_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number of occupants:").grid(row=1, column=0, padx=5, pady=5)
occupants_entry = tk.Entry(root)
occupants_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Heating power (kW):").grid(row=2, column=0, padx=5, pady=5)
heating_power_entry = tk.Entry(root)
heating_power_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Appliances energy (kWh/day):").grid(row=3, column=0, padx=5, pady=5)
appliances_energy_entry = tk.Entry(root)
appliances_energy_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Insulation quality (coefficient):").grid(row=4, column=0, padx=5, pady=5)
insulation_quality_entry = tk.Entry(root)
insulation_quality_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="Windows area (m^2):").grid(row=5, column=0, padx=5, pady=5)
windows_area_entry = tk.Entry(root)
windows_area_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Window type:").grid(row=6, column=0, padx=5, pady=5)
window_type_var = tk.StringVar(root)
window_type_var.set("single")
window_type_menu = tk.OptionMenu(root, window_type_var, "single", "double")
window_type_menu.grid(row=6, column=1, padx=5, pady=5)

tk.Label(root, text="External temperature (Celsius):").grid(row=7, column=0, padx=5, pady=5)
external_temp_entry = tk.Entry(root)
external_temp_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Label(root, text="Renewable energy sources (kWh/year):").grid(row=8, column=0, padx=5, pady=5)
renewable_sources_entry = tk.Entry(root)
renewable_sources_entry.grid(row=8, column=1, padx=5, pady=5)

tk.Label(root, text="Wall insulation factor (0-1):").grid(row=9, column=0, padx=5, pady=5)
wall_insulation_entry = tk.Entry(root)
wall_insulation_entry.grid(row=9, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_energy_consumption)
calculate_button.grid(row=10, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=2, pady=5)

root.mainloop()