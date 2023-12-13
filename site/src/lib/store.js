import { writable, get } from "svelte/store";
const serverAddress = "http://localhost:8080";

export let
    result = writable(null),
    processing = writable(false),
    prompt = writable(""),
    error = writable(false);

export function clear() {
    result.set(null);
    processing.set(false);
    error.set(false);
}

export async function submit(topic = "bananas", prompt) {
    processing.set(true);
    prompt = prompt?.replace(/%topic/g, topic) || topic;

    await fetch(`${serverAddress}/generate?prompt=${encodeURIComponent(prompt)}`).then(async e => {
        if(get(processing)) {
            processing.set(false);
            result.set(await e.text());
        }
    }).catch(e => {
        processing.set(false);
        error.set(true);

        console.error(e);
    });
}