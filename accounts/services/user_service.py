from accounts.models.repository.user_repository import UserRepository


class UserService:
    """
    this class help to maintain all kind of user activity functions.
    """

    def __init__(self):
        """
        initializer of UserService class it call when
        we creates the UserService object
        """
        self._user_repo = UserRepository()

    def create_customer(self, request):
        """
        This server function help to create user in db.
        """
        user_object = self._user_repo.create_user(request)
        if user_object:
            self._user_repo.assign_user_group("customer", user_object)
        return user_object
