from f1dbExtract import f1dbExtract

response1 = f1dbExtract("F1Drivers_Dataset.csv")

response1.queries()
response1.response()

print(response1.response())