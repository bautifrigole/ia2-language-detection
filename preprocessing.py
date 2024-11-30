import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("language_detection.csv")
print(df.describe())
language_counts = df['Language'].value_counts()

plt.figure(figsize=(12, 6))
language_counts.plot(kind='bar', color='skyblue')
plt.title("Distribución de Idiomas en el Dataset")
plt.xlabel("Idioma")
plt.ylabel("Cantidad de Textos")
plt.xticks(rotation=45)
plt.savefig("plots/language_distribution.png")


# Añadir una columna con la longitud del texto
df['Text_length'] = df['Text'].str.len()

# Graficar
plt.figure(figsize=(14, 6))
df.boxplot(column='Text_length', by='Language', grid=False, showfliers=False, patch_artist=True, 
           boxprops=dict(facecolor='lightblue', color='blue'))
plt.title("Distribución de la Longitud del Texto por Idioma")
plt.suptitle("")  # Elimina el título generado automáticamente por pandas
plt.xlabel("Idioma")
plt.ylabel("Longitud del Texto")
plt.xticks(rotation=45)
plt.savefig("plots/text_length_distribution.png")


from wordcloud import WordCloud

# Filtrar un idioma específico (ejemplo: inglés)
english_texts = " ".join(df[df['Language'] == 'English']['Text'])

# Generar nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(english_texts)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Nube de Palabras para Textos en Inglés")
plt.savefig("plots/english_wordcloud.png")


plt.figure(figsize=(8, 8))
language_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab10')
plt.title("Porcentaje de Textos por Idioma")
plt.ylabel("")  # Elimina etiqueta por defecto
plt.savefig("plots/language_pie_chart.png")


spanish_texts = " ".join(df[df['Language'] == 'Spanish']['Text'])

# Generar nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(spanish_texts)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Nube de Palabras para Textos en Español")
plt.savefig("plots/spanish_wordcloud.png")
