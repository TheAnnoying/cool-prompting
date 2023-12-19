<script>
	import "../app.css";
	import { validateKey, error } from "../lib/store.js";
	import { browser } from "$app/environment";

	import { Input } from "$lib/components/ui/input";
	import * as Dialog from "$lib/components/ui/dialog";
	import { fly } from "svelte/transition";

	let keyDialog = false, value, valid;

	async function checkKey(value) {
		if(browser && !window.localStorage.getItem("key")) keyDialog = true;
		if(value) valid = await validateKey(value);
		if(valid) {
			if(browser) window.localStorage.setItem("key", value);
			setTimeout(() => keyDialog = false, 1000);
		}

	}

	$: checkKey(value);
</script>
<Dialog.Root bind:open={keyDialog} closeOnEscape={false} closeOnOutsideClick={false}>
	<Dialog.Trigger />
	<Dialog.Content>
		<Dialog.Header>
			<Dialog.Title>Provide an API key</Dialog.Title>
			<Dialog.Description>In order to use this service you must provide your API key.</Dialog.Description>
		</Dialog.Header>
		<Input type="text" placeholder="Input your API key" bind:value={value} />
		{#if valid}
			<p class="text-sm leading-none text-green-400" transition:fly={{ y: -5 }}>thanks :)</p>
		{/if}
		{#if $error.validate}
			<p class="text-sm leading-none text-destructive">An error occured - <a href="https://github.com/TheAnnoying/cool-prompting/issues/new" target="_blank" class="underline">Report on Github</a></p>
		{/if}
	</Dialog.Content>
	<style>
		[data-melt-dialog-close] {
			display: none;
		}
	</style>
</Dialog.Root>
<svelte:head>
	<title>Cool Prompting</title>
</svelte:head>
<slot />