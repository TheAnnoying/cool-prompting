<script>
	import "../app.css";

	import { Sun, Moon } from "lucide-svelte";
	import { Button } from "$lib/components/ui/button";
	import { toggleMode } from "mode-watcher";
</script>
<svelte:head>
	<title>Faster Prompting</title>
</svelte:head>
<Button on:click={toggleMode} variant="outline" size="icon" class="absolute top-5 right-5">
	<Sun class="h-[1.2rem] w-[1.2rem] dark:hidden" />
	<Moon class="h-[1.2rem] w-[1.2rem] hidden dark:block"/>
</Button>
<slot />