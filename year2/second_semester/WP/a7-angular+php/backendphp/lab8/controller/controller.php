<?php

header("Access-Control-Allow-Origin: *");

require_once '../model/model.php';
require_once '../view/view.php';

class Controller
{
    private $view;
    private $model;

    public function __construct()
    {
        $this->view = new View();
        $this->model = new Model();
    }

    public function service(){
        if (isset($_GET['action']) && !empty($_GET['action'])){
            if( $_GET['action'] == "selectAllFiles"){
                $this->{$_GET['action']}();
            }
            else if($_GET['action'] == "getTypes"){
                $this->{$_GET['action']}();
            }

            else if($_GET['action'] == "getFilteredFiles"){
                $this->{$_GET['action']}($_GET['type']);
            }
            else if($_GET['action'] == 'addFile'){
                $this->{$_GET['action']}($_GET['title'], $_GET['formatType'], $_GET['genre'], $_GET['path']);
            }
            else if($_GET['action'] == 'deleteFile'){
                $this->{$_GET['action']}($_GET['id']);
            }
            else if($_GET['action'] == 'updateFile'){
                $this->{$_GET['action']}($_GET['id'], $_GET['title'], $_GET['formatType'], $_GET['genre'], $_GET['path']);
            }
           
         
        }
    }


    private function selectAllFiles(){
        $documents = $this->model->selectAllFiles();
        return $this->view->output($documents);
    }

   
    private function getFilteredFiles($type){
        $docs = $this->model->getFilteredFiles($type);
        $this->view->output($docs);
    }



    private function getTypes(){
        $types = $this->model->getTypes();
        $this->view->output($types);
    }

    private function addFile($title, $formatType, $genre, $path){
        $result = $this->model->addFile($title, $formatType, $genre, $path);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Failure";
        }
        $this->view->returnResult($r);
    }

    private function deleteFile($id){
        $result = $this->model->deleteFile($id);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Failure";
        }
        $this->view->returnResult($r);
    }

    private function updateFile($id, $title, $formatType, $genre, $path){ 
        $result = $this->model->updateFile($id, $title, $formatType, $genre, $path);
        if($result > 0){
            $r = "Success";
        }
        else{
            $r = "Failure";
        }
        $this->view->returnResult($r);
        
    }

}

$controller = new Controller();
$controller->service();

?>