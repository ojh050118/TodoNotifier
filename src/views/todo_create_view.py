import discord.ui

from views.todo_category import ToDoCategory


class ToDoCreateView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ToDoCategory())
