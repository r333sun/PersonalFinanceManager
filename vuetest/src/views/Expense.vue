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
                    prop="category"
                    label="Category"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="subcategory"
                    label="Sub Category"
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
                    prop="payee"
                    label="Payee"
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
                    <el-dialog title="Edit Expense" :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="Account" :label-width="formLabelWidth">
                                <el-input v-model="form.account" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Category" :label-width="formLabelWidth">
                                <el-cascader :options="options" v-model="form.category"></el-cascader>
                                <el-button type="text" @click="addCategory">Manage Category</el-button>
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
                            <el-form-item label="Payee" :label-width="formLabelWidth">
                                <el-input v-model="form.payee" autocomplete="off"></el-input>
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
                        <el-popconfirm title="Are sure to delete the expense" @onConfirm="deleteRow">
                            <el-button type="text" slot="reference"> Remove
                            </el-button>
                        </el-popconfirm>
                    </template>
                </template>
            </el-table-column>
        </el-table>
        <br>
        <el-button type="addAccount" plain @click="addExpense">Add Expense</el-button>

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
                    category: 'Mortage',
                    subcategory: 'Rent',
                    date: '2020-07-08',
                    amount: '1000',
                    payee:"John Doe",
                    note:'rent for July'
                }, {
                    account: '0001',
                    category: 'Shopping',
                    subcategory: 'Clothes',
                    date: '2020-07-08',
                    amount: '1000',
                    payee:'Mall',
                    note:'Shopping the next season'
                }],
                dialogFormVisible: false,
                form: {
                    account: '',
                    category: '',
                    subcategory:'',
                    date: '',
                    amount: '',
                    payee:'',
                    note:'',
                },
                options: [{
                    value: 'shopping',
                    label: 'Shopping',
                    children: [{
                        value: 'clothes',
                        label: 'Clothes'
                    }, {
                        value: 'daily',
                        label: 'Daily Stuff'
                    }, {
                        value: 'food',
                        label: 'Food'
                    }]
                },
                    {
                        value: 'entertainment',
                        label: 'Entertainment',
                        children: [{
                            value: 'music',
                            label: 'Music'
                        }, {
                            value: 'art',
                            label: 'Art'
                        },]
                    },
                    {
                        value: 'medical',
                        label: 'Medical Care',
                        children: [{
                            value: 'insurrance',
                            label: 'Insurrance'
                        }, {
                            value: 'mishap',
                            label: 'Mishap'
                        },]
                    }],
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
            addExpense() {
                this.$router.push("/addExpense")
            },
            submitForm() {
                this.dialogFormVisible = false;
                this.form.subcategory = this.form.category[1];
                this.form.category = this.form.category[0];
                console.log(this.form);
                alert("Expense Updated");
                this.$router.push("/expense");
            },
            deleteRow(index, rows) {
                //alert("The Account is Deleted!");
                this.$router.push("/expense");
            },
            show() {
                alert("hello")
            },
            addCategory() {
                this.$router.push("/Category");
            }
        },
    };
</script>