from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, DATE, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app import db

Base = declarative_base()


class DictSearch:
    def __init__(self):
        self.data = {}
        # dataset = db.query(Cls).all()
        # for record in dataset:
        #     self.data[record.color] = record.id
        self.inc = 0
        self._id = 0
        self.value = 0

    def add(self, key):
        # last = self.__get_last()
        # if last:
        #     id = self.data.get(last)
        # else:
        #     id = 0
        self.inc = self.inc + 1
        self.data[key] = self.inc
        return self.inc

    def __get_last(self):
        if len(list(self.data)) > 0:
            return list(self.data)[-1]
        else:
            return None

    def get_id(self, key):
        val = self.data.get(key)
        if val:
            self.value = key
            self._id = int(val)
        else:
            self._id = -(self.add(key))
        return self

# version2: declarative
class Ownership(Base, DictSearch):
    __tablename__ = 'ownership'
    id = Column(INTEGER, primary_key=True)
    owner = Column(VARCHAR(2), nullable=False, unique=True)
    records = relationship('TZ_data', backref='owner', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Ownership).order_by(Ownership.id).all():
            self.data[record.owner] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Ownership {}>'.format(self.owner)


class Koatu(Base, DictSearch):
    __tablename__ = 'koatu'
    id = Column(INTEGER, primary_key=True)
    code = Column(VARCHAR(10), nullable=False, unique=True)
    records = relationship('TZ_data', backref='koatu', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Koatu).order_by(Koatu.id).all():
            self.data[record.code] = record.id
            self.inc = record.id


    def __repr__(self):
        return '<Koatu {}>'.format(self.code)


class Operations(Base, DictSearch):
    __tablename__ = 'operations'
    id = Column(INTEGER, primary_key=True)
    oper_code = Column(INTEGER, nullable=False, unique=True)
    oper_name =Column(VARCHAR(128), nullable=False)
    records = relationship('TZ_data', backref='operation', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Operations).order_by(Operations.id).all():
            self.data[record.oper_code] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Operations {}>'.format(self.oper_code)


class Departments(Base, DictSearch):
    __tablename__ = 'departments'
    id = Column(INTEGER, primary_key=True)
    dep_code = Column(INTEGER, nullable=False, unique=True)
    dep = Column(VARCHAR(200), nullable=False)
    records = relationship('TZ_data', backref='department', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Departments).order_by(Departments.id).all():
            self.data[record.dep_code] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Operations {}>'.format(self.dep_code)


class Brands(Base, DictSearch):
    __tablename__ = 'brands'
    id = Column(INTEGER, primary_key=True)
    brand = Column(VARCHAR(64), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='brand', lazy='dynamic')
    models = relationship('Models', backref='brand', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Brands).order_by(Brands.id).all():
            self.data[record.brand] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Brand {}>'.format(self.brand)


class Models(Base, DictSearch):
    __tablename__ = 'models'
    id = Column(INTEGER, primary_key=True)
    brand_id = Column(INTEGER, ForeignKey('brands.id'), nullable=False)
    model = Column(VARCHAR(64), nullable=False)
    vehicles = relationship('Vehicles', backref='model', lazy='dynamic')
    __table_args__ = (UniqueConstraint('brand_id', 'model', name='_model_uc'),)

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Models).order_by(Models.id).all():
            self.data[record.brand_id, record.model] = record.id
            self.inc = record.id


    def __repr__(self):
        return '<Model {}>'.format(self.model)


class Colors(Base, DictSearch):
    __tablename__ = 'colors'
    id = Column(INTEGER, primary_key=True)
    color = Column(VARCHAR(20), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='colors', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Colors).order_by(Colors.id).all():
            self.data[record.color] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Color {}>'.format(self.color)


class Kinds(Base, DictSearch):
    __tablename__ = 'kinds'
    id = Column(INTEGER, primary_key=True)
    kind = Column(VARCHAR(20), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='kinds', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Kinds).order_by(Kinds.id).all():
            self.data[record.kind] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Kind {}>'.format(self.kind)


class Body(Base, DictSearch):
    __tablename__ = 'body'
    id = Column(INTEGER, primary_key=True)
    body = Column(VARCHAR(40), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='body', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Body).order_by(Body.id).all():
            self.data[record.body] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Body {}>'.format(self.body)


class Purpose(Base, DictSearch):
    __tablename__ = 'purpose'
    id = Column(INTEGER, primary_key=True)
    purpose = Column(VARCHAR(20), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='purpose', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Purpose).order_by(Purpose.id).all():
            self.data[record.purpose] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Purpose {}>'.format(self.purpose)


class Fuel(Base, DictSearch):
    __tablename__ = 'fuel'
    id = Column(INTEGER, primary_key=True)
    fuel = Column(VARCHAR(20), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='fuel', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Fuel).order_by(Fuel.id).all():
            self.data[record.fuel] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Fuel {}>'.format(self.fuel)


class Plates(Base, DictSearch):
    __tablename__ = 'plates'
    id = Column(INTEGER, primary_key=True)
    plate = Column(VARCHAR(10), nullable=False, unique=True)
    vehicles = relationship('Vehicles', backref='plate', lazy='dynamic')

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Plates).order_by(Plates.id).all():
            self.data[record.plate] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Plates {}>'.format(self.plate)

class Vehicles(Base, DictSearch):
    __tablename__ = 'vehicles'
    id = Column(INTEGER, primary_key=True)
    brand_id = Column(INTEGER, ForeignKey('brands.id'), nullable=False)
    model_id = Column(INTEGER, ForeignKey('models.id'), nullable=False)
    color_id = Column(INTEGER, ForeignKey('colors.id'), nullable=False)
    kind_id = Column(INTEGER, ForeignKey('kinds.id'), nullable=False)
    body_id = Column(INTEGER, ForeignKey('body.id'), nullable=False)
    purpose_id = Column(INTEGER, ForeignKey('purpose.id'), nullable=False)
    fuel_id = Column(INTEGER, ForeignKey('fuel.id'))
    plate_id = Column(INTEGER, ForeignKey('plates.id'))
    year = Column(INTEGER, nullable=False)
    capacity = Column(INTEGER)
    own_weight = Column(INTEGER, nullable=False)
    total_weight = Column(INTEGER, nullable=False)
    # combination = Column(VARCHAR(10), unique=True, nullable=False)

    def __init__(self):
        DictSearch.__init__(self)
        print("initializing ", type(self))
        for record in db.query(Vehicles).order_by(Vehicles.id).all():
            self.data[record.brand_id, record.model_id, record.color_id, record.kind_id, record.body_id,
                      record.purpose_id, record.fuel_id, record.plate_id, record.year, record.capacity,
                      record.own_weight, record.total_weight] = record.id
            self.inc = record.id

    def __repr__(self):
        return '<Vehicle {}>'.format(self.combination)


class  TZ_data(Base):
    __tablename__ = 'tz_data'
    id = Column(INTEGER, primary_key=True)
    owner_id = Column(INTEGER, ForeignKey('ownership.id'), nullable=False)
    koatu_id = Column(INTEGER, ForeignKey('koatu.id'))
    operation_id = Column(INTEGER, ForeignKey('operations.id'), nullable=False)
    department_id = Column(INTEGER, ForeignKey('departments.id'), nullable=False)
    date = Column(DATE, nullable=False)
    # vehicle_id = Column(INTEGER, ForeignKey('vehicles.id'))




