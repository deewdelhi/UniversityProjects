<?php

use FTP\Connection;
include ('database/connection.php');
session_start();
if ($_SERVER['REQUEST_METHOD'] == 'POST'){
    $con = OpenConnection();
    if(isset($_POST['update'])){
        // $id = $con->real_escape_string($_POST['id']);
        // $title = $con->real_escape_string($_POST['title']);
        // $author = $con->real_escape_string($_POST['author']);
        // $numberPages = $con->real_escape_string($_POST['numberPages']);
        // $type = $con->real_escape_string($_POST['type']);
        // $format = $con->real_escape_string($_POST['format']);
        $id = $_POST['id'];
        $title = $_POST['title'];
        $formatType = $_POST['formatType'];
        $genre = $_POST['genre'];
        $path = $_POST['path'];
        // $query = mysqli_prepare($con, "UPDATE document SET title=?, author=?, numberPages=?, type=?, format=? WHERE id=?");
        // mysqli_stmt_bind_param($query, "ssissi", $title, $author, $numberPages, $type, $format, $id);
        // mysqli_stmt_execute($query);
        // mysqli_stmt_close($query);
        $stmt = $con->prepare("UPDATE multimediafile2 SET title=?, formatType=?, genre=?, path=? WHERE id=?");
        $stmt->bind_param("ssssi", $title, $formatType, $genre, $path, $id);
        $stmt->execute();
    }

    CloseConnection($con);
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Documents Processing </title>
    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
</head>

<body>
<button class="home" type="button" onclick="location.href='./index.html'">HOME </button>
<br>

<section class="update_form">
    <form action="modify.php" method="post">
        <input id="id" type="text" name="id" placeholder="id">
        <input id="title" type="text" name="title" placeholder="title">
        <input id="formatType" type="text" name="formatType" placeholder="formatType">
        <input id="genre" type="text" name="genre" placeholder="genre">
        <input id="path" type="text" name="path" placeholder="path">
        <input id="update" type="submit" name="update" value="Update document">
    </form>
</section>

<section class="display_modify">
    <br>
    <table class="display-table">
        <thead>
            <th>ID</th>
            <th>Title</th>
            <th>File Type</th>
            <th>Genre</th>
            <th>Path</th>
            <th> </th>
        </thead>
        <tbody>

            <?php
            $con = OpenConnection();
            $result_set = mysqli_query($con, "SELECT * FROM multimediafile2");
            
            while($row = mysqli_fetch_array($result_set)){
                echo "<tr>";
                echo  "<td>" . $row['id'] . "</td>";
                echo  "<td>" . $row['title'] . "</td>";
                echo  "<td>" . $row['formatType'] . "</td>";
                echo  "<td>" . $row['genre'] . "</td>";
                echo  "<td>" . $row['path'] . "</td>";
                echo  "<td> 
                            <button class='btnUpdate' type='button'>Update</button>
                      </td>
                      </tr>";
            }
            CloseConnection($con);
            ?>

        </tbody>
    </table>
</section>


<!-- <button class='btnUpdate' id='edit' name='edit' type='button' value= ". $row['id'] . " onclick=\"location.href='./update.php'\">Update</button> -->
</body>

</html>