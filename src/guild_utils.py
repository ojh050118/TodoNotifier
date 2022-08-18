import discord


def to_objects(guilds: list):
    result = []
    for guild in guilds:
        result.append(discord.Object(id = guild.id))

    return result
