<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <TITLE>Cerradura electronica</TITLE>
<!--  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> -->
  <link rel="stylesheet" href="/css/bootstrap.min.css">
  <script src="/css/jquery.min.js"></script>
  <script src="/css/bootstrap.min.js"></script>

  <style>
  .carousel-inner > .item > img {
    object-fit: scale-down;
    width: 100%;
      height: 300px;
  }
  .carousel-inner > .item > a > img{
    height: 100%;
      width: 100%;
  } 
  .imagenes{
    width: 50%;
    margin: auto;
}

  </style>
</head>
<body>
<?php 
  include 'conexion.php';
?>
<section class="container">
  <div class="row">
    <header>
      <nav class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
          </div>
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav navbar-text">
              <li>Proyecto de Pepe Molinero</li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
  </div>
</section>
        <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <!-- Indicators -->
          <ol class="carousel-indicators">
            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#myCarousel" data-slide-to="1"></li>
            <li data-target="#myCarousel" data-slide-to="2"></li>
            <li data-target="#myCarousel" data-slide-to="3"></li>
          </ol>

           <!-- Wrapper for slides -->
          <div class="carousel-inner">
            <div class="item active">
              <img src="img/1.jpg">
            </div>
            <div class="item">
              <img src="img/2.jpg">
            </div>
            <div class="item">
              <img src="img/3.jpg">
            </div>
            <div class="item">
              <img src="img/4.jpg">
            </div>
          </div>

          <!-- Left and right controls -->
          <a class="left carousel-control" href="#myCarousel" data-slide="prev">
          <!-- <span class="glyphicon glyphicon-chevron-left"></span> -->
            <span class="sr-only">Previous</span>
          </a>
          <a class="right carousel-control" href="#myCarousel" data-slide="next">
           <!-- <span class="glyphicon glyphicon-chevron-right"></span> -->
            <span class="sr-only">Next</span>
          </a> 
        </div>

<div class='imagenes'>
            <ul class="nav navbar-nav navbar-text">
              <a href="transicion.php"><img width="275px" height="275px" src="img/boton1.png"></a>
            </ul>
            <ul class="nav navbar-nav navbar-text">
              <a href="transicion2.php"><img width="275px" height="275px" src="img/boton2.png"></a>
            </ul>
</div>

</body>
</html>
