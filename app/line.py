from datetime import datetime

OWN = 0
KOATU = 1
OPER_CODE = 2
OPER_NAME = 3
DATE = 4
DEP_CODE = 5
DEP = 6
BRAND = 7
MODEL = 8
YEAR = 9
COLOR = 10
KIND = 11
BODY = 12
PURPOSE = 13
FUEL = 14
CAPACITY = 15
OWN_WEIGHT = 16
TOTAL_WEIGHT = 17
PLATE = 18


class Line:
    def __init__(self, row):
        row = row.strip("\n").upper().split(';')
        self.owner = row[OWN].strip('"')
        koatu = row[KOATU].strip('"')
        self.koatu = koatu if koatu and koatu != "NULL" else '0000000000'
        self.oper = (row[OPER_CODE].strip('"'), row[OPER_NAME].strip('"'))
        self.date = datetime.strptime(row[DATE].strip('"'), "%Y-%m-%d").date()
        self.dep = (row[DEP_CODE].strip('"'), row[DEP].strip('"'))
        self.brand = row[BRAND].strip('"')
        self.model = row[MODEL].strip('"')
        self.year = row[YEAR].strip('"')
        self.color = row[COLOR].strip('"')
        self.kind = row[KIND].strip('"')
        self.body = row[BODY].strip('"')
        self.purpose = row[PURPOSE].strip('"')
        self.fuel = row[FUEL].strip('"')
        capacity = row[CAPACITY].strip('"')
        own_weight = row[OWN_WEIGHT].strip('"')
        total_weight = row[TOTAL_WEIGHT].strip('"')
        self.capacity = capacity if capacity and capacity != "NULL" else 0
        self.own_weight = own_weight if own_weight and own_weight != "NULL" else 0
        self.total_weight = total_weight if total_weight and total_weight != "NULL" else 0
        self.plate = row[PLATE].strip('"').strip(" ")


