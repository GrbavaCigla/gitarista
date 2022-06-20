import { writable, type Writable } from "svelte/store";

export let refresh_token: Writable<string> = writable("");
export let access_token: Writable<string> = writable("");

// TODO: Critical: store this as cookies instead of localStorage and prevent CSRF and XSS
if (typeof window !== 'undefined') {
    refresh_token = writable(localStorage.getItem("refresh_token") || "");
    access_token = writable(localStorage.getItem("access_token") || "");
}

refresh_token.subscribe((val) => {
    if (typeof window !== 'undefined') {
        localStorage.setItem("refresh_token", val)
    }
});
access_token.subscribe((val) => {
    if (typeof window !== 'undefined') {
        localStorage.setItem("access_token", val)
    }
});
