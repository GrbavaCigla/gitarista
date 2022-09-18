<!-- TODO: Split into multiple components -->
<script lang="ts">
	import { access_token, refresh_token } from '../stores/auth';
	import CheckBoxTile from '../components/tiles/CheckBoxTile.svelte';
	import Entry from '../components/Entry.svelte';

	let email: string;
	let password: string;
	let error = {
		username: [],
		password: [],
		detail: null
	};

	// TODO: Add loading indication
	// TODO: Change hardcoded url
	async function login() {
		let response = await fetch('http://localhost:8000/api/token/', {
			method: 'POST',
			mode: 'cors',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				username: email,
				password: password
			})
		});

		let json = await response.json();

		if (response.ok) {
			refresh_token.set(json['refresh']);
			access_token.set(json['access']);

			// TODO: Redirect
		} else {
			error = json;
		}
	}
</script>

<!-- TODO: Input validation -->
<div class="w-screen h-screen bg-light2 dark:bg-dark0 sm:background-pattern">
	<div class="relative top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
		<a href="#" class="text-center block text-4xl mb-6 font-logo text-primary">Gitarista</a>
		<div
			class="mx-auto space-y-4 max-w-md p-4 sm:rounded-xl sm:shadow-xl sm:bg-light0 sm:dark:bg-dark1"
		>
			<div>
				<h1 class="font-extrabold text-2xl text-center">Sign in to your account</h1>
				<h2 class="text-md text-center">
					or <a href="#">create one</a> now!
				</h2>
			</div>

			<Entry
				name="email"
				bind:value={email}
				placeholder="Email address"
				type="email"
				errors={error.username}
			/>

			<Entry
				name="password"
				bind:value={password}
				placeholder="Password"
				type="password"
				errors={error.password}
			/>

			<CheckBoxTile name="remember-me">
				<span slot="leading" class="text-sm">Remember me</span>
				<a href="#" slot="trailing" class="text-sm">Forgot your password?</a>
			</CheckBoxTile>

			<!-- TODO: Add button animations -->
			<button class="w-full" on:click={login}>Sign in</button>
			{#if error.detail !== null && error.detail !== undefined}
				<p class="text-error">{error.detail}</p>
			{/if}
		</div>
	</div>
</div>
