#uvicorn main:app --reload
import pandas_access as mdb
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    db_filename = 'Burdata.mdb'
    df = mdb.read_table(db_filename, "Burdata")[['顧客連番', '買上高']]
    return df.groupby('顧客連番', as_index=False).sum().to_html()