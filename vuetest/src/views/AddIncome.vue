<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="Account" prop="account">
                <el-input v-model="ruleForm.account"></el-input>
            </el-form-item>
            <el-form-item label="Source" prop="source">
                <el-input v-model="ruleForm.source"></el-input>
            </el-form-item>
            <el-form-item label="Date" prop="date">
                <!--                <el-input v-model="ruleForm.date"></el-input>-->
                <el-date-picker
                        v-model="ruleForm.date"
                        type="date"
                        placeholder="Pick a day">
                </el-date-picker>
            </el-form-item>
            <el-form-item label="Amount" prop="amount">
                <el-input v-model="ruleForm.amount"></el-input>
            </el-form-item>
            <el-form-item label="Note" prop="note">
                <el-input v-model="ruleForm.note"></el-input>
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
        name: "AddIncome",
        data() {
            return {
                ruleForm: {
                    account: '',
                    source: '',
                    date: '',
                    amount: '',
                    note:'',
                },
                rules: {
                    account: [
                        {required: true, message: 'Please enter the account of the expense', trigger: 'blur'},
                    ],
                    source: [
                        {required: true, message: 'Please enter the source', trigger: 'blur'}
                    ],
                    date: [
                        {required: true, message: 'Please enter the date of the income', trigger: 'change'}
                    ],
                    amount: [
                        {required: true, message: 'Please enter the amount', trigger: 'change'}
                    ],
                    note:[
                        { required: false}
                    ],

                },
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert("Add Successfully!")
                        console.log(this.ruleForm);
                        this.$router.push("/income");

                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
        }
    }
</script>

<style scoped>

</style>