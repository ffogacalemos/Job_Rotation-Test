import json

file = open('dados.json')
data = json.load(file)


def less():
    menor = (data[0]["valor"])
    for i in range(len(data)):
        if menor >= (data[i]["valor"]):
            menor = (data[i]["valor"])

    print(menor)


def more():
    maior = (data[0]["valor"])
    for i in range(len(data)):
        if maior <= (data[i]["valor"]):
            maior = (data[i]["valor"])

    print(maior)


def average():
    days = 0
    total = 0
    for i in range(len(data)):
        if data[i]['valor'] != 0:
            days += 1
            total += data[i]['valor']
    print(total / days)
