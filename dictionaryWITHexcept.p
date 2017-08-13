studnet = {
    "name": 'Mark',
    'id': '176',
    'year': 1988
}

print(studnet)
studnet['name']="Mark Jon"
print(studnet)
print(studnet["id"])
print(studnet.keys())
print(studnet.values())
del studnet['year']
try:
    n=studnet["nazwiko"]
except Exception as error:
    print("Nie może znleźć nazwiska ")
    print(error)
print(studnet)
