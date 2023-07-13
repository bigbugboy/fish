<template>
  <div>
    <!-- 头部区域 -->
    <div class="header">
      <img src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" alt="">
    </div>

    <!-- 内容展示区 -->
    <!-- 也就是二级路由(左侧菜单)的出口 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Content',

}
</script>

<style lang="less" scoped>
.header {
  background-color: #1e78bf;
  height: 50px;
  line-height: 50px;
  color: #fff;
  widows: 100%;
  text-align: right;

  img{
    width: 40px;
    height: 40px;
    border-radius: 40px;
    vertical-align: middle;
    margin-right: 10px;
    margin-left: 10px;
  }
}
</style>