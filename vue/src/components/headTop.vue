<template>
  <div class="header_container">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item v-for="(item, index) in $route.meta" :key="index">
        {{ item }}
      </el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
// import { mapActions, mapState } from "vuex";

export default {
  data() {
    return {
    };
  },
  created() {
    // if (!this.adminInfo.id) {
    //   this.getAdminData();
    // }
  },
  // computed: {
  //   ...mapState(["adminInfo"]),
  // },
  methods: {
    // ...mapActions(["getAdminData"]),
  },
};
</script>

<style lang="less">
@import "../style/mixin";
.header_container {
  background-color: #eff2f7;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 20px;
}
</style>
