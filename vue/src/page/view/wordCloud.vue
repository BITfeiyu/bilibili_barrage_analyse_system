<template>
  <div class="fill-contain">
    <head-top />
    <!-- <el-row>
      <el-col :span="12">
        <el-radio-group v-model="useDefaultPicture">
          <el-radio :label="true">使用默认图片</el-radio>
          <el-radio :label="false">上传图片</el-radio>
        </el-radio-group>

        <el-upload
          class="uploader"
          ref="upload"
          action="#"
          :file-list="fileList"
          :auto-upload="false"
          :v-show="useDefaultPicture"
        >
          <el-button slot="trigger" size="small" type="primary"
            >选取文件</el-button
          >
          <el-button
            style="margin-left: 10px"
            size="small"
            type="success"
            @click="submitUpload"
            >上传文件</el-button
          >
          <div slot="tip" class="el-upload__tip">
            只能上传jpg/png文件，且不超过500kb
          </div>
        </el-upload>
      </el-col>
      <el-col :span="12">
        <p>{{ notify }}</p>
        <img :src="wordcloud_img" />
      </el-col>
    </el-row> -->
    <el-row>
      <el-button type="primary" @click="initialize()">生成词云图</el-button>
    </el-row>
    <el-row>
      <img :src="wordcloud_img" class="display_wordcloud" />
    </el-row>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import { mapState } from "vuex";
import { GetWordCloudImg } from "../../api/request";

export default {
  data() {
    return {
      useDefaultPicture: true,
      fileList: [],
      wordcloud_img: "",
      isloading: false,
    };
  },
  components: {
    headTop,
  },
  computed: {
    ...mapState(["barrage"]),
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit();
    },
    initialize() {
      this.isloading = false;
      if (this.barrage.bv != "" && this.barrage.crawled) {
        this.$message({
          type: "success",
          message: "词云图生成中，请稍候...",
        });
        GetWordCloudImg(this.barrage.bv).then((response) => {
          this.wordcloud_img =
            "data:image/png;base64," +
            window.btoa(
              new Uint8Array(response.data).reduce(
                (data, byte) => data + String.fromCharCode(byte),
                ""
              )
            );
        });
        this.isloading = true;
      } else {
        this.$notify.error({
          title: "错误",
          message: "先爬取弹幕数据",
        });
      }
    },
  },
  // created: function () {
  //   this.initialize();
  // },
};
</script>

<style lang="less" scoped>
@import "../../style/mixin";

.display_wordcloud {
  text-align: center;
  width: 60%;
  height: 45%;
}
</style>
