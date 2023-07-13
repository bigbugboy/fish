<template>
  <div class="layout">
    <!-- 左侧导航 -->
    <div class="menu">
      <Menu></Menu>
    </div>
    <!-- 右侧内容 -->
    <div class="content">
      <Content></Content>
    </div>
  </div>
</template>

<script>
import Menu from './Menu'
import Content from './Content'

export default {
  name: 'Layout',
  components: {Menu, Content},

}
</script>

<style lang="less" scoped>
.layout{
  .menu{
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    width: 200px;
    background-color: #112f50;
  }
  .content{
    padding-left: 200px;

  }
}

</style>