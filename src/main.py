import os
from ast import literal_eval

import discord

from debug import Logger
from todo_notifier import TodoNotifier

logger = Logger('discord')

application_id = str(os.environ.get('todonotifier_application_id'))
token = os.environ.get('todonotifier_token')

if not application_id or not token:
    logger.logger.warning('The token or application ID does not exist in the environment variable. ' +
                          'Loading from config.json...')

    with open('files/config.json', 'r') as f:
        config = literal_eval(f.read())
        application_id = str(config['application_id'])
        token = config['token']

if application_id.isdigit():
    application_id = int(application_id)
else:
    logger.logger.error('Application ID cannot contain characters!')


bot = TodoNotifier(application_id, logger)


@bot.tree.error
async def on_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    embed = discord.Embed(title = ':no_entry: 오류!', description = '명령을 실행하는 도중 오류가 발생했습니다!',
                          color = discord.Colour.red())
    embed.add_field(name = 'Error description:', value = error)
    logger.logger.error(error)

    await interaction.response.send_message(embed = embed, ephemeral = True)

bot.run(token, log_handler = logger.handler, log_level = logger.log_level, log_formatter = logger.formatter)
