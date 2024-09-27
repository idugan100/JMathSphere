from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import csv 
# setup favicon
# host server on aws so it can be accessed from the internet
# get james setup with ssh credentials into server so he can see the data


app = FastAPI()

@app.post("/favcolor-survey")
def color_form(favcolor:Annotated[str, Form()], color: Annotated[str, Form()], country: Annotated[str, Form()],Gender: Annotated[str, Form()]):

    with open("color.csv","a") as f:
        w = csv.writer(f)
        w.writerow([favcolor,color,country, Gender])

    html_content = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>JMathSphere</title>
            <link
            rel="stylesheet"
            type="text/css"
            href="https://unpkg.com/chimeracss/build/chimera-dark.css"
        />
        </head>
        <body>
            <h1>hi</h1>
            <p>thanks for your response!</p>
            <button style="background-color: aliceblue;">
                <a href="https://idugan100.github.io/JMathSphere/">Home</a>
            
            </button>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

