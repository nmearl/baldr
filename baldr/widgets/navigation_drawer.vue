<template>
    <v-navigation-drawer
            v-model="drawer"
            :mini-variant.sync="mini"
            app
            fixed
            clipped
    >
        <v-toolbar flat class="transparent">
            <v-list class="pa-0">
                <v-list-tile avatar>
                    <v-list-tile-avatar>
                        <img src="https://randomuser.me/api/portraits/men/85.jpg">
                    </v-list-tile-avatar>

                    <v-list-tile-content>
                        <v-list-tile-title>John Leider</v-list-tile-title>
                    </v-list-tile-content>

                    <v-list-tile-action>
                        <v-btn
                                icon
                                @click.stop="mini = !mini"
                        >
                            <v-icon>chevron_left</v-icon>
                        </v-btn>
                    </v-list-tile-action>
                </v-list-tile>
            </v-list>
        </v-toolbar>

        <v-list class="pt-0">
            <v-list-group prepend-icon='dashboard'>
                <template v-slot:activator>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-list-tile-title>Data</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <v-sheet height="100" v-if="data_items.length == 0">
                    <v-container bg fill-height grid-list-md text-xs-center>
                        <v-layout row wrap align-center>
                            <v-flex>
                                No Data Loaded
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-sheet>

                <template v-for="(item, i) in data_items">
                    <v-list-tile
                            :key="item.title"
                            @click="data_selected(i)"
                            class="highlighted"
                    >
                        <v-list-tile-action>
                            <v-checkbox :value="item.selected"></v-checkbox>
                        </v-list-tile-action>

                        <v-list-tile-content>
                            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                        </v-list-tile-content>

                        <v-list-tile-action>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-tile-action>
                    </v-list-tile>
                </template>
            </v-list-group>

            <v-list-group prepend-icon='dashboard' no-action>
                <template v-slot:activator>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-list-tile-title>Subsets</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <v-sheet height="100" v-if="subset_items.length == 0">
                    <v-container bg fill-height grid-list-md text-xs-center>
                        <v-layout row wrap align-center>
                            <v-flex>
                                No Subsets Loaded
                            </v-flex>
                        </v-layout>
                    </v-container>
                </v-sheet>

                <v-list-tile
                        v-for="item in subset_items"
                        :key="item.title"
                        @click=""
                >
                    <v-list-tile-content>
                        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                    </v-list-tile-content>

                    <v-list-tile-action>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-tile-action>
                </v-list-tile>
            </v-list-group>

            <v-list-group prepend-icon='dashboard' no-action>
                <template v-slot:activator>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-list-tile-title>Layer Options</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <v-card flat>
                    <b-layer-options></b-layer-options>
                </v-card>
            </v-list-group>

            <v-list-group prepend-icon='dashboard' no-action>
                <template v-slot:activator>
                    <v-list-tile>
                        <v-list-tile-content>
                            <v-list-tile-title>Viewer Options</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <b-viewer-options></b-viewer-options>
            </v-list-group>
        </v-list>
    </v-navigation-drawer>
</template>