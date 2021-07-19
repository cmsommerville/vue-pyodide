import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import LoadScript from "vue-plugin-load-script";

import App from "./App.vue";

// Import Bootstrap an BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);
Vue.use(LoadScript);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
