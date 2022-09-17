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
	import { savePDF } from '../../functions/save_pdf';
	import { onMount } from 'svelte';

	onMount(async () => {
		let color: string;
		if (isDarkTheme()) {
			color = '#eceff4';
		} else {
			color = '#2e3440';
		}

		var container = document.getElementsByClassName('osmd').item(0);

		var osmd = new OpenSheetMusicDisplay(container);

		osmd.setOptions({
			defaultFontFamily: 'Cantarell',
			defaultFontStyle: 1
		});

		// TODO: Unhardocde this
		// TODO: Add listener on prefers-color-scheme
		var sheet_promise = osmd.load(metadata.sheet_url).then(function () {
			osmd.zoom = 0.8;
			osmd.render();

			document.getElementById('download-pdf-button')!.onclick = () => {savePDF(metadata.title, osmd)};

			changeFill(container, color);
		});
	});

	export let metadata: JSON;
</script>

<div class="min-h-screen w-full background-pattern bg-light2 dark:bg-dark0">
	<div class="container mx-auto items-start flex flex-col 2xl:flex-row p-4">
		<div class="2xl:basis-full w-full rounded-xl shadow-xl bg-light0 dark:bg-dark1 osmd m-4" />
		<div class="2xl:basis-96 w-full rounded-xl shadow-xl bg-light0 dark:bg-dark1 m-4 px-6 py-4">
			<table class="w-full table-auto text-lg divide-gray-400 divide-y-2">
				<tr>
					<th class="p-2 text-left font-normal text-dark3 dark:text-light0">Title</th>
					<th class="p-2 text-right">{metadata.title}</th>
				</tr>
				<tr>
					<th class="p-2 text-left font-normal text-dark3 dark:text-light0">Author</th>
					<th class="p-2 text-right">{metadata.author}</th>
				</tr>
				<tr>
					<th class="p-2 text-left font-normal text-dark3 dark:text-light0">Publisher</th>
					<th class="p-2 text-right"><a href="#">{metadata.publisher}</a></th>
				</tr>
				<tr>
					<th class="p-2 text-left font-normal text-dark3 dark:text-light0">Date</th>
					<th class="p-2 text-right">{metadata.created}</th>
				</tr>
			</table>
			<div class="flex gap-4 mt-2">
				<button class="w-full" id="download-pdf-button">PDF</button>
				<button class="w-full">MusicXML</button>
			</div>
		</div>
	</div>
</div>
