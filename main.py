# -*- coding: utf-8 -*-
import asyncio
import discord
import os
import sqlite3
client = discord.Client()
conn = sqlite3.connect('data.db')
c = conn.cursor()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    uname = message.author.id
    con = message.content
    sql = 'insert into data (userid, message) values (?,?)'
    namelist = (uname, con)
    c.execute(sql, namelist)
    conn.commit()

if __name__ == "__main__":
    client.run(os.environ['LOGGER_TOKEN'])