<?php

use FTP\Connection;
session_start();
include ('database/connection.php');
if($_SERVER['REQUEST_METHOD'] == 'POST'){
	$con = OpenConnection();
	if(isset($_POST['add'])){
		/*$bid = $con->real_escape_string($_POST['bid']);*/
		$title = $con->real_escape_string($_POST['title']);
		$formatType = $con->real_escape_string($_POST['formatType']);
		$genre = $con->real_escape_string($_POST['genre']);
		$path = $con->real_escape_string($_POST['path']);
		// $query = "INSERT INTO books VALUES('$bid', '$title', '$author', '$nrPages', '$genre', '$borrowed')";
        // $con->query($query);


		$stmt = $con->prepare("INSERT INTO multimediafile2(id, title, formatType, genre, path) VALUES(?, ?, ?, ?, ?)");
        $stmt->bind_param("issss", $id, $title, $formatType, $genre, $path);
        $stmt->execute();
	}
	CloseConnection($con);
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Files Processing</title>
	<script type="https://code.jquery.com/jquery-3.3.1.js"></script>
	<link rel="stylesheet" type="text/css" href="style.css">
    <script type="text/javascript" src="script.js"></script>
</head>

<body>
<button class="home" type="button" onclick="location.href='./index.html'">HOME </button>
<br>

<section class="add_form">
    <form action="add.php" method="post">
        <!--<input id="bid" type="text" name="bid" placeholder="bid">-->
        <input id="title" type="text" name="title" placeholder="title">
        <input id="formatType" type="text" name="formatType" placeholder="formatType">
        <input id="genre" type="text" name="genre" placeholder="genre">
        <input id="path" type="text" name="path" placeholder="path">
        <input id="add" type="submit" name="add" value="Add new book">
        <!-- <input id="update" type="submit" name="update" value="Update document"> -->
    </form>
</section>

<section class="display_add">
    <br>
    <table class="display-table">
        <thead>
            <!--<th>ID</th>-->
            <th>Title</th>
            <th>Format Type</th>
            <th>Genre</th>
            <th>Path</th>
        </thead>
        <tbody>

            <?php
            $con = OpenConnection();
            $result_set = mysqli_query($con, "SELECT * FROM multimediafile2");
            
            while($row = mysqli_fetch_array($result_set)){
                echo "<tr>";
                /*echo  "<td>" . $row['bid'] . "</td>";*/
                echo  "<td>" . $row['title'] . "</td>";
                echo  "<td>" . $row['formatType'] . "</td>";
                echo  "<td>" . $row['genre'] . "</td>";
                echo  "<td>" . $row['path'] . "</td>";
                echo   "</tr>";
            }
            CloseConnection($con);
            ?>

        </tbody>
    </table>
</section>


<!-- <button class='btnUpdate' id='edit' name='edit' type='button' value= ". $row['id'] . " onclick=\"location.href='./update.php'\">Update</button> -->
</body>

</html>