"""
Запуск приложения.
"""

import asyncclick as click

from reader import Reader
from renderer import Renderer

# import tabulate


# from tabulate import tabulate


@click.command()
@click.option(
    "--location",
    "-l",
    "location",
    type=str,
    help="Страна и/или город",
    prompt="Страна и/или город",
)
async def process_input(location: str) -> None:
    """
    Поиск и вывод информации о стране, погоде и курсах валют.

    :param str location: Страна и/или город
    """

    location_info = await Reader().find(location)
    if location_info:
        lines = await Renderer(location_info).render()

        for line in lines:
            click.secho("| {:20} | {:100} ".format(*line), fg="green")
    else:
        click.secho("Информация отсутствует.", fg="yellow")


if __name__ == "__main__":
    # запуск обработки входного файла
    # pylint: disable=E1120
    process_input(_anyio_backend="asyncio")
