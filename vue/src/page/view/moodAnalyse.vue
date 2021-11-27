<template>
  <div class="fill-contain">
    <head-top />
    <el-row>
      <el-button type="primary" @click="initialize()">生成情感分析</el-button>
    </el-row>
    <el-row style="height: 100%">
      <el-col :span="12" style="min-height: 100%">
        <div id="histgram" style="width: 600px; height: 400px"></div>
      </el-col>
      <el-col :span="12" style="height: 100%; overflow: auto">
        <div id="piegram" style="width: 600px; height: 400px"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import { mapState } from "vuex";
import { GetMoodAnalyseResult } from "../../api/request";

export default {
  data() {
    return {
      histgram: {
        // data: null,
        option: {
          title: { text: "情感分析直方图" },
          tooltip: {},
          xAxis: {
            // data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            data: [],
          },
          yAxis: {},
          series: [
            {
              name: "弹幕数量",
              type: "bar",
              data: [],
            },
          ],
        },
      },
      piegram: {
        // data: null,
        option: {
          title: { text: "情感分析饼图" },
          tooltip: {
            trigger: "item",
          },
          legend: {
            top: "5%",
            left: "center",
          },
          series: [
            {
              name: "Emotions",
              type: "pie",
              radius: ["0", "70%"],
              avoidLabelOverlap: false,
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: "40",
                  fontWeight: "bold",
                },
              },
              labelLine: {
                show: false,
              },
              data: [],
            },
          ],
        },
      },
      isloading: false,
    };
  },
  computed: {
    ...mapState(["barrage"]),
  },
  mounted() {
    this.drawHistgram();
    this.drawPiegram();
  },
  methods: {
    initialize() {
      this.isloading = true;
      if (this.barrage.bv != "" && this.barrage.crawled) {
        this.$message({
          type: "success",
          message: "情感分析生成中，请稍候...",
        });
        GetMoodAnalyseResult(this.barrage.bv).then((response) => {
          this.histgram.option.xAxis = response.data.data.hist_data.x;
          this.histgram.option.series[0].data = response.data.data.hist_data.y;
          this.piegram.option.series[0].data = response.data.data.pie_data;
          this.drawHistgram();
          this.drawPiegram();
          console.log(response.data.message);
        });
        this.isloading = false;
      } else {
        this.$notify.error({
          title: "错误",
          message: "先爬取弹幕数据",
        });
      }
    },
    drawHistgram() {
      let histgram = this.$echarts.init(document.getElementById("histgram"));
      histgram.setOption(this.histgram.option);
    },
    drawPiegram() {
      let piegram = this.$echarts.init(document.getElementById("piegram"));
      piegram.setOption(this.piegram.option);
    },
  },
  components: {
    headTop,
  },
  // created: function () {
  //   this.initialize();
  // },
};
</script>
