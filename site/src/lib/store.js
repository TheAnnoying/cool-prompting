import { browser } from "$app/environment";
import { writable, get } from "svelte/store";
const serverAddress = "http://localhost:8080";

export let
    result = writable(null),
    processing = writable(false),
    prompt = writable(""),
    error = writable({ validate: false, generate: false});

export function clear() {
    result.set(null);
    processing.set(false);
    error.set({ validate: false, generate: false });
}

export async function submit(topic = "bananas", prompt) {
    processing.set(true);
    prompt = prompt?.replace(/%topic/g, topic) || topic;

    if(browser) {
        await fetch(`${serverAddress}/generate?prompt=${encodeURIComponent(prompt)}`, {
            headers: { key: window.localStorage.getItem("key") }
        }).then(async e => {
            if(get(processing)) {
                processing.set(false);
                result.set(await e.text());
            }
        }).catch(e => {
            processing.set(false);
            error.set({ validate: false, generate: true });
    
            console.error(e);
        });
    }
}

export async function validateKey(key) {
    return await fetch(`${serverAddress}/validatekey`, {
        headers: { key }
    }).then(async e => {
        error.set({ validate: false, generate: false });
        return (await e.json()).valid ?? false;
    }).catch(e => {
        error.set({ validate: true, generate: false });
        console.error(e);
    });
}