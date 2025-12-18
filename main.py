from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AgentX-Backend")

app = FastAPI(title="AgentX Backend")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AgentX Backend is running"}

@app.websocket("/ws/agent")
async def agent_websocket(websocket: WebSocket):
    await websocket.accept()
    logger.info("Client connected to agent websocket")
    try:
        while True:
            # Placeholder for agent interaction loop
            # In a real scenario, this would send state and receive actions/config
            data = await websocket.receive_text()
            logger.info(f"Received: {data}")
            
            # Echo back for now
            response = {"status": "alive", "echo": data}
            await websocket.send_text(json.dumps(response))
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        logger.info("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
