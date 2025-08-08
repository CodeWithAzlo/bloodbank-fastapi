# from fastapi import FastAPI
# from app.database import engine, Base
# from routes import blood, admin


# app = FastAPI()


# # Create DB tables
# Base.metadata.create_all(bind=engine)

# # Include routers
# app.include_router(blood.router)
# app.include_router(admin.router)


from fastapi import FastAPI
from app.database import engine, Base
from routes import blood, admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend  to access backend APIs
origins = [
    "http://localhost:3000",  # React dev server
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
