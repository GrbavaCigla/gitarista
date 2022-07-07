<script lang="ts">
	export let name: string;
	export let id = name;
</script>

<div class="flex items-center justify-between font-bold">
	<div class="flex items-center">
		<input {id} {name} type="checkbox" class="border-transparent rounded" />
		<label for={name} class="ml-2">
			<slot name="leading" />
		</label>
	</div>
	<slot name="trailing" />
</div>
