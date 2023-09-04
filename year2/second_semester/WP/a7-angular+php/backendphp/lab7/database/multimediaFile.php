<?php

class MultimediaFile {

    public $id;
    public $title;
    public $formatType;
    public $genre;
    public $path;

    function __construct ($id, $title,$formatType,$genre, $path) 
    {
        $this -> id = $id;
        $this -> title = $title;
        $this -> formatType = $formatType;
        $this -> genre = $genre;
        $this -> path = $path;
        

    }

    function get_id() {
        return $this->id;
    }

   function set_id( $newId) {
    $this->id = $newId;
   }

   function get_title () {
    return $this->title;
   }

   function set_title( $newTitle) {
    $this->title = $newTitle;
   }
   function get_formatType() {
    return $this->formatType;
    }

    function set_formatType( $newformatType) {
    $this->formatType = $newformatType;
    }

    function get_genre () {
    return $this->genre;
    }
   

    function set_genre( $newgenre) {
    $this->genre = $newgenre;
    }

    function get_path () {
    return $this->path;
    }


    function set_path( $newpath) {
        $this->path = $newpath;
    }
}
    

    
?>
