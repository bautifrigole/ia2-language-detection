import matplotlib.pyplot as plt

modelos = ['Naive Bayes', 'Regresión Lineal', 'LSTM', 'Transformer']
accuracy = [0.2, 17.7, 995, 1024]

plt.figure(figsize=(8, 6))
bars = plt.bar(modelos, accuracy, color=['skyblue', 'orange', 'lightgreen', 'salmon'])

plt.title('Comparación del Tiempo de Entrenamiento entre Modelos')
plt.xlabel('Modelos')
plt.ylabel('Tiempo de Entrenamiento (s)')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.1f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('plots/comparative_time.png')
plt.show()
