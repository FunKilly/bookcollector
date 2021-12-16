import uvicorn
from fastapi import FastAPI

from src.app_1.api.routes.books import router as app_1_router


class TestFastApi(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.include_api_routers()

    def include_api_routers(self):
        self.include_router(app_1_router)


app = TestFastApi()


# Run the middleware.
if __name__ == "__main__":
    uvicorn.run(app)
