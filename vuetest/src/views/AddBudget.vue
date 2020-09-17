<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="Category" prop="category">
                <el-cascader :options="options" v-model="ruleForm.category"></el-cascader>
                <el-button type="text" @click="addCategory">Manage Category</el-button>
            </el-form-item>
            <el-form-item label="Date" prop="startdate">
                <!--                <el-input v-model="ruleForm.date"></el-input>-->
                  <el-date-picker
                                        v-model="ruleForm.startdate"
                                        type="daterange"
                                        range-separator="To"
                                        start-placeholder="Start date"
                                        end-placeholder="End date">
                                </el-date-picker>
            </el-form-item>
            <el-form-item label="Amount" prop="amount">
                <el-input v-model="ruleForm.amount"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">Submit</el-button>
                <el-button @click="resetForm('ruleForm')">Reset</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "AddExpense",
        data() {
            return {
                ruleForm: {
                    category: '',
                    subcategory:'',
                    startdate: '',
                    enddate:'',
                    amount: '',
                },
                rules: {
                    category: [
                        {required: true, message: 'Please select the category', trigger: 'blur'}
                    ],
                    startdate: [
                        {required: true, message: 'Please enter the date range of the budget', trigger: 'change'}
                    ],
                    amount: [
                        {required: true, message: 'Please enter the amount', trigger: 'change'}
                    ]
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
                    }]
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert("Add Successfully!")
                        this.ruleForm.subcategory = this.ruleForm.category[1];
                        this.ruleForm.category = this.ruleForm.category[0];
                        this.ruleForm.enddate = this.ruleForm.startdate[1];
                        this.ruleForm.startdate = this.ruleForm.startdate[0];
                        console.log(this.ruleForm);
                        this.$router.push("/budget");

                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            addCategory() {
                this.$router.push("/Category");
            }
        }
    }
</script>

<style scoped>

</style>