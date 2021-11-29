# bilibili_barrage_analyse_system
 B站弹幕爬取以及情感分析系统

|板块|技术栈|
|:---|:---|
|前端|vue.js; echarts; element-ui|
|后端|flask; jieba; snownlp|

## 部署方法
 1、进入vue文件夹，打开命令行，安装vue所需要的依赖，这可能需要一些时间；安装完成后，vue文件夹下会多一个名为node_modules的依赖包
 ```
 > npm install
 ```
 
 启动vue服务
 ```
 > npm run serve
 ```
 
 打开浏览器进入本地的8080端口，即可看到前端页面
 ```
 localhost:8080
 ```
 
 2、进入flask文件夹，创建一个data文件夹作为默认的数据存储路径
 ```
 > mkdir data
 ```
 
 在命令行创建一个虚拟运行环境，并将其打开，这有助于python项目的封装和包管理
 ```
 > py -3 -m venv venv
 > venv\Scripts\activate
 ```
 
 此外，执行以下命令可以退出虚拟环境
 ```
 (venv)> deactivate
 ```
 
 在虚拟环境下安装python项目需要的依赖，这可能需要一点时间
 ```
 (venv)> pip install -r requirements.txt
 ```
 
 启动后端程序，程序将在flask默认的5050端口运行 (无所谓是否在虚拟环境下执行这条命令)
 ```
 > flask run
 ```
 
 3、登录页面的用户名和密码均为admin
 
 4、这只是笔者初学vue和flask所做的一个测试项目，仅供参考和学习交流使用，如有意见欢迎指出
 
 ## 效果展示
 
 
 ![image](https://user-images.githubusercontent.com/47128987/143800953-16e31d0f-643e-46bd-9ad0-cb779053e447.png)
 ![image](https://user-images.githubusercontent.com/47128987/143800980-4b135509-c5fc-415a-9e31-bd99fae0ec97.png)
 ![image](https://user-images.githubusercontent.com/47128987/143801009-cf8cecbe-16ff-44df-81a0-2b29b8215423.png)
 
