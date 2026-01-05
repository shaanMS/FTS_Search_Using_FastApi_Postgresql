from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BrowsingHistory(Base):
    __tablename__ = "browsing_history"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(TIMESTAMP)
    navigated_to_url = Column(Text)
    page_title = Column(Text)
    search_vector = Column(TSVECTOR)
