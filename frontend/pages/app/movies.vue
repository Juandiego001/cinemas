<template>
    <v-container fluid class="fill-height align-start">
        <v-card width="100%" flat>
            <v-card-title>Películas</v-card-title>
            <v-card-text>
                <v-data-table :items="items" :headers="headers" :items-per-page="perPage"
                    @update:itemsPerPage="v => perPage = v">

                    <template v-slot:item.option="{ item }">
                        <v-btn class="my-2 bg-grey-darken-4" icon="mdi-pencil" @click="getMovie(item.id)"></v-btn>
                        <span class="mx-2"></span>
                        <v-btn class="my-2 bg-red" icon="mdi-trash-can"
                            @click="form.id = item.id; deleteDialog = true"></v-btn>
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
                    Create movie
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="createDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="createMovie">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="form.name" hide-details="auto" label="Name"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.durationMinutes" hide-details="auto"
                                label="Duration minutes" type="number"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.classificationAge" hide-details="auto"
                                label="Classification age" type="number"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-select v-model="form.categoryId" hide-details="auto" label="Category"
                                :items="categories" item-title="name" item-value="id"></v-select>
                        </v-col>

                        <v-col cols="12">
                            <v-file-input v-model="form.trailerVideo" :prepend-icon="null" prepend-inner-icon="mdi-paperclip"  label="Trailer video"></v-file-input>
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
                    Update movie
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="updateDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <v-form @submit.prevent="updateMovie">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field v-model="form.name" hide-details="auto" label="Name"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.classificationAge" type="number" hide-details="auto"
                                label="Classification age"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field v-model="form.durationMinutes" type="number" hide-details="auto"
                                label="Duration minutes"></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-select v-model="form.categoryId" hide-details="auto" label="Category"
                                :items="categories" item-title="name" item-value="id"></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-file-input v-model="form.trailerVideo" :prepend-icon="null" prepend-inner-icon="mdi-paperclip"  label="Trailer video"></v-file-input>
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
                    Delete movie
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="deleteDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text class="text-center py-6">
                <p class="text-subtitle-1 mb-6 text-center">¿Are you sure you want to delete the movie?</p>

                <v-btn @click="deleteDialog = false" variant="outlined">Cancel</v-btn>
                <span class="mx-2"></span>
                <v-btn @click="deleteMovie" class="bg-red">Confirm</v-btn>
            </v-card-text>
        </v-card>
    </v-dialog>

    <!-- Search Dialog -->
    <v-dialog v-model="searchDialog" max-width="500">
        <v-card>
            <v-card-title class="bg-grey-darken-4">
                <v-row no-gutters align="center">
                    Search movies
                    <v-spacer></v-spacer>
                    <v-btn class="bg-grey-darken-4" icon="mdi-close" @click="searchDialog = false"></v-btn>
                </v-row>
            </v-card-title>
            <v-card-text>
                <p class="text-subtitle-2 pb-2">Search movies by name</p>
                <v-form @submit.prevent="doSearch">
                    <v-row no-gutters="">
                        <v-col cols="12">
                            <v-text-field v-model="search" label="Name" hide-details="auto"
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
            name: '',
            durationMinutes: 0,
            classificationAge: 0,
            categoryId: '',
            trailerVideo: '',
            status: '',
            created_at: '',
            updated_at: ''
        },
        categories: [],
        updateDialog: false,
        deleteDialog: false
    }),
    computed: {
        headers() {
            return [
                { title: 'Id', key: 'id' },
                { title: 'Movie Name', key: 'name' },
                { title: 'Options', key: 'option', align: 'center' }
            ]
        }
    },
    watch: {
        async perPage(value) { await this.getMovies(); },
        async createDialog(value) {
            if (value) {
                const { items } = await $fetch('/api/categories', {
                    query: { search: '', page: 1, perPage: 15 }
                });
                this.categories = items
            }
        },
        async updateDialog(value) {
            if (value) {
                const { items } = await $fetch('/api/categories', {
                    query: { search: '', page: 1, perPage: 15 }
                });
                this.categories = items
            }
        }
    },
    async beforeMount() { await this.getMovies(); },
    methods: {
        async getMovies() {
            try {
                const { items } = await $fetch('/api/movies/', {
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
        async getMovie(id) {
            try {
                const movie = await $fetch(`/api/movies/${id}`, {
                    method: 'GET'
                })
                this.form = movie
                this.updateDialog = true
            } catch (err) {
                console.log(err)
            }
        },
        async createMovie() {
            try {
                const formData = new FormData()

                formData.append('name', this.form.name)
                formData.append('durationMinutes', this.form.durationMinutes)
                formData.append('classificationAge', this.form.classificationAge)
                formData.append('categoryId', this.form.categoryId)

                if (this.form.trailerVideo) formData.append('trailerVideo', this.form.trailerVideo);

                const response = await $fetch('/api/movies/', {
                    method: 'POST',
                    body: formData
                })
                await this.getMovies()
                this.createDialog = false
            } catch (err) {
                console.log(err)
            }
        },
        async updateMovie() {
            try {
                const formData = new FormData()

                formData.append('id', this.form.id)
                formData.append('name', this.form.name)
                formData.append('durationMinutes', this.form.durationMinutes)
                formData.append('classificationAge', this.form.classificationAge)
                formData.append('categoryId', this.form.categoryId)

                if (this.form.trailerVideo) formData.append('trailerVideo', this.form.trailerVideo);

                const response = await $fetch(`/api/movies/${this.form.id}`, {
                    method: 'PUT',
                    body: formData
                })
                await this.getMovies()
                this.updateDialog = false
            } catch (err) {
                console.log(err)
            }
        },
        async deleteMovie() {
            const response = await $fetch(`/api/movies/${this.form.id}`, {
                method: 'DELETE'
            })
            await this.getMovies()
            this.deleteDialog = false
        },
        async doSearch() {
            try {
                this.page = 1
                this.perPage = 15
                await this.getMovies()
                this.searchDialog = false
            } catch (err) {
                console.log(err)
            }
        }
    }
}
</script>