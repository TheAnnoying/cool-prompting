# Cool Prompting
> Create re-usable prompts for AI

Just like a programmer's function, create a prompt and give it some input. Examples of a few prompts you could use:
* `Make the following text longer without adding new information: %topic`
* `Create a funny story about %topic`.
* `Give me some information about %topic`

You can now change the input topic for different purposes.

## Libraries & Frameworks
The frontend was built using [shadcn-svelte](https://shadcn-svelte.com/), [Tailwind CSS](https://tailwindcss.com/) and [SvelteKit](https://kit.svelte.dev/).

The backend is coded in [Python](https://www.python.org/) using [Flask](https://flask.palletsprojects.com/). The text is generated using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python/) using the [StableLM Zephyr 3B](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/) model.