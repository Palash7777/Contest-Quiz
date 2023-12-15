class User:
    def __init__(self, name):
        self.name = name

    def update_name(self, name):
        self.name = name

user = User('palash')
user.update_name('jatin')
print(user.name)