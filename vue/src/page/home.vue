<template>
  <div>
    <head-top></head-top>
    <div class="submit_page fill-contain">
      <transition name="form-fade" mode="in-out">
        <section class="form_contianer">
          <el-form :model="bvForm" :rules="rules" ref="bvForm">
            <el-form-item prop="bv">
              <el-input v-model="bvForm.bv" placeholder="请输入视频BV号" />
            </el-form-item>
            <el-form-item prop="title">
              <el-input
                v-model="bvForm.title"
                :placeholder="bvForm.title"
                :readonly="true"
              />
            </el-form-item>
            <el-form-item>
              <el-button
                type="primary"
                class="submit_btn"
                @click="handleSubmit('bvForm')"
                >检索视频</el-button
              >
            </el-form-item>
            <el-form-item>
              <el-button
                type="primary"
                class="submit_btn"
                @click="crawlBarrage('bvForm')"
                >爬取弹幕</el-button
              >
            </el-form-item>
          </el-form>
        </section>
      </transition>
    </div>
  </div>
</template>

<script>
import headTop from "../components/headTop";
import { mapState, mapMutations } from "vuex";
import { GetTitleData, GetBarrageData } from "@/api/request";

export default {
  data() {
    return {
      bvForm: {
        bv: "",
        title: "显示视频标题",
      },
      rules: {
        bv: [{ required: true, message: "请输入BV号", trigger: "blur" }],
      },
    };
  },
  components: {
    headTop,
  },
  computed: {
    ...mapState(["barrage"]),
  },
  methods: {
    ...mapMutations(["setBVNumber", "setVideoTitle", "setCrawledFlag"]),
    handleSubmit(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          GetTitleData(this.bvForm)
            .then((response) => {
              this.setBVNumber(this.bvForm.bv);
              let title = response.data.data.title;
              this.bvForm.title = title;
              this.setVideoTitle(title);
              console.log(response.data.message);
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },
    crawlBarrage(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          this.$message({
            type: "success",
            message: "正在爬取弹幕数据，请稍候...",
          });
          GetBarrageData(this.bvForm)
            .then((response) => {
              this.setBVNumber(this.bvForm.bv);
              let title = response.data.data.title;
              this.bvForm.title = title;
              this.setVideoTitle(title);
              this.$message({
                type: "success",
                message:
                  "视频" +
                  this.bvForm.bv +
                  "共获得" +
                  response.data.data.leng +
                  "条弹幕数据",
              });
              this.setCrawledFlag(true);
              console.log(response.data.message);
            })
            .catch((error) => {
              console.log(error);
            });
        }
      });
    },
  },
};
</script>

<style lang="less" scoped>
@import "../style/mixin";

.manage_tip {
  position: absolute;
  width: 100%;
  top: -100px;
  left: 0;
  p {
    font-size: 20px;
    color: #000;
  }
}
.form_contianer {
  .wh(320px, 210px);
  .ctp(320px, 210px);
  padding: 25px;
  border-radius: 5px;
  text-align: center;
  background-color: #fff;
  .submit_btn {
    width: 100%;
    font-size: 16px;
  }
}
.form-fade-enter-active,
.form-fade-leave-active {
  transition: all 1s;
}
.form-fade-enter,
.form-fade-leave-active {
  transform: translate3d(0, -50px, 0);
  opacity: 0;
}
</style>
