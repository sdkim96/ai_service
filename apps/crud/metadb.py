from typing import (Any, Dict, Iterator, List, Optional, Literal, Sequence, Tuple, Union,)
from apps.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from apps.schema import Message

def truncate_word(content: Any, *, length: int, suffix: str = "...") -> str:
    if not isinstance(content, str) or length <= 0:
        return content
 
    if len(content) <= length:
        return content
 
    return content[: length - len(suffix)].rsplit(" ", 1)[0] + suffix


class Metadb():

    _db = None

    @property
    def db(self):
        if self.__class__._db is None:
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
            self.__class__._db = sessionmaker(bind=engine)()
        return self.__class__._db
    

    def run(
        self,
        command: str,
        fetch: Literal["all", "one"] = "all",
        include_columns: bool = False,
    ) -> str:
        """Execute a SQL command and return a string representing the results.
 
        If the statement returns rows, a string of the results is returned.
        If the statement returns no rows, an empty string is returned.
        """
        result = self.db._execute(command, fetch)
 
        res = [
            {
                # column: truncate_word(value, length=self.__class__.db._max_string_length)
                column: truncate_word(value, length=6000)
                for column, value in r.items()
            }
            for r in result
        ]
 
        if not include_columns:
            res = [tuple(row.values()) for row in res]
 
        return res
    

    

    

    def insert_messages_list(self, messages: Message) -> str:
        sql="""
            INSERT INTO messages (thread_id, status, incomplete_details, completed_at, role, content, assistant_id, run_id, attachments)

            
            """
        
        return ""

