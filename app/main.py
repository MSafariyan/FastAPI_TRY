from fastapi import FastAPI
from .routers import book as bookRouter
from .schemes import book as bookSchemes
from .models import book as bookModels
from .routers import user as userRouter
from .schemes import user as userSchemes
from .models import user as userModels
from .routers import authentication as auth
from .database import engin, conn


try:
    bookModels.Base.metadata.create_all(bind=engin)
    userModels.Base.metadata.create_all(bind=engin)
except Exception as e:
    print(e)

app = FastAPI(
    title="M. Safarian",
    description = "This is a Test Restfull api for my resume.",
    version = "0.0.1",
    contact={
        "name": "Mahdi Safarian",
        "url": "http://www.github.com/mSafariyan/",
        "email": "ma.hiccup@gmail.com",
    },
)

app.include_router(auth.router,
                   tags=["Auth"])

app.include_router(bookRouter.router,
                   prefix="/api/v1/book",
                   tags=["Book"]
)

app.include_router(userRouter.router,
                   prefix="/api/v1/user",
                   tags=["User"]
)
