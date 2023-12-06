from llama_cpp import Llama
from flask import Flask, request

app = Flask(__name__)
llm = Llama(model_path="./models/llama-2-13b-chat.Q4_K_M.gguf", n_threads=4)

@app.after_request
def cors_headers(response):
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Headers"] = "Content-Type"
	response.headers["Access-Control-Allow-Methods"] = "GET"
	return response

@app.route("/generate", methods=["GET"])
def send():
	prompt = f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\nInstruction:\n{request.args.get("prompt")}\n\nResponse:"
	output = llm(prompt)
	return output["choices"][0]["text"]

app.run(port=8080)