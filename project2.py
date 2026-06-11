from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message': 'Patient management system API'}

@app.get("/about")
def about():
    return {'message':'To manage patient records'}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "ID of patient", example = "P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = "patient not found")

@app.get("/sort")
def sort_patient(sort_by: str = Query(...,description="sort by h,w,bmi"), order: str = Query('asc', description = "sort in asc to desc order")):
    valid_fields = ['height', 'weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail=f'INVALID FIELDS SELECT FROM {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail='INVALID order SELECT between asc and desc')

data = load_data()
sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0),reverse = False)
sorted_order = True if order =='desc' else False