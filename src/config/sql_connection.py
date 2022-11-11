import sqlalchemy as alch
import os
from dotenv import load_dotenv

# -----------------------------------------------------------------------------

load_dotenv()

db_name = "got"

password=os.getenv("sql_password")

connectionData = f"mysql+pymysql://root:{password}@localhost/{db_name}"
engine = alch.create_engine(connectionData)