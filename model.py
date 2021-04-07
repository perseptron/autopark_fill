from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Ownership(Base):
    __tablename__ = 'ownership'
    id = Column(INTEGER, primary_key=True)
    owner = Column(VARCHAR(2), nullable=False)
    records = relationship('TZ_data', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Ownership {}>'.format(self.owner)


class Koatu(Base):
    __tablename__ = 'koatu'
    id = Column(INTEGER, primary_key=True)
    code = Column(VARCHAR(10), nullable=False)
    records = relationship('TZ_data', backref='koatu', lazy='dynamic')

    def __repr__(self):
        return '<Koatu {}>'.format(self.code)


class Operations(Base):
    __tablename__ = 'operations'
    id = Column(INTEGER, primary_key=True)
    oper_code = Column(INTEGER, nullable=False)
    oper_name =Column(VARCHAR(128), nullable=False)
    records = relationship('TZ_data', backref='operation', lazy='dynamic')

    def __repr__(self):
        return '<Operations {}>'.format(self.oper_code)


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(INTEGER, primary_key=True)
    dep_code = Column(INTEGER, nullable=False)
    dep = Column(VARCHAR(64), nullable=False)
    records = relationship('TZ_data', backref='department', lazy='dynamic')

    def __repr__(self):
        return '<Operations {}>'.format(self.dep_code)


class Brands(Base):
    __tablename__ = 'brands'
    id = Column(INTEGER, primary_key=True)
    brand = Column(VARCHAR(64), nullable=False)
    vehicles = relationship('Vehicles', backref='brand', lazy='dynamic')

    def __repr__(self):
        return '<Brand {}>'.format(self.brand)


class Models(Base):
    __tablename__ = 'models'
    id = Column(INTEGER, primary_key=True)
    model = Column(VARCHAR(64), nullable=False)
    vehicles = relationship('Vehicles', backref='model', lazy='dynamic')

    def __repr__(self):
        return '<Model {}>'.format(self.model)


class Colors(Base):
    __tablename__ = 'colors'
    id = Column(INTEGER, primary_key=True)
    color = Column(VARCHAR(20), nullable=False)
    vehicles = relationship('Vehicles', backref='colors', lazy='dynamic')

    def __repr__(self):
        return '<Color {}>'.format(self.color)


class Kinds(Base):
    __tablename__ = 'kinds'
    id = Column(INTEGER, primary_key=True)
    kind = Column(VARCHAR(20), nullable=False)
    vehicles = relationship('Vehicles', backref='kinds', lazy='dynamic')

    def __repr__(self):
        return '<Kind {}>'.format(self.kind)


class Body(Base):
    __tablename__ = 'body'
    id = Column(INTEGER, primary_key=True)
    body = Column(VARCHAR(30), nullable=False)
    vehicles = relationship('Vehicles', backref='body', lazy='dynamic')


    def __repr__(self):
        return '<Body {}>'.format(self.body)


class Purpose(Base):
    __tablename__ = 'purpose'
    id = Column(INTEGER, primary_key=True)
    purpose = Column(VARCHAR(20), nullable=False)
    vehicles = relationship('Vehicles', backref='purpose', lazy='dynamic')

    def __repr__(self):
        return '<Purpose {}>'.format(self.purpose)


class Fuel(Base):
    __tablename__ = 'fuel'
    id = Column(INTEGER, primary_key=True)
    fuel = Column(VARCHAR(20), nullable=False)
    vehicles = relationship('Vehicles', backref='fuel', lazy='dynamic')

    def __repr__(self):
        return '<Fuel {}>'.format(self.fuel)


class Plates(Base):
    __tablename__ = 'plates'
    id = Column(INTEGER, primary_key=True)
    plate = Column(VARCHAR(10), nullable=False)
    vehicles = relationship('Vehicles', backref='plate', lazy='dynamic')

    def __repr__(self):
        return '<Plates {}>'.format(self.plate)


class Vehicles(Base):
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
    combination = Column(VARCHAR(10), unique=True, nullable=False)

    def __repr__(self):
        return '<Vehicle {}>'.format(self.combination)


class  TZ_data(Base):
    __tablename__ = 'tz_data'
    id = Column(INTEGER, primary_key=True)
    owner_id = Column(INTEGER, ForeignKey('ownership.id'), nullable=False)
    koatu_id = Column(INTEGER, ForeignKey('koatu.id'))
    operation_id = Column(INTEGER, ForeignKey('operations.id'), nullable=False)
    department_id = Column(INTEGER, ForeignKey('departments.id'), nullable=False)
    data = Column(DATE, nullable=False)
    vehicle_id = Column(INTEGER, ForeignKey('vehicles.id'))




