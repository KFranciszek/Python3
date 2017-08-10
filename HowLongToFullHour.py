from datetime import datetime
now=datetime.now()
m=now.minute
ile=60-m
print("Do pełnej godziny pozostało:" +str(ile)+ "minut")
