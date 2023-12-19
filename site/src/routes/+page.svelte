<script>
	import { submit, clear, result, processing, error } from "../lib/store.js";
	import { browser } from "$app/environment";
	let topic, prompt;

	import { SlidersHorizontal, Loader2 } from "lucide-svelte";
	import { fly } from "svelte/transition";

	import { Input } from "$lib/components/ui/input";
	import { Button } from "$lib/components/ui/button";
	import { Skeleton } from "$lib/components/ui/skeleton";
	import { Textarea } from "$lib/components/ui/textarea";
	import * as Dialog from "$lib/components/ui/dialog";

	if(browser) prompt = window.localStorage.getItem("prompt") ?? "";
	$: if(browser) window.localStorage.setItem("prompt", prompt);
</script>
<form class="flex flex-col gap-2 w-96">
	<div class="flex flex-row gap-2">
		<Input type="text" placeholder="Input a topic..." disabled={$processing ? "disabled" : ""} bind:value={topic} />
		<Dialog.Root>
			<Dialog.Trigger>
				<Button class="flex-1" variant="outline" size="icon">
					<SlidersHorizontal class="w-[1.2rem] h-[1.2rem]" />
				</Button>
			</Dialog.Trigger>
			<Dialog.Content>
				<Dialog.Header>
					<Dialog.Title>Prompt</Dialog.Title>
					<Dialog.Description>Create a prompt. Use <code class="relative rounded bg-muted px-1 py-1 font-semibold">%topic</code> as the topic input.</Dialog.Description>
				</Dialog.Header>
				<Textarea placeholder="Type your custom prompt here" bind:value={prompt} />
				<span class="text-sm text-muted-foreground">* Changes are saved automatically</span>
			</Dialog.Content>
		</Dialog.Root>
	</div>
	<div class="flex gap-2">
		<Button class="flex-1" variant="outline" on:click={() => {clear(); topic = ""}}>Clear</Button>
		<Button class="flex-1" disabled={$processing ? "disabled" : ""} on:click={() => submit(topic, prompt)}>
			{#if $processing}<Loader2 class="mr-2 h-4 w-4 animate-spin" />{/if}
			Submit
		</Button>
	</div>
</form>
{#if $error.generate}
	<div class="min-w-[24rem] w-1/3 min-h-[12rem] border border-destructive mt-10 text-destructive flex flex-col items-center justify-center rounded-xl px-10 py-5" transition:fly={{ y: -5 }}>
		<p>An error occured</p>
		<a href="https://github.com/TheAnnoying/cool-prompting/issues/new" target="_blank" class="underline">Report on Github</a>
	</div>
{/if}

{#if $result && !$processing && !$error.generate}
	<div class="min-w-[24rem] w-1/3 min-h-[12rem] border mt-10 grid place-items-center rounded-xl px-10 py-5" transition:fly={{ y: -5 }}>{$result}</div>
{:else if !$result && $processing && !$error}
	<div class="min-w-[24rem] w-1/3 h-48 relative grid place-items-center mt-10 py-5">
		<p class="absolute z-10 font-mono">generating...</p>
		<Skeleton class="w-full h-full"></Skeleton>
	</div>
{/if}