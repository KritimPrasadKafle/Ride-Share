from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.models.base import Base
from app.models import *

from app.core.config import settings

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_url():
    # convert asyncpg URL → sync URL
    return settings.DATABASE_URL.replace("+asyncpg", "")


def run_migrations_online():
    config.set_main_option("sqlalchemy.url", get_url())

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()