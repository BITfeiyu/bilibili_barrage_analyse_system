<template>
  <div class="manage_page fillcontain">
    <el-row style="height: 100%">
      <!-- <el-col :span="4" style="min-height: 100%; background-color: #324057"> -->
      <el-col :span="4" style="min-height: 100%; background-color: #fff">
        <el-menu
          :default-active="defaultActive"
          style="min-height: 100%"
          theme="dark"
          router
        >

          <!--一级目录-->
          <el-menu-item
            v-for="(item, itemIndex) in menu"
            :index="item.name"
            :key="itemIndex"
          >
            <i :class="'el-icon-' + item.icon" />
            <span slot="title">{{ item.label }}</span>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%; overflow: auto">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      menu: [
        {
          name: "manage",
          label: "首页",
          icon: "menu",
        },
        {
          name: "wordCloud",
          label: "词云图",
          icon: "view",
        },
        {
          name: "moodAnalyse",
          label: "情感分析",
          icon: "service",
        },
      ],
    };
  },
  methods: {},
  computed: {
    defaultActive: function () {
      return this.$route.path.replace("/", "");
    },
  },
};
</script>

<style lang="less" scoped>
@import "../style/mixin";
</style>
