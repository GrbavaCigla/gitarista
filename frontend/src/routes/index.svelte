<script lang="ts">
	import Background from '../components/Background.svelte';
</script>

<Background class="text-nord4 text-6xl font-bold" />
<div class="w-screen h-screen bg-nord0">
	<div
		class="max-w-md p-4 relative top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-nord0 sm:bg-nord2 sm:rounded-xl sm:shadow-xl"
	>
		<form action="" class="space-y-4" method="post">
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
				/>
			</div>

			<div class="flex items-center justify-between px-1">
				<div class="flex items-center">
					<input
						id="remember-me"
						name="remember-me"
						type="checkbox"
						class="text-nord8 focus:ring-nord8 border-transparent rounded"
					/>
					<label for="remember-me" class="text-sm ml-2 text-nord4"> Remember me </label>
				</div>
				<a href="#" class="text-sm text-nord4">Forgot your password?</a>
			</div>

			<!-- TODO: Add button animations -->
			<input
				type="submit"
				class="w-full rounded-xl font-bold text-nord4 shadow-xl py-2 bg-nord9 cursor-pointer"
				value="Sign in"
			/>
		</form>
	</div>
</div>
