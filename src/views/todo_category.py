import discord

from modals.todo_reminder import ToDoReminder
from todo_utils import todo_store


class ToDoCategory(discord.ui.Select):
    def __init__(self, user_id: int):
        self.user_id = user_id
        options = [
            discord.SelectOption(label = '작업', emoji = '🏠')
            ]

        super().__init__(placeholder = '목록', min_values = 1, max_values = 1,
                         options = options)

    async def callback(self, interaction: discord.Interaction):
        user_todo = todo_store.todo[interaction.guild_id][self.user_id]
        todo_name = list(user_todo.keys())[-1]
        user_todo[todo_name]['category'] = self.values

        await interaction.response.send_modal(ToDoReminder(self.user_id))
