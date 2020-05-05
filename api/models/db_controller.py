"""
This module establishes connection with DataBase
"""
from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as david
from api import app


class Dbcontroller:
    """
    class handles database connection
    """

    def __init__(self):
        database_url = app.config['DATABASE_URL']
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=david.RealDictCursor)
        print("Successfully connected to"+database_url)
        self.create_tables()


    def create_tables(self):
        """
        method creates tables
        """
        worker_table = "CREATE TABLE IF NOT EXISTS workers(workerId serial PRIMARY KEY,\
          name varchar(50), email varchar(100), company varchar(100))"

        orders_table = "CREATE TABLE IF NOT EXISTS orders(orderId serial PRIMARY KEY,\
          title varchar(100), description varchar(200),\
          workerId INTEGER REFERENCES workers(workerId),\
         deadline bigint)"
          

        self.cursor.execute(worker_table)
        self.cursor.execute(orders_table)

    def drop_tables(self):
        """
        method drops tables
        """
        drop_worker_table = "DROP TABLE workers cascade"
        drop_orders_table = "DROP TABLE orders cascade"
        self.cursor.execute(drop_worker_table)
        self.cursor.execute(drop_orders_table)

    def fetch_all_entries(self,table_name):
        """ Fetches all entries from the database"""
        query = ("SELECT * FROM %s;") %(table_name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
        
    def add_worker(self,new_worker):
        self.cursor.execute("INSERT INTO workers(name,email,company) VALUES\
        (%s, %s, %s);",(new_worker.name,new_worker.email,new_worker.company))

    def fetch_worker(self,worker):
        """Returns a worker in form of a dict or None if user not found"""
        query = "SELECT * FROM workers WHERE name=%s"
        self.cursor.execute(query, (worker.name,))
        worker = self.cursor.fetchone()
        return worker

    def fetch_orders(self,order):
        """Returns a orders in form of a dict or None if order not found"""
        query = "SELECT * FROM orders WHERE title=%s"
        self.cursor.execute(query, (order.title,))
        orders = self.cursor.fetchall()
        return orders

    def fetch_all_workers(self):
        return self.fetch_all_entries('workers')

    def add_order(self,order):
        self.cursor.execute("INSERT INTO orders(title, description,\
        deadline, workerId)\
        VALUES(%s, %s, %s, %s);",(order.title,order.description,\
        order.deadline,order.workerid))

    def fetch_all_orders(self):
        return self.fetch_all_entries('orders')

    def fetch_order(self,column,did):
        """Returns a orders in form of a dict or None if order not found"""
        query = """SELECT * FROM orders WHERE {0}={1}""".format(column,did,)
        self.cursor.execute(query,)
        order = self.cursor.fetchall()
        return order

    def fetch_specific_worker_orders(self,did):
        """Returns  orders in form of a dict ordered by deadlines or None if order not found"""
        query = """SELECT * FROM orders WHERE workerId={0} ORDER BY deadline ASC""".format(did,)
        self.cursor.execute(query,)
        orders = self.cursor.fetchall()
        return orders

    def delete(self,table_name,column, id):
            query = """DELETE FROM {0} WHERE {1}={2};""".format(table_name,column, id)
            self.cursor.execute(query,)

    def query_last_item(self):
        query = """SELECT * FROM orders ORDER BY orderId DESC LIMIT 1"""
        self.cursor.execute(query,)
        order = self.cursor.fetchone()
        return order

   

    def fetch_worker_by_id(self,worker_id):
        """Returns a worker in form of a dict or None if user not found"""
        query = "SELECT * FROM workers WHERE workerid=%s"
        self.cursor.execute(query, (worker_id,))
        worker = self.cursor.fetchone()
        return worker
