<script lang="ts">
	import { onMount } from 'svelte';
	import { getRandomNumber } from '../functions/random';

	export let cuts = 4;
	export let offset = 0.0002;

	let height = 100;
	let width = 100;

	// TODO: Remove any add real type
	let particles: any[] = [];

	let chars = [
		'&#119134;',
		'&#119135;',
		'&#119136;',
		'&#119137;',
		'&#9837;',
		'&#9838;',
		'&#9839;',
		'&#119070;',
		'&#119074;',
		'&#119101;',
		'&#119102;',
		'&#119103;'
	];

	// TODO: ~~Make this work on window resize~~ This is partially done
	onMount(() => {
		let xcount: number;
		let ycount: number;

		let roffset = offset * width * height;

		if (width > height) {
			xcount = 2 ** Math.ceil(cuts / 2);
			ycount = 2 ** Math.floor(cuts / 2);
		} else {
			xcount = 2 ** Math.floor(cuts / 2);
			ycount = 2 ** Math.ceil(cuts / 2);
		}

		for (let i = 0; i < xcount; i++) {
			for (let j = 0; j < ycount; j++) {
				particles.push({
					char: chars[getRandomNumber(0, chars.length)],
					pos: [
						getRandomNumber((width / xcount) * i + roffset, (width / xcount) * (i + 1) - roffset),
						getRandomNumber((height / ycount) * j + roffset, (height / ycount) * (j + 1) - roffset)
					]
				});
			}
		}
		particles = particles;
	});
</script>

<div class="absolute w-screen h-screen overflow-hidden">
	{#each particles as particle}
		<p
			style="left: {particle.pos[0]}%; top: {particle.pos[1]}%; {$$props.style}"
			class="absolute -translate-x-1/2 -translate-y-1/2 {$$props.class}"
		>
			{@html particle.char}
		</p>
	{/each}
</div>
