<?php

header('Access-Control-Allow-Origin: *');

$connect = new PDO("mysql:host=localhost;dbname=id20421005_databasevuejs", "id20421005_victormoro", "6Um/!(=<^O4^aQsD"); //o script estabelece uma conexão com o banco de dados MySQL usando a classe PDO (PHP Data Objects).

$received_data = json_decode(file_get_contents("php://input")); //o script recebe os dados enviados pela requisição em formato JSON e converte para um objeto PHP usando a função json_decode.

$data = array(); //o script cria um array vazio para armazenar os dados que serão retornados.

if($received_data->query != '') //o script verifica se a propriedade "query" do objeto recebido não está vazia. Se não estiver vazia, o script constrói uma consulta SQL que busca por registros na tabela "fatec_alunos" que tenham o valor da propriedade "query" em qualquer posição dos campos "first_name" ou "last_name". A consulta é ordenada pela coluna "id" em ordem decrescente.
{
	$query = "
	SELECT * FROM fatec_professores 
	WHERE nome LIKE '%".$received_data->query."%' 
	ORDER BY id DESC
	";
}
else
{
	$query = "
	SELECT * FROM fatec_professores 
	ORDER BY id DESC
	";
}

$statement = $connect->prepare($query); //o script prepara a consulta SQL usando o método prepare da classe PDO.

$statement->execute(); //o script executa a consulta usando o método execute da classe PDO.

while($row = $statement->fetch(PDO::FETCH_ASSOC)) //o script itera sobre os resultados da consulta usando o método fetch da classe PDO e armazena cada registro no array $data.
{
	$data[] = $row;
}

echo json_encode($data); //o script retorna os dados em formato JSON usando a função json_encode.

?>