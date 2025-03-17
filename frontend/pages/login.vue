<template>
    <v-container fluid class="fill-height justify-center pa-0 position-relative">
        <v-img width="100%" height="100%" cover class="position-absolute" src="/blade.webp"></v-img>
        <v-card max-width="400" class="bg-transparent px-6 pb-6" elevation="3">
            <v-card-title class="text-center text-h4 text-white py-4">Log In</v-card-title>
            <v-form @submit.prevent="logIn">
                <v-row>
                    <v-col cols="12">
                        <v-text-field class="text-white" v-model="email" label="Email" hide-details="auto" type="email">
                        </v-text-field>
                    </v-col>

                    <v-col cols="12 pb-0">
                        <v-text-field class="text-white" v-model="password" label="Password" hide-details="auto"
                            type="password"></v-text-field>
                    </v-col>

                    <v-col cols="12" class="text-end">
                        <NuxtLink to="/recover-password" class="text-caption text-white text-decoration-none">Forgot
                            password?</NuxtLink>
                    </v-col>

                    <v-col cols="12">
                        <v-btn class="text-white" block variant="outlined" type="submit">
                            Log In
                        </v-btn>
                    </v-col>

                    <v-col class="text-caption text-white text-center pt-0" cols="12">
                        Don't have an account?
                        <NuxtLink to="/signup" class="text-white">Sign up</NuxtLink>
                    </v-col>
                </v-row>
            </v-form>
        </v-card>
    </v-container>
</template>

<script>
definePageMeta({
    layout: 'account'
})

export default {
    data: () => ({
        email: '',
        password: ''
    }),
    methods: {
        async logIn() {
            try {
                console.log({ email: this.email })
                console.log({ password: this.password })
                const response = await $fetch('/api/users/login', {
                    method: 'POST',
                    body: {
                        email: this.email,
                        password: this.password
                    }
                })

                console.log('RESPONSE: ', response)
                if (response.status == 200) navigateTo('/app');
            } catch (err) {
                console.log(err);
            }
        }
    }
}
</script>