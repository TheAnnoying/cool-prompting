from llama_cpp import Llama
from flask import Flask, request

app = Flask(__name__)
llm = Llama(model_path="./models/stablelm-zephyr-3b.Q4_K_M.gguf", n_threads=4, n_gpu_layers=0)

@app.after_request
def cors_headers(response):
	response.headers["Access-Control-Allow-Origin"] = "*"
	response.headers["Access-Control-Allow-Headers"] = "Content-Type"
	response.headers["Access-Control-Allow-Methods"] = "GET"
	return response

@app.route("/generate", methods=["GET"])
def send():
	prompt = f"""<|user|>
{request.args.get("prompt")}<|endoftext|>
<|assistant|>"""
	output = llm(prompt, max_tokens=4096)
	return output["choices"][0]["text"]

app.run(port=8080)