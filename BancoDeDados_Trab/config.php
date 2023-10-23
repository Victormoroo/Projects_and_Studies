<?php

$host = "localhost"; // nome do servidor MySQL
$user = "id20421005_victormoro"; // usuário do MySQL
$pass = "6Um/!(=<^O4^aQsD"; // senha do MySQL
$dbname = "id20421005_databasevuejs"; // nome do banco de dados

// Conexão com o banco de dados MySQL
$conn = mysqli_connect($host, $user, $pass, $dbname);

// Verifica se houve erro na conexão
if (!$conn) {
    die("Falha na conexão: " . mysqli_connect_error());
}
