import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  userInfo: {
    hasLogin: false,
    nickname: "管理员",
  },
  barrage: {
    bv: "",
    title: "",
    crawled: false,
    positive: 0,
    negative: 0,
  },
};

const mutations = {
  userLogin(state) {
    state.userInfo.hasLogin = true;
  },
  setBVNumber(state, bv) {
    state.barrage.bv = bv;
  },
  setVideoTitle(state, title) {
    state.barrage.title = title;
  },
  setCrawledFlag(state, flag){
    state.barrage.crawled = flag;
  },
};

export default new Vuex.Store({
  state,
  mutations,
});
