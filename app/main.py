import MySQLdb

from app import engine, db, cursor, connection
from app.line import Line
from app.utils import get_lines_count
from app.model import Base, DictSearch


def main():
    create_db()
    # download(files.zip_2013, '2013.zip', progress=progress_down)
    file = 'tz_opendata_z01012013_po31122013.txt'
    # file = unzip('2013.zip', progress=progress_unzip)[0].filename
    # os.remove("2013.zip")
    print(get_lines_count(file))
    # test()
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
    own = DictSearch()
    koatu = DictSearch()
    oper = DictSearch()
    dpt = DictSearch()
    brand = DictSearch()
    model = DictSearch()
    color = DictSearch()
    kind = DictSearch()
    body = DictSearch()
    purpose = DictSearch()
    fuel = DictSearch()
    plate = DictSearch()
    vehicle =DictSearch()
    record = DictSearch()

    sql_own = """Insert into Ownership (id, owner) values  (%s, %s)"""
    own_val = []
    sql_koatu = """Insert into Koatu (id, code) values  (%s, %s)"""
    koatu_val = []
    sql_oper = """Insert into Operations (id, oper_code, oper_name) values  (%s, %s, %s)"""
    oper_val = []
    sql_dpt = """Insert into Departments (id, dep_code, dep) values  (%s, %s, %s)"""
    dpt_val = []
    sql_brand = """Insert into Brands (id, brand) values  (%s, %s)"""
    brand_val = []
    sql_model = """Insert into Models (id, brand_id, model) values  (%s, %s, %s)"""
    model_val = []
    sql_color = """Insert into Colors (id, color) values  (%s, %s)"""
    color_val = []
    sql_kind = """Insert into Kinds (id, kind) values  (%s, %s)"""
    kind_val = []
    sql_body = """Insert into Body (id, body) values  (%s, %s)"""
    body_val = []
    sql_purpose = """Insert into Purpose (id, purpose) values  (%s, %s)"""
    purpose_val = []
    sql_fuel = """Insert into Fuel (id, fuel) values  (%s, %s)"""
    fuel_val = []
    sql_plate = """Insert into Plates (id, plate) values  (%s, %s)"""
    plate_val = []
    sql_vehicle = """Insert into Vehicles (id, brand_id, model_id, color_id, kind_id, body_id, purpose_id, fuel_id, plate_id, year, capacity, own_weight, total_weight)  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    vehicle_val = []
    sql_rec = """ Insert into TZ_data(owner_id, koatu_id, operation_id, department_id, date) values (%s, %s, %s, %s, %s)"""
    rec_val = []

    for row in csv_file:
        count += 1
        if count == 1:
            continue
        data = Line(row)

        own = own.get_id(data.owner)
        koatu = koatu.get_id(data.koatu)
        oper = oper.get_id(data.oper[0])
        dpt = dpt.get_id(data.dep[0])
        brand = brand.get_id(data.brand)
        model = model.get_id((abs(brand.id), data.model))
        color = color.get_id(data.color)
        kind = kind.get_id(data.kind)
        body = body.get_id(data.body)
        purpose = purpose.get_id(data.purpose)
        fuel = fuel.get_id(data.fuel)
        plate = plate.get_id(data.plate)
        vehicle = vehicle.get_id(
            (abs(brand.id), abs(model.id), abs(color.id), abs(kind.id), abs(body.id), abs(purpose.id),
             abs(fuel.id), abs(plate.id), data.year, data.capacity, data.own_weight, data.total_weight))

        if own.id < 0:
            own_val.append(((abs(own.id), data.owner)))
            # db.add(Ownership(id=abs(own.id), owner=data.owner))
        if koatu.id < 0:
            koatu_val.append(((abs(koatu.id), data.koatu)))
            # db.add(Koatu(id=abs(koatu.id), code=data.koatu))
        if oper.id < 0:
            oper_val.append(((abs(oper.id), data.oper[0], data.oper[1])))
            # db.add(Operations(id=abs(oper.id), oper_code=data.oper[0], oper_name=data.oper[1]))
        if dpt.id < 0:
            dpt_val.append(((abs(dpt.id), data.dep[0], data.dep[1])))
            # db.add(Departments(id=abs(dpt.id), dep_code=data.dep[0], dep=data.dep[1]))
        if brand.id < 0:
            brand_val.append(((abs(brand.id), data.brand)))
            # db.add(Brands(id=abs(brand.id), brand=data.brand))
        if model.id < 0:
            model_val.append(((abs(model.id), abs(brand.id), data.model)))
            # db.add(Models(id=abs(model.id), brand_id=abs(brand.id), model=data.model))
        if color.id < 0:
            color_val.append(((abs(color.id), data.color)))
            # db.add(Colors(id=abs(color.id), color=data.color))
        if kind.id < 0:
            kind_val.append(((abs(kind.id), data.kind)))
            # db.add(Kinds(id=abs(kind.id), kind=data.kind))
        if body.id < 0:
            body_val.append(((abs(body.id), data.body)))
            # db.add(Body(id=abs(body.id), body=data.body))
        if purpose.id < 0:
            purpose_val.append(((abs(purpose.id), data.purpose)))
            # db.add(Purpose(id=abs(purpose.id), purpose=data.purpose))
        if fuel.id < 0:
            fuel_val.append(((abs(fuel.id), data.fuel)))
            # db.add(Fuel(id=abs(fuel.id), fuel=data.fuel))
        if plate.id < 0:
            plate_val.append(((abs(plate.id), data.plate)))
            # db.add(Plates(id=abs(plate.id), plate=data.plate))

        if vehicle.id < 0:
            vehicle_val.append(((abs(vehicle.id), abs(brand.id), abs(model.id), abs(color.id), abs(kind.id),
                                         abs(body.id), abs(purpose.id), abs(fuel.id), abs(plate.id), data.year,
                                         data.capacity, data.own_weight, data.total_weight)))

        rec_val.append(((abs(own.id), abs(koatu.id), abs(oper.id), abs(dpt.id), data.date)))


        #     db.add(Vehicles(id=abs(vehicle.id), brand_id=abs(brand.id), model_id=abs(model.id), color_id=abs(color.id), kind_id=abs(kind.id), body_id=abs(body.id),
        #                    purpose_id=abs(purpose.id), fuel_id=abs(fuel.id), plate_id=abs(plate.id), year=data.year, capacity=data.capacity,
        #                    own_weight=data.own_weight, total_weight=data.total_weight))
        #
        # db.add(TZ_data(owner_id=abs(own.id), koatu_id=abs(koatu.id), operation_id=abs(oper.id), department_id=abs(dpt.id),
        #                  date=data.date))



        # record = TZ_data(owner_id=abs(own.id), koatu_id=abs(koatu.id), operation_id=abs(oper.id), department_id=abs(dpt.id),
        #                  date=data.date)
        # db.add(record)
        if count%100 == 0:
            print(count)
            if len(own_val) > 0:
                cursor.executemany(sql_own, own_val)
                own_val.clear()
            if len(koatu_val) > 0:
                cursor.executemany(sql_koatu, koatu_val)
                koatu_val.clear()
            if len(oper_val) > 0:
                cursor.executemany(sql_oper, oper_val)
                oper_val.clear()
            if len(dpt_val) > 0:
                cursor.executemany(sql_dpt, dpt_val)
                dpt_val.clear()
            if len(brand_val) > 0:
                cursor.executemany(sql_brand, brand_val)
                brand_val.clear()
            if len(model_val) > 0:
                cursor.executemany(sql_model, model_val)
                model_val.clear()
            if len(color_val) > 0:
                cursor.executemany(sql_color, color_val)
                color_val.clear()
            if len(kind_val) > 0:
                cursor.executemany(sql_kind, kind_val)
                kind_val.clear()
            if len(body_val) > 0:
                cursor.executemany(sql_body, body_val)
                body_val.clear()
            if len(purpose_val) > 0:
                cursor.executemany(sql_purpose, purpose_val)
                purpose_val.clear()
            if len(fuel_val) > 0:
                cursor.executemany(sql_fuel, fuel_val)
                fuel_val.clear()
            if len(plate_val) > 0:
                cursor.executemany(sql_plate, plate_val)
                plate_val.clear()
            if len(vehicle_val) > 0:
                cursor.executemany(sql_vehicle, vehicle_val)
                vehicle_val.clear()

            cursor.executemany(sql_rec, rec_val)
            rec_val.clear()

            # db.commit()
            connection.commit()


        # print("Line{}: {}".format(count, line.strip()))

    # Closing files
    csv_file.close()
    print('the end')
