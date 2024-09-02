# Rating portal

## What is that?
- U can use this application to rate books

## How can I do that?
- Type command `make run`
- Launch your browser and type `localhost:8000/docs` to see available endpoints
- This is a backend app so u will need to use `curl` or `postman` to test it


## More about this application
- It's a simple app that is using FastAPI as its backbone
- Whole project uses Onion Architecture with patterns like dependency inversion, repository and unit of work.
- It's possible to slightly modify the CommandBus to EventBus, some part of the work like adding a review, could
- be treated as an event.
- If I had more time I would definitely add tests, while adding every part of them system, however I was in hurry.
- Same applies to envs that are visible in the code.