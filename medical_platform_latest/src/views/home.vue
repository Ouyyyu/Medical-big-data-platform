<template>
    <header>
        <div class="mybackgournd">
            <transition>
                <div ref="breathing_lamp" class="breathing_lamp" @click="onclick()" @touchstart.stop="handleTouchStart"
                    @touchmove.prevent.stop="handleTouchMove($event)" @touchend.stop="handleTouchEnd"
                    :style="{ left: left + 'px', top: top + 'px', width: itemWidth + 'px', height: itemHeight + 'px' }"
                    v-text="text" v-if="isShow"></div>
            </transition>
            <div style="background-color;: #fff">
                <div style="font-size: 50px;font-style: STKaiti;color:#5b9cf9;display: flex">
                    <span class="wenzi2"
                        style="margin-left: 400px;margin-top: 36px;width: 93%;font-style: Microsoft YaHei">欢迎使用春笋健康医疗大数据平台</span>
                    <div v-if="loged" style="margin-top: 30px; margin-right: 40px;">
                        <el-row>
                            <el-col :span="13" style="font-size:20px;color:darksalmon">
                                <img src="../assets/头像-女学生4.png" class="pic" v-if="this.isShow" />
                                <img src="../assets/头像-男学生4.png" class="pic" v-else />
                                {{ this.name }}
                            </el-col>
                            <el-col :span="8">
                                <el-button type="primary" size="small" @click="noLogin">退出登录</el-button>
                            </el-col>
                        </el-row>
                    </div>
                    <div v-else>
                        <el-button type="primary" style="margin-right: 15px;margin-top: 30px" @click="backLogin">登录
                        </el-button>
                    </div>
                </div>
                <el-divider></el-divider>
                <!--走马灯图片展示-->
                <div id="picture" class="div2">
                    <template>
                        <el-carousel :interval="4000" type="card" height="356px" width="434px" ref="carousel"
                            @click.native="linkTo">
                            <el-carousel-item v-for="item in imgUrls" :key="item.urls">
                                <img :src="item.urls" class="image" />
                            </el-carousel-item>
                        </el-carousel>
                    </template>
                </div>
                <div style="margin-bottom: 30px"></div>
                <el-divider>
                </el-divider>
            </div>
            <!--功能选择区-->
            <div class="father" style="margin-top: 50px">
                <el-row>
                    <el-col :span="8">
                        <router-link :to="{ path: './baike', query: { msg: this.username } }">
                            <div class="son1"
                                style="background-color:lightyellow;width: 80%;height: 250px;margin-left: 30px">
                                <div type="text" style="font-size: 24px;color: #293047">
                                    医疗百科
                                </div>
                            </div>
                        </router-link>
                    </el-col>
                    <el-col :span="8">
                        <router-link :to="{ path: './person', query: { msg: this.username } }">
                            <div class="son2"
                                style="background-color: lightskyblue;width: 80%;height: 250px;margin-left: 30px">
                                <div type="text" style="font-size: 24px;color: #293047">
                                    个人档案
                                </div>
                            </div>
                        </router-link>
                    </el-col>
                    <el-col :span="8">
                        <router-link :to="{ path: './chat', query: { msg: this.username } }">
                            <div class="son3"
                                style="background-color: mistyrose;width: 80%;height: 250px;margin-left: 30px">
                                <div type="text" style="font-size: 24px;color: #293047">
                                    医疗问诊
                                </div>
                            </div>
                        </router-link>
                    </el-col>
                </el-row>
            </div>
            <div class="t">
                <el-row>
                    <a href="javascript:void(0)" v-on:click="goAnchor('production')">
                        <el-button v-on:click="s1" type="primary" class="button1" round>
                            <h1>运动</h1>
                        </el-button>
                    </a>
                    <a href="javascript:void(0)" v-on:click="goAnchor('production1')">
                        <el-button v-on:click="s2" type="success" class="button1" round>
                            <h1>健康</h1>
                        </el-button>
                    </a>
                    <a href="javascript:void(0)" v-on:click="goAnchor('production2')">
                        <el-button v-on:click="s3" type="info" class="button1" round>
                            <h1>营养</h1>
                        </el-button>
                    </a>
                    <a href="javascript:void(0)" v-on:click="goAnchor('production3')">
                        <el-button v-on:click="s3" type="primary" class="button1" round>
                            <h1>生活</h1>
                        </el-button>
                    </a>
                </el-row>
            </div>
            <div class="jiange1">
                <div class="con">运动小贴士</div>
            </div>
            <div class="m" id='production'>
                <el-carousel height="356px" direction="vertical" :autoplay="true" @click.native="linkTo1"
                    class="kapian">
                    <el-carousel-item v-for="item in imgs" :key="item">
                        <img :src="item.idView">
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="jiange1">
                <!-- <img src="../assets/熊猫.png" class="cat2"/> -->
                <div class="con">健康小贴士</div>
            </div>
            <div class="m" id='production1'>
                <el-carousel height="356px" width="100px" direction="vertical" :autoplay="true" @click.native="linkTo2"
                    class="kapian">
                    <el-carousel-item v-for="item in imgs2" :key="item">
                        <img :src="item.idView">
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="jiange1">
                <div class="con">营养小贴士</div>
            </div>
            <div class="m" id='production2'>
                <el-carousel height="356px" direction="vertical" :autoplay="true" @click.native="linkTo3"
                    class="kapian">
                    <el-carousel-item v-for="item in imgs3" :key="item">
                        <img :src="item.idView">
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="jiange1">
                <div class="con">生活小贴士</div>
            </div>
            <div class="m" id='production3'>
                <el-carousel height="356px" direction="vertical" :autoplay="true" @click.native="linkTo4"
                    class="kapian">
                    <el-carousel-item v-for="item in imgs4" :key="item.link">
                        <img :src="item.idView">
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="p1">
                <h1 class="wenzi">感谢您使用春笋健康平台！</h1>
                <lottie :options="defaultOptions" :height="350" :width="350" @click="onclick()" class="pp1" />
            </div>
        </div>
    </header>
</template>
<script></script>
<script>
import animationData from '../assets/办公.json';
export default {
    props: {
        // 球名字默认：“球”
        text: {
            type: String,
            default: "知识图谱"
        },
        // 球宽度默认：“40”
        itemWidth: {
            type: Number,
            default: 100
        },
        // 球高度默认：“40”
        itemHeight: {
            type: Number,
            default: 100
        }
    },
    name: "home",
    data() {
        return {
            defaultOptions: { animationData: animationData },
            animationSpeed: 1,
            anim: {},
            isShow: true, // 组件是否显示
            drawer: false,
            direction: 'btt',
            imgUrls: [
                { urls: require('../assets/银发人生.png'), link: '/article2' },
                { urls: require('../assets/无肉不欢.png'), link: '/article3' },
                { urls: require('../assets/少盐.png'), link: '/article' }
            ],
            imgs: [
                { id: 0, idView: require('../assets/浅绿2.png'), link: "/exersie" },
                { id: 1, idView: require('../assets/4-1.png'), link: "/exersie" },
                { id: 2, idView: require('../assets/浅绿1.png'), link: "/exersie" },
                { id: 3, idView: require('../assets/浅绿2.png'), link: "/exersie" }
            ],
            imgs2: [
                { id: 0, idView: require('../assets/4-4.png'), link: "/health" },
                { id: 1, idView: require('../assets/4-2.png'), link: "/health" },
                { id: 2, idView: require('../assets/3-3.png'), link: "/health" },
                { id: 3, idView: require('../assets/4-4.png'), link: "/health" }
            ],
            imgs3: [
                { id: 0, idView: require('../assets/3-4.png'), link: "/yingyang" },
                { id: 1, idView: require('../assets/蓝1.png'), link: "/yingyang" },
                { id: 2, idView: require('../assets/蓝2.png'), link: "/yingyang" },
                { id: 3, idView: require('../assets/3-4.png'), link: "/yingyang" }
            ],
            imgs4: [
                { id: 0, idView: require('../assets/4-3.png'), link: "/life" },
                { id: 1, idView: require('../assets/3-1.png'), link: "/life" },
                { id: 2, idView: require('../assets/3-2.png'), link: "/life" },
                { id: 3, idView: require('../assets/4-3.png'), link: "/life" }
            ],
            imgs5: [
                { id: 0, idView: require('../assets/专家问诊.png') },
                { id: 1, idView: require('../assets/专家问诊.png') },
                { id: 2, idView: require('../assets/个人信息.jpg') },
                { id: 3, idView: require('../assets/专家问诊.png') }
            ],

            //浏览器高度
            screenWidth: 0,
            name: '',
            sex: '',
            isShow: false,
            loged: false,
        }
    },
    created(){
        this.name = this.$cookies.get("username");
        this.sex = this.$cookies.get("sex");
        if (this.sex == 1) { this.isShow = true; }
        if (this.name) { this.loged = true; }
    },
    mounted() {
        document.title = "医疗大数据平台",
            // 首次加载时,需要调用一次
            this.screenWidth = window.innerWidth;
        this.setSize();
        // 窗口大小发生改变时,调用一次
        window.onresize = () => {
            this.screenWidth = window.innerWidth;
            this.setSize();
        }
        // this.name = this.$cookies.get("username");
        // this.sex = this.$cookies.get("sex");
        // if (this.sex == 1) { this.isShow = true; }
        // if (this.name) { this.loged = true; }
    },
    methods: {
        handleAnimation() {
            this.$router.push("./tupu");
        },
        backLogin() {
            this.$router.push("./login");
        },
        linkTo() {
            let activeIndex = this.$refs.carousel.activeIndex
            // window.open(this.imgUrls[activeIndex].link,"_blank")
            this.$router.push(this.imgUrls[activeIndex].link)
        },
        linkTo1() {
            // let activeIndex = this.$refs.carousel.activeIndex
            // window.open(this.imgUrls[activeIndex].link,"_blank")
            this.$router.push("./exerise")
        },
        linkTo2() {
            // let activeIndex = this.$refs.carousel.activeIndex
            // window.open(this.imgUrls[activeIndex].link,"_blank")
            this.$router.push("./health")
        },
        linkTo3() {
            // let activeIndex = this.$refs.carousel.activeIndex
            // window.open(this.imgUrls[activeIndex].link,"_blank")
            this.$router.push("./yingyang")
        },
        linkTo4() {
            // let activeIndex = this.$refs.carousel.activeIndex
            // window.open(this.imgUrls[activeIndex].link,"_blank")
            this.$router.push("./life")
        },
        onclick() {
            this.$router.push("/tupu");
        },
        //下面是自适应框体大小的设置
        setSize: function () {
            // 通过浏览器宽度(图片宽度)实现计算高度
            this.bannerHeight = 400 / 1920 * this.screenWidth;
        },
        noLogin() {
            this.$cookies.remove("username");
            this.$router.go(0);
        },
        s2() {
            imgs: [
                { id: 0, idView: require('../assets/专家问诊.png') },
                { id: 1, idView: require('../assets/专家问诊.png') },
                { id: 2, idView: require('../assets/个人信息.jpg') },
                { id: 3, idView: require('../assets/专家问诊.png') }
            ]

        },
        goAnchor(id) {
            var anchor = document.getElementById(id);
            anchor.scrollIntoView();
        },
    },
}
</script>

<style scoped>
.wenzi2 {
    color: transparent;
    -webkit-text-stroke: 1px #88aeff;
    letter-spacing: 0.01em;
}

.wenzi {
    text-align: center;
    color: transparent;
    -webkit-text-stroke: 1px #FF88C2;
    letter-spacing: 0.04em;
    margin-left: 100px;
}

.p1 {
    margin-right: 80px;
}

.breathing_lamp {
    position: fixed;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background-color: rgb(0, 200, 255);
    background-image: url("../assets/羊招手.png");
    line-height: 90px;
    text-align: center;
    color: rgb(255, 255, 255);
    margin-top: 650px;
}

.pic1 {
    width: 300px;
}

.pic {
    width: 80px;
}

.kapian {
    border-radius: 20px 20px 20px 20px;
}

header {
    background: url("../assets/羊招手.png") right bottom, url("../assets/logo.jpg") left top;
    background-repeat: no-repeat;
    background-attachment: fixed, scroll;
    background-size: 200px, 500px;
}

.jiange1 {
    height: 90px;
    display: flex;
    align-items: center;
    /* position: relative; */
    /* background-color: #799dff00; */
}

.cat2 {
    width: 200px;
}

.con {
    /* position: absolute; */
    /* top: 50%; */
    margin-top: 10px;
    background-color: rgba(215, 236, 250, 0.769);
    width: 400px;
    height: 70px;
    margin: auto;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
    border-bottom-left-radius: 50px;
    border-bottom-right-radius: 50px;
    line-height: 70px;
    font-size: 40px;
    text-align: center;
    margin: auto;
    color: transparent;
    -webkit-text-stroke: 1px #FF88C2;
    letter-spacing: 0.04em;
}

.m {
    margin-top: 100px;
    border-radius: 80px;
    width: 70%;
    height: 70%;
    margin: 0 auto;
}

.t {
    margin-top: 150px;
    margin-left: 240px;
}

.info {
    font-weight: 100;
    text-align: right;
}

.mybackgournd {
    height: 100%;
    padding: 0;
    margin: 0;
    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
}

.button1 {
    height: 100px;
    width: 200px;
    margin-left: 83px;
    /* border-top-left-radius:50px; */

}

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #cad8ff;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #799dff;
}

img {
    /*设置图片宽度和浏览器宽度一致*/
    width: 100%;
    height: inherit;
}

.el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
}

.el-icon-arrow-down {
    font-size: 12px;
}

.demonstration {
    display: block;
    color: #8492a6;
    font-size: 14px;
    margin-bottom: 20px;
}

.father {
    margin-top: 20px;
    width: 100%;
    height: 200px;
    border: none;
    font-size: 0;
    position: static;
    left: 25px;
}

.son1 {
    cursor: pointer;
    background-image: url("../assets/预约疫苗.jpg");
    background-repeat: repeat-y;

    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
    /*边角弧度*/
    border-radius: 10px;
    /*阴影*/
    -moz-box-shadow: 2px 2px 5px #285a63;
    -webkit-box-shadow: 2px 2px 5px #285a63;
    box-shadow: 7px 15px 30px #285a63;
    width: 25%;
    height: 200px;
    display: inline-block;
    *display: inline;
    *zoom: 1;
    text-align: center;
    margin-left: 30px;
    line-height: 150px;
    margin-right: 35px;
    font-size: 24px;
}

.son2 {
    cursor: pointer;
    background-image: url("../assets/个人信息.jpg");
    background-repeat: repeat-y;
    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
    /*边角弧度*/
    border-radius: 10px;
    /*阴影*/
    -moz-box-shadow: 2px 2px 5px #00aaff;
    -webkit-box-shadow: 2px 2px 5px #00aaff;
    box-shadow: 7px 15px 30px #84cdf1;
    /* Safari 和 Chrome */
    width: 25%;
    height: 200px;
    display: inline-block;
    *display: inline;
    *zoom: 1;
    text-align: center;
    line-height: 150px;
    margin-right: 35px;
    font-size: 24px;
}

.son3 {
    cursor: pointer;
    background-image: url("../assets/个人记录.jpg");
    background-repeat: repeat-y;
    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
    /*边角弧度*/
    border-radius: 10px;
    /*阴影*/
    -moz-box-shadow: 2px 2px 5px #b6b1f4;
    -webkit-box-shadow: 2px 2px 5px #b6b1f4;
    box-shadow: 7px 15px 30px #b6b1f4;
    /* Safari 和 Chrome */
    width: 25%;
    height: 200px;
    display: inline-block;
    *display: inline;
    *zoom: 1;
    text-align: center;
    line-height: 150px;
    margin-right: 35px;
    font-size: 24px;
}

.wraper {
    margin-right: -30px;
}

.notification {
    background: none;
    margin-top: 30px;
    position: absolute;
    right: 10px;
}

.notice {
    border-width: 0px;
    border-radius: 3px;
    background: skyblue;
    cursor: pointer;
    outline: none;
    font-family: Microsoft YaHei;
    color: white;
    font-size: 13px;
}

.notice:hover {
    background-color: burlywood;
}

.app {
    margin-top: 60px;
    position: absolute;
    right: 10px;
}
</style>
