<template>
    <v-toolbar fixed dark app clipped-left color="primary">
        <v-btn
            outline
            @click="load_data"
            >
            Open
        </v-btn>
        <v-btn outline>
            New
        </v-btn>
        <v-btn outline>
            Save
        </v-btn>

        <v-spacer></v-spacer>
        <v-divider vertical></v-divider>

        <v-overflow-btn
            :items='viewers'
            dark=false
            hide-details
            label="Create viewer..."
            v-model='selected_viewer'
        ></v-overflow-btn>

        <v-divider vertical></v-divider>
        <v-spacer></v-spacer>
        <v-divider vertical></v-divider>

        <v-overflow-btn
            dark=false
            hide-details
            label="Select subset..."
        ></v-overflow-btn>

        <v-divider vertical></v-divider>
        <v-spacer></v-spacer>

        <v-btn icon>
            <v-icon>search</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>apps</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>refresh</v-icon>
        </v-btn>

        <v-btn icon>
            <v-icon>more_vert</v-icon>
        </v-btn>
    </v-toolbar>
</template>
