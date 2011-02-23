class BusRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on bus models to 'mongo'"
        if model._meta.app_label == 'bus':
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on bus models to 'mongo'"
        if model._meta.app_label == 'bus':
            return 'mongo'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in bus is involved"
        if obj1._meta.app_label == 'bus' or obj2._meta.app_label == 'bus':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the bus app only appears on the 'mongo' db"
        if db == 'mongo':
            return model._meta.app_label == 'bus'
        elif model._meta.app_label == 'bus':
            return False
        return None
