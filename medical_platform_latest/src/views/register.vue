<template>
  <header title="注册界面">
    <body id="paper">
      <div class="background">
        <el-form class="login-container" label-position="left" label-width="0px">
          <h3 class="login_title">用户注册</h3>
          <el-form-item>
            <el-input type="text" v-model="loginForm.name" auto-complete="off" placeholder="用户名" rule="^.{6,16}$"
              @inputchange="(res) => (this.username = res)"></el-input>
          </el-form-item>
          <el-form-item>
            <el-radio v-model="loginForm.radio" label=0>男</el-radio>
            <el-radio v-model="loginForm.radio" label=1>女</el-radio>
          </el-form-item>
          <el-form-item>
            <el-input type="password" v-model="loginForm.password" auto-complete="off" placeholder="密码" rule="^.{6,16}$"
              @inputchange="(res) => (this.password = res)"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input type="number" v-model="loginForm.age" auto-complete="off" placeholder="年龄"></el-input>
          </el-form-item>
          <el-form-item>
            <!-- <el-input type="text" v-model="loginForm.province" auto-complete="off" placeholder="省份"></el-input>  -->
            <el-select v-model="loginForm.province" placeholder="请选择省份">
              <el-option v-for="city in loginForm.provinceArr" :label="city.name" :value="city.id" :key="city.id">
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item style="width: 100%">
            <el-button type="primary" style="width: 100%;background: #505458;border: none" v-on:click="register">注册
            </el-button>
          </el-form-item>
          <div style="position: center;text-align: center;width: 100%"><a href="/">已有帐号？登录</a></div>
        </el-form>
      </div>
    </body>
  </header>
</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
export default {
  name: 'register',
  data() {
    return {
      loginForm: {
        provinceArr: '',
        name: '',
        password: '',
        age: '',
        radio: '',
        provinceArr: [{
          id: 1,
          name: '北京'
        },
        {
          id: 2,
          name: '天津'
        },
        {
          id: 3,
          name: '上海'
        },
        {
          id: 4,
          name: '重庆'
        },
        {
          id: 5,
          name: '河南省'
        },
        {
          id: 6,
          name: '云南省'
        },
        {
          id: 7,
          name: '辽宁省'
        },
        {
          id: 8,
          name: '黑龙江省'
        },
        {
          id: 9,
          name: '湖南省'
        },
        {
          id: 10,
          name: '安徽省'
        },
        {
          id: 11,
          name: '山东省'
        },
        {
          id: 12,
          name: '新疆维吾尔自治区'
        },
        {
          id: 13,
          name: '江苏省'
        },
        {
          id: 14,
          name: '浙江省'
        },
        {
          id: 15,
          name: '江西省'
        },
        {
          id: 16,
          name: '湖北省'
        },
        {
          id: 17,
          name: '广西壮族'
        },
        {
          id: 18,
          name: '甘肃省'
        },
        {
          id: 19,
          name: '山西省'
        },
        {
          id: 20,
          name: '内蒙古自治区'
        },
        {
          id: 21,
          name: '陕西省'
        },
        {
          id: 22,
          name: '吉林省'
        },
        {
          id: 23,
          name: '福建省'
        },
        {
          id: 24,
          name: '贵州省'
        },
        {
          id: 25,
          name: '广东省'
        },
        {
          id: 26,
          name: '青海省'
        },
        {
          id: 27,
          name: '西藏'
        },
        {
          id: 28,
          name: '四川省'
        },
        {
          id: 29,
          name: '宁夏回族'
        },
        {
          id: 30,
          name: '海南省'
        },
        {
          id: 31,
          name: '香港特别行政区'
        },
        {
          id: 32,
          name: '澳门特别行政区'
        },
        {
          id: 33,
          name: '台湾省'
        }]
      },
    }
  },
  mounted() {
    document.title = "注册界面"
  },

  methods: {
    register() {
      if (!this.loginForm.name || !this.loginForm.password) {
        alert('请完整填写表单');
      } else {
        this.axios
          .post("http://43.142.181.243/user/register", `username=${this.loginForm.name}&password=${this.loginForm.password}&age=${this.loginForm.age}&province=${this.loginForm.province}&sex=${this.loginForm.radio}`)
          // .post("http://localhost:8000/user/register", `username=${this.loginForm.name}&password=${this.loginForm.password}&age=${this.loginForm.age}&province=${this.loginForm.province}&sex=${this.loginForm.radio}`)
          .then((res) => {
            if (res.status === "200" || res.data.result == 1) {
              this.axios
                .post("http://43.142.181.243/my_archive/create_data", `username=${this.loginForm.name}&password=${this.loginForm.password}&age=${this.loginForm.age}&province=${this.loginForm.province}&sex=${this.loginForm.radio}`)
                // .post("http://localhost:8000/my_archive/create_data", `username=${this.loginForm.name}`)

              // alert('欢迎'+this.loginForm.name+'注册成功');
              this.$alert('注册成功', '提示', {
                confirmButtonText: '确定',
                callback: action => {
                  this.$message({
                    type: 'info',
                    message: `action: ${action}`
                  });
                }
              });
              this.$cookies.set("username", this.loginForm.name, "30MIN");
              this.$cookies.set("sex", this.loginForm.radio, "30MIN");
              this.$router.push("/login");
              // alert("设置了cookie"+this.loginForm.name+"在注册界面")
            } else {
              // alert(JSON.stringify(res.data.message));
              this.$alert('用户名已注册过', '提示', {
                confirmButtonText: '确定',
                callback: action => {
                  this.$message({
                    type: 'info',
                    message: `action: ${action}`
                  });
                }
              });
            }
          });
      }
    },

  }
};
</script>

<style>
body {
  margin: -5px 0px;
}

.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 130px auto;
  margin-bottom: 10px;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}

.login_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}

.background {
  background: url("../assets/专家问诊.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
</style>
