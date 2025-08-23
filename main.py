from Extract.f1dbExtract import f1dbExtract

response1 = f1dbExtract(r"C:\Users\javim\Documents\U\8\Big data\F1DB\F1Drivers_Dataset.csv")
response1.queries()

print(response1.response())