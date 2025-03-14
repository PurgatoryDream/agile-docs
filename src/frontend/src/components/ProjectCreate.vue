<script setup lang="ts">
const emit = defineEmits(["submit"]);
function submitNewProject() {
	let project = {"id": 1, "name": "Project 1"};
	emit("submit", project)
}

</script>

<template>
	<div class="pj-prev-container">
		<div class="pj-prev-viewer" @click="submitNewProject">
			<span class="pj-prev-name">New project...</span>
		</div>
	</div>
</template>

<style scoped>
.pj-prev-container {
	display: flex;
	justify-content: center;
	align-items: center;

	width: 16vw;
	min-width: 200px;
	height: 16vw;
	min-height: 200px;
}

.pj-prev-viewer {
	display: flex;
	justify-content: center;
	align-items: center;

	width: 80%;
	height: 80%;
	margin: auto;
	border: dotted black;
	border-radius: 10px;
	box-shadow: 2px 2px 4px black;
}

.pj-prev-viewer:hover {
	background-color: #a0a0a0;
	cursor: pointer;
}
</style>
