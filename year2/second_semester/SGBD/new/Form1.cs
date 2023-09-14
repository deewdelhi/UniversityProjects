using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SGBD_new
{
    public partial class Form1 : Form
    {
        SqlConnection cs = new SqlConnection("Data Source = DESKTOP-85ACGG0\\SQLEXPRESS ; Initial Catalog = SGBD ; Integrated Security = True");

        SqlDataAdapter da = new SqlDataAdapter();

        DataSet ds = new DataSet();

        DataSet ds1 = new DataSet();

        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            da.SelectCommand = new SqlCommand("Select * from DogBreeds", cs);

            ds.Clear();

            da.Fill(ds);

            dataGridView1.DataSource = ds.Tables[0];
        }

        private void dataGridView1_RowHeaderMouseClick(object sender, DataGridViewCellEventArgs e)
        {
          
            da.SelectCommand = new SqlCommand("Select * from Dogs where breed_id=@id", cs);
            if (dataGridView1.SelectedRows.Count > 0)
            {
                int parentId = (int)dataGridView2.SelectedRows[0].Cells["breed_id"].Value;

                da.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = parentId;

                ds1.Clear();

                da.Fill(ds1);

                dataGridView2.DataSource = ds1.Tables[0];
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            da.InsertCommand = new SqlCommand("Insert into Dogs(name,  breed_id) values (@c1,  @id)", cs);
            da.InsertCommand.Parameters.Add("@c1", SqlDbType.VarChar).Value = textBox1.Text.Trim();

            // da.InsertCommand.Parameters.Add("@c2", SqlDbType.Int).Value = numericUDBreedId.Value;

            int id = int.Parse(dataGridView1.SelectedRows[0].Cells[0].Value.ToString());

            da.InsertCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

            cs.Open();

            da.InsertCommand.ExecuteNonQuery();

            MessageBox.Show("Inserted succesfull to the Database");

            cs.Close();

            ds1.Clear();

            da.Fill(ds1);

            dataGridView2.DataSource = ds1.Tables[0];

        }

        private void button3_Click(object sender, EventArgs e)
        {
            da.DeleteCommand = new SqlCommand("Delete from Dogs where dog_id=@id", cs);

            int id = int.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());

            da.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

            cs.Open();

            da.DeleteCommand.ExecuteNonQuery();

            MessageBox.Show("Deleted succesfull from the Database");

            cs.Close();

            ds1.Clear();

            da.Fill(ds1);

            dataGridView2.DataSource = ds1.Tables[0];

        }

        private void button4_Click(object sender, EventArgs e)
        {
            

            da.UpdateCommand = new SqlCommand("Update Dogs set name=@c1 where dog_id=@id", cs);
            da.UpdateCommand.Parameters.Add("@c1", SqlDbType.VarChar).Value = textBox1.Text.Trim();

            // da.UpdateCommand.Parameters.Add("@c2", SqlDbType.Int).Value = numericUpDown1.Value;

            int id = int.Parse(dataGridView2.SelectedRows[0].Cells[0].Value.ToString());

            da.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

            cs.Open();

            da.UpdateCommand.ExecuteNonQuery();

            MessageBox.Show("Updated succesfull to the Database");

            cs.Close();

            ds1.Clear();

            da.Fill(ds1);

            dataGridView2.DataSource = ds1.Tables[0];

        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
