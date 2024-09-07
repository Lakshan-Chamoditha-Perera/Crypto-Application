from com.crypto.repositories.user_repo import UserRepository


class UserService:
    @staticmethod
    def create_user(email, name, password):
        # Business logic (e.g., hashing password) goes here
        return UserRepository.create_user(email, name, password)

    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def list_users():
        return UserRepository.get_all_users()
