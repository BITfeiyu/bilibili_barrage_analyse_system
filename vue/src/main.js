import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store/";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import axios from "axios";
// import VueAxios from "vue-axios";
import * as echarts from "echarts";

// 设置网络超时时间
// axios.defaults.timeout = 6*60*1000;

// Vue.prototype.$axios = axios;

new Vue({
  el: "#app",
  router,
  store,
  template: "<App/>",
  components: { App },
});

// Vue.use(axios, VueAxios);
Vue.prototype.$axios = axios;
Vue.prototype.$echarts = echarts;
Vue.use(ElementUI);
