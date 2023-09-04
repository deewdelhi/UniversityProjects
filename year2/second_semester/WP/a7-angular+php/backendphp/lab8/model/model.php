<?php


require_once '../repo/DBUtils.php';
require_once 'entity/multimediaFile.php';


class Model{
    private $db;
    
    public function __construct()
    {
        $this->db = new DBUtils();
    }
    
    public function selectAllFiles(){
        $resultSet = $this->db->selectAllFiles();
        $all_files = array();
        foreach($resultSet as $key=>$val){
            $file = new MultimediaFile($val['id'], $val['title'], $val['formatType'], $val['genre'], $val['path']);
            array_push($all_files, $file);
        }
        return $all_files;
    }
    public function getTypes()
    {
        $typesSet = $this->db->getTypes();
        $types = array();
        foreach($typesSet as $t){
            array_push($types, $t['formatType']);
        }
        return $types;
    }


    public function getFilteredFiles($type){
        $resultSet = $this->db->getFilteredFiles($type);
        $docs = array();
        foreach($resultSet as $key=>$val){
            $doc = new MultimediaFile($val['id'], $val['title'], $val['formatType'], $val['genre'], $val['path']);
            array_push($docs, $doc);
        }
        return $docs;
    }


    public function addFile( $title, $formatType, $genre, $path){
        return $this->db->addFile($title, $formatType, $genre, $path);
    }

    public function deleteFile($id){
        return $this->db->deleteFile($id);
    }

    public function updateFile($id, $title, $formatType, $genre, $path){
        return $this->db->updateFile($id, $title, $formatType, $genre, $path);
    }

}

?>