<template>
    <div>
        <el-table
                :data="tableData"
                style="width: 100%">
            <el-table-column
                    fixed
                    prop="account"
                    label="Account"
                    width="150">
            </el-table-column>
            <el-table-column
                    prop="source"
                    label="Source"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="date"
                    label="Date"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="amount"
                    label="Amount"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="note"
                    label="Note"
                    width="120">
            </el-table-column>
            <el-table-column
                    label="Operations"
                    width="200">
                <template slot-scope="scope">
                    <el-button @click="dialogFormVisible = true" type="text"> Edit</el-button>
                    <br/>
                    <el-dialog title="Edit Income" :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="Account" :label-width="formLabelWidth">
                                <el-input v-model="form.account" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Source" :label-width="formLabelWidth">
                                <el-input v-model="form.source" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Date" :label-width="formLabelWidth">
                                <!--                                <el-input v-model="form.date" autocomplete="off"></el-input>-->
                                <el-date-picker
                                        v-model="form.date"
                                        type="date"
                                        placeholder="Pick a day">
                                </el-date-picker>
                            </el-form-item>
                            <el-form-item label="Amount" :label-width="formLabelWidth">
                                <el-input v-model="form.amount" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Note" :label-width="formLabelWidth">
                                <el-input v-model="form.note" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm">Confirm</el-button>
  </span>
                    </el-dialog>
                    <template>
                        <el-popconfirm title="Are sure to delete the income" @onConfirm="deleteRow">
                            <el-button type="text" slot="reference"> Remove
                            </el-button>
                        </el-popconfirm>
                    </template>
                </template>
            </el-table-column>
        </el-table>
        <br>
        <el-button type="addAccount" plain @click="addIncome">Add Income</el-button>

        <el-button type="main" plain @click="backToMain">Back To Main</el-button>
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
        name:"Expense",
        data() {
            return {
                tableData: [{
                    account: '0001',
                    source: 'Income',
                    date: '2020-07-08',
                    amount: '1000',
                    note:"June Salary"
                }, {
                    account: '0001',
                    source: 'Investment',
                    date: '2020-07-08',
                    amount: '1000',
                    note:'Stock'
                }],
                dialogFormVisible: false,
                form: {
                    account: '',
                    amount:'',
                    date:'',
                    source: '',
                    note:'',
                },
                formLabelWidth: '120px',
                search: '',
            }
        },
        methods: {
            backToMain() {
                this.$router.push("/")
            },
            handleClick() {
                console.log('click');
            },
            addIncome() {
                this.$router.push("/addIncome")
            },
            submitForm() {
                this.dialogFormVisible = false;
                console.log(this.form);
                alert("Income Updated");
                this.$router.push("/Income");
            },
            deleteRow(index, rows) {
                //alert("The Account is Deleted!");
                this.$router.push("/Income");
            },
            addCategory() {
                this.$router.push("/Category");
            }
        },
    };
</script>