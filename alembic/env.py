from __future__ import with_statement
import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context

# Зчитування конфігурації з файлу alembic.ini
config = context.config

# Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Налаштування метаданих для міграцій
target_metadata = None

# Якщо у вас є моделі, імплементуйте їх тут:
# from myapp.models import Base
# target_metadata = Base.metadata

def run_migrations_online():
    # Отримання підключення до бази даних за допомогою налаштувань з alembic.ini
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    # Запуск міграцій
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    # Міграції в офлайн режимі (не використовується в нашому випадку)
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

# Основна функція для запуску міграцій
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
