import discord
from todo_utils import todo_store, todo_scheduler
import time
import datetime


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
    day = discord.ui.TextInput(
            label='일',
            placeholder='숫자 입력...',
            required = False
            )

    hour = discord.ui.TextInput(
            label = '시',
            placeholder = '숫자 입력...',
            required = False,
            max_length = 2,
            )

    minute = discord.ui.TextInput(
            label = '분',
            placeholder = '숫자 입력...',
            required = False,
            max_length = 2
            )

    async def on_submit(self, interaction: discord.Interaction):
        last_todo_name = list(todo_store.get_guild_user_todo(interaction).keys())[-1]
        last_todo = todo_store.get_todo_info(interaction, last_todo_name)

        time_until_remind = parse_to_seconds(self.day.value, self.hour.value, self.minute.value)
        remind_time = int(time.time()) + time_until_remind

        last_todo['time_until_remind'] = time_until_remind
        last_todo['remind_time_timestamp'] = remind_time

        todo_store.save()
        todo_scheduler.add(last_todo)

        embed = discord.Embed(title = f':white_check_mark: To Do 추가됨!', timestamp = datetime.datetime.now(),
                              color = discord.Colour.green())
        embed.add_field(name = last_todo['name'], value = f'`메모`**:** {last_todo["memo"]}\n'
                                                          f'`URL`**:** [URL]({last_todo["url"]})\n'
                                                          f'`카테고리`**:** {last_todo["category"]}\n'
                                                          f'`미리 알림`**:** <t:{last_todo["remind_time_timestamp"]}:f>')
        embed.set_footer(text = interaction.user, icon_url = interaction.user.avatar)

        await interaction.response.send_message(embed = embed)
