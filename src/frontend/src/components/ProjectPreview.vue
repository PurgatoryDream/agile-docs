<script setup lang="ts">
</script>

<template>
	<div class="pj-prev-container">
		<div class="pj-prev-viewer">
			<span class="pj-prev-name"><slot>Unnamed.</slot></span>
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
	border: solid black;
	border-radius: 10px;
	box-shadow: 2px 2px 4px black;
}
</style>
