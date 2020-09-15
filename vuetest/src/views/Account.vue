<template>
   <div>
       <el-table :data="tableData">
        <el-table-column prop="date" label="Date" width="140">
        </el-table-column>
        <el-table-column prop="account" label="Account" width="120">
        </el-table-column>

        <el-table-column prop="type" label="Type" width="100">
        </el-table-column>
        <el-table-column prop="amount" label="Amount" width="120">
          <template scope="scope">
          <span v-if="scope.row.amount > 0" style="color: crimson">{{scope.row.amount}}</span>
          <span v-if="scope.row.amount < 0 " style="color: #42b983;">{{scope.row.amount}}</span>
            </template>
          </el-table-column>
        <el-table-column prop="balance" label="Balance">
        </el-table-column>
      </el-table>
       <br>
       <button router>
           back to Main
       </button>
   </div>
</template>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }
</style>

<script>
  export default {
    data() {
      // const item = {
      //   date: '2016-05-02',
      //   account: 'Citi Debit',
      //   type: 'Income',
      //   amount:"1000.0"
      // };
      return {
        tableData: [{
          date: '2016-05-02',
          account: 'Citi Debit',
          type: 'Income',
          amount:"1000.0",
          balance:"2000.0"
        },
        {
          date: '2016-05-02',
          account: 'Citi Debit',
          type: 'Expense',
          amount:"-1000.0",
          balance:"2000.0"
        }]
      }
    }
  };
</script>