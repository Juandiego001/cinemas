<template>
    <v-container fluid class="fill-height align-start">
        <v-card width="100%" flat>
            <v-card-title>Tickets</v-card-title>
            <v-card-text>
                <v-data-table :items="items" :headers="headers" :items-per-page="perPage"
                    @update:itemsPerPage="v => perPage = v">

                    <template v-slot:item.option="{ item }">
                        <v-btn class="my-2 bg-grey-darken-4" icon="mdi-pencil" @click="getTicket(item.id)"></v-btn>
                        <span class="mx-2"></span>
                        <v-btn class="my-2 bg-red" icon="mdi-trash-can"
                            @click="form.id = item.id; deleteDialog=true"></v-btn>
                    </template>

                </v-data-table>
            </v-card-text>
        </v-card>
    </v-container>

    <!-- Create Dialog -->
    <v-dialog v-model="createDialog" max-width="500">
        <v-card>
            <v-card-title class="bg-grey-darken-4">
                <v-row no-gutters align="center">
                    Create ticket
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="createDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="createTicket">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="form.fullName" hide-details="auto" label="Full name"></v-text-field>
                        </v-col>

                        <v-col class="text-end">
                            <v-btn variant="outlined" @click="updateDialog = false">Cancel</v-btn>
                            <span class="mx-1"></span>
                            <v-btn type="submit" class="bg-grey-darken-4">Create</v-btn>
                        </v-col>
                    </v-row>
                </v-form>

            </v-card-text>
        </v-card>
    </v-dialog>

    <!-- Update Dialog -->
    <v-dialog v-model="updateDialog" max-width="500">
        <v-card>
            <v-card-title class="bg-grey-darken-4">
                <v-row no-gutters align="center">
                    Update ticket
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="updateDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="updateTickets">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="form.fullName" hide-details="auto" label="Full name"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.email" type="email" hide-details="auto"
                                label="Email"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.password" type="password" hide-details="auto"
                                label="Password"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.document" hide-details="auto" label="Document"></v-text-field>
                        </v-col>

                        <v-col class="text-end">
                            <v-btn variant="outlined" @click="updateDialog = false">Cancel</v-btn>
                            <span class="mx-1"></span>
                            <v-btn type="submit" class="bg-grey-darken-4">Update</v-btn>
                        </v-col>
                    </v-row>
                </v-form>

            </v-card-text>
        </v-card>
    </v-dialog>

    <!-- Delete Dialog -->
    <v-dialog v-model="deleteDialog" max-width="500">
        <v-card>
            <v-card-title class="bg-grey-darken-4">
                <v-row no-gutters align="center">
                    Delete ticket
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="deleteDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text class="text-center py-6">
                <p class="text-subtitle-1 mb-6 text-center">¿Are you sure you want to delete the ticket?</p>

                <v-btn @click="deleteDialog = false" variant="outlined">Cancel</v-btn>
                <span class="mx-2"></span>
                <v-btn @click="deleteSchedules" class="bg-red">Confirm</v-btn>
            </v-card-text>
        </v-card>
    </v-dialog>

    <!-- Search Dialog -->
    <v-dialog v-model="searchDialog" max-width="500">
        <v-card>
            <v-card-title class="bg-grey-darken-4">
                <v-row no-gutters align="center">
                    Search ticket
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="searchDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <p class="text-subtitle-2 pb-2">Search ticket by name</p>
                <v-form @submit.prevent="doSearch">
                    <v-row no-gutters="">
                        <v-col cols="12">
                            <v-text-field v-model="search" label="Full name, email, document" hide-details="auto"
                                prepend-inner-icon="mdi-magnify" clearable></v-text-field>
                        </v-col>

                        <v-col class="text-end mt-4" cols="12">
                            <v-btn class="bg-grey-darken-4" type="submit">Search</v-btn>
                        </v-col>

                    </v-row>
                </v-form>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>

<script>
import { toRefs } from 'vue'
import { search } from '~/mixins/search'
import { create } from '~/mixins/create'

definePageMeta({
    layout: 'app'
})

export default {
    setup() {
        return {
            ...toRefs(search),
            ...toRefs(create)
        }
    },
    data: () => ({
        items: [],
        search: '',
        page: 1,
        perPage: 15,
        form: {
            id: '',
            fullName: '',
            email: '',
            password: '',
            document: '',
            status: '',
            created_at: '',
            updated_at: ''
        },
        updateDialog: false,
        deleteDialog: false
    }),
    computed: {
        headers() {
            return [
                { title: 'Id', key: 'id' },
                { title: 'Name', key: 'name' },
                { title: 'Options', key: 'option', align: 'center' }
            ]
        }
    },
    watch: {
        async perPage(value) { await this.getTickets(); }
    },
    async beforeMount() { await this.getTickets(); },
    methods: {
        async getTickets() {
            try {
                const { items } = await $fetch('/api/tickets/', {
                    query: {
                        search: this.search,
                        page: this.page,
                        perPage: this.perPage
                    },
                    method: 'GET'
                })
                this.items = items
            } catch (err) {
                console.log(err)
            }
        },
        async getTicket(id) {
            try {
                const ticket = await $fetch(`/api/tickets/${id}`, {
                    method: 'GET'
                })
                this.form = ticket
                this.updateDialog = true
            } catch (err) {
                console.log(err)
            }
        },
        async createTicket () {
            try {
                const response = await $fetch('/api/tickets/signup', {
                    method: 'POST',
                    body: this.form
                })
                await this.getTickets()
                this.createDialog = false
            } catch (err) {
                console.log(err)
            }
        },
        async updateTickets() {
            try {
                const response = await $fetch(`/api/tickets/${this.form.id}`, {
                    method: 'PUT',
                    body: this.form
                })
                await this.getTickets()
                this.updateDialog = false
            } catch (err) {
                console.log(err)
            }
        },
        async deleteSchedules() {
            const response = await $fetch(`/api/tickets/${this.form.id}`, {
                method: 'DELETE'
            })
            await this.getTickets()
            this.deleteDialog = false
        },
        async doSearch() {
            try {
                this.page = 1
                this.perPage = 15
                await this.getTickets()
                this.searchDialog = false
            } catch (err) {
                console.log(err)
            }
        }
    }
}
</script>