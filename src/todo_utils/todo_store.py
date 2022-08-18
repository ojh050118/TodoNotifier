import os
import pickle

import discord

from debug import Logger

todo = {}
TODO_FILENAME = 'todo_data.bin'
logger = Logger('todo_store')


def add_todo(new_todo: dict):
    if not new_todo['guild_id'] in todo:
        todo[new_todo['guild_id']] = {}

    if not str(new_todo['user_id']) in todo[new_todo['guild_id']]:
        todo[new_todo['guild_id']][new_todo['user_id']] = {}

    todo[new_todo['guild_id']][new_todo['user_id']][new_todo['name']] = {
        'guild_id' : new_todo['guild_id'],
        'user_id' : new_todo['user_id'],
        'name' : new_todo['name'],
        'memo' : new_todo['memo'],
        'url' : new_todo['url'],
        'category' : None,
        'time_until_remind' : None,
        'remind_time_timestamp' : None
        }


def get_guild_user_todo(interaction: discord.Interaction) -> dict:
    return todo[interaction.guild_id][interaction.user.id]


def get_todo_info(interaction: discord.Interaction, name: str) -> dict:
    return todo[interaction.guild_id][interaction.user.id][name]


def exists(todo_info: dict) -> bool:
    if not todo_info['guild_id'] in todo:
        return False
    elif not todo_info['user_id'] in todo[todo_info['guild_id']]:
        return False
    elif not todo_info['name'] in todo[todo_info['guild_id']][todo_info['user_id']]:
        return False

    return True


def load():
    global todo

    get_directory('files')

    if not os.path.isfile(os.path.join('files', TODO_FILENAME)):
        logger.logger.warning(f'Could not find file "{TODO_FILENAME}". Create new...')
        save()

    with open(os.path.join('files', TODO_FILENAME), 'rb') as file:
        todo = pickle.load(file)
        logger.logger.info('Loaded todo_store data!')


def save():
    get_directory('files')

    with open(os.path.join('files', TODO_FILENAME), 'wb') as file:
        pickle.dump(todo, file)


def get_directory(path: str):
    if not os.path.isdir(path):
        os.mkdir(path)
