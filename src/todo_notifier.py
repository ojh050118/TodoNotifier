import os

import discord
from discord.ext import commands

import guild_utils
from todo_utils import todo_store, todo_scheduler
from debug import Logger


class TodoNotifier(commands.Bot):
    def __init__(self, application_id: int, logger: Logger):
        super().__init__(
                command_prefix = '!',
                intents = discord.Intents.default(),
                application_id = application_id
                )

        self.logger = logger
        self.initial_cogs = []
        for file_name in os.listdir('src/cogs'):
            if file_name.endswith('.py'):
                self.initial_cogs.append(f'cogs.{os.path.splitext(file_name)[0]}')

        todo_store.load()

    async def setup_hook(self):
        for initial_cog in self.initial_cogs:
            await self.load_extension(initial_cog)

    async def on_ready(self):
        for guild in guild_utils.to_objects(list(self.guilds)):
            self.tree.copy_global_to(guild = guild)
            await self.tree.sync(guild = guild)

        todo_scheduler.bot = self
        todo_scheduler.update_remind_todo()

        self.logger.logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
