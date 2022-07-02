<script lang="ts" context="module">
	import type { Load } from '@sveltejs/kit';
	import { OpenSheetMusicDisplay } from 'opensheetmusicdisplay';

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
	import { onMount } from 'svelte';

	onMount(async () => {
		var container: HTMLElement = <HTMLElement>document.getElementsByClassName('osmd')[0];

		var osmd = new OpenSheetMusicDisplay(container);
		osmd.setOptions({
			backend: 'svg',
			drawTitle: true
		});

		// TODO: Unhardocde this
		osmd.load('http://localhost:8000/api/sheets/1.musicxml').then(function () {
			osmd.render();
		});
	});

	export let metadata: JSON;
</script>

<div class="w-screen absolute h-screen osmd" />
