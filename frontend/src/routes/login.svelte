<script lang="ts">
	import { access_token, refresh_token } from '../stores/auth';
	import Background from '../components/Background.svelte';
	
	let email: string;
	let password: string;

	// TODO: Add loading indication
	// TODO: Handle errors
	// TODO: Change hardcoded url
	async function signin() {
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

		console.log(json);

		refresh_token.set(json['refresh']);
		access_token.set(json['access']);
	}
</script>

<!-- TODO: Input validation -->
<Background class="text-nord4 text-6xl font-bold" />
<div class="w-screen h-screen bg-nord0">
	<div
		class="space-y-4 max-w-md p-4 relative top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-nord0 sm:bg-nord2 sm:rounded-xl sm:shadow-xl"
	>
		<div>
			<h1 class="text-nord6 font-extrabold text-2xl text-center">Sign in to your account</h1>
			<h2 class="text-nord4  text-md text-center">
				or <a href="#" class="text-nord8">create one</a> now!
			</h2>
		</div>
		<div>
			<label for="email-address" class="sr-only">Email address</label>
			<input
				type="email"
				placeholder="Email address"
				class="font-bold w-full rounded-xl border-transparent text-nord1 bg-nord4 focus:outline-none focus:border-nord8 focus:ring-nord8"
				name=""
				id="email-address"
				bind:value={email}
			/>
		</div>

		<!-- TODO: Add reveal password -->
		<div>
			<label for="password" class="sr-only">Password</label>
			<input
				type="password"
				placeholder="Password"
				class="font-bold w-full rounded-xl border-transparent text-nord1 bg-nord4 focus:outline-none focus:border-nord8 focus:ring-nord8"
				name=""
				id="password"
				bind:value={password}
			/>
		</div>

		<div class="flex items-center justify-between px-1">
			<div class="flex items-center">
				<input
					id="remember-me"
					name="remember-me"
					type="checkbox"
					class="text-nord8 focus:ring-nord8 bg-nord4 border-transparent rounded"
				/>
				<label for="remember-me" class="text-sm ml-2 font-bold text-nord4"> Remember me </label>
			</div>
			<a href="#" class="text-sm text-nord4 font-bold">Forgot your password?</a>
		</div>

		<!-- TODO: Add button animations -->
		<button
			class="w-full rounded-xl font-bold text-nord4 shadow-xl py-2 bg-nord10 cursor-pointer"
			on:click={signin}
		>
			Sign in
		</button>
	</div>
</div>
