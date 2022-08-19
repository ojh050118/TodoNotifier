import discord.ui

from views.todo_category import ToDoCategory


class ToDoCreateView(discord.ui.View):
    def __init__(self, user_id: int):
        super().__init__()
        self.add_item(ToDoCategory(user_id))
