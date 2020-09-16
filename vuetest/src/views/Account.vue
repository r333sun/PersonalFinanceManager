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
                    prop="name"
                    label="Name"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="type"
                    label="Type"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="currency"
                    label="Currency"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="balance"
                    label="Balance"
                    width="150">
            </el-table-column>
            <el-table-column
                    label="Operations"
                    width="200">
                <template slot-scope="scope">
                    <el-button @click="dialogTableVisible = true" type="text">Detail</el-button>
                    <br/>
                    <el-dialog title="Account Details" :visible.sync="dialogTableVisible">
                        <el-table :data="gridData">
                            <el-table-column property="date" label="Date" width="150"></el-table-column>
                            <el-table-column property="type" label="Type" width="200"></el-table-column>
                            <el-table-column property="amount" label="Amount"></el-table-column>
                            <el-table-column property="balance" label="Balance"></el-table-column>
                        </el-table>
                    </el-dialog>
                    <el-button @click="dialogFormVisible = true" type="text"> Edit</el-button>
                    <br/>
                    <el-dialog title="Edit Account" :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="Account" :label-width="formLabelWidth">
                                <el-input v-model="form.account" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Name" :label-width="formLabelWidth">
                                <el-input v-model="form.name" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="type" :label-width="formLabelWidth">
                                <el-select v-model="form.type" placeholder="Please select a type">
                                    <el-option label="Credit" value="credit"></el-option>
                                    <el-option label="Debit" value="Debit"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="currency" :label-width="formLabelWidth">
                                <el-input v-model="form.currency" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm">Confirm</el-button>
  </span>
                    </el-dialog>
                    <template>
                        <el-popconfirm title="Are sure to delete the acccount" @onConfirm="deleteRow">
                            <el-button  type="text" slot="reference"> Remove
                            </el-button>
                        </el-popconfirm>
                    </template>
                </template>
            </el-table-column>
        </el-table>
        <br>
        <el-button type="addAccount" plain @click="addAccount">Add Account</el-button>

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
        data() {
            return {
                tableData: [{
                    account: '0001',
                    name: 'Tom',
                    type: 'credit',
                    currency: 'CNY',
                    balance: '1000',
                }, {
                    account: '0002',
                    name: 'Tom',
                    type: 'Debit',
                    currency: 'GBP',
                    balance: '2000.0',
                    tag: 'Office'
                }],
                gridData: [{
                    date: '2016-05-02',
                    type: 'Income',
                    amount: '100.2',
                    balance: '1420.2'
                }, {
                    date: '2016-05-06',
                    type: 'Income',
                    amount: '100.2',
                    balance: '1550.2'
                }, {
                    date: '2016-04-29',
                    type: 'Expense',
                    amount: '100.2',
                    balance: '170.2'
                }, {
                    date: '2016-03-20',
                    type: 'Income',
                    amount: '160.2',
                    balance: '1770.5'
                },],
                dialogTableVisible: false,
                dialogFormVisible: false,
                form: {
                    account: '',
                    name: '',
                    type: '',
                    currency: '',
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
            addAccount() {
                this.$router.push("/addAccount")
            },
            submitForm() {
                this.dialogFormVisible = false;
                console.log(this.form);
                alert("Account Updated");
                this.$router.push("/account");
            },
            deleteRow(index, rows) {
                // alert("The Account is Deleted!");
                this.$router.push("/account");
            },
            show(){
                alert("hello")
            }
        },
    };
</script>
