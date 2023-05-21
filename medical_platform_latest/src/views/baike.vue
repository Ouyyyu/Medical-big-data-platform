<template>
  <!-- template下总体必须用一个标签封装 -->

  <body>
    <div>
      <!-- el-row：顶端导航栏与项目标志 -->
      <el-row :gutter="5">
        <el-col :span="4">
          <img class="img1" src="../assets/ourlogo.png" height=90px width=250px style="margin:5px;">
        </el-col>
        <el-col :span="8" class="menu">
          <div sytle="display: table-cell;margin: 0 auto;">
            <el-menu :default-active="activeIndex" mode="horizontal" text-color="#409eff">
              <el-menu-item index="1"><a href="#/home"
                  style="font-size: 20px; text-align: center; text-decoration: none;">首页</a>
              </el-menu-item>
              <el-menu-item index="2"><a href="#/person"
                  style="font-size: 20px; text-align: center; text-decoration: none;">个人档案</a>
              </el-menu-item>
              <el-menu-item index="3"><a href="#/chat"
                  style="font-size: 20px; text-align: center; text-decoration: none; ">医疗问诊</a>
              </el-menu-item>
            </el-menu>
          </div>
        </el-col>
        <el-col :span="12"></el-col>
      </el-row>
      <!-- 主题内容：包含侧边栏与内容栏 -->
      <el-container>
        <el-aside width="250px" style="background-color:aliceblue; margin:15px; border-radius: 30px;">
          <h1 class="keshi el-icon-first-aid-kit">科室</h1>
          <el-divider class="divider1"></el-divider>
          <div class="cascader">
            <el-cascader v-model="category" :options="options" :show-all-levels="false"></el-cascader>
          </div>
          <el-button type="primary" plain class="button1" @click="ChangeV">检索</el-button>
          <img src="../assets/zixun.png" width=250px height=180px style="margin-top: 40%;">
        </el-aside>
        <el-main style="background-color:aliceblue; margin:15px; border-radius: 30px;">
          <el-tabs v-model="active" :key="flash">
            <el-tab-pane label="检索" name="jiansuo">
              <div style="text-align:right;">
                <el-pagination layout="prev, pager, next" :total="size" :background="true"
                  @next-click="ChangeV1($event)" @prev-click="ChangeV2($event)" @current-change="ChangeV3($event)">
                </el-pagination>
              </div>
              <div class="arraycard">
                <el-row class="listcard" :gutter="35" v-for="count in 3" :key="count">
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '20px' }" class="wangshihanNB" @click.native="ChangeV4(list[loc][count * 3 - 3].name)" shadow="hover" style="border-radius: 20px">
                      <div>
                        <div class="desc">
                          <span style="font-size: larger;">{{ list[loc][count * 3 - 3].name }}</span>
                        </div>
                        <div style="margin-bottom: 10%; font-size: medium;">
                          <span v-if="list[loc][count * 3 - 3].symptom.split(';').length">
                            <span class="desc1"
                              v-for="count1 in (list[loc][count * 3 - 3].symptom.split(';').length > 3 ? 3 : list[loc][count * 3 - 3].symptom.split(';').length)"
                              :key="count1">
                              <el-tag color="#EFE2F8" size="mini">{{ list[loc][count * 3 - 3].symptom.split(';')[count1
                                  - 1]
                              }}</el-tag>
                            </span>
                          </span>
                          <span v-else>
                            <el-tag type="info" size="mini">暂无</el-tag>
                          </span>
                        </div>
                        <!-- <span class="desc1" v-for="count1 in 3" :key="count1">
                          <span v-if="count1 < list[loc][count * 3 - 3].symptom.split(';').length">
                            <el-tag type="success" size="mini">{{  list[loc][count * 3 - 3].symptom.split(';')[count1 - 1]  }}</el-tag>
                          </span>
                          <span v-else>
                            <el-tag type="info" size="mini">暂无</el-tag>
                          </span>
                        </span> -->
                        <!-- <el-button class="button" type="primary" plain size="mini"
                          @click="ChangeV4(list[loc][count * 3 - 3].name)">详情
                        </el-button> -->
                      </div>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '20px' }" class="wangshihanNB" @click.native="ChangeV4(list[loc][count * 3 - 2].name)" shadow="hover" style="border-radius: 20px">
                      <div>
                        <div class="desc">
                          <span style="font-size:larger;">{{ list[loc][count * 3 - 2].name }}</span>
                        </div>
                        <!-- <div v-if="list[loc][count * 3 - 2].symptom.split(';').length" class="desc1"
                          v-for="count1 in (list[loc][count * 3 - 2].symptom.split(';').length > 3 ? 3 : list[loc][count * 3 - 2].symptom.split(';').length)"
                          :key="count1">
                          {{  list[loc][count * 3 - 2].symptom.split(';')[count1 - 1]  }}
                        </div> -->
                        <div style="margin-bottom: 10%; font-size: medium;">
                          <span v-if="list[loc][count * 3 - 2].symptom.split(';').length">
                            <span class="desc1"
                              v-for="count1 in (list[loc][count * 3 - 2].symptom.split(';').length > 3 ? 3 : list[loc][count * 3 - 2].symptom.split(';').length)"
                              :key="count1">
                              <el-tag color="#FFFAE6" size="mini">{{ list[loc][count * 3 - 2].symptom.split(';')[count1
                                  - 1]
                              }}</el-tag>
                            </span>
                          </span>
                          <span v-else>
                            <el-tag type="info" size="mini">暂无</el-tag>
                          </span>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card :body-style="{ padding: '20px' }" class="wangshihanNB" @click.native="ChangeV4(list[loc][count * 3 - 1].name)" shadow="hover" style="border-radius: 20px">
                      <div>
                        <div class="desc">
                          <span style="font-size:larger;">{{ list[loc][count * 3 - 1].name }}</span>
                        </div>
                        <div style="margin-bottom: 10%; font-size: medium;">
                          <span v-if="list[loc][count * 3 - 1].symptom.split(';').length">
                            <span class="desc1"
                              v-for="count1 in (list[loc][count * 3 - 1].symptom.split(';').length > 3 ? 3 : list[loc][count * 3 - 1].symptom.split(';').length)"
                              :key="count1">
                              <el-tag hit="true" color="white" size="mini">{{ list[loc][count * 3 -
                                  1].symptom.split(';')[count1 - 1]
                              }}</el-tag>
                            </span>
                          </span>
                          <span v-else>
                            <el-tag type="info" size="mini">暂无</el-tag>
                          </span>
                        </div>
                      </div>
                    </el-card>
                  </el-col>
                </el-row>
              </div>
            </el-tab-pane>
            <el-tab-pane label="详情" name="xiangqing">
              <div class="detail" v-if="disease.desc.length">
                <p class="el-icon-notebook-1" style="font-size: 30px;"> {{ disease.name }}</p>
                <p style="line-height: 2em;">{{ disease.desc }}</p>
                <el-divider class="divider"></el-divider>
                <p class="el-icon-notebook-1" style="font-size: 30px;"> 病因与症状</p>
                <br />
                <p class="el-icon-edit-outline" style="font-size: 20px;"> 病因</p>
                <p style="line-height: 2em;">{{ disease.cause }}</p>
                <p class="el-icon-edit-outline" style="font-size: 20px;"> 症状</p>
                <p style="line-height: 2em;">{{ disease.symptom }}</p>
                <el-divider class="divider"></el-divider>
                <p class="el-icon-notebook-1" style="font-size: 30px;"> 预防与药物</p>
                <br />
                <p class="el-icon-edit-outline" style="font-size: 20px;"> 预防</p>
                <p style="line-height: 2em;">{{ disease.prevent }}</p>
                <p class="el-icon-edit-outline" style="font-size: 20px;"> 药物</p>
                <p style="line-height: 2em;">{{ disease.recommand_drug }}</p>
              </div>
              <div v-else>
                <el-empty description="暂无信息>A<"></el-empty>
              </div>
            </el-tab-pane>
          </el-tabs>
        </el-main>
      </el-container>
      <el-backtop :bottom="60"> </el-backtop>
    </div>
  </body>
</template>

<!-- 引入vue和axios依赖 -->
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>

<!-- js部分 -->
<script>
export default {
    name:"baike",
    // 数据区
    data() {
        return {
          size: 50,
          loc: 0,
          active: 'jiansuo',
          flag: 0,
          category: [],
          disease: {desc:''},
          options: [{
          value: '内科',
          label: '内科',
          children: [{
            value: '呼吸内科',
            label: '呼吸内科'
          }, {
            value: '心内科',
            label: '心内科'
          }, {
            value: '神经内科',
            label: '神经内科'
          }, {
            value: '风湿免疫科',
            label: '风湿免疫科'
          }, {
            value: '内分泌科',
            label: '内分泌科'
          }, {
            value: '消化内科',
            label: '消化内科'
          }, {
            value: '血液科',
            label: '血液科'
          }, {
            value: '遗传病科',
            label: '遗传病科'
          }, {
            value: '肾内科',
            label: '肾内科'
          }, {
            value: '泌尿外科',
            label: '泌尿外科'
          }]
        }, {
          value: '儿科',
          label: '儿科',
          children: [{
            value: '小儿内科',
            label: '小儿内科'
          }, {
            value: '儿科综合',
            label: '儿科综合'
          }, {
            value: '小儿外科',
            label: '小儿外科'
          }]
        }, {
            value: '肿瘤科',
            label: '肿瘤科',
            children: [{
            value: '肿瘤内科',
            label: '肿瘤内科'
          }, {
            value: '肿瘤外科',
            label: '肿瘤外科'
          }]
        }, {
            value: '外科',
            label: '外科',
            children: [{
            value: '心胸外科',
            label: '心胸外科'
          }, {
            value: '感染科',
            label: '感染科'
          }, {
            value: '普外科',
            label: '普外科'
          }, {
            value: '肛肠科',
            label: '肛肠科'
          }, {
            value: '肝胆外科',
            label: '肝胆外科'
          }, {
            value: '泌尿外科',
            label: '泌尿外科'
          }, {
            value: '烧伤科',
            label: '烧伤科'
          }, {
            value: '骨外科',
            label: '骨外科'
          }, {
            value: '神经外科',
            label: '神经外科'
          }, {
            value: '整形美容科',
            label: '整形美容科'
          }]
        }, {
            value: '妇产科',
            label: '妇产科',
            children: [{
            value: '产科',
            label: '产科'
          }, {
            value: '妇科',
            label: '妇科'
          }]
        }, {
            value: '五官科',
            label: '五官科',
            children: [{
            value: '眼科',
            label: '眼科'
          }, {
            value: '耳鼻喉科',
            label: '耳鼻喉科'
          }, {
            value: '口腔科',
            label: '口腔科'
          }]
        }, {
            value: '皮肤性病科',
            label: '皮肤性病科',
            children: [{
            value: '皮肤科',
            label: '皮肤科'
          }, {
            value: '性病科',
            label: '性病科'
          }]
        }, {
            value: '中医科',
            label: '中医科',
            children: [{
            value: '中医综合',
            label: '中医综合'
          }]
        }, {
            value: '生殖健康',
            label: '生殖健康',
            children: [{
            value: '不孕不育',
            label: '不孕不育'
          }]
        }, {
            value: '其他科室',
            label: '其他科室',
            children: [{
            value: '其他综合',
            label: '其他综合'
          }, {
            value: '康复科',
            label: '康复科'
          }, {
            value: '减肥',
            label: '减肥'
          }]
        }],
        list: [[{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''},{name:'', symptom:''}]],
        };
    },
    // 响应函数的定义
    methods: {
        ChangeV() {
            this.axios
                .post("http://43.142.181.243/baike/", `category=${this.category[1]}`)
                .then((res) =>{
                    console.log(res.data.data)
                    this.list = res.data.data
                    this.size = this.list.length * 10
                });
        },
        ChangeV1(val) {
          this.loc = val - 1
        },
        ChangeV2(val) {
          this.loc = val - 1
        },
        ChangeV3(val) {
          this.loc = val - 1
        },
        ChangeV4(val) {
          this.axios
              .post("http://43.142.181.243/baike/", `disease=${val}`)
              // .post("http://localhost:8000/baike/", `disease=${val}`)
              .then((res) =>{
                console.log(res.data.data[0])
                this.disease = res.data.data[0]
              })
          this.active = 'xiangqing'
        }
    },
    // 页面渲染时便进行的操作
    mounted(){
      this.category = ['内科', '呼吸内科']
      this.ChangeV()
    }
}
</script>
<!-- css元素样式定义 -->
<style scoped>
.menu {
  margin: 20px;
}

.img1 {
  margin-top: -10px;
}

.keshi.el-icon-first-aid-kit {
  color: black;
  font-family: "PingFang SC";
  font-size: 20px;
  margin-left: 35%;
  margin-right: 35%;
  margin-top: 20%;
}

.wangshihanNB:hover {
  cursor: pointer;
}

.desc {
  margin-top: 0px;
  margin-bottom: 20px;
}

.button {
  float: right;
  margin-bottom: 8px;
  margin-right: -2px;
}

.button1 {
  margin-left: 35%;
  margin-right: 35%;
  margin-top: 20%;
}

.listcard {
  margin-top: 20px;
}

.arraycard {
  padding: 10px;
}

.divider {
  height: 3px;
}

.divider1 {
  height: 10px;
  margin-top: 6%;
}

.cascader {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 20%;
}

.detail {
  margin: 3%;
}

.desc1 {
  font-size: small;
  margin: 2%;
}
</style>
