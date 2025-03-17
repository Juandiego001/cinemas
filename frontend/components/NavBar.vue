<template>
    <v-container fluid class="bg-grey-darken-4 py-0 border border-b-lg">
        <v-row no-gutters class="ma-0 py-2">
            <v-col class="d-flex align-center" cols="3">
                <NuxtLink class="text-decoration-none text-white" to="/">CINEMAS</NuxtLink>
            </v-col>

            <v-col class="d-flex align-center justify-center" cols="6">
                <v-btn class="text-none" to="/contact">
                    Contact
                </v-btn>
                <v-btn class="text-none mx-2" to="/movies" variant="text">
                    Movies
                </v-btn>
                <v-btn class="text-none" to="/about" variant="text">
                    About
                </v-btn>
            </v-col>

            <v-col class="text-end" cols="3">
                <v-btn class="text-none" variant="text" to="/login">
                    Log In
                </v-btn>
                <v-btn class="text-none" variant="text" to="/signup">
                    Sign Up
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>