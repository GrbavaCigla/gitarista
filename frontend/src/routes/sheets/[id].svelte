<script lang="ts" context="module">
	import type { Load } from '@sveltejs/kit';

	export const load: Load = async ({ params, fetch, session, stuff }) => {

		// TODO: Unhardcode url
		let resp = await fetch('http://127.0.0.1:8000/api/sheets/' + params.id);
		let meta = await resp.json();

		return {
			props: {
				metadata: meta
			}
		};
	};
</script>

<script lang="ts">
	import { OpenSheetMusicDisplay } from 'opensheetmusicdisplay';
	import { changeFill } from '../../functions/filler';
	import { isDarkTheme } from '../../functions/color_scheme';
	import { onMount } from 'svelte';

	let sheet_promise: Promise<{}>;

	onMount(async () => {
		let color: string;
		if(isDarkTheme()) {
			color = "#eceff4";
		} else {
			color = "#2e3440";
		}

		var container: HTMLElement = document.getElementsByClassName('osmd').item(0);

		var osmd = new OpenSheetMusicDisplay(container);

		osmd.setOptions({
			defaultFontFamily: "Cantarell",
			defaultFontStyle: 1
		});

		console.log(metadata);

		// TODO: Unhardocde this
		// TODO: Add listener on prefers-color-scheme
		sheet_promise = osmd.load(metadata["sheet_url"]).then(function () {
			osmd.zoom = 0.8;
			osmd.render();
			
			changeFill(container, color);
		});
	});

	export let metadata: JSON;
</script>

<div class="min-h-screen w-full background-pattern bg-light2 dark:bg-dark0">
	<div class="container mx-auto flex justify-center items-start flex-col md:flex-row p-4">
		<div class="basis-full rounded-xl shadow-xl bg-light0 dark:bg-dark1 osmd m-4" />
		<div class="basis-96 h-32 bg-red-600 m-4"></div>
	</div>
</div>
