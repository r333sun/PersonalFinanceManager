<template>
    <div>
        <el-table
                :data="tableData"
                style="width: 100%">
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
                    prop="startdate"
                    label="Start Date"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="enddate"
                    label="End Date"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="amount"
                    label="Amount"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="left"
                    label="Left"
                    width="120">
            </el-table-column>
            <el-table-column
                    label="Operations"
                    width="200">
                <template slot-scope="scope">
                    <el-button @click="dialogFormVisible = true" type="text"> Edit</el-button>
                    <br/>
                    <el-dialog title="Edit Budget" :visible.sync="dialogFormVisible">
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
                                        v-model="form.startdate"
                                        type="daterange"
                                        range-separator="To"
                                        start-placeholder="Start date"
                                        end-placeholder="End date">
                                </el-date-picker>
                            </el-form-item>
                            <el-form-item label="Amount" :label-width="formLabelWidth">
                                <el-input v-model="form.amount" autocomplete="off"></el-input>
                            </el-form-item>

                        </el-form>
                        <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm">Confirm</el-button>
  </span>
                    </el-dialog>
                    <template>
                        <el-popconfirm title="Are sure to delete the budget" @onConfirm="deleteRow">
                            <el-button type="text" slot="reference"> Remove
                            </el-button>
                        </el-popconfirm>
                    </template>
                </template>
            </el-table-column>
        </el-table>
        <br>
        <el-button type="addAccount" plain @click="addBudget">Add Budget</el-button>

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
        name: "budget",
        data() {
            return {
                tableData: [{
                    category: 'Mortage',
                    subcategory: 'Rent',
                    startdate: '2020-07-08',
                    enddate: '2020-09-08',
                    amount: '1000',
                    left:'800',
                }, {
                    category: 'Shopping',
                    subcategory: 'Clothes',
                    startdate: '2020-07-08',
                    enddate: '2020-08-08',
                    amount: '1000',
                    left:'700'
                }],
                dialogFormVisible: false,
                form: {
                    account: '',
                    category: '',
                    subcategory:'',
                    startdate: '',
                    enddate:'',
                    amount: '',
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
            submitForm() {
                this.dialogFormVisible = false;
                this.form.subcategory = this.form.category[1];
                this.form.category = this.form.category[0];
                this.form.enddate = this.form.startdate[1];
                this.form.startdate = this.form.startdate[0];
                console.log(this.form);
                alert("Budget Updated");
                this.$router.push("/budget");
            },
            deleteRow(index, rows) {
                //alert("The Account is Deleted!");
                this.$router.push("/budget");
            },
            show() {
                alert("hello")
            },
            addCategory() {
                this.$router.push("/Category");
            },
            addBudget(){
                this.$router.push("/addBudget");
            }
        },
    };
</script>
<style scoped>

</style>