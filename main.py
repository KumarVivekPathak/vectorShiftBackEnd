from fastapi import FastAPI, Form, HTTPException
from typing import List
from check_dag import analyze_pipeline
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
async def parse_pipeline(pipeline: dict):
    nodes = pipeline.get("nodes", [])
    edges = pipeline.get("edges", [])
    
    result = analyze_pipeline(nodes, edges)
    return result