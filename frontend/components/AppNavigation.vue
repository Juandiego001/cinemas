<template>
    <v-navigation-drawer v-model="drawer" class="bg-grey-darken-4" location="left">
        <v-list-item>
            <v-list-item-title>
                <NuxtLink to="/" class="text-white text-decoration-none">Cinemas</NuxtLink>
            </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item link to="/app/users" title="Users"></v-list-item>
        <v-list-item link to="/app/groups" title="Groups"></v-list-item>
        <v-list-item link to="/app/categories" title="Categories"></v-list-item>
        <v-list-item link to="/app/movies" title="Movies"></v-list-item>
        <v-list-item link to="/app/rooms" title="Rooms"></v-list-item>
        <v-list-item link to="/app/tickets" title="Tickets"></v-list-item>
        <v-list-item link to="/app/schedules" title="Schedules"></v-list-item>

        <template v-slot:append>
          <div class="pa-2">
            <v-btn class="bg-grey-darken-4" block variant="text" @click="navigateTo('/')">
                <v-icon icon="mdi-logout" class="me-2"></v-icon>
                Logout
            </v-btn>
          </div>
        </template>
    </v-navigation-drawer>

    <v-app-bar color="grey-darken-4">
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Cinemas</v-toolbar-title>
        <v-spacer></v-spacer>
        <template v-if="$vuetify.display.mdAndUp">
            <v-btn icon="mdi-plus" variant="text" @click="createDialog=!createDialog"></v-btn>
            <v-btn icon="mdi-magnify" variant="text" @click="searchDialog=!searchDialog"></v-btn>
        </template>

        <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>
    </v-app-bar>
</template>

<script>
import { toRefs } from 'vue'
import { search } from '~/mixins/search'
import { create } from '~/mixins/create'

export default {
    setup () {
        return {
            ...toRefs(search),
            ...toRefs(create)
        }
    },
    data: () => ({
        drawer: true
    }),
    methods: {
        toggleSearchDialog () {
            console.log('LLEGA AQUI!')
            search.toggle();
        }
    }
}
</script>