using System.Collections.Generic;
using System.Configuration;
using System.Drawing;
using System;
using System.Windows.Forms;

namespace SGBD
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dgvDogBreeds = new System.Windows.Forms.DataGridView();
            this.dgvDogs = new System.Windows.Forms.DataGridView();
            this.btnPopulateDgvDogBreeds = new System.Windows.Forms.Button();
            this.btnAddDog = new System.Windows.Forms.Button();
            this.btnDeleteDog = new System.Windows.Forms.Button();
            this.btnUpdateDog = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            ((System.ComponentModel.ISupportInitialize)(this.dgvDogBreeds)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvDogs)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvDogBreeds
            // 
            this.dgvDogBreeds.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvDogBreeds.Location = new System.Drawing.Point(12, 12);
            this.dgvDogBreeds.Name = "dgvDogBreeds";
            this.dgvDogBreeds.Size = new System.Drawing.Size(314, 370);
            this.dgvDogBreeds.TabIndex = 0;
            this.dgvDogBreeds.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvDogBreeds_RowHeaderMouseClick);
            // 
            // dgvDogs
            // 
            this.dgvDogs.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvDogs.Location = new System.Drawing.Point(423, 12);
            this.dgvDogs.Name = "dgvDogs";
            this.dgvDogs.Size = new System.Drawing.Size(305, 370);
            this.dgvDogs.TabIndex = 1;
            this.dgvDogs.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvDogs_RowHeaderMouseClick);
            // 
            // btnPopulateDgvDogBreeds
            // 
            this.btnPopulateDgvDogBreeds.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnPopulateDgvDogBreeds.Location = new System.Drawing.Point(118, 403);
            this.btnPopulateDgvDogBreeds.Name = "btnPopulateDgvDogBreeds";
            this.btnPopulateDgvDogBreeds.Size = new System.Drawing.Size(100, 54);
            this.btnPopulateDgvDogBreeds.TabIndex = 2;
            this.btnPopulateDgvDogBreeds.Text = "Populate";
            this.btnPopulateDgvDogBreeds.UseVisualStyleBackColor = true;
            this.btnPopulateDgvDogBreeds.Click += new System.EventHandler(this.btnPopulateDgvDogBreeds_Click);
            // 
            // btnAddDog
            // 
            this.btnAddDog.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAddDog.Location = new System.Drawing.Point(401, 403);
            this.btnAddDog.Name = "btnAddDog";
            this.btnAddDog.Size = new System.Drawing.Size(100, 54);
            this.btnAddDog.TabIndex = 3;
            this.btnAddDog.Text = "Add";
            this.btnAddDog.UseVisualStyleBackColor = true;
            this.btnAddDog.Click += new System.EventHandler(this.btnAddDog_Click);
            // 
            // btnDeleteDog
            // 
            this.btnDeleteDog.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDeleteDog.Location = new System.Drawing.Point(647, 403);
            this.btnDeleteDog.Name = "btnDeleteDog";
            this.btnDeleteDog.Size = new System.Drawing.Size(100, 54);
            this.btnDeleteDog.TabIndex = 4;
            this.btnDeleteDog.Text = "Delete";
            this.btnDeleteDog.UseVisualStyleBackColor = true;
            this.btnDeleteDog.Click += new System.EventHandler(this.btnDeleteDog_Click);
            // 
            // btnUpdateDog
            // 
            this.btnUpdateDog.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnUpdateDog.Location = new System.Drawing.Point(529, 403);
            this.btnUpdateDog.Name = "btnUpdateDog";
            this.btnUpdateDog.Size = new System.Drawing.Size(100, 54);
            this.btnUpdateDog.TabIndex = 5;
            this.btnUpdateDog.Text = "Update";
            this.btnUpdateDog.UseVisualStyleBackColor = true;
            this.btnUpdateDog.Click += new System.EventHandler(this.btnUpdateDog_Click);
            // 
            // panel1
            // 
            this.panel1.Location = new System.Drawing.Point(799, 12);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(335, 370);
            this.panel1.TabIndex = 7;
            // 
            // Form1
            // 
            this.ClientSize = new System.Drawing.Size(1168, 788);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.btnUpdateDog);
            this.Controls.Add(this.btnDeleteDog);
            this.Controls.Add(this.btnAddDog);
            this.Controls.Add(this.btnPopulateDgvDogBreeds);
            this.Controls.Add(this.dgvDogs);
            this.Controls.Add(this.dgvDogBreeds);
            this.Name = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgvDogBreeds)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvDogs)).EndInit();
            this.ResumeLayout(false);

        }


        #endregion

        private System.Windows.Forms.DataGridView dgvDogBreeds;
        private System.Windows.Forms.DataGridView dgvDogs;
        private System.Windows.Forms.Button btnPopulateDgvDogBreeds;
        private System.Windows.Forms.Button btnAddDog;
        private System.Windows.Forms.Button btnDeleteDog;
        private System.Windows.Forms.Button btnUpdateDog;
        private System.Windows.Forms.Panel panel1;
    }
}

