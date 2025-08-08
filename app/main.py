from fastapi import FastAPI
from app.database import engine, Base
from routes import blood, admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access the backend APIs
origins = [
    "http://localhost:3000",  # Pass here  React  or angular dev server, give an example of http://localhost:3000 of the react app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (like Content-Type, Authorization, etc.)
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(blood.router)
app.include_router(admin.router)
