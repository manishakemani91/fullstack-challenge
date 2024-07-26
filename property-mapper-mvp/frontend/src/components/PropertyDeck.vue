<template>
<div class="container mx-auto p-4 relative">
    <div class="p-4">
        <div class="flex items-center space-x-4 mb-4">
            <label for="searchField" class="block text-sm font-medium text-gray-700">
                Search by:
            </label>

            <select id="searchField" v-model="searchField" @change="onCategoryChange" class="block w-1/3 pl-3 pr-10 py-2 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm text-gray-700">
                <option value="full_address">Full Address</option>
                <option value="class_description">Class Description</option>
                <option value="estimated_market_value">Estimated Market Value</option>
                <option value="bldg_use">Building Use</option>
                <option value="building_sq_ft">Building Square Feet</option>
            </select>

            <div class="relative flex-1">
                <input type="text" v-model="searchQuery" placeholder="Search..." @input="onSearch" class="p-2 w-full text-gray-700"></input>
               <v-virtual-scroll ref="virtualScroll" v-if="showScrollList" :items="filteredProperties" class="absolute w-full overflow-auto bg-white border border-gray-300 rounded-md shadow-lg max-h-60" @scroll.native="onScroll">
                    <template v-slot:default="slotProps">
                        <v-list-item @click="selectResult(slotProps.item)">
                            <v-list-item-content>
                                <v-list-item-title class="text-gray-700">{{ slotProps.item[searchField] }}</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                    </template>
                </v-virtual-scroll>
            </div>
        </div>
    </div>

    <l-map :zoom="zoom" :center="[centerLatitude, centerLongitude]" style="height: 500px; width: 100%;">
        <l-tile-layer :url="tireUrl" :attribution="attribution"></l-tile-layer>
        <l-marker v-for="property in matchedProperties" :key="property.id" :lat-lng="[property.latitude, property.longitude]">
            <l-popup>
                <div class="popup-content">
                    <strong>Full Address:</strong> {{ property.full_address }} <br>
                    <strong>Class Description:</strong> {{ property.class_description }} <br>
                    <strong>Estimated Market Value:</strong> {{ property.estimated_market_value }} <br>
                    <strong>Building Use:</strong> {{ property.bldg_use }} <br>
                    <strong>Building Square Feet:</strong> {{ property.building_sq_ft }} <br>
                </div>
            </l-popup>
        </l-marker>
    </l-map>

</div>
</template>

<script>
import axios from "axios";
import {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
} from "@vue-leaflet/vue-leaflet";
import "leaflet/dist/leaflet.css";
import _ from "lodash";
const backendUrl =
    import.meta.env.VITE_API_URL;

export default {
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup,
    },
    data() {
        return {
            properties: [],
            filteredProperties: [],
            matchedProperties: [],
            searchQuery: "",
            uniqueItems: new Set(),
            selectedProperty: null,
            showScrollList: false,
            searchField: "",
            zoom: 13,
            page: 1,
            limit: 20,
            hasMore: true,
            centerLatitude: 41.8857718,
            centerLongitude: -87.6656355,
            tireUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        };
    },
    watch: {
        matchedProperties(newProperties) {
            this.updateMapCenter(newProperties);
        },
    },
    methods: {
        onSearch: _.debounce(async function () {
            this.showScrollList = true;
            if (this.searchQuery.trim() === "") {
                this.showScrollList = false;
                this.filter = [];
                return;
            }
            this.fetchProperties()
        }, 300),

        //to fetch properties 
        async fetchProperties(reset = false) {
            const response = await axios.get(`${backendUrl}/api/autocomplete`, {
                params: {
                    query: this.searchQuery,
                    field: this.searchField,
                    page: this.page,
                    page_size: this.limit,
                },
            });
            this.hasMore = response.data.hasMore;
            this.properties.push(...response.data.results);

            this.filterProperties(this.searchQuery)
            this.page++;
        },
        //handle search record selection
        selectResult(value) {
            this.matchedProperties = this.properties.filter(p => p[this.searchField] === value[this.searchField]);
            this.searchQuery = value[this.searchField]
            this.showScrollList = false;
        },
        //generic function to fetch property records based 
        filterProperties(query) {
            this.uniqueItems.clear();
            if (!query) {
                this.filteredProperties = this.properties.filter(property =>
                    this.uniqueItems.has(property[this.searchField]) ?
                    false :
                    this.uniqueItems.add(property[this.searchField])
                );
            } else {
                this.filteredProperties = (this.searchField === 'estimated_market_value' || this.searchField === 'building_sq_ft') ?
                    (this.properties.filter(property =>
                        property[this.searchField].toString().toLowerCase().includes(query.toString().toLowerCase()) &&
                        (!this.uniqueItems.has(property[this.searchField]) &&
                            this.uniqueItems.add(property[this.searchField])))) :
                    (this.properties.filter(property =>
                        property[this.searchField].toLowerCase().includes(query.toLowerCase()) &&
                        (!this.uniqueItems.has(property[this.searchField]) &&
                            this.uniqueItems.add(property[this.searchField]))
                    ))
            }
        },
        //reset search query when searching field is changed
        onCategoryChange() {
            this.searchQuery = "";
            this.properties = [];
            this.filteredProperties = [];
            this.matchedProperties = [];
            this.page = 1;
            this.hasMore = true;
            this.showScrollList = false;
        },
        //for infintie scroll through list
        onScroll() {
            const scrollEl = this.$refs.virtualScroll.$el;
            if (scrollEl.scrollTop + scrollEl.clientHeight >= scrollEl.scrollHeight - 200) {
                this.fetchProperties()
            }
        },
        //to center map on the properties
        updateMapCenter(properties) {
            if (properties.length === 0) return;

            const latSum = properties.reduce((sum, prop) => sum + prop.latitude, 0);
            const lngSum = properties.reduce((sum, prop) => sum + prop.longitude, 0);

            this.centerLatitude = latSum / properties.length;
            this.centerLongitude = lngSum / properties.length;
        },
    },
};
</script>

<style scoped>
.v-virtual-scroll {
    z-index: 10000
}
</style>
