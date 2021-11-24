import request from "@/utils/request";

/**
 * 登录函数
 */
export function Login(data) {
  return request({
    url: "/user/login",
    method: "post",
    data,
  });
}

/**
 * 登出函数
 */
export function LogOut() {
  return request({
    url: "/user/logout",
    method: "post",
  });
}

/**
 * 向后端发送BV号
 */
export function GetTitleData(data) {
  return request({
    url: "/data/bv",
    method: "post",
    data,
  });
}

/**
 * 向后端请求爬取弹幕数据
 */
export function GetBarrageData(data) {
  return request({
    url: "/data/barrage",
    method: "post",
    data,
  });
}

/**
 * 向后端请求词云图图片
 */
export function GetWordCloudImg(bv) {
  return request({
    url: "/wordcloud",
    method: "post",
    data: {
      bv: bv,
    },
    responseType: "arraybuffer",
  });
}

/**
 * 向后端请求情感分析结果
 */
export function GetMoodAnalyseResult(bv) {
  return request({
    url: "/moodAnalyse",
    method: "post",
    data: {
      bv: bv,
    },
  });
}
