import asyncio
import time

import discord
from discord.ext import commands

from debug import Logger
from todo_utils import todo_store

remind_todo_info = []
bot: commands.Bot
logger = Logger('todo_scheduler')


def update_remind_todo():
    current_time = int(time.time())

    for guild in todo_store.todo.keys():
        for user in todo_store.todo[guild].keys():
            for todo in todo_store.todo[guild][user].keys():
                todo_info = todo_store.todo[guild][user][todo]

                if todo_info['remind_time_timestamp'] > current_time:
                    logger.logger.info(f'Reminder found valid To Do \"{todo_info["name"]}\". Updating...')
                    add(todo_info)


def add(todo_info: dict):
    current_time = int(time.time())
    delay = todo_info['remind_time_timestamp'] - current_time

    remind_todo_info.append(todo_info)
    asyncio.create_task(send_delayed_dm(delay, todo_info))
    logger.logger.info(f'Registered a new task in the scheduler. {delay} seconds left to run.')


async def send_delayed_dm(delay: int, todo_info: dict):
    await asyncio.sleep(delay)
    await send_dm(todo_info)
    remind_todo_info.remove(todo_info)


async def send_dm(todo_info: dict):
    if bot is None:
        logger.logger.error('"todo_scheduler.bot" is not assigned. Cancel sending a DM message.')
        return

    user = await bot.fetch_user(todo_info['user_id'])
    dm_channel = await bot.create_dm(user)

    embed = discord.Embed(title = ':timer: 미리 알림', description = f'**{todo_info["name"]}**',
                          color = discord.Colour.blue())
    embed.add_field(name = '메모', value = todo_info['memo'] if todo_info['memo'] else '비어있음.')
    embed.add_field(name = 'URL', value = f'[URL]({todo_info["url"]})' if todo_info['url'] else '비어있음.')
    embed.add_field(name = '카테고리', value = todo_info['category'], inline = False)
    embed.add_field(name = '미리 알림', value = f'<t:{todo_info["remind_time_timestamp"]}:f>')
    embed.set_footer(text = user, icon_url = user.avatar)

    await dm_channel.send(embed = embed)
    logger.logger.info(f'Successfully sent a DM to user "{user}"!')


async def get_user(user_id: int) -> discord.User:
    return await bot.fetch_user(user_id)
