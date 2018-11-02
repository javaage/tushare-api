from peewee import *

database = MySQLDatabase('ichess', **{'charset': 'utf8', 'use_unicode': True, 'host': 'rm-bp149hof32gt0cewt7o.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'root', 'password': 'Java19786028'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Allstock(BaseModel):
    code = CharField(null=True)
    name = CharField(null=True)
    py = CharField(null=True)

    class Meta:
        table_name = 'allstock'

class Attend(BaseModel):
    ascrate = FloatField(null=True)
    code = CharField(null=True)
    descrate = FloatField(null=True)
    equalrate = FloatField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'attend'

class Bkrecord(BaseModel):
    code = CharField(null=True)
    date = DateField(null=True)
    increase = FloatField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'bkrecord'

class CandRate(BaseModel):
    a = FloatField(null=True)
    b = FloatField(null=True)
    code = CharField(null=True)
    increase = FloatField(null=True)
    name = CharField(null=True)
    r = FloatField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'cand_rate'

class Candidate(BaseModel):
    id = CharField(null=True)
    preflist = TextField(null=True)
    time = DateTimeField(null=True)

    class Meta:
        table_name = 'candidate'
        primary_key = False

class Category(BaseModel):
    code = CharField(null=True)
    content = CharField(null=True)
    name = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'category'

class Collect(BaseModel):
    code = CharField(null=True)
    date = DateField(null=True)
    flag = IntegerField(null=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'collect'

class Crecord(BaseModel):
    code = CharField(null=True)
    date = DateField(null=True)
    increase = FloatField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'crecord'

class Daily(BaseModel):
    clmn = FloatField(null=True)
    code = CharField(null=True)
    current = FloatField(null=True)
    date = DateField(null=True)
    high = FloatField(null=True)
    low = FloatField(null=True)
    open = FloatField(null=True)

    class Meta:
        table_name = 'daily'

class DailyRate(BaseModel):
    a = FloatField(null=True)
    b = FloatField(null=True)
    code = CharField(null=True)
    date = DateField(null=True)
    r = FloatField(null=True)

    class Meta:
        table_name = 'daily_rate'

class Director(BaseModel):
    arrow = CharField(null=True)
    code = CharField(null=True)
    level = IntegerField(null=True)
    name = CharField(null=True)
    price = FloatField(null=True)
    time = TextField(null=True)
    total = IntegerField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'director'

class History(BaseModel):
    ftime = TextField(null=True)
    id = CharField(null=True)
    ltime = TextField(null=True)
    record = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'history'
        primary_key = False

class Holder(BaseModel):
    ascrate = FloatField(null=True)
    code = CharField(null=True)
    descrate = FloatField(null=True)
    equalrate = FloatField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'holder'

class IchessTest(BaseModel):
    age = IntegerField(null=True)
    name = CharField(null=True)

    class Meta:
        table_name = 'ichess_test'
        primary_key = False

class Indexrecord(BaseModel):
    avg = FloatField(null=True)
    clmn = FloatField(null=True)
    close = FloatField(null=True)
    code = CharField(index=True, null=True)
    current = FloatField(null=True)
    date = DateField(null=True)
    high = FloatField(null=True)
    low = FloatField(null=True)
    money = FloatField(null=True)
    name = CharField(null=True)
    open = FloatField(null=True)
    time = IntegerField(null=True)

    class Meta:
        table_name = 'indexrecord'

class Inspect(BaseModel):
    code = CharField(null=True)
    create_date = TextField(null=True)
    flag = IntegerField(null=True)
    name = CharField(null=True)
    opt = CharField(null=True)
    type = TextField(null=True)
    value = FloatField(null=True)

    class Meta:
        table_name = 'inspect'

class Message(BaseModel):
    code = CharField(null=True)
    flag = IntegerField(null=True)
    message = CharField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'message'

class Sign(BaseModel):
    buy = IntegerField(null=True)
    code = CharField(null=True)
    concept = CharField(null=True)
    current = FloatField(null=True)
    high = FloatField(null=True)
    low = FloatField(null=True)
    prefbuy = FloatField(column_name='prefBuy', null=True)
    prefsell = FloatField(column_name='prefSell', null=True)
    sell = IntegerField(null=True)

    class Meta:
        table_name = 'sign'

class Stockaction(BaseModel):
    action = CharField(null=True)
    arrow = CharField(null=True)
    content = CharField(null=True)
    detail = CharField(null=True)
    dex = FloatField(null=True)
    ftime = TextField(null=True)
    gw = CharField(null=True)
    ltime = TextField(null=True)
    pref = CharField(null=True)
    pref1 = CharField(null=True)
    queue = CharField(null=True)
    strong = FloatField(null=True)
    time = TextField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'stockaction'

class Stockrecord(BaseModel):
    avg = FloatField(null=True)
    clmn = FloatField(null=True)
    close = FloatField(null=True)
    code = CharField(null=True)
    current = FloatField(null=True)
    date = DateField(null=True)
    high = FloatField(null=True)
    low = FloatField(null=True)
    money = FloatField(null=True)
    name = CharField(null=True)
    open = FloatField(null=True)
    time = IntegerField(null=True)

    class Meta:
        table_name = 'stockrecord'

class TestTable(BaseModel):
    age = IntegerField(null=True)
    name = CharField(primary_key=True)
    time = DateTimeField(null=True)

    class Meta:
        table_name = 'test_table'

class Wavedaily(BaseModel):
    ac = IntegerField(null=True)
    arrow = CharField(null=True)
    code = CharField(primary_key=True)
    dt = DateField(null=True)
    gw = TextField(null=True)

    class Meta:
        table_name = 'wavedaily'

class Waveindex(BaseModel):
    ac = IntegerField(null=True)
    arrow = CharField(null=True)
    code = CharField()
    dt = DateField()
    duration = IntegerField(null=True)
    gw = TextField(null=True)
    max = FloatField(null=True)
    min = FloatField(null=True)
    name = CharField(null=True)
    time = IntegerField(null=True)

    class Meta:
        table_name = 'waveindex'
        indexes = (
            (('code', 'dt'), True),
        )
        primary_key = CompositeKey('code', 'dt')

class Waverecord(BaseModel):
    ac = IntegerField(null=True)
    arrow = CharField(null=True)
    code = CharField(null=True)
    dt = DateField(null=True)
    gw = CharField(null=True)
    wv = CharField(null=True)

    class Meta:
        table_name = 'waverecord'
        primary_key = False

class Wavestock(BaseModel):
    ac = IntegerField(null=True)
    arrow = CharField(null=True)
    code = CharField()
    dt = DateField()
    duration = IntegerField(null=True)
    gw = TextField(null=True)
    max = FloatField(null=True)
    min = FloatField(null=True)
    name = CharField(null=True)
    time = IntegerField(null=True)

    class Meta:
        table_name = 'wavestock'
        indexes = (
            (('code', 'dt'), True),
        )
        primary_key = CompositeKey('code', 'dt')

class Weak(BaseModel):
    ascrate = FloatField(null=True)
    code = CharField(null=True)
    descrate = FloatField(null=True)
    equalrate = FloatField(null=True)
    name = CharField(null=True)
    time = TextField(null=True)

    class Meta:
        table_name = 'weak'

