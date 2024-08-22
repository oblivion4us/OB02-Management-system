class User:
    def __init__(self, ID, name):
        self.__ID = f"{int(ID):04}"
        self.__name = name
        self.__access_level = "user"

    def get_user_ID(self):
        return self.__ID

    def get_user_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_user_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.access_level = "admin"
        self.users_list = {}

    def add_user(self, user):
        user_id = user.get_user_ID()
        user_name = user.get_user_name()
        if user_id in self.users_list:
            print(f"ID {user_id} уже занят")
        else:
            self.users_list[user_id] = user_name
            print(f"Пользователь {user_name} с ID {user_id} добавлен")

    def remove_user(self, ID):
        user_id = f"{int(ID):04}"
        if user_id in self.users_list:
            del self.users_list[user_id]
            print(f"Пользователь {user_id} удален")
        else:
            print(f"Пользователь {user_id} не найден")

    def display_users(self):
        print("Список пользователей:")
        for user_id, name in self.users_list.items():
            print(f"{user_id}: {name}")

admin = Admin(1, "Константин")
user1 = User(11, "Андрей")
user2 = User(12, "Валерий")
admin.add_user(user1)
admin.add_user(user2)
user3 = User(12, "Анатолий")
user4 = User(101, "Георгий")
admin.add_user(user3)
admin.add_user(user4)
admin.display_users()
admin.remove_user(101)
admin.display_users()

