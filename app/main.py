import MySQLdb

from app import engine, db, cursor, connection
from app.line import Line
from app.utils import get_lines_count
from app.model import Base, DictSearch, DsOwnership, DsKoatu, DsOperations, DsDepartments, DsBrands, DsModels, DsColors, \
    DsKinds, DsBody, DsPurpose, DsFuel, DsPlates, DsVehicles, DsRecords


def main():
    create_db()
    # download(files.zip_2013, '2013.zip', progress=progress_down)
    file = 'tz_opendata_z01012013_po31122013.csv'
    # file = unzip('2013.zip', progress=progress_unzip)[0].filename
    # os.remove("2013.zip")
    print(get_lines_count(file))
    # test()
    fill_db(file)


def progress_down(cur, total):
    print('{} %, of total {} MB'.format(cur, round(total / 1024 / 1024)))
    # print ('\rDownload [%d%%]'%cur, end="")


def progress_unzip(cur, total):
    print('unzipping file {} MB'.format(round(total / 1024 / 1024)))


def create_db():
    Base.metadata.create_all(engine)


def fill_db(file_path):
    # Opening file
    csv_file = open(file_path, 'r', encoding='utf-8')
    count = 0

    own = DsOwnership()
    koatu = DsKoatu()
    oper = DsOperations()
    dpt = DsDepartments()
    brand = DsBrands()
    model = DsModels()
    color = DsColors()
    kind = DsKinds()
    body = DsBody()
    purpose = DsPurpose()
    fuel = DsFuel()
    plate = DsPlates()
    vehicle = DsVehicles()
    records = DsRecords()

    print("Using for loop")
    for row in csv_file:
        count += 1
        if count == 1:
            continue
        data = Line(row)

        own = own.get_id(data.owner)
        koatu = koatu.get_id(data.koatu)
        oper = oper.get_id(data.oper[0], fields=(data.oper[1],))
        dpt = dpt.get_id(data.dep[0], fields=(data.dep[1],))
        brand = brand.get_id(data.brand)
        model = model.get_id((brand._id, data.model))
        color = color.get_id(data.color)
        kind = kind.get_id(data.kind)
        body = body.get_id(data.body)
        purpose = purpose.get_id(data.purpose)
        fuel = fuel.get_id(data.fuel)
        plate = plate.get_id(data.plate)
        vehicle = vehicle.get_id(
            (brand._id, model._id, color._id, kind._id, body._id, purpose._id, fuel._id, plate._id,
             data.year, data.capacity, data.own_weight, data.total_weight))

        records = records.get_id((oper._id, data.date, vehicle._id), fields=(own._id, koatu._id, dpt._id))

        if count % 10000 == 0:
            print(count)

            own.save()
            koatu.save()
            oper.save()
            dpt.save()
            brand.save()
            model.save()
            color.save()
            kind.save()
            body.save()
            purpose.save()
            fuel.save()
            plate.save()
            vehicle.save()
            records.save()

            connection.commit()

        # print("Line{}: {}".format(count, line.strip()))

    # Closing files
    csv_file.close()
    print('the end')
