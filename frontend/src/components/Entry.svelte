<script lang="ts">
import { empty } from "svelte/internal";

	export let name: string;
	export let id = name;
	export let value: string;
	export let placeholder: string | null;
	export let type: string = 'text';
	export let errors: string[] = [];

	$: if (errors == undefined) {
		errors = [];
	}

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<!-- TODO: Add reveal password -->
<div>
	<label for={name} class="sr-only">{placeholder}</label>
	<input
		use:typeAction
		{placeholder}
		class={errors.length == 0 ? "font-bold w-full rounded-xl focusable" : "font-bold w-full rounded-xl focusable outline-error"}
		{name}
		{id}
		bind:value
	/>
	{#each errors as error}
		<label for={name} class="inline-block text-error mt-2">{error}</label>
	{/each}
</div>
