<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item label="Account" prop="account">
                <el-input v-model="ruleForm.account"></el-input>
            </el-form-item>
            <el-form-item label="Name" prop="name">
                <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>
            <el-form-item label="Account Type" prop="type">
                <el-select v-model="ruleForm.type" placeholder="Account Type">
                    <el-option label="Debit Card" value="debit"></el-option>
                    <el-option label="Credit Card" value="credit"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="Currency" prop="currency">
                <el-input v-model="ruleForm.currency"></el-input>
            </el-form-item>
            <el-form-item label="Balance" prop="balance">
                <el-input v-model="ruleForm.balance"></el-input>
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
        name: "AddAccount",
        data() {
            return {
                ruleForm: {
                    account: '',
                    name: '',
                    type: '',
                    currency: '',
                    balance: '',
                },
                rules: {
                    account: [
                        {required: true, message: 'Please Enter Your Account Number', trigger: 'blur'},
                    ],
                    name: [
                        {required: true, message: 'Please enter Card Holder\'s Name', trigger: 'blur'}
                    ],
                    type: [
                        {required: true, message: 'Please pick a date', trigger: 'change'}
                    ],
                    currency: [
                        {required: true, message: 'Please pick a time', trigger: 'change'}
                    ],
                    balance: [
                        {required: true, message: 'Please enter your current balance', trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert("Add Successfully!")
                        console.log(this.ruleForm);
                        this.$router.push("/account");

                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style scoped>

</style>