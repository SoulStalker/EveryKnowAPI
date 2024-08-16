import uvicorn
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()

easter_egg = ("The life of coder is like a dance,\n"
              "With keys that tap in rhythmic trance.\n"
              "Through lines of code and logic's maze,\n"
              "They chase the dawn in endless ways.\n\n"
              "Debugging thoughts, a puzzle's hold,\n"
              "With every bug, a story told.\n"
              "In silent nights or early day,\n"
              "The coder's mind will find its way.\n\n"
              "From coffee sips to midnight glare,\n"
              "They weave the bytes with utmost care.\n"
              "A digital world, both vast and wide,\n"
              "Where dreams and data coincide.\n\n"
              "The life of coder, swift and bright,\n"
              "A journey long through endless night.\n"
              "Yet with each line, a path is drawn,\n"
              "And through their work, the world's reborn.")


@app.get("/")
async def root():
    return {"message": easter_egg}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
