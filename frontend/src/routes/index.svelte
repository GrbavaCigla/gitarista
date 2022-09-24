<script lang="ts">
	import type { Sheet } from '../models/sheet';
	import { onMount } from 'svelte';

	async function fetchSheets() {
		let resp = await fetch('http://127.0.0.1:8000/api/sheets/');
		let meta: Sheet[] = await resp.json();

		return meta;
	}

	onMount(() => {
		sheets = fetchSheets();
	});

	export let sheets: Promise<Sheet[]> = Promise.resolve([]);
</script>

<div class="bg-light1 dark:bg-dark1 background-pattern min-h-screen flex flex-col">
	<nav class="bg-light0 dark:bg-dark0 sticky top-0 w-full shadow-xl z-10">
		<dir class="container mx-auto my-0 p-4 flex items-center justify-between font-bold">
			<a href="/" class="text-3xl font-logo text-primary">Gitarista</a>

			<div class="basis-2/5 hidden sm:block relative">
				<dir class="absolute p-2.5 inset-y-0 left-0">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="2"
						stroke="#4c566a"
						class="w-5 h-5"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
						/>
					</svg>
				</dir>
				<label for="search" class="sr-only">Search</label>
				<input
					class="font-bold w-full rounded-xl focusable py-2 pl-10 pr-24 text-dark0"
					placeholder="Recuerdos de la Alhambra..."
					name="search"
					id="search"
				/>
				<dir class="absolute right-0 inset-y-0">
					<button class="px-4 rounded-l-none shadow-none">Search</button>
				</dir>
			</div>

			<a
				href="login"
				class="text-lg dark:text-light2 text-dark2 hover:bg-light1 dark:hover:bg-dark1 py-2 px-6 transition rounded-xl"
				>Login</a
			>
		</dir>
	</nav>

	<div class="bg-light2 dark:bg-dark2 shadow-xl container mx-auto flex-auto">
		<div class="grid grid-cols-[repeat(auto-fit,_minmax(18em,_1fr))] gap-6 p-6">
			{#await sheets}
				<svg
					class="animate-spin text-dark1 dark:text-light0 w-10 h-10 mx-auto"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
				>
					<circle
						class="opacity-25"
						cx="12"
						cy="12"
						r="10"
						stroke="currentColor"
						stroke-width="4"
					/>
					<path
						class="opacity-75"
						fill="currentColor"
						d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
					/>
				</svg>
			{:then resp}
				{#each resp as sheet}
					<div
						class="h-96 bg-light1 dark:bg-dark3 rounded-2xl shadow-md flex flex-col items-center pt-4 px-4 pb-2 space-y-2"
					>
						<div class="bg-light0 dark:bg-tertiary rounded-xl w-full flex-1 text-center text-3xl" />
						<p class="text-lg font-bold">{sheet.title}</p>
					</div>
				{/each}
			{/await}
		</div>
	</div>
</div>
