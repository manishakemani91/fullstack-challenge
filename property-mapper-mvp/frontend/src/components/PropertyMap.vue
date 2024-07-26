<template>
  <div id="map" style="height: 500px"></div>
</template>

<script>
import L from "leaflet";
import * as L1 from "leaflet.markercluster";
import { MarkerClusterGroup } from "leaflet.markercluster/src";

export default {
  props: {
    properties: Array,
  },
  mounted() {
    this.initMap();
  },

  methods: {
    initMap() {
      const map = L.map("map").setView([41.8819, -87.6278], 12);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(map);

      const markers = MarkerClusterGroup({ chunkedLoading: true });
      this.properties.forEach((property) => {
        const marker = L.marker([property.latitude, property.longitude]);
        marker.bindPopup(`<b>ID: ${property.id}</b>`);
        markers.addLayer(marker);
      });

      map.addLayer(markers);
    },
  },
};
</script>
