from discord.flags import Intents
import discord
import plot_lib as pl


class ChartBot(discord.Client):
    """ChartBot class"""

    def __init__(self, token) -> None:
        _intents = Intents.default()
        _intents.message_content = True
        super().__init__(intents=_intents)
        self._token = token
        super().run(self._token)

    async def on_message(self, message):
        """Message event"""
        if message.author == self.user:
            return
        msg = message.content.lower()
        split_msg = msg.split(" ")
        try:
            action = split_msg[0]
            if action in ("!chart", "!wchart"):
                ticker = split_msg[1]
                kwargs = {}
                if len(split_msg) > 2:
                    for arg in split_msg[1:]:
                        if "=" in arg:
                            key, value = arg.split("=")
                            kwargs[key] = int(value) if value.isdecimal() else value
                pl.create_chart_image(
                    ticker,
                    "!wchart" in action,
                    kwargs.get("style", "qullamaggie"),
                    kwargs.get("offset", 9 if action == "!chart" else 40),
                )
                await message.channel.send(file=discord.File("img.png"))

        except Exception as e:
            await message.channel.send(str(e))


if __name__ == "__main__":
    YOUR_DISCORD_TOKEN = "TOKEN_FROM_DISCORD_WEBSITE"
    chart_bot = ChartBot(YOUR_DISCORD_TOKEN)
