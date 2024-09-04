import pandas as pd
import matplotlib.pyplot as plt

# Lista de valores de pH coletados manualmente
ph_values = [7.1, 6.5, 7.8, 6.9, 7.0, 6.8, 7.2, 7.3, 6.7, 7.4]  # Exemplo de valores, trocar pelos valores coletados !!

df = pd.DataFrame({
    'Reading': range(1, len(ph_values) + 1),
    'pH': ph_values
})

df.to_csv('ph_readings.csv', index=False)
print("Dados salvos em 'ph_readings.csv'")

mean_ph = df['pH'].mean()
min_ph_value = df['pH'].min()
max_ph_value = df['pH'].max()

print(f"Valor médio de pH: {mean_ph:.2f}")
print(f"Valor mínimo de pH: {min_ph_value:.2f}")
print(f"Valor máximo de pH: {max_ph_value:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(df['Reading'], df['pH'], marker='o', linestyle='-', color='b')
plt.title('Leituras de pH da Água')
plt.xlabel('Leitura')
plt.ylabel('pH')
plt.grid(True)
plt.savefig('ph_readings_plot.png')
plt.show()
print("Gráfico salvo como 'ph_readings_plot.png'")
