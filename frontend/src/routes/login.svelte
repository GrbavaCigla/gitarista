<!-- TODO: Split into multiple components -->
<script lang="ts">
	import { access_token, refresh_token } from '../stores/auth';
	import CheckBoxTile from '../components/tiles/CheckBoxTile.svelte';
	import Entry from '../components/Entry.svelte';

	let email: string;
	let password: string;

	// TODO: Add loading indication
	// TODO: Handle errors
	// TODO: Change hardcoded url
	async function login() {
		let response = await fetch('http://localhost:8000/api/token/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: email,
				password: password
			})
		});

		let json = await response.json();

		refresh_token.set(json['refresh']);
		access_token.set(json['access']);
	}
</script>

<!-- TODO: Input validation -->
<div class="w-screen h-screen ">
	<div
		class="space-y-4 max-w-md p-4 relative top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 sm:rounded-xl sm:shadow-xl"
	>
		<div>
			<h1 class="font-extrabold text-2xl text-center">Sign in to your account</h1>
			<h2 class="text-md text-center">
				or <a href="#" class="">create one</a> now!
			</h2>
		</div>
		
		<Entry name="email" bind:value={email} placeholder="Email address" />

		<Entry name="password" bind:value={password} placeholder="Password" />

		<CheckBoxTile name="remember-me">
			<span slot="leading" class="text-sm">Remember me</span>
			<a href="#" slot="trailing" class="text-sm">Forgot your password?</a>
		</CheckBoxTile>

		<!-- TODO: Add button animations -->
		<button class="w-full" on:click={login}>
			Sign in
		</button>
	</div>
</div>
