<?php

use FTP\Connection;

include ('database/connection.php');
if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
    $con =OpenConnection();
    if(isset($_POST['update'])){
        $id = $_POST['id'];
        $title = $con->real_escape_string($_POST['title']);
        $formatType = $con->real_escape_string($_POST['formatType']);
        $genre = $con->real_escape_string($_POST['genre']);
        $path = $con->real_escape_string($_POST['path']);
        $query = "UPDATE multimediafile2 SET title='$title', formatType='$formatType', genre='$genre', path='$path' WHERE id='$id'";
        // $con->query($query);
    }

    CloseConnection($con);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Files Processing </title>
    <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
<button type="button" onclick="location.href='./index.html'">HOME </button>
<!-- <button type="button" onclick="location.href='./crud_documents.php'">BACK </button> -->
<br>

</body>

<section class="update_form">
    <form class="update" action="update.php" method="post">
        <input id="title" type="text" name="title" placeholder="title" value="<?=$title?>" required/>
        <input id="formatType" type="text" name="formatType" placeholder="formatType" value="<?=$formatType?>" required/>
        <input id="genre" type="text" name="genre" placeholder="genre" value="<?=$genre?>" required/>
        <input id="path" type="text" name="path" placeholder="path" value="<?=$path?>" required/>
        <input id="update" type="submit" name="update" value="Update document">
    </form>
</section>


</html>