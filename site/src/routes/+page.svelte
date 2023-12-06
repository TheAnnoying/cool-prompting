<script>
	import { Input } from "$lib/components/ui/input";
	import { Button } from "$lib/components/ui/button";
	import { Badge } from "$lib/components/ui/badge";
	import { Skeleton } from "$lib/components/ui/skeleton";
	import { Textarea } from "$lib/components/ui/textarea";
	import * as Dialog from "$lib/components/ui/dialog";

	import { SlidersHorizontal } from 'lucide-svelte';
	import { Loader2 } from "lucide-svelte";
	import { fly } from "svelte/transition";

	import { submit, clear, result, processing } from "../lib/store.js";
	let topic, prompt;
</script>
<form class="flex flex-col gap-2 w-96">
	<div class="relative">
		<Badge class="absolute translate-x-1/2 -translate-y-1/2 end-0 bg-gradient-to-r from-blue-600 to-purple-500 z-10 text-white" variant="noborder">beta</Badge>
		<Input type="text" placeholder="Input a topic..." disabled={$processing ? "disabled" : ""} bind:value={topic} />
	</div>
	<div class="flex gap-2">
		<Button class="flex-1" variant="outline" on:click={() => {clear(); topic = ""}}>Clear</Button>
		<Button class="flex-1" disabled={$processing ? "disabled" : ""} on:click={() => submit(topic, prompt)}>
			{#if $processing}
				<Loader2 class="mr-2 h-4 w-4 animate-spin" />
			{/if}
			Submit
		</Button>
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
</form>
{#if $result}
	<div class="w-1/3 h-48 border mt-10 grid place-items-center rounded-xl px-10" transition:fly={{ y: -5 }}>{$result}</div>
{:else if !$result && $processing}
	<div class="w-1/3 h-48 relative grid place-items-center mt-10">
		<p class="absolute z-10 font-mono drop-shadow-lg">generating with topic {topic ?? "bananas"}...</p>
		<Skeleton class="w-full h-full"></Skeleton>
	</div>
{/if}