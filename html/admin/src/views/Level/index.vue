<template>
  <div class="container">
    <el-button type="primary">新建</el-button>
    <br>
    <el-table :data="tableData" style="width: 50%">
      <el-table-column prop="id" label="ID" width="180">
      </el-table-column>
      <el-table-column prop="name" label="难度等级" width="180">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data(){
    return {
      tableData: [
        {id: 1, name: '一颗星'}
      ],
    }
  },
  methods: {
    loadData(){

    },
    handleEdit(index, row){},
    handleDelete(index, row){},
  },

}
</script>

<style scoped>
.container {
  height: calc(100vh - 50px);
  padding: 10px
}
</style>