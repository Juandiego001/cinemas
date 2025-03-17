<template>
<v-container fluid class="fill-height justify-center">
    <template :key="`${i}category`" v-for="category, i  in categories">
        <p class="text-h2">{{ category.name }}</p>
        <div v-for="movies, i in category.movies">
            {{  movies.trailerVideo  }}
            <video v-if="movies.trailerVideo" :src="`http://localhost:5000/api/${movies.trailerVideo}`">
            </video>
        </div>
    </template>
</v-container>
</template>

<script>

export default {
    data: () => ({
      test: '1' ,
      categories: [],
      movies: []
    }),
    async beforeMount () {
        const { items } = await $fetch('/api/categories/', {
            query: {
                search: '',
                page: 1,
                perPage: 15
            }
        })
        console.log('ITEMS: ', items)
        this.categories = items
    },
    watch: {
        async categories (val) {
            for (const category of val) {
                category.movies = await this.getMovies(category.id)
            }
        }
    },
    methods: {
        async getMovies(categoryId) {
            try {
                console.log('CATEGORY ID:_ ', categoryId)
                const { items } = await $fetch(`/api/movies/category/${categoryId}`, {
                    query: {
                        search: '',
                        page: 1,
                        perPage: 15
                    }
                })
                console.log('MOVIES: ');
                console.log(items);
                return items
            } catch (err ) {
                console.log(err)
            }
        }
    }
}
</script>
