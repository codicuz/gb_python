import json

person = [
    {
        "name": "Jhon",
        "salary": 15000,
    },
    {
        "name": "Jhon2",
        "salaries": 21000
    },
    {
        "name": "Jhon3",
        "salaries": 21000
    },
    {
        "name": "Jhon4",
        "salaries": 20000
    },
    {
        "name": "Jhon5",
        "salaries": 19000
    },
    {
        "name": "Jhon6",
        "salaries": 20000
    },
    {
        "name": "Jhon7",
        "salaries": 34000
    },
    {
        "name": "Jhon8",
        "salaries": 17000
    },
    {
        "name": "Jhon9",
        "salaries": 18000
    },
    {
        "name": "Jhon10",
        "salaries": 21000
    },
    {
        "name": "Jhon11",
        "salaries": 19500
    },
    {
        "name": "Jhon12",
        "salaries": 21500
    }
]


with open('person.json', 'w') as file_stream:
    json.dump(person, file_stream)

