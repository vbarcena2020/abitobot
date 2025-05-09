import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV usando numpy
file_path = "joint_states.csv"
data = np.genfromtxt(file_path, delimiter=',', names=True, dtype=None, encoding='utf-8')

# Filtrar los joints relevantes
joints_of_interest = [
  "arm_1_link_joint",
  "arm_2_link_joint",
  "arm_3_link_joint",
  "gripper_left_link_joint",
  "gripper_right_link_joint"
]
filtered_data = data[np.isin(data["joint_name"], joints_of_interest)]

# Calcular el gasto (G) en cada instante de tiempo
abs_effort = np.abs(filtered_data["effort"])
timestamps = filtered_data["timestamp"]
unique_timestamps = np.unique(timestamps)

# Ajustar el tiempo para que inicie en 0
min_timestamp = unique_timestamps.min()
adjusted_timestamps = unique_timestamps - min_timestamp

g_per_time = np.array([
  (timestamp, abs_effort[timestamps == (timestamp + min_timestamp)].sum())
  for timestamp in adjusted_timestamps
], dtype=[("timestamp", float), ("G", float)])

# Graficar el gasto (G) a lo largo del tiempo
plt.figure(figsize=(10, 6))
plt.plot(g_per_time["timestamp"], g_per_time["G"], label="G_parcial")
plt.xlabel("Tiempo (s)")
plt.ylabel("Gasto")
plt.title("Gasto de Potencia")
plt.legend()
plt.grid()
plt.show()

