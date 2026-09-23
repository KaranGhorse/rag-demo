from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="Health Server")

# Server start hone ka time
server_start_time = datetime.now(timezone.utc)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "server": "running",
        "login_time": server_start_time.isoformat(),
        "current_time": datetime.now(timezone.utc).isoformat()
    }
