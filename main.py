class User():
    def __init__(self, ID, name):
        self.ID = f"{ID:04}"
        self.name = name
        self.access_level = "user"

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(f"{int(ID):04}", name)
        self.access_level = "admin"
        self.users_list = {}

    def add_user(self, ID, name):
        user_id = f"{int(ID):04}"
        if user_id in self.users_list:
            print(f"ID {user_id} уже занят")
        else:
            self.users_list[user_id] = name
            print(f"Пользователь {name} с ID {user_id} добавлен")

    def delete_user(self, ID):
        user_id = f"{int(ID):04}"
        if user_id in self.users_list:
            del self.users_list[user_id]
            print(f"Пользователь {int(ID):04} удален")
        else:
            print(f"Пользователь {user_id} не найден")

    def display_users(self):
        print("Список пользователей:")
        for user_id, name in self.users_list.items():
            print(f"{user_id}: {name}")

users_1b = Admin(1, "Валерий")
users_1b.add_user(1101, "Игорь")
users_1b.add_user(99, "Елисей")
users_1b.add_user(20, "Константин")
users_1b.add_user(20, "Виктор")
users_1b.display_users()
