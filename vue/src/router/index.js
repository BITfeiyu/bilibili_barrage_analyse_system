import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const login = (r) =>
  require.ensure([], () => r(require("@/page/login")), "login");
const manage = (r) =>
  require.ensure([], () => r(require("@/page/manage")), "manage");
const home = (r) => require.ensure([], () => r(require("@/page/home")), "home");
const wordCloud = (r) =>
  require.ensure([], () => r(require("@/page/view/wordCloud")), "wordCloud");
const moodAnalyse = (r) =>
  require.ensure(
    [],
    () => r(require("@/page/view/moodAnalyse")),
    "moodAnalyse"
  );

const routes = [
  {
    path: "/",
    component: login,
  },
  {
    path: "/manage",
    component: manage,
    name: "",
    children: [
      {
        path: "",
        component: home,
        meta: ["首页"],
      },
      {
        path: "/home",
        component: home,
        meta: ["提交"],
      },
      {
        path: "/wordCloud",
        component: wordCloud,
        meta: ["词云图"],
      },
      {
        path: "/moodAnalyse",
        component: moodAnalyse,
        meta: ["情感分析"],
      },
    ],
  },
];

export default new Router({
  routes,
  strict: process.env.NODE_ENV !== "production",
});
