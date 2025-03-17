<template>
    <v-row no-gutters class="bg-grey-darken-4 border border-t-lg">
        <v-col cols="6 pa-4">
            <NuxtLink class="text-white text-decoration-none" to="/">Cinemas</NuxtLink>
        </v-col>

        <v-col class="text-end" cols="6 pa-4">
            <NuxtLink class="text-white text-decoration-none me-4 text-caption" to="/movies">Movies</NuxtLink>
            <NuxtLink class="text-white text-decoration-none me-4 text-caption" to="/contact">Contact</NuxtLink>
            <NuxtLink class="text-white text-decoration-none me-4 text-caption" to="/about">About</NuxtLink>
            <NuxtLink class="text-white text-decoration-none me-4 text-caption" to="/login">Log In</NuxtLink>
            <NuxtLink class="text-white text-decoration-none text-caption" to="/signup">Sign Up</NuxtLink>
        </v-col>

        <v-col cols="12" class="text-center">
            <v-btn class="bg-grey-darken-4" icon="mdi-facebook"></v-btn>
            <v-btn class="bg-grey-darken-4" icon="mdi-twitter"></v-btn>
            <v-btn class="bg-grey-darken-4" icon="mdi-instagram"></v-btn>
            <v-btn class="bg-grey-darken-4 px-0" :icon="true">
                <svg style="width: 24px; height: 24px;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" fill="white">
                    <path d="M448 209.9a210.1 210.1 0 0 1 -122.8-39.3V349.4A162.6 162.6 0 1 1 185 188.3V278.2a74.6 74.6 0 1 0 52.2 71.2V0l88 0a121.2 121.2 0 0 0 1.9 22.2h0A122.2 122.2 0 0 0 381 102.4a121.4 121.4 0 0 0 67 20.1z"/>
                </svg>
            </v-btn>
        </v-col>

        <v-col cols="12" class="text-center mb-3">
            <v-btn class="text-caption" variant="plain" to="/terms">Terms and conditions</v-btn>
            <v-btn class="text-caption" variant="plain" to="/privacy">Privacy policy</v-btn>
        </v-col>

        <v-col cols="12 ma-0 pa-0">
            <v-divider color="white" opacity="0.5"></v-divider>
        </v-col>

        <v-col class="text-center pa-2" cols="12">
            <p class="text-caption">
                With <v-icon icon="mdi-heart"></v-icon>
                from
                <a class="text-white text-decoration-none" href="http://jdcabal.com" target="_blank">jdcabal.com</a>
            </p>
        </v-col>
    </v-row>
</template>

<script>
export default {

}
</script>
