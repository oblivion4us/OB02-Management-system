class User():
    def __init__(self, ID, name, access_level="user"):
        self.ID = ID
        self.name = name
        self.access_level = access_level

class Admin(User):
    def __init__(self, ID, name, access_level="admin"):
        super().__init__(ID, name)
        self.access_level = access_level
        self.user_list = {}

    def add_user(self, ID, name):
        self.users_list[ID] = name

    def delete_user(self, ID):
        if ID in self.user_list:
            del.self.user_list[ID]
        else:
            print(f"Пользователь {ID} не найден")

    def display_users(self):
        print(f"Список пользователей:\n {self.user_list}")

users_1b = Admin(1, "Админ_Валерий")
users_1b.add_user(10, "Пользователь_Игорь")
users_1b.display_users()

