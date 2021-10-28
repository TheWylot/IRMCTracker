from modules.config import Config
from modules.tracker import get_servers

from modules.utils import *

from discord.ext import tasks
from discord.ext.commands import Cog


class StatsTask(Cog):
    """Updating tracker stats channels task
    """

    def __init__(self, bot):
        self.bot = bot

        # Running stats updating task
        self.stats_task.start()

    @tasks.loop(minutes=5)
    async def stats_task(self):
        await self.bot.wait_until_ready()

        await self.update_members_count()
        await self.update_servers_count()

    async def update_members_count(self):
        channel = self.bot.get_channel(Config.Channels.MEMBERS)
        guild = self.bot.get_guild(Config.GUILD_ID)
        await channel.edit(
            name=f"👥・ Members「{guild.member_count}」"
        )

    async def update_servers_count(self):
        channel = self.bot.get_channel(Config.Channels.SERVERS)
        servers_count = str(len(get_servers()))
        await channel.edit(
            name=f"🌐・ Servers「{servers_count}」"
        )

    
def setup(client):
    client.add_cog(StatsTask(client))
