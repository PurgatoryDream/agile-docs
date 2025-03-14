<script setup lang="ts">
import { ref } from "vue"
import type { Ref } from "vue"
import ProjectPreview from "../components/ProjectPreview.vue"
import ProjectCreate from "../components/ProjectCreate.vue"

interface Project {
	id: number;
	name: string;
}
const projects: Ref<Project[]> = ref([]);

function createNewProject(newproj: Project) {
	projects.value.push(newproj);
}
</script>

<template>
	<main class="project-list-main">
		<div class="pj-list-header">
			Projects
		</div>
		<div class="pj-list-container">
			<ProjectPreview v-for="pj in projects" :key="pj.id">
				{{pj.name}}
			</ProjectPreview>
			<ProjectCreate @submit="createNewProject" />
		</div>
	</main>
</template>

<style scoped>
.project-list-main {
	height: 100%;
	width: 100%;

	background-color: #fff;
	display: flex;
	flex-direction: column;
	justify-content: flex-start;
}

.pj-list-header {
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	
	height: 10%;
	width: 100%;
	font-size: 20px;
}

.pj-list-container {
	height: 90%;
	width: 100%;

	display: flex;
	flex-wrap: wrap;
	justify-content: flex-start;
	align-content: flex-start;
	align-items: flex-start;
}
</style>
