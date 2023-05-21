<template>

  <body id="poster">
    <div class="background">
      <el-form class="login-container" label-position="left" label-width="0px">
        <h3 class="login_title">系统登录</h3>
        <el-form-item>
          <el-input type="text" v-model="loginForm.username" auto-complete="on" placeholder="用户名" rule="^.{6,16}$"
            @inputchange="(res) => (this.username = res)"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input type="password" v-model="loginForm.password" auto-complete="off" placeholder="密码" rule="^.{6,16}$"
            @inputchange="(res) => (this.password = res)"></el-input>
        </el-form-item>
        <el-form-item style="width: 100%">
          <el-button type="primary" style="width: 100%; background: #505458; border: none" v-on:click="login">登录
          </el-button>
        </el-form-item>
        <div style="text-align: center"><a href="#/register">注册</a></div>
      </el-form>
      <!-- <div style="text-align: center"><a href="#/register">注册</a></div> -->
    </div>
  </body>
</template>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
      sex: "",
    };
  },
  created() {
    var getcookie = this.$cookies.get("username");
    if (getcookie !== undefined) {
      this.loginForm.username = getcookie;
    }
    // alert('这是'+this.loginForm.username+'的cookie,在登陆页面');
  },
  mounted() {
    document.title = "登录界面"
  },
  methods: {
    login() {
      if (!this.loginForm.username || !this.loginForm.password) {
        alert('请完整填写表单');
      } else {
        this.axios
          .post("http://43.142.181.243/user/login", `username=${this.loginForm.username}&password=${this.loginForm.password}`)
          // .post("http://localhost:8000/user/login", `username=${this.loginForm.username}&password=${this.loginForm.password}`)
          .then((res) => {
            if (res.status === "200" || res.data.result == 1) {
              this.$alert('登陆成功', '提示', {
                confirmButtonText: '确定',
                callback: action => {
                  this.$message({
                    type: 'info',
                    message: `action: ${action}`
                  });
                }
              });
              // alert('欢迎'+this.loginForm.username+'登陆成功');
              this.axios
                .post("http://43.142.181.243/user/get_mess", `user_id=${this.loginForm.username}`)
                .then(res => {
                  this.sex = res.data.sex
                  if (this.sex == '女') {
                    this.$cookies.set("sex", 1, "30MIN");
                  }
                  else {
                    this.$cookies.set("sex", 0, "30MIN");
                  }

                });
              this.$cookies.set("username", this.loginForm.username, "30MIN");
              this.$router.push("/home");
            } else {
              this.$alert('用户名或密码登录错误', '提示', {
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
  },
};
</script>

<style>
body {
  margin: -5px 0px;
}

.background {
  background: url("../assets/专家问诊.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}

.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 290px auto;
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
</style>
