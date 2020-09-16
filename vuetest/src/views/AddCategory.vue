<template>
    <div>
        <el-table
                :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                style="width: 100%">
            <el-table-column
                    label="Category"
                    prop="category">
            </el-table-column>
            <el-table-column
                    label="Sub Category"
                    prop="subcategory">
            </el-table-column>
            <el-table-column
                    align="right">
                <template slot="header" slot-scope="scope">
                    <el-input
                            v-model="search"
                            size="mini"
                            placeholder="Type to search"/>
                </template>
                <template slot-scope="scope">
                    <el-button
                            size="mini"
                            @click="handleEdit(scope.$index, scope.row)">Edit
                    </el-button>
                    <el-dialog :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="Category" :label-width="formLabelWidth">
                                <el-input v-model="form.category" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Sub Category" :label-width="formLabelWidth">
                                <el-input v-model="form.subcategory" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm">Confirm</el-button>
  </span>
                    </el-dialog>
                    <el-popconfirm title="Are sure to delete the category" @onConfirm="deleteRow">
                        <el-button size="mini" type="danger" slot="reference"> Remove
                        </el-button>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
        <br>
        <el-button @click="addCategory">Add New Category</el-button>
        <el-dialog :visible.sync="dialogForm1Visible">
                        <el-form :model="form1">
                            <el-form-item label="Category" :label-width="formLabelWidth">
                                <el-input v-model="form1.category" autocomplete="off"></el-input>
                            </el-form-item>
                            <el-form-item label="Sub Category" :label-width="formLabelWidth">
                                <el-input v-model="form1.subcategory" autocomplete="off"></el-input>
                            </el-form-item>
                        </el-form>
                        <span slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">Cancel</el-button>
    <el-button type="primary" @click="submitForm1">Confirm</el-button>
  </span>
                    </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "AddCategory",
        data() {
            return {
                tableData: [{
                    category: 'Shopping',
                    subcategory: 'Clothes',
                }, {
                    category: 'Shopping',
                    subcategory: 'Daily',
                }, {
                    category: 'Medical',
                    subcategory: 'Mishap',
                }],
                dialogFormVisible: false,
                dialogForm1Visible: false,
                form: {
                    category: '',
                    subcategory: '',
                },
                form1: {
                    category: '',
                    subcategory: '',
                },
                formLabelWidth: '120px',
                search: '',
            }
        },
        methods: {
            handleEdit(index, row) {
                this.dialogFormVisible = true;
                console.log(index, row);
            },
            handleDelete(index, row) {
                console.log(index, row);
            },
            addCategory() {
                this.dialogForm1Visible = true;
            },
            submitForm() {
                this.dialogFormVisible = false;
                console.log(this.form);
                alert("category updated");
                this.$router.push("/category");
            },
            submitForm1() {
                this.dialogForm1Visible = false;
                console.log(this.form1);
                alert("category added");
                this.$router.push("/category");
            },
            deleteRow(index, rows) {
                 //alert("The Account is Deleted!");
                this.$router.push("/category");
            },
        }
    }
</script>

<style scoped>
</style>