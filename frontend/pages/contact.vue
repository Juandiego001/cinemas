<template>
<v-container fluid class="fill-height justify-center bg-grey-darken-4">
    <v-card max-width="600" class="my-6 pa-6 bg-grey-darken-4" elevation="10">
        <v-card-title class="text-center">
            <p class="text-h4">Contact us</p>
        </v-card-title>
        <v-card-text>
            <p class="my-6">
                Got Questions? We’ve Got Answers!<br /><br />

                Whether you’re curious about our products, need support, or just want to say hello—we’re here for you!
                Drop us a message below, and our team will get back to you as soon as possible. Let’s start
                the conversation!<br /><br />

                💡 Tip: The more details you provide, the better we can assist you.<br /><br />

                We can’t wait to hear from you! 😊
            </p>
            <v-form>
                <v-row>
                    <v-col cols="12">
                        <v-text-field label="Email" hide-details="auto"></v-text-field>
                    </v-col>

                    <v-col cols="12">
                        <v-textarea label="Message" hide-details="auto"></v-textarea>
                    </v-col>

                    <v-col class="text-end" cols="12">
                        <v-btn type="submit" variant="outlined">Send</v-btn>
                    </v-col>
                </v-row>
            </v-form>
        </v-card-text>
    </v-card>
</v-container>
</template>

<script>
export default {

}
</script>
