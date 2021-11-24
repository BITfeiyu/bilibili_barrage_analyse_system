import axios from "axios";
import { baseUrl } from "@/config/env";

// create an axios instance
const service = axios.create({
  baseURL: baseUrl, // url = base url + request url
  timeout: 6 * 60 * 1000, // request timeout
  //   withCredentials: true, // send cookies when cross-domain requests
});

export default service;
