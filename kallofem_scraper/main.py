from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess
import os
import json

app = FastAPI()


@app.get("/scrape")
def run_scraper(url: str = Query(...)):
    output_file = "products.json"
    try:
        if os.path.exists("products.json"):
            os.remove("products.json")

        result = subprocess.run([
            "python", "-m", "scrapy", "crawl", "products",
            "-o", "products.json",
            "-a", f"url={url}"
        ], cwd=".", capture_output=True, text=True)

        if result.returncode != 0:
            return {
                "error": result.stderr,
                "output": result.stdout
            }

        return {"message": "Scraping completed"}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/")
def get_scraped_products():
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except FileNotFoundError:
        return JSONResponse(status_code=404, content={"error": "products.json not found"})
