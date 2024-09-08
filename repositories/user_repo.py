from models.models import User

class UserRepository:
    @staticmethod
    def create_user(email, name, password):
        user = User(email=email, name=name, password=password)
        user.save()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.find_by_id(user_id)

    @staticmethod
    def get_all_users():
        return User.find_all()
