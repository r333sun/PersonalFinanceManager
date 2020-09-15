<template>
  <div id="app">
  <el-container style="height: 500px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1']">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-menu"></i>Your Actions</template>
          <el-menu-item index="1-1" default-active="true" >Account</el-menu-item>
          <el-menu-item index="1-2">Expenses</el-menu-item>
          <el-menu-item index="1-3">Incomes</el-menu-item>
        <el-menu-item index="1-4">Budget</el-menu-item>
      </el-submenu>
<!--      <el-submenu index="2">-->
<!--        <template slot="title"><i class="el-icon-menu"></i>Navigator Two</template>-->
<!--        <el-menu-item-group>-->
<!--          <template slot="title">Group 1</template>-->
<!--          <el-menu-item index="2-1">Option 1</el-menu-item>-->
<!--          <el-menu-item index="2-2">Option 2</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-menu-item-group title="Group 2">-->
<!--          <el-menu-item index="2-3">Option 3</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-submenu index="2-4">-->
<!--          <template slot="title">Option 4</template>-->
<!--          <el-menu-item index="2-4-1">Option 4-1</el-menu-item>-->
<!--        </el-submenu>-->
<!--      </el-submenu>-->
<!--      <el-submenu index="3">-->
<!--        <template slot="title"><i class="el-icon-setting"></i>Navigator Three</template>-->
<!--        <el-menu-item-group>-->
<!--          <template slot="title">Group 1</template>-->
<!--          <el-menu-item index="3-1">Option 1</el-menu-item>-->
<!--          <el-menu-item index="3-2">Option 2</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-menu-item-group title="Group 2">-->
<!--          <el-menu-item index="3-3">Option 3</el-menu-item>-->
<!--        </el-menu-item-group>-->
<!--        <el-submenu index="3-4">-->
<!--          <template slot="title">Option 4</template>-->
<!--          <el-menu-item index="3-4-1">Option 4-1</el-menu-item>-->
<!--        </el-submenu>-->
<!--      </el-submenu>-->
    </el-menu>
  </el-aside>

  <el-container>
    <el-header style="text-align: left; font-size: 20px">Personal Finance Manager
      <el-dropdown>
<!--        <i class="el-icon-message" style="margin-right: 15px"></i>-->
<!--        <el-dropdown-menu slot="dropdown">-->
<!--          <el-dropdown-item>View</el-dropdown-item>-->
<!--          <el-dropdown-item>Add</el-dropdown-item>-->
<!--          <el-dropdown-item>Delete</el-dropdown-item>-->
<!--        </el-dropdown-menu>-->
      </el-dropdown>
<!--      <span>Tom</span>-->
    </el-header>

    <el-main>
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
    </el-main>
  </el-container>
</el-container>
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
