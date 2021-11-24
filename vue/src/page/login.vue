<template>
  <div class="login_page fillcontain">
    <transition name="form-fade" mode="in-out">
      <section class="form_contianer">
        <div class="manage_tip">
          <p>B站弹幕情感分析系统</p>
        </div>
        <el-form :model="loginForm" :rules="rules" ref="loginForm">
          <el-form-item prop="username">
            <el-input v-model="loginForm.username" placeholder="用户名" />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              type="password"
              placeholder="密码"
              v-model="loginForm.password"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              type="primary"
              @click="handleLogin('loginForm')"
              class="submit_btn"
              >登录</el-button
            >
          </el-form-item>
        </el-form>
      </section>
    </transition>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import { Login } from "@/api/request";

export default {
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" },
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  computed: {
    ...mapState(["userInfo"]),
  },
  // mounted() {
  //   if (!this.userInfo.hasLogin) {
  //     this.userLogin();
  //   }
  // },
  methods: {
    ...mapMutations(["userLogin"]),
    handleLogin(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          Login(this.loginForm)
            .then((response) => {
              // console.log(response.data);
              if (response.data.code != 0) {
                this.$notify.error({
                  title: "错误",
                  message: "请输入正确的用户名密码",
                });
              } else {
                this.$message({
                  type: "success",
                  message: "登录成功！欢迎你，" + this.userInfo.nickname,
                });
                if (!this.userInfo.hasLogin) {
                  this.userLogin();
                }
                this.$router.push("home");
              }
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
.login_page {
  background-color: #324057;
}
.manage_tip {
  position: absolute;
  width: 100%;
  top: -100px;
  left: 0;
  p {
    font-size: 34px;
    color: #fff;
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
