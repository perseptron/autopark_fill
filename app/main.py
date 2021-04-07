import os
import time
from datetime import datetime
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
        if count == 1:
            continue
        row = line.split(';')
        row_owner = row[OWN].strip('"')
        row_koatu = row[KOATU].strip('"')
        row_oper_code = row[OPER_CODE].strip('"')
        row_oper_name = row[OPER_NAME].strip('"')
        row_date = datetime.strptime(row[DATE].strip('"'), "%Y-%m-%d").date()
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

        owner = db.query(Ownership).filter_by(owner=row_owner).first()
        if not owner:
            owner = Ownership(owner=row_owner)
            db.add(owner)
        koatu = db.query(Koatu).filter_by(code=row_koatu).first()
        if not koatu:
            koatu = Koatu(code=row_koatu)
            db.add(koatu)
        operation = db.query(Operations).filter_by(oper_code=row_oper_code).filter_by(oper_name=row_oper_name).first()
        if not operation:
            operation = Operations(oper_code=row_oper_code, oper_name=row_oper_name)
            db.add(operation)
        department = db.query(Departments).filter_by(dep_code=row_dep_code).filter_by(dep=row_dep).first()
        if not department:
            department = Departments(dep_code=row_dep_code, dep=row_dep)
            db.add(department)
        brand = db.query(Brands).filter_by(brand=row_brand).first()
        if not brand:
            brand = Brands(brand=row_brand)
            db.add(brand)
        model = db.query(Models).filter_by(model=row_model).first()
        if not model:
            model = Models(model=row_model)
            db.add(model)
        color = db.query(Colors).filter_by(color=row_color).first()
        if not color:
            color = Colors(color=row_color)
            db.add(color)
        kind = db.query(Kinds).filter_by(kind=row_kind).first()
        if not kind:
            kind = Kinds(kind=row_kind)
            db.add(kind)
        body = db.query(Body).filter_by(body=row_body).first()
        if not body:
            body = Body(body=row_body)
            db.add(body)
        purpose = db.query(Purpose).filter_by(purpose=row_purpose).first()
        if not purpose:
            purpose = Purpose(purpose=row_purpose)
            db.add(purpose)
        fuel = db.query(Fuel).filter_by(fuel=row_fuel).first()
        if not fuel:
            fuel = Fuel(fuel=row_fuel)
            db.add(fuel)
        plate = db.query(Plates).filter_by(plate=row_plate).first()
        if not plate:
            plate = Plates(plate=row_plate)
            db.add(plate)
        db.flush()
        vehicle = Vehicles(brand_id=brand.id, model_id=model.id, color_id=color.id, kind_id=kind.id, body_id=body.id,
                           purpose_id=purpose.id, fuel_id=fuel.id, plate_id=plate.id, year=row_year, capacity=row_capacity,
                           own_weight=row_own_weight, total_weight=row_total_weight)
        db.add(vehicle)
        db.flush()
        record = TZ_data(owner_id=owner.id, koatu_id=koatu.id, operation_id=operation.id, department_id=department.id,
                         date=row_date, vehicle_id=vehicle.id)
        db.add(record)
        db.commit()


        print(count)
        # print("Line{}: {}".format(count, line.strip()))

    # Closing files
    csv_file.close()
    print('the end')
