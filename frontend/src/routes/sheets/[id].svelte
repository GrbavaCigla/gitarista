<script lang="ts" context="module">
	import type { Load } from '@sveltejs/kit';

	export const load: Load = async ({ params, fetch, session, stuff }) => {
		// TODO: Unhardcode url

		let resp = await fetch('http://localhost:8000/api/sheets/' + params.id);
		let meta = await resp.json();

		// TODO: This should be loaded after everything is mounted
		// let resp = await fetch("http://localhost:8000/api/sheets/${params.id}.musicxml");
		// let musicxml = await resp.json();

		return {
			props: {
				metadata: meta
			}
		};
	};
</script>

<script lang="ts">
	import { OpenSheetMusicDisplay } from 'opensheetmusicdisplay';
	import { onMount } from 'svelte';

	onMount(async () => {
		var container: HTMLElement = document.getElementsByClassName('osmd').item(0);

		var osmd = new OpenSheetMusicDisplay(container);

		osmd.setOptions({
			drawTitle: false,
			drawComposer: false,
			drawCredits: false,
			drawLyricist: false,
			drawSubtitle: false
		});

		// TODO: Unhardocde this
		osmd.load('http://localhost:8000/api/sheets/1.musicxml').then(function () {
			osmd.render();
		});
	});

	export let metadata: JSON;
</script>

<div class=" min-h-screen">
	<h1 class="text-6xl text-center p-4">{metadata.title}</h1>
	<div class="mx-32 py-4 flex">
		<!-- TODO: Change this to nord color instead of white -->
		<div class="basis-full rounded-xl mx-4 shadow-xl">
			<div class="osmd invert" />
		</div>
		<div class="basis-1/4 rounded-xl mx-4 self-start shadow-xl">
			<!-- TODO: Add controls -->
		</div>
	</div>
</div>
