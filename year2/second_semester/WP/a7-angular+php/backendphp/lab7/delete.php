<?php
use FTP\Connection;


include ('database/connection.php');
session_start();
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $connection = OpenConnection();
    $id = $connection->real_escape_string($_POST['id']);
    $stmt = $connection->prepare("DELETE FROM multimediafile2 WHERE id=?");   
    $stmt->bind_param("i", $id);
    $stmt->execute();
    CloseConnection($connection);
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
<button class="home" type="button" onclick="location.href='./index.html'">HOME</button>
<br>

<section class="display_delete">
    <br>
    <table class="display-table">
        <thead>
            <th>ID</th>
            <th>Title</th>
            <th>Format Type</th>
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
                            <button class='btnDelete' type='button'>Delete</button>
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