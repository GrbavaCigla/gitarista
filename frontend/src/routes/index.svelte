<script lang="ts">
	import Entry from '../components/Entry.svelte';

	// import { access_token } from '../stores/auth';
	// import { onMount } from 'svelte';

	// let authenticated = false;
	// access_token.subscribe((val) => {
	// 	if (val !== '') {
	// 		authenticated = true;
	// 	}
	// });
</script>

<nav class="bg-light1 dark:bg-dark1">
	<dir class="max-w-7xl mx-auto my-0 p-4 flex items-center justify-between font-bold">
		<a href="/" class="text-3xl font-logo text-primary">Gitarista</a>

		<div class="">
			<Entry
				name="search"
				placeholder="Search"
				type="text"
			/>
		</div>

		<a href="login" class="text-xl dark:text-light2 text-dark2 hover:bg-slate-300 dark:hover:bg-dark3 py-2 px-6 transition rounded-xl">Login</a>
	</dir>
</nav>
