<template>
  <div>
    <div id="bg-penuh" />
    <el-form :model="loginForm" :rules="rules" ref="loginForm" class="form">
      <h1 class="form-heading">登录</h1>
      <el-form-item prop="username">
        <el-input v-model="loginForm.username" placeholder="Username"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input v-model="loginForm.password" show-password placeholder="Password"></el-input>
      </el-form-item>

      <el-button type="primary" @click="loginHandler">登录</el-button>
    </el-form>

  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [{ required: true, trigger: 'blur' }],
        password: [{ required: true, trigger: 'blur' }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      descriptions: [
        {
          icon: 'address-book',
          title: 'ADDRESS BOOK',
          text: 'You can log in to the system and make calls, texts, emails, etc. with your colleagues.',
          path: "/book",
        },
        {
          icon: 'reservation',
          title: 'RESERVATION',
          text: 'You can reserve a meeting room and vehicle in advance, no longer need to enter a name when booking.',
          path: "/reservation",
        },
        {
          icon: 'email',
          title: 'WEB MAIL',
          text: 'You can quickly log in to your web mailbox to send and receive emails, and more.',
          path: "http://mail.netsoft.me",
        }
      ]
    }
  },
  methods: {
    resetForm() {
      this.$refs['loginForm'].resetFields();
    },


    loginHandler() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
              this.loading = false
            })
            .catch((error) => {
              console.error(error);
              this.loading = false
            })
        } else {
          console.error('error submit!!')
        }
      })
    },
  }
}
</script>

<style scoped>
#bg-penuh {
  z-index: -1;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0px;
  box-shadow: rgba(0, 0, 0, 0.498039) 0px 2000px inset;
  background: url("https://unsplash.it/1920/1080/?random") no-repeat center center fixed;
  background-size: cover;
}

.form {
  max-width: 300px;
  margin: 100px auto 10px;
  text-align: center;
}

.form .form-heading {
  text-align: center;
  font-weight: bold;
  color: #fff;
  margin-bottom: 50px;
}
</style>