from f1dbExtract import f1dbExtract

response1 = f1dbExtract("D:\Aplicaciones\Visual Studio Code\Proyectos Visual\F1DB\F1Drivers_Dataset.csv")

response1.queries()

print(response1.response())