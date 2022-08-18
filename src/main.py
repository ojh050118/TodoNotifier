import discord

from debug import Logger
from todo_notifier import TodoNotifier

TOKEN = 'MTAwNTQ5NjQwMjcwNjcxNDY0NQ.GdK9-Y.GbGIPIlVbrdwrg1N1XcsXbV6ae1U7e_QiX7SOI'
APPLICATION_ID = 1005496402706714645

logger = Logger('discord')
bot = TodoNotifier(APPLICATION_ID, logger)


@bot.tree.error
async def on_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    embed = discord.Embed(title = ':no_entry: 오류!', description = '명령을 실행하는 도중 오류가 발생했습니다!',
                          color = discord.Colour.red())
    embed.add_field(name = 'Error description:', value = error)
    logger.logger.error(error)

    await interaction.response.send_message(embed = embed, ephemeral = True)

bot.run(TOKEN, log_handler = logger.handler, log_level = logger.log_level, log_formatter = logger.formatter)
