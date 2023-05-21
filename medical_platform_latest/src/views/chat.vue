<template>
    <div>
        <el-row :gutter="5">
        <el-col :span="4">
          <img class="img1" src="../assets/logo.jpg" height=90px width=250px style="margin:5px;">
        </el-col>

        <el-col :span="8" class="menu">
          <div sytle="display: table-cell;margin: 0 auto;">
            <el-menu :default-active="activeIndex" mode="horizontal" text-color="#409eff">
              <el-menu-item index="1"><a href="#/home"
                  style="font-size: 20px; text-align: center; text-decoration: none;">首页</a>
              </el-menu-item>
              <el-menu-item index="2"><a href="#/baike"
                  style="font-size: 20px; text-align: center; text-decoration: none; ">医疗百科</a>
              </el-menu-item>
              <el-menu-item index="3"><a href="#/person"
                  style="font-size: 20px; text-align: center; text-decoration: none;">个人档案</a>
              </el-menu-item>
            </el-menu>
          </div>
        </el-col>

        <el-col :span="12"></el-col>
      </el-row>
        <div class="left-page"></div>
        <div class="right-page"></div>
        <div class="container" style="padding-left:30%">
            <div class="list" id="list" ref="list">
                <ul>
                    <li v-for="(item, index) in msglist" :key="index">
                        <RightItem :id="item.id" :type="item.type" :content="item.content" v-if="item.me"></RightItem>
                        <LeftItem :id="item.id" :type="item.type" :content="item.content" v-else></LeftItem>
                        <div v-scroll style="height: 0"></div>
                    </li>
                </ul>
            </div>
            <div class="bottom">
                <div class="line"></div>
                <div class="input-send">
                    <el-form @submit.native.prevent>
                        <el-form-item>
                            <el-input type="text" v-model="text" placeholder="请输入聊天内容..." class="input"
                                @keyup.enter.native="send">
                            </el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button value="发送" v-on:click="send" class="send" plain type="info">发送</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </div>
        </div>
    </div>
</template>
<script></script>
<script>
import Vue from "vue";
    import LeftItem from "@/views/LeftItem";
    import RightItem from "@/views/RightItem";
    Vue.directive('scroll', {
        inserted(el) {
            el.scrollIntoView()
        }
    })
    export default {
        name: "Chat",
        components: {LeftItem, RightItem},
        data: () => {
            return {
                text: '',
                msglist: [{
                    id: 1,
                    type: 1,
                    content: '欢迎你！',
                    me: false
                }]
            }
        },
        methods: {
            send() {
                if (this.text) {
                    this.msglist.push({
                        me: true,
                        id: this.msglist[this.msglist.length - 1].id + 1,
                        type: 0,
                        content: this.text,
                        // me: true
                    })
                    this.axios
                    // .post("http://43.142.181.243/robot/", `question=${this.text}`).then(res => {
                    .post("http://localhost:8000/robot/", `question=${this.text}`).then(res => {
                    console.log(res)
                    this.msglist.push({
                        me: false,
                        id: this.msglist[this.msglist.length - 1].id + 1,
                        type: 1,
                        content: res.data.answer,
                        // me: false
                    })
                    this.text=''
                })
                }
            }
        }
    }
</script>

<style>
    .menu {
  margin: 20px;
}

.img1 {
  margin-top: -10px;
}
.container {
    background: url("../assets/星球.svg.png") no-repeat;
    background-size: cover;
    background-position: center;
}

.container ul {
    padding: 0;
    margin: 0;
}

.container ul li {
    list-style: none;
}

.list {
    width: 40%;
    /* height: 80%; */
    min-height: 530px;
    /* margin-bottom: 0px; */
    list-style: none;
}

.bottom {
    width: 40%;
    /* height: 2%; */
    /* margin-bottom: 0%; */
    /* position:static; */
    margin: 0;
}

.line {
    width: 100%;
    height: 1px;
    margin-bottom: 5px;
    background-color: #ddd;
}

.input-send {
    /* display:flex; */
    justify-content: space-between;
    /* background-color: #fff; */
}

.input {
    /* padding-right: 10px; */
    padding: 0;
    margin: 0;
}

.send {
    /* width: 80px;
    height: 30px;
    margin-top: 7px;
    margin-right: 10px; */
    /* height: 30%; */
    margin: 0;
    margin-right: 10%;
    margin-left: 80%;
}
</style>
