import datetime
import time

import discord

from todo_utils import todo_store, todo_scheduler


def parse_to_seconds(day: str, hour: str, minute: str):
    second = 0

    if day.isdigit():
        second += int(day) * 86400

    if hour.isdigit():
        second += int(hour) * 3600

    if minute.isdigit():
        second += int(minute) * 60

    return second


class ToDoReminder(discord.ui.Modal, title = '미리 알림'):
    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id

    day = discord.ui.TextInput(
            label='일',
            placeholder='지금으로 부터...',
            required = False
            )

    hour = discord.ui.TextInput(
            label = '시',
            placeholder = '지금으로 부터...',
            required = False,
            max_length = 2,
            )

    minute = discord.ui.TextInput(
            label = '분',
            placeholder = '지금으로 부터...',
            required = False,
            max_length = 2
            )

    async def on_submit(self, interaction: discord.Interaction):
        user_todo = todo_store.todo[interaction.guild_id][self.user_id]
        last_todo_name = list(user_todo.keys())[-1]
        last_todo = user_todo[last_todo_name]
        user = await todo_scheduler.get_user(self.user_id)

        time_until_remind = parse_to_seconds(self.day.value, self.hour.value, self.minute.value)
        remind_time = int(time.time()) + time_until_remind

        last_todo['time_until_remind'] = time_until_remind
        last_todo['remind_time_timestamp'] = remind_time

        todo_store.save()
        todo_scheduler.add(last_todo)

        embed = discord.Embed(title = f':white_check_mark: {user}에게 To Do 추가됨!', timestamp = datetime.datetime.now(),
                              color = discord.Colour.green())
        embed.add_field(name = last_todo['name'], value = f'`메모`**:** {last_todo["memo"]}\n'
                                                          f'`URL`**:** [URL]({last_todo["url"]})\n'
                                                          f'`카테고리`**:** {last_todo["category"]}\n'
                                                          f'`미리 알림`**:** <t:{last_todo["remind_time_timestamp"]}:f>')
        embed.set_footer(text = user, icon_url = user.avatar)

        await interaction.response.send_message(embed = embed)
