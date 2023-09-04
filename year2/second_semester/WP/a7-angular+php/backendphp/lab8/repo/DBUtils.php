<?php

class DBUtils {

    private $host = "127.0.0.1"; //"127.0.0.1";
    private $user = "root";
    private $password = "";
    private $db = "multimediafile_database";
    private $charset = 'utf8';

    private $pdo;
    private $error;

    public function __construct()
    {
        $dsn = "mysql:host=$this->host;dbname=$this->db;charset=$this->charset";
		$opt = array(PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false);
		try {
            $this->pdo = new PDO($dsn, $this->user, $this->password, $opt);		
		} // Catch any errors
		catch(PDOException $e){
            $this->error = $e->getMessage();
			echo "Error connecting to DB: " . $this->error;
		}        
    }
    
    public function selectAllFiles(){
        $stmt = $this->pdo->query("SELECT * FROM multimediafile2");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
    
    public function getFilteredFiles($formatType){
        $stmt = $this->pdo->query("SELECT * FROM multimediafile2 WHERE formatType = '" . $formatType ."' ");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getTypes(){
        $stmt = $this->pdo->query("SELECT DISTINCT formatType FROM multimediafile2");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }


    public function addFile( $title, $formatType, $genre, $path){    
        $affected_rows = $this->pdo->exec("INSERT INTO multimediafile2( id,title, formatType,genre, path) values(NULL,'" . $title . "', '" . $formatType . "', '" . $genre ."', '". $path .  "')");

        return $affected_rows;
    }

    public function deleteFile($id){
        $affected_rows = $this->pdo->exec("DELETE FROM multimediafile2 WHERE id = ". $id ."");
        
        return $affected_rows;
    }

    public function updateFile($id, $title, $formatType, $genre, $path){
        $affected_rows = $this->pdo->exec("UPDATE multimediafile2 SET title = '" . $title . "', formatType = '" . $formatType . "', genre= '" . $genre . "', path = '" . $path .  "' WHERE id = '" . $id . "' ");
   
        return $affected_rows;
    }


}

?>