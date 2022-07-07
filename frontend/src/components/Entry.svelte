<script lang="ts">
	enum TextType {
		TEXT = 'text',
		EMAIL = 'email',
		PASSWORD = 'password'
	}

	export let name: string;
	export let id = name;
	export let value: string;
	export let placeholder: string | null;
	export let type: TextType = TextType.TEXT;

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<!-- TODO: Add reveal password -->
<div>
	<label for={name} class="sr-only">{placeholder}</label>
	<input
		use:typeAction
		{placeholder}
		class="font-bold w-full rounded-xl border-transparent focus:outline-none"
		{name}
		{id}
		bind:value
	/>
</div>
