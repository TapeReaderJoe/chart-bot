# ChartBot

Simple chart-bot for discord that listens to the command `!chart` or `!wchart`.

## Installation

First off you need to configure a bot to get a token, try this [guide](https://discordpy.readthedocs.io/en/stable/discord.html).
Add your bot-token to `chart_bot.py:45`.

Install the requirements for the code.

```bash
pip3 install -r requirements.txt
```

Start the bot by running `chart_bot.py`.

And if everything is done correctly the bot should appear in your Discord server and starts listenting to the command `!chart`
or `!wchart` for weekly charts.

The CLI:
`!chart <ticker> <style='defined_styles'> <offset=int>`

`style:` provide one of the defined styles {'qullamaggie', 'ibd', 'stockbee', 'light'}, default value is 'qullamaggie'.

`offset:` the number of months history of stock data, default = 9 for daily and 40 for weekly.

## Examples

`!chart nvda`
![qullamaggie](./chart_examples/qullamaggie.png)

`!chart nvda style=ibd`
![ibd](./chart_examples/ibd.png)

`!chart nvda style=stockbee`
![stockbee](./chart_examples/stockbee.png)

`!chart nvda style=light`
![light](./chart_examples/light.png)
