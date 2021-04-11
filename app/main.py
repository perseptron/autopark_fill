from app import engine, db
from app.line import Line
from app.utils import get_lines_count
from app.model import Base, Colors, Ownership, Koatu, Operations, Departments, Brands, Models, Kinds, Body, Purpose, \
    Fuel, \
    Plates, Vehicles, TZ_data, DictSearch


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

        # if own.id < 0:
        #     db.add(Ownership(id=abs(own.id), owner=data.owner))
        # if koatu.id < 0:
        #     db.add(Koatu(id=abs(koatu.id), code=data.koatu))
        # if oper.id < 0:
        #     db.add(Operations(id=abs(oper.id), oper_code=data.oper[0], oper_name=data.oper[1]))
        # if dpt.id < 0:
        #     db.add(Departments(id=abs(dpt.id), dep_code=data.dep[0], dep=data.dep[1]))
        # if brand.id < 0:
        #     db.add(Brands(id=abs(brand.id), brand=data.brand))
        # if model.id < 0:
        #     db.add(Models(id=abs(model.id), brand_id=abs(brand.id), model=data.model))
        # if color.id < 0:
        #     db.add(Colors(id=abs(color.id), color=data.color))
        # if kind.id < 0:
        #     db.add(Kinds(id=abs(kind.id), kind=data.kind))
        # if body.id < 0:
        #     db.add(Body(id=abs(body.id), body=data.body))
        # if purpose.id < 0:
        #     db.add(Purpose(id=abs(purpose.id), purpose=data.purpose))
        # if fuel.id < 0:
        #     db.add(Fuel(id=abs(fuel.id), fuel=data.fuel))
        # if plate.id < 0:
        #     db.add(Plates(id=abs(plate.id), plate=data.plate))
        # if vehicle.id < 0:
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
            db.commit()




        # print("Line{}: {}".format(count, line.strip()))

    # Closing files
    csv_file.close()
    print('the end')
