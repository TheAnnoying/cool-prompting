import { writable } from "svelte/store";
const serverAddress = "http://localhost:8080";

export let
    result = writable(null),
    processing = writable(false),
    prompt = writable("");

export function clear() {
    result.set(null);
    processing.set(false);
}

export async function submit(topic = "bananas", prompt) {
    processing.set(true);
    prompt = prompt?.replace(/%topic/g, topic) || `Explain the following: ${topic}`;

    await fetch(`${serverAddress}/generate?prompt=${encodeURIComponent(prompt)}`).then(async e => {
        if(processing) {
            processing.set(false);
            result.set(await e.text());
        }
    });
}