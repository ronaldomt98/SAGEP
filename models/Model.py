import persistent
import transaction

from .Mizodb import MiZODB


class Model(persistent.Persistent):
    # getAll
    @staticmethod
    def get_all(self):
        print("dentro del getAll!")
        db = MiZODB('sagep-data.fs')
        dbroot = db.root
        recursos = []
        print("Clave: ", self.getClave(self))
        for i in dbroot[self.getClave(self)]:
            recursos.append(i.copy())
            print("Dato existe")
        db.close()
        return recursos

    # createObject in DB
    def create(self):
        print("Clave: ", self.getClave())
        db = MiZODB('sagep-data.fs')
        dbroot = db.root
        if not self.getClave() in dbroot.keys():
            print("Creo el slot")
            recursos = [self]
            db.root[self.getClave()] = recursos
            transaction.commit()
        else:
            print("Intenta guardar los datos")
            recursos = dbroot[self.getClave()]
            print("Clave: ", self.getClave())
            idx = len(recursos)
            recursos.append(self)
            db.root[self.getClave()] = recursos
            print("Se guardaron los datos!")
            transaction.commit()
        db.close()
        return idx

    # getOne
    @staticmethod
    def get_one(self):
        db = MiZODB('sagep-data.fs')
        dbroot = db.root
        recursos = []
        for i in dbroot[self.getClave(self)]:
            recursos.append(i.copy())
            break
        db.close()
        return recursos

    def delete(self):
        pass
