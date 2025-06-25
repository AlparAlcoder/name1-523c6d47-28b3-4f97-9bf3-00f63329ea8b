from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None

def connect_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()

@app.post("/items/")
async def create_item(item: Item):
    """
    Endpoint POST que realiza a integração com um banco de dados, gravando os itens recebidos.
    """
    conn, cursor = connect_db()
    try:
        cursor.execute("INSERT INTO items VALUES (?, ?, ?, ?)", 
                        (item.id, item.name, item.price, item.is_offer))
        conn.commit()
        return {"status": "Item added successfully"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=400, detail="Error in database operation")
    finally:
        close_db(conn, cursor)