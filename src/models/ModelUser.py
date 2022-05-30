from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = "call PObtenerDatosUsuario('{}')".format(user.usuUsuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], 
                            User.check_password(row[7], user.passUsuario), row[8], row[9])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getById(self, db, idUsuario):
        try:
            cursor = db.connection.cursor()
            sql = "call PDatosUsuario({});".format(idUsuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def listAll(self, db):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM MUsuario"
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception as ex:
            raise Exception(ex)