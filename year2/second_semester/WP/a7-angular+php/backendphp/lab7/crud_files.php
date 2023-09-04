<?php

use FTP\Connection;

include ('database/connection.php');
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $con = OpenConnection();
    if(isset($_POST['add'])){
        $id = $_POST['id'];
        $title = $_POST['title'];
        $formatType = $_POST['formatType'];
        $numberPages = $_POST['genre'];
        $type = $_POST['path'];
        $query = "INSERT INTO multimediafiles2 VALUES('$id', '$title', '$formatType', '$genre', '$path')";
        $con->query($query);
    }
    else if(isset($_POST['update'])){
        $id = $_POST['id'];
        $title = $_POST['title'];
        $formatType = $_POST['formatType'];
        $genre = $_POST['genre'];
        $path = $_POST['path'];
        $query = "UPDATE document SET title='$title', formatType='$formatType', genre='$genre', path='$path' WHERE id='$id'";
        $con->query($query);
    }

    CloseConnection($con);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Multimedia files Processing </title>
    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
</head>

<body>
<button class="home" type="button" onclick="location.href='./index.html'">HOME </button>
<br>

<section class="add_form">
    <form action="crud_files.php" method="post">
        <input id="id" type="text" name="id" placeholder="id">
        <input id="title" type="text" name="title" placeholder="title">
        <input id="formatType" type="text" name="formatType" placeholder="formatType">
        <input id="genre" type="text" name="genre" placeholder="genre">
        <input id="path" type="text" name="path" placeholder="path">
        <input id="add" type="submit" name="add" value="Add new file">
        <!-- <input id="update" type="submit" name="update" value="Update document"> -->
    </form>
</section>

<section class="update_form">
    <form action="crud_files.php" method="post">
        <input id="id" type="text" name="id" placeholder="id">
        <input id="title" type="text" name="title" placeholder="title">
        <input id="formatType" type="text" name="formatType" placeholder="formatType">
        <input id="genre" type="text" name="genre" placeholder="genre">
        <input id="path" type="text" name="path" placeholder="path">
        <input id="update" type="submit" name="update" value="Update document">
    </form>
</section>

<section class="display">
    <br>
    <table class="display-table">
        <thead>
            <th>ID</th>
            <th>Title</th>
            <th>File Path</th>
            <th>NumberPages</th>
            <th>Type</th>
            <th>Format</th>
            <th> </th>
        </thead>
        <tbody>

            <?php
            $con = OpenConnection();
            $result_set = mysqli_query($con, "SELECT * FROM multimediafiles2");
            
            while($row = mysqli_fetch_array($result_set)){
                echo "<tr>";
                echo  "<td>" . $row['id'] . "</td>";
                echo  "<td>" . $row['title'] . "</td>";
                echo  "<td>" . $row['formatType'] . "</td>";
                echo  "<td>" . $row['genre'] . "</td>";
                echo  "<td>" . $row['path'] . "</td>";
                echo  "<td> 
                            <button class='btnUpdate' type='button'>Update</button>
                            <button class='btnDelete' type='button'>Delete</button>
                      </td>
                      </tr>";
            }
            CloseConnection($con);
            ?>

        </tbody>
    </table>
</section>
</body>
</html>