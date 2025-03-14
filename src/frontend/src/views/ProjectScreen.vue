<script setup lang="ts">
import { ref } from "vue"
import Navbar from "../components/ProjectScreenElems/Navbar.vue"
import VerticalNavbar from "../components/ProjectScreenElems/VerticalNavbar.vue"
import FileViewer from "../components/ProjectScreenElems/FileViewer.vue"

const ws_mode = ref("files");
</script>

<template>
	<main class="pj-ws-main">
		<Navbar />
		<div class="pj-ws-body">
			<VerticalNavbar />
			<div class="pj-ws-module">
				<FileViewer v-if="ws_mode == 'files'" />
			</div>
		</div>
	</main>
</template>

<style scoped>
.pj-ws-main {
	width: 100%;
	height: 100%;
}

.pj-ws-body {
	width: 100%;
	height: 97%;

	display: flex;
}

.pj-ws-module {
	flex-grow: 1;
}
</style>
