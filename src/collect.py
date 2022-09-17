"""
Запуск приложения.
"""
import logging

from collectors.collector import Collectors

if __name__ == "__main__":
    logging.info("Запуск обновления данных ...")
    # запуск обработки
    Collectors().collect()

    logging.info("Обновление завершено.")
