<script lang="ts">
	import { access_token, refresh_token } from '../stores/auth';
	import Background from '../components/Background.svelte';
	import { onMount } from 'svelte';

	let authenticated = false;
	access_token.subscribe((val) => {
		if (val !== '') {
			authenticated = true;
		}
	});

	onMount(() => {
		if (!authenticated) {
			// TODO: Redirect to login
		}
	});
</script>


<!-- TODO: Add user page -->
