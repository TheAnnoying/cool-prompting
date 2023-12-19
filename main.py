from llama_cpp import Llama
from flask import Flask, request, jsonify
from threading import Lock
import sqlite3

lock = Lock()
connection = sqlite3.connect("data.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS keys(
		auth_key TEXT PRIMARY KEY,
		creation_timestamp INTEGER
	)
""")

app = Flask(__name__)
llm = Llama(model_path="./models/stablelm-zephyr-3b.Q4_K_M.gguf", n_threads=4, n_gpu_layers=0)

@app.after_request
def cors_headers(response):
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Headers"] = "Content-Type, key"
	response.headers["Access-Control-Allow-Methods"] = "GET"
	return response

@app.route("/validatekey", methods=["GET"])
def validate():
	cursor.execute("SELECT * from keys WHERE auth_key = ?", (request.headers.get("key"),))
	result = cursor.fetchone()

	if result:
		return jsonify({ "valid": True })
	else:
		return jsonify({ "valid": False })

@app.route("/generate", methods=["GET"])
def send():
	prompt = f"<|user|>\n{request.args.get("prompt")}<|endoftext|>\n<|assistant|>"

	cursor.execute("SELECT * from keys WHERE auth_key = ?", (request.headers.get("key"),))
	result = cursor.fetchone()

	if result:
		with lock:
			output = llm(prompt, max_tokens=4096)
		return output["choices"][0]["text"]
	else:
		return "Not authorized"

app.run(port=8080)
connection.close()