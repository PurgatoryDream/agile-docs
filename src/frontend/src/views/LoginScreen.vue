<script setup lang="ts">
</script>

<template>
	<main class="login-main">
		<div class="login-container">
			<div class="login-logo">
				Welcome!
			</div>
			<div class="login-form">
				<div class="login-form-elem">
					<label for="login-email">Email:</label>
					<input type="text" name="login-email" id="login-email" placeholder="example@gmail.com" />
				</div>
				<div class="login-form-elem">
					<label for="login-pass">Password:</label>
					<input type="password" name="login-pass" id="login-pass" />
				</div>
				<div class="login-form-submit">
					<button class="login-button">Submit</button> 
				</div>
			</div>
			<div class="login-footer">
				<div class="login-footer-elem">
					<RouterLink to="/register">Register?</RouterLink>
				</div>
				<div class="login-footer-elem">
					<RouterLink to="/">Forgot?</RouterLink>
				</div>
			</div>
		</div>
	</main>
</template>

<style scoped>
.login-main {
	background-color: #232c4d;
	width: 100%;
	height: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
}

.login-container {
	background-color: #666;
	width: 40%;
	height: 75%;
	border-radius: 5px;
	box-shadow: 1px 1px 8px 4px black;
}

.login-logo {
	width: 100%;
	height: 40%;

	display: flex;
	justify-content: center;
	align-items: center;
}

.login-form {
	width: 100%;
	height: 50%;

	display: flex;
	flex-direction: column;
	justify-content: flex-start;
	align-items: flex-start;
	overflow: auto;
}

.login-form-elem {
	width: 90%;
	height: 20%;
	margin-left: auto;
	margin-right: auto;

	display: flex;
	flex-direction: column;
}

.login-form-elem label {
	font-size: 15px;
}

.login-form-elem input[type=text], .login-form-elem input[type=password] {
	padding: 8px 12px;
	border-radius: 5px;
}

.login-form-submit {
	width: 100%;
	height: 20%;
	margin: auto;

	display: flex;
	flex-direction: column;
}

.login-form-submit button {
	width: 80%;
	height: 50%;
	margin: auto;
	padding: 8px 12px;
	border-radius: 5px;
}

.login-footer {
	width: 100%;
	height: 10%;

	display: flex;
}

.login-footer-elem {
	width: 50%;
	height: 100%;

	display: flex;
	justify-content: center;
	align-items: center;
}

</style>
