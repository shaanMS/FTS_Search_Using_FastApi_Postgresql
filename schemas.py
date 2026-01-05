from pydantic import BaseModel

class HistoryItem(BaseModel):
    page_title: str
    navigated_to_url: str

    class Config:
        orm_mode = True
