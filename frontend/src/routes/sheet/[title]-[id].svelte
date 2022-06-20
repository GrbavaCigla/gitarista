<script lang="ts" context="module">
    import type { Load } from "@sveltejs/kit";

	export const load: Load = ({ params, fetch, session, stuff }) => {
        // TODO: Fetch from API

        return {
            props: {
                title: params.title
            }
        };
	};
</script>

<script lang="ts">
    export let title: string;
</script>

<h1>{title}</h1>