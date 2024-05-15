from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL
from contextlib import contextmanager
from apps.config import get_settings
from typing import Literal

from apps.schema import Assistant, Message

# Helper function to manage session lifecycle
@contextmanager
def session_scope():
    conf = get_settings()
    url = URL.create(
        drivername="mysql+mysqlconnector",
        username=conf.mysql_user,
        password=conf.mysql_password,
        host=conf.mysql_host,
        port=conf.mysql_port,
        database=conf.mysql_db,
    )
    engine = create_engine(url, pool_recycle=360, pool_pre_ping=True, pool_size=3, max_overflow=5)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class Metadb:
    def run(self, command: str, parameters: dict = None, fetch: Literal["all", "one"] = "all"):
        with session_scope() as session:
            result = session.execute(text(command), parameters)
            if fetch == "all":
                rows = result.fetchall()
            elif fetch == "one":
                rows = result.fetchone()
            return rows
        

    def insert_assistant(self, assistant):
        sql = """
            INSERT INTO assistant (assistant_id, created_at, name, model, instructions, user_id)
            VALUES (:id, :created_at, :name, :model, :instructions, :user_id)
        """
        parameters = {
            "id": assistant.id,
            "created_at": assistant.created_at,
            "name": assistant.name,
            "model": assistant.model,
            "instructions": assistant.instructions,
            "user_id": "김성동"  # Assuming static user ID for the example
        }
        self.run(sql, parameters)

    def insert_message_list(self, messages):
        sql = """
            INSERT INTO message (message_id, created_at, thread_id, role, content, assistant_id, run_id, user_id)
            VALUES (:id, :created_at, :thread_id, :role, :content, :assistant_id, :run_id, :user_id)
        """
        parameters = {
            "id": messages.id,
            "created_at": messages.created_at,
            "thread_id": messages.thread_id,
            "role": messages.role,
            "content": messages.content.text[0].value,
            "assistant_id": messages.assistant_id,
            "run_id": messages.run_id,
            "user_id": "김성동"  # Assuming static user ID for the example
        }
        self.run(sql, parameters)
