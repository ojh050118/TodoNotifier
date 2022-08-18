from ast import literal_eval

import discord
from discord import app_commands
from discord.ext import commands

import guild_utils
from modals.generate_todo import ToDoGenerator
from todo_utils import todo_store


class ToDo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.interaction = None

    @app_commands.command(name = 'add', description = '새로운 작업을 추가합니다.')
    async def add_todo(self, interaction: discord.Interaction):
        await interaction.response.send_modal(ToDoGenerator())

    @app_commands.command(name = 'todo', description = '자신의 할 것들을 봅니다.')
    async def todo(self, interaction: discord.Interaction):
        embed = discord.Embed(title = f':ballot_box_with_check: {interaction.user.name}님의 To Do',
                              color = discord.Colour.blue())

        if interaction.guild_id in todo_store.todo and interaction.user.id in todo_store.todo[interaction.guild_id]:
            user_todos = todo_store.todo[interaction.guild_id][interaction.user.id]
            for key in user_todos:
                todo = user_todos[key]
                embed.add_field(name = todo['name'], value = f'`메모`**:** {todo["memo"]}\n'
                                                             f'`URL`**:** [URL]({todo["url"]})\n'
                                                             f'`카테고리`**:** {todo["category"]}\n'
                                                             f'`미리 알림`**:** <t:{todo["remind_time_timestamp"]}:f>\n',
                                inline = False)
        else:
            embed.description = '**비어있음.**'

        embed.set_footer(text = interaction.user, icon_url = interaction.user.avatar)

        await interaction.response.send_message(embed = embed)

    @app_commands.command(name = 'import', description = '모든 To Do데이터를 포함하는 파일에 새로운 데이터를 덮어씌웁니다.')
    @app_commands.describe(data = 'dict(json)형식으로 구성된 텍스트')
    async def import_data(self, interaction: discord.Interaction, data: str):
        old_todo = todo_store.todo
        todo_store.todo = literal_eval(data)
        todo_store.save()

        embed = discord.Embed(title = ':arrow_heading_down: Import', description = '임포트 완료!',
                              color = discord.Colour.green())

        todo_store.logger.logger.info(f'To do data overwritten by user "{interaction.user}".\n'
                                      f'Old data: {old_todo}\n'
                                      f'New data: {todo_store.todo}')

        await interaction.response.send_message(embed = embed, ephemeral = True)

    @app_commands.command(name = 'export', description = '모든 To Do데이터를 내보냅니다.')
    async def export_data(self, interaction: discord.Interaction):
        embed = discord.Embed(title = ':arrow_heading_up: Export', description = '내보내기 완료!',
                              color = discord.Colour.green())
        embed.add_field(name = 'Data', value = f'```json\n{todo_store.todo}\n```')

        todo_store.logger.logger.info(f'To do data has been sent to user "{interaction.user}".\n'
                                      f'Exported data: {todo_store.todo}')

        await interaction.response.send_message(embed = embed, ephemeral = True)


async def setup(bot: commands.Bot):
    await bot.add_cog(ToDo(bot), guilds = guild_utils.to_objects(list(bot.guilds)))
