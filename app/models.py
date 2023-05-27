from .database import Base

class Post(Base):
    
    title: str
    content: str
    published: bool = True