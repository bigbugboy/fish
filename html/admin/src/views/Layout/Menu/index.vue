<template>
  <!-- 
  el-meunu配置向含义：
    router：让el-menu具有router作用
    default-active： 开启router后，表示路径
    index：开启router后，表示路径    
   -->
  <el-menu default-active="/" router background-color="#112f50" text-color="#fff"
    active-text-color="#ffd04b">

    <el-menu-item index="/">
      <i class="el-icon-menu"></i>
      <span slot="title">首页</span>
    </el-menu-item>

    <el-submenu index="/sc">
      <template slot="title">单项选择</template>
      <el-menu-item index="/sc/published">已发布</el-menu-item>
      <el-menu-item index="/sc/unpublished">待发布</el-menu-item>
    </el-submenu>

    <el-menu-item index="/level">
      <i class="el-icon-menu"></i>
      <span slot="title">难度等级</span>
    </el-menu-item>
    <el-menu-item index="/category">
      <i class="el-icon-document"></i>
      <span slot="title">分类管理</span>
    </el-menu-item>

  </el-menu>
</template>

<script>
export default {
  name: 'Menu',

}
</script>


<style>
.el-menu{
  border-right: none;
}
</style>