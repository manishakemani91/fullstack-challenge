import { createApp } from "vue";
import { createPinia } from "pinia";
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(createVuetify({
    components,
    directives,
}));
app.use(router);

app.mount("#app");
