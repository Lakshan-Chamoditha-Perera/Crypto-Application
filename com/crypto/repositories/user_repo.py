from com.crypto.models.models import User, db


class UserRepository:
    @staticmethod
    def create_user(email, name, password):
        new_user = User(email=email, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()
