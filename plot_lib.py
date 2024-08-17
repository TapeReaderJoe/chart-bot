"""Module providing chart-plotting functions"""

import pandas as pd
import numpy as np
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from zigzag.core import peak_valley_pivots
import utils as ut
from scraper import scrape_finviz


def get_ibd_config() -> dict:
    """returns ibd-like config"""
    return {
        "mpl_cfg": {
            "base_mpl_style": "fast",
            "marketcolors": {
                "candle": {"up": "#2A3FE5", "down": "#DB39AD"},
                "edge": {"up": "#00ff00", "down": "#ff0000"},
                "wick": {"up": "#00ff00", "down": "#ff0000"},
                "ohlc": {"up": "#2A3FE5", "down": "#DB39AD"},
                "volume": {"up": "#2A3FE5", "down": "#DB39AD"},
                "vcedge": {"up": "#2A3FE5", "down": "#DB39AD"},
                "vcdopcod": False,
                "alpha": 1,
            },
            "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
            "facecolor": "#ffffff",
            "figcolor": "#ffffff",
            "gridcolor": "#2c2e31",
            "gridstyle": "--",
            "y_on_right": True,
            "rc": {
                "axes.grid": False,
                "axes.grid.axis": "y",
                "axes.edgecolor": "#ffffff",
                "axes.titlecolor": "red",
                "figure.facecolor": "#161a1e",
                "figure.titlesize": "x-large",
                "figure.titleweight": "semibold",
            },
            "base_mpf_style": "ibd",
        },
        "price_addplots": [
            ("sma10", "red", 1.2),
            ("sma20", "blue", 1.2),
            ("sma50", "green", 1.2),
        ],
        "volume_addplots": [("volume_sma50", "black", 1.2)],
        "weekly_price_addplots": [("sma10", "red", 1.2), ("sma30", "blue", 1.2)],
        "weekly_volume_addplots": [("volume_sma10", "black", 1.2)],
        "weekly": False,
        "foreground": "#000000",
        "background": "#ffffff",
        "plot_type": "ohlc",
        "finviz": "#000000",
        "font": "Arial",
    }


def get_qullamaggie_config() -> dict:
    """returns qullamaggie-like config"""
    return {
        "mpl_cfg": {
            "base_mpl_style": "dark_background",
            "marketcolors": {
                "candle": {"up": "#00ff00", "down": "#ff0000"},
                "edge": {"up": "#00ff00", "down": "#ff0000"},
                "wick": {"up": "#00ff00", "down": "#ff0000"},
                "ohlc": {"up": "green", "down": "red"},
                "volume": {"up": "#00ff00", "down": "#ff0000"},
                "vcedge": {"up": "#00ff00", "down": "#ff0000"},
                "vcdopcod": False,
                "alpha": 1,
            },
            "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
            "facecolor": "#000000",
            "figcolor": "#000000",
            "gridcolor": "#2c2e31",
            "gridstyle": "--",
            "y_on_right": True,
            "rc": {
                "axes.grid": False,
                "axes.grid.axis": "y",
                "axes.edgecolor": "#000000",
                "axes.titlecolor": "red",
                "figure.facecolor": "#161a1e",
                "figure.titlesize": "x-large",
                "figure.titleweight": "semibold",
            },
            "base_mpf_style": "binance-dark",
        },
        "price_addplots": [
            ("ema9", "red", 1.2),
            ("ema21", "yellow", 1.2),
            ("sma50", "green", 1.2),
        ],
        "volume_addplots": [("volume_sma50", "white", 1.2)],
        "weekly_price_addplots": [("sma10", "red", 1.2), ("sma30", "yellow", 1.2)],
        "weekly_volume_addplots": [("volume_sma10", "white", 1.2)],
        "weekly": False,
        "foreground": "#ffffff",
        "background": "#000000",
        "plot_type": "candle",
        "finviz": "#ffffff",
        "font": "DejaVu Sans",
    }


def get_light_config() -> dict:
    """returns light-themed config"""
    return {
        "mpl_cfg": {
            "base_mpl_style": "dark_background",
            "marketcolors": {
                "candle": {"up": "#ffffff", "down": "#000000"},
                "edge": {"up": "#000000", "down": "#000000"},
                "wick": {"up": "#000000", "down": "#000000"},
                "ohlc": {"up": "green", "down": "red"},
                "volume": {"up": "#ffffff", "down": "#000000"},
                "vcedge": {"up": "#808080", "down": "#000000"},
                "vcdopcod": False,
                "alpha": 1,
            },
            "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
            "facecolor": "#ffffff",
            "figcolor": "#ffffff",
            "gridcolor": "#2c2e31",
            "gridstyle": "--",
            "y_on_right": True,
            "rc": {
                "axes.grid": False,
                "axes.grid.axis": "y",
                "axes.edgecolor": "#ffffff",
                "axes.titlecolor": "red",
                "figure.facecolor": "#161a1e",
                "figure.titlesize": "x-large",
                "figure.titleweight": "semibold",
            },
            "base_mpf_style": "binance-dark",
        },
        "price_addplots": [
            ("sma10", "red", 1.2),
            ("sma20", "blue", 1.2),
            ("sma50", "green", 1.2),
        ],
        "volume_addplots": [("volume_sma50", "black", 1.2)],
        "weekly_price_addplots": [("sma10", "red", 1.2), ("sma30", "blue", 1.2)],
        "weekly_volume_addplots": [("volume_sma10", "black", 1.2)],
        "weekly": False,
        "foreground": "#000000",
        "background": "#ffffff",
        "plot_type": "candle",
        "finviz": "#000000",
        "font": "Arial",
    }


def get_stockbee_config() -> dict:
    """returns stockbee-like config"""
    return {
        "mpl_cfg": {
            "base_mpl_style": "dark_background",
            "marketcolors": {
                "candle": {"up": "#ffffff", "down": "#000000"},
                "edge": {"up": "#000000", "down": "#000000"},
                "wick": {"up": "#000000", "down": "#000000"},
                "ohlc": {"up": "green", "down": "red"},
                "volume": {"up": "#ffffff", "down": "#000000"},
                "vcedge": {"up": "#808080", "down": "#000000"},
                "vcdopcod": False,
                "alpha": 1,
            },
            "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
            "facecolor": "#ffffff",
            "figcolor": "#ffffff",
            "gridcolor": "#2c2e31",
            "gridstyle": "--",
            "y_on_right": True,
            "rc": {
                "axes.grid": False,
                "axes.grid.axis": "y",
                "axes.edgecolor": "#ffffff",
                "axes.titlecolor": "red",
                "figure.facecolor": "#161a1e",
                "figure.titlesize": "x-large",
                "figure.titleweight": "semibold",
            },
            "base_mpf_style": "binance-dark",
        },
        "weekly": False,
        "foreground": "#000000",
        "background": "#ffffff",
        "plot_type": "candle",
        "finviz": "#000000",
        "font": "Arial",
    }


def _create_chart_with_config(
    df: pd.DataFrame, config: dict, img_path: str = "img.png"
):
    thres = 0.1
    df["max"] = df.high[peak_valley_pivots(np.array(df.high), thres, -thres) == 1]
    df["min"] = df.low[peak_valley_pivots(np.array(df.low), thres, -thres) == -1]

    egrid = (21, 29)
    fig = mpf.figure(style=config["mpl_cfg"], figsize=(16, 9))
    price_ax = plt.subplot2grid(egrid, (0, 0), colspan=29, rowspan=17)
    volume_ax = plt.subplot2grid(egrid, (17, 0), colspan=29, rowspan=4, sharex=price_ax)
    volume_ax.tick_params(
        which="both",
        labelbottom=True,
        labeltop=False,
        labelright=False,
        bottom=True,
        top=False,
        right=False,
        labelleft=False,
        left=False,
    )
    price_ax.tick_params(
        which="both",
        labelbottom=False,
        labeltop=False,
        labelright=False,
        bottom=False,
        top=False,
        right=False,
    )
    kwargs = {
        "horizontalalignment": "center",
        "color": config["foreground"],
        "fontsize": 8,
        "backgroundcolor": config["background"],
        "bbox": {
            "boxstyle": "square",
            "fc": config["background"],
            "ec": "none",
            "pad": 0,
            "alpha": 0,
        },
    }
    window_volume = 10
    for i in range(window_volume, len(df)):
        df_slice = df[i - window_volume : i + window_volume].copy()
        if df["rvol"].iloc[i] > 1.5 and df_slice["rvol"].max() <= df["rvol"].iloc[i]:
            volume_ax.text(
                i + 1,
                df["volume"].iloc[i] * 1.1,
                str(int(df["rvol"].iloc[i] * 100))
                + "%\n"
                + str(np.round(df["volume"].iloc[i] / 1e6, 1))
                + "M",
                **kwargs,
                verticalalignment="bottom",
            )

    stock_name = df["ticker"].values[-1]
    finviz = scrape_finviz(stock_name)
    addplots = []
    if not config.get("weekly", False):
        for ap in config.get("price_addplots", []):
            addplots.append(
                mpf.make_addplot(df[ap[0]], ax=price_ax, color=ap[1], width=ap[2])
            )
        for ap in config.get("volume_addplots", []):
            addplots.append(
                mpf.make_addplot(df[ap[0]], ax=volume_ax, color=ap[1], width=ap[2])
            )
    else:
        for ap in config.get("weekly_price_addplots", []):
            addplots.append(
                mpf.make_addplot(df[ap[0]], ax=price_ax, color=ap[1], width=ap[2])
            )
        for ap in config.get("weekly_volume_addplots", []):
            addplots.append(
                mpf.make_addplot(df[ap[0]], ax=volume_ax, color=ap[1], width=ap[2])
            )

    mpf.plot(
        df[["open", "high", "low", "close", "volume"]],
        type=config.get("plot_type", "candle"),
        ax=price_ax,
        volume=volume_ax,
        addplot=addplots,
        xrotation=0,
        tight_layout=False,
        datetime_format="%Y-%m-%d",
        scale_width_adjustment={"volume": 0.7},
        update_width_config={"ohlc_ticksize": 0.5, "ohlc_linewidth": 1.5},
    )
    ticker_watermark = (
        f'{stock_name}{", 1W" if config.get("weekly", False) else ", 1D"}'
    )
    sector = f"{df['sector'].values[-1]}" if "sector" in df.columns else ""
    props = {"boxstyle": "square", "facecolor": "none", "alpha": 0, "edgecolor": "none"}
    font = config.get("font", "Arial")
    labelfont = {
        "fontname": font,
        "fontsize": 40,
        "color": config["foreground"],
        "alpha": 0.20,
    }
    subfont = {
        "fontname": font,
        "fontsize": 20,
        "color": config["foreground"],
        "alpha": 0.20,
    }
    fvfont = {
        "fontname": font,
        "fontsize": 10,
        "alpha": 0.5,
        "weight": "bold",
        "horizontalalignment": "center",
        "color": config["finviz"],
    }
    price_ax.text(
        0.5,
        0.75,
        ticker_watermark,
        transform=price_ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
        bbox=props,
        **labelfont,
    )
    price_ax.text(
        0.5,
        0.68,
        df["short_name"].values[-1],
        transform=price_ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
        bbox=props,
        **subfont,
    )
    price_ax.text(
        0.5,
        0.61,
        sector,
        transform=price_ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
        bbox=props,
        **subfont,
    )
    if finviz:
        sh_fl = (
            str(round(finviz["shares_float"] / 1000, 2)) + "B"
            if finviz["shares_float"] > 1000
            else str(int(finviz["shares_float"])) + "M"
        )
        price_ax.text(
            0.5,
            0.95,
            f"Float: {sh_fl}    PE {round(finviz['pe'],1)}    PS {round(finviz['ps'],1)}    PB {round(finviz['pb'],1)}    Inst.Own {round(finviz['inst_own']*100,1)}%    Ins.Own {round(finviz['insider_own']*100,1)}%    ADR {round((df['high']/df['low']-1).tail(20).mean()*100,1)}%    Short Float {round(finviz['short_float']*100,2)}%",
            transform=price_ax.transAxes,
            bbox=props,
            **fvfont,
        )
    volume_ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, _: str(np.round(x / 1e6, 1)) + "M")
    )
    price_ax.grid(False)
    volume_ax.grid(False)
    if config.get("log", False):
        price_ax.set_yscale("log")
    price_ax.xaxis.set_major_locator(mticker.AutoLocator())
    price_ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    price_ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())

    volume_ax.set_ylabel("")
    volume_ax.yaxis.set_label_position("right")
    price_ax.set_ylabel("")

    price_ax.margins(x=0.02, y=0.1)
    price_ax.set_ylim(top=0.4 * (df["high"].max() - df["low"].min()) + df["high"].max())
    fig.subplots_adjust(hspace=0, wspace=0)
    plt.savefig(img_path, bbox_inches="tight")
    plt.close("all")


def create_chart_image(ticker, weekly, config_type, offset):
    """generates chart config and creates chart image for provided ticker"""
    if config_type.lower() == "qullamaggie":
        config = get_qullamaggie_config()
    elif config_type.lower() == "ibd":
        config = get_ibd_config()
    elif config_type.lower() == "light":
        config = get_light_config()
    elif config_type.lower() == "stockbee":
        config = get_stockbee_config()
    else:
        config = get_qullamaggie_config()
    stock_data = ut.get_stock_data(ticker=ticker, weekly=weekly, offset=offset)
    _create_chart_with_config(stock_data, config)


if __name__ == "__main__":
    create_chart_image("pltr", False, "qullamaggie", offset=9)
