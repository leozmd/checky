from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(
    self,
    idUsuario,
    nomUsuario,
    appatUsuario,
    apmatUsuario,
    sexoUsuario,
    matUsuario,
    usuUsuario,
    passUsuario,
    idRol,
    idEstado
    ) -> None:
        self.idUsuario = idUsuario
        self.nomUsuario = nomUsuario
        self.appatUsuario = appatUsuario
        self.apmatUsuario = apmatUsuario
        self.sexoUsuario = sexoUsuario
        self.matUsuario = matUsuario
        self.usuUsuario = usuUsuario
        self.passUsuario = passUsuario
        self.idRol = idRol
        self.idEstado = idEstado

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    def get_id(self):
        try:
            return self.idUsuario # Rename 'id' to 'userid'
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')