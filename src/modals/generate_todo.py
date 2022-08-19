import discord

from todo_utils import todo_store
from views.todo_create_view import ToDoCreateView


class ToDoGenerator(discord.ui.Modal, title = 'To Do 추가'):
    def __init__(self, user_id: int = None):
        super().__init__()
        self.user_id = user_id

    name = discord.ui.TextInput(
            label = 'Todo',
            placeholder = '할 것 이름...',
            max_length = 100
            )

    memo = discord.ui.TextInput(
            label = '메모',
            style = discord.TextStyle.long,
            placeholder = '메모',
            required = False
            )

    url = discord.ui.TextInput(
            label = 'URL',
            placeholder = 'URL',
            required = False
            )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = ':ballot_box_with_check: To Do', description = f'To Do의 카테고리를 골라주세요.',
                              color = discord.Colour.blue())

        if self.user_id is None:
            self.user_id = interaction.user.id

        todo_info = { 'guild_id' : interaction.guild_id, 'user_id' : self.user_id,
                      'name' : self.name.value,
                      'memo' : self.memo.value,
                      'url' : self.url.value }

        exists = todo_store.exists(todo_info)

        if not exists:
            todo_store.add_todo(todo_info)

            await interaction.response.send_message(embed = embed, view = ToDoCreateView(self.user_id))
        else:
            embed.title = ':warning: To Do'
            embed.description = '같은 이름을 가진 To Do가 존재합니다.'
            embed.colour = discord.Colour.gold()

            await interaction.response.send_message(embed = embed)
