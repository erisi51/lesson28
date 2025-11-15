from typing inport List, Optional
import sqlite3from models import Item
from database import get_db_connection


def create_item(item: Item) -> Item:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) Values (?,?)", (item.name, item.description))
    conn.commit()
    item.id = cursor.lastrowid
    conn.close()
    return item

def get_items() -> List[Item]:
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items"). fetchall()
    conn.close()
    return [Item(**dict(item) for item in items)]


def get_item(item_id: int) -> Optional[Item]:
    conn = get_db_connection()
    item = conn.execute("SELECT * FROM items where id = ?",(item_id)).fetchall()
    conn.close()
    if item is None:
        return None
    else:
        return Item(**dict(item))

    def update_item(item_id: int, item: item) -> Optional[Item]:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE items set name = ?, description = ? Where id = ?", (item.name, item.description, item_id))
        conn.commit()
        updated = cursor.rowcount
        conn.close()
        if updated == 0:
            return None
        item.id = item_id
        return item



