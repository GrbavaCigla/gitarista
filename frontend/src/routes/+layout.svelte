<script>
	import SearchBar from '../components/SearchBar.svelte';
	import '../app.postcss';
</script>

<div class="navbar sticky top-0 bg-base-200">
	<div class="container mx-auto flex justify-between">
		<a class="text-3xl font-logo text-primary" href="#">Gitarista</a>
		
		<div class="basis-2/5">
			<SearchBar></SearchBar>
		</div>

		<!-- TODO: Add plus sign here -->
		<a class="btn btn-primary font-bold normal-case text-lg gap-1" href="#">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-6 h-6">
				<path d="M10.75 4.75a.75.75 0 00-1.5 0v4.5h-4.5a.75.75 0 000 1.5h4.5v4.5a.75.75 0 001.5 0v-4.5h4.5a.75.75 0 000-1.5h-4.5v-4.5z" />
			</svg>
			Create
		</a>
	</div>
</div>

<div class="background-pattern min-h-screen bg-base-100">
	<slot />
</div>
