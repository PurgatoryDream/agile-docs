<script setup lang="ts">
import { useRouter, useRoute } from "vue-router"

const router = useRouter();
const route = useRoute();

function returnHome() {
	router.push("/projects");
}
</script>

<template>
	<div class="navbar-container">
		<div class="navbar-left">
			<div class="navbar-left-elem" @click="returnHome"><span>&#11145;</span></div>
		</div>
		<div class="navbar-right">

		</div>
	</div>
</template>

<style scoped>
.navbar-container {
	height: 3%;
	width: 100%;
	background-color: #37383b;
	box-shadow: 2px 2px 4px black;
	font-size: 20px;

	display: flex;
	justify-content: flex-start;
}

.navbar-left {
	height: 100%;
	width: 50%;

	display: flex;
	justify-content: flex-start;
}

.navbar-left-elem {
	height: 100%;
	width: 5%;

	display: flex;
	justify-content: center;
	align-items: center;
}

.navbar-left-elem:hover {
	background-color: #1f2021;
	cursor: pointer;
}
</style>
