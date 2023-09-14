using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;




namespace SGBD
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

        private void tbNameDog_TextChanged(object sender, EventArgs e)
        {

        }

        private void btnPopulateDgvDogBreeds_Click(object sender, EventArgs e)
            
        {

            string command = ConfigurationManager.AppSettings["selectParent"];

            da.SelectCommand = new SqlCommand(command,cs);

            ds.Clear();

            da.Fill(ds);

            dgvDogBreeds.DataSource = ds.Tables[0];

            List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

            int pointX = 30;

            int pointY = 40;

            int numberOfColumns = Convert.ToInt32(ConfigurationManager.AppSettings["ChildNumberOfColumns"]);

            panel1.Controls.Clear();

            foreach (string column in ColumnNames)

            {

                System.Windows.Forms.TextBox a = new System.Windows.Forms.TextBox();

                a.Text = column;

                a.Name = column;

                a.Location = new Point(pointX, pointY);

                a.Visible = true;

                a.Parent = panel1;

                panel1.Show();

                pointY += 30;

            }

        }

        private void dgvDogBreeds_RowHeaderMouseClick(object sender, DataGridViewCellEventArgs e)
        {

            da.SelectCommand = new SqlCommand(ConfigurationManager.AppSettings["selectChild"], cs);

            int id = int.Parse(dgvDogBreeds.SelectedRows[0].Cells[0].Value.ToString());

            da.SelectCommand.Parameters.AddWithValue("@id",id);

            ds1.Clear();

            da.Fill(ds1);

            dgvDogs.DataSource = ds1.Tables[0];

  

        }

        private void dgvDogs_RowHeaderMouseClick(object sender, DataGridViewCellEventArgs e)
        {

            List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

            int id = int.Parse(dgvDogs.CurrentRow.Cells[0].Value.ToString());

            int i = 1;

            foreach (string column in ColumnNames)

            {

                TextBox textBox = (TextBox)panel1.Controls[column];

                textBox.Text = dgvDogs.CurrentRow.Cells[i].Value.ToString();

                i++;

            }

        }

        private void btnAddDog_Click(object sender, EventArgs e)
        {
            

            try

            {

                string ChildTableName = ConfigurationManager.AppSettings["ChildTableName"];

                string ChildColumnNames = ConfigurationManager.AppSettings["ChildColumnNames"];

                List<string> ColumnNamesList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                string InsertQuery = ConfigurationManager.AppSettings["InsertQuery"];
                

                SqlCommand cmd = new SqlCommand(InsertQuery, cs);
                int id = int.Parse(dgvDogBreeds.SelectedRows[0].Cells[0].Value.ToString());


               
                cmd.Parameters.AddWithValue("@id", id);

                foreach (string column in ColumnNamesList)

                {

                    TextBox textbox = (TextBox)panel1.Controls[column];

                    cmd.Parameters.AddWithValue("@" + column, textbox.Text);

                }

                cs.Open();

                cmd.ExecuteNonQuery();

                ds1.Clear();

                da.Fill(ds1);

                dgvDogs.DataSource = ds1.Tables[0];

                MessageBox.Show("Inserted succesfully!");

                cs.Close();

            }

            catch (Exception ex)

            {

                MessageBox.Show(ex.Message);

                cs.Close();

            }
        }

        private void btnUpdateDog_Click(object sender, EventArgs e)
        {

            string ChildTableName = ConfigurationManager.AppSettings["ChildTableName"];

            string ChildColumnNames = ConfigurationManager.AppSettings["ChildColumnNames"];

            List<string> ColumnNamesList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));


            string UpdateQuery = ConfigurationManager.AppSettings["UpdateQuery"];


            SqlCommand cmd = new SqlCommand(UpdateQuery, cs);      

            int id = int.Parse(dgvDogs.SelectedRows[0].Cells[0].Value.ToString());
            cmd.Parameters.AddWithValue("@id", id);

            foreach (string column in ColumnNamesList)

            {

                TextBox textbox = (TextBox)panel1.Controls[column];

                cmd.Parameters.AddWithValue("@" + column, textbox.Text);

            }


            cs.Open();
            cmd.ExecuteNonQuery();

            ds1.Clear();

            da.Fill(ds1);

            dgvDogs.DataSource = ds1.Tables[0];

            MessageBox.Show("Updated succesfull to the Database");

            cs.Close();

        }

        private void btnDeleteDog_Click(object sender, EventArgs e)
        {
            string DeleteQuery = ConfigurationManager.AppSettings["DeleteQuery"];
            da.DeleteCommand = new SqlCommand(DeleteQuery, cs);

            int id = int.Parse(dgvDogs.SelectedRows[0].Cells[0].Value.ToString());

            da.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

            cs.Open();

            da.DeleteCommand.ExecuteNonQuery();

            MessageBox.Show("Deleted succesfull from the Database");

            cs.Close();

            ds1.Clear();

            da.Fill(ds1);

            dgvDogs.DataSource = ds1.Tables[0];


        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
