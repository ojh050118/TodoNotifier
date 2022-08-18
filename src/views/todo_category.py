import discord

from todo_utils import todo_store
from modals.todo_reminder import ToDoReminder


class ToDoCategory(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = '작업', emoji = '🏠')
            ]

        super().__init__(placeholder = '목록', min_values = 1, max_values = 1,
                         options = options)

    async def callback(self, interaction: discord.Interaction):
        todo_name = list(todo_store.get_guild_user_todo(interaction).keys())[-1]
        todo_store.get_todo_info(interaction, todo_name)['category'] = self.values

        await interaction.response.send_modal(ToDoReminder())
