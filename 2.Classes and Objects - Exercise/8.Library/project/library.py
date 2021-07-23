class Library:
    def __init__(self):
        self.user_records = []  # to store users objects
        self.books_available = {}  # Key author : available
        self.rented_books = {}  # ({usernames: {book names: days left}}).

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
            for user_name, data in self.rented_books.items():
                if user_name == user:
                    del self.rented_books[user_name]
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        filtered_users = [u for u in self.user_records if u.user_id == user_id]
        if filtered_users:
            user = filtered_users[0]

            if not user.username == new_username:
                old_username = user.username
                user.username = new_username

                if old_username in self.rented_books:
                    old_books_from_user = self.rented_books[old_username]
                    del self.rented_books[old_username]
                    self.rented_books[user.username] = old_books_from_user

                return f'Username successfully changed to: {new_username}' \
                       f' for userid: {user_id}'

            else:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"

        else:
            return f"There is no user with id = {user_id}!"