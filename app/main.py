import os
import time
from zipfile import ZipFile

from tqdm import tqdm

from app import engine, db, files
from app.utils import download, unzip, get_lines_count
from model import Base, Colors, Ownership, Koatu, Operations, Departments, Brands, Models, Kinds, Body, Purpose, Fuel, \
    Plates, Vehicles, TZ_data

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


def main():
    create_db()
    # download(files.zip_2013, '2013.zip', progress=progress_down)
    file = 'tz_opendata_z01012013_po31122013.txt'
    # file = unzip('2013.zip', progress=progress_unzip)[0].filename
    # os.remove("2013.zip")
    print(get_lines_count(file))
    fill_db(file)


def progress_down(cur, total):
    print('{} %, of total {} MB'.format(cur, round(total/1024/1024)))
    # print ('\rDownload [%d%%]'%cur, end="")


def progress_unzip(cur, total):
    print('unzipping file {} MB'.format(round(total/1024/1024)))


def create_db():
    Base.metadata.create_all(engine)



def fill_db(file_path):
    # Opening file
    csv_file = open(file_path, 'r', encoding='utf-8')
    count = 0

    # Using for loop
    print("Using for loop")
    for line in csv_file:
        count += 1
        row = line.split(';')
        row_owner = row[OWN].strip('"')
        row_koatu = row[KOATU].strip('"')
        row_oper_code = row[OPER_CODE].strip('"')
        row_oper_name = row[OPER_NAME].strip('"')
        row_date = row[DATE].strip('"')
        row_dep_code = row[DEP_CODE].strip('"')
        row_dep = row[DEP].strip('"')
        row_brand = row[BRAND].strip('"')
        row_model = row[MODEL].strip('"')
        row_year = row[YEAR].strip('"')
        row_color = row[COLOR].strip('"')
        row_kind = row[KIND].strip('"')
        row_body = row[BODY].strip('"')
        row_purpose = row[PURPOSE].strip('"')
        row_fuel = row[FUEL].strip('"')
        row_capacity = row[CAPACITY].strip('"')
        row_own_weight = row[OWN_WEIGHT].strip('"')
        row_total_weight = row[TOTAL_WEIGHT].strip('"')
        row_plate = row[PLATE].strip('"')

        owner = Ownership(owner=row_owner)
        koatu = Koatu(koatu=row_koatu)
        operation = Operations(oper_code=row_oper_code, oper_name=row_oper_name)
        department = Departments(dep_code=row_dep_code, dep=row_dep)
        brand = Brands(brand=row_brand)
        model = Models(model=row_model)
        color = Colors(color=row_color)
        kind = Kinds(kind=row_kind)
        body = Body(body=row_body)
        purpose = Purpose(purpose=row_purpose)
        fuel = Fuel(fuel=row_fuel)
        plate = Plates(plate=row_plate)
        vehicle = Vehicles(brand_id=brand.id, model_id=model.id, color_id=color.id, kind_id=kind.id, body_id=body.id,
                           purpose_id=purpose.id, fuel_id=fuel.id, plate_id=plate.id, year=row_year, capacity=row_capacity,
                           own_weight=row_own_weight, total_weight=row_total_weight)
        record = TZ_data(owner_id=owner.id, koatu_id=koatu.id, operation_id=operation.id, department_id=department.id,
                         date=row_date, vehicle_id=vehicle.id)




        for data in row:
            print(data.strip('"'))
        # print("Line{}: {}".format(count, line.strip()))

    # Closing files
    csv_file.close()
    print('the end')
