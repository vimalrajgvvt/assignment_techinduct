# assignment_techinduct

### Project Structure
Controller/: API Route definitions (The "Front Desk").

service/: Business logic and distance filtering (The "Brain").

model/: SQLAlchemy database definitions.

schema/: Pydantic data validation rules.

utils/: Mathematical helpers (Haversine logic).

database/: Connection setup for the SQLite engine.

## install the required libraries
pip install -r requirements.txt

## run the server
uvicorn app:app --host 0.0.0.0 --port 5002 --reload

## Method,Endpoint

POST,/create,Add a new address with Lat/Long.
GET,/nearby,Search addresses near Bangalore (default 5km).
PUT,/update/{id},Modify an existing address by ID.
DELETE,/delete_address/{id},Remove an address from the system.

## Interactive Documentation

#FastAPI automatically generates documentation for you. Once the server is running, visit:

Swagger UI: http://127.0.0.1:8000/docs

## Configuration

Database: SQLite (Stored locally as address_book.db).
Reference Point: Bangalore Center