from fastapi import FastAPI

app = FastAPI(title="Insider Service")

@app.get("/")
async def root():
    return {"service": "insider-service", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

