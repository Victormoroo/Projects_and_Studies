<?php
header('Access-Control-Allow-Origin: *');

$connect = new PDO("mysql:host=localhost;dbname=id20421005_databasevuejs", "id20421005_victormoro", "6Um/!(=<^O4^aQsD"); //conecta o código PHP com o banco de dados MySQL usando a classe PDO do PHP.
//definem uma condição para buscar todos os registros de alunos no banco de dados, ordenados pelo ID em ordem decrescente. O resultado é armazenado em um array de dados que é codificado em JSON e enviado de volta para a aplicação Vue.js.
$received_data = json_decode(file_get_contents("php://input"));
$data = array();
if ($received_data->action == 'fetchall') {
    $query = "
 SELECT * FROM fatec_professores
 ORDER BY id DESC
 ";
    $statement = $connect->prepare($query);
    $statement->execute();
    while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
        $data[] = $row;
    }
    echo json_encode($data);
}

//definem uma condição para inserir um novo registro de aluno no banco de dados, usando as informações do aluno fornecidas pela aplicação Vue.js.
if ($received_data->action == 'insert') {
    $data = array(
        ':nome' => $received_data->nome,
        ':endereco' => $received_data->endereco,
        ':curso' => $received_data->curso,
        ':salario' => $received_data->salario,
    );

    $query = "
 INSERT INTO fatec_professores 
 (nome, endereco, curso, salario) 
 VALUES (:nome, :endereco, :curso, :salario)
 ";

    $statement = $connect->prepare($query);

    $statement->execute($data);

    $output = array(
        'message' => 'Professor Adicionado'
    );

    echo json_encode($output);
}

//definem uma condição para buscar um único registro de aluno no banco de dados, com base no ID fornecido pela aplicação Vue.js.
if ($received_data->action == 'fetchSingle') {
    $query = "
 SELECT * FROM fatec_professores 
 WHERE id = '" . $received_data->id . "'
 ";

    $statement = $connect->prepare($query);

    $statement->execute();

    $result = $statement->fetchAll();

    foreach ($result as $row) {
        $data['id'] = $row['id'];
        $data['nome'] = $row['nome'];
        $data['endereco'] = $row['endereco'];
        $data['curso'] = $row['curso'];
        $data['salario'] = $row['salario'];
    }

    echo json_encode($data);
}

//definem uma condição para atualizar as informações de um registro de aluno no banco de dados, com base nas informações do aluno fornecidas pela aplicação Vue.js.
if ($received_data->action == 'update') {
    $data = array(
        ':nome' => $received_data->firstName,
        ':endereco' => $received_data->lastName,
        ':curso' => $received_data->lastName,
        ':salario' => $received_data->lastName,
        ':id' => $received_data->hiddenId
    );

    $query = "
 UPDATE fatec_alunos 
 SET nome = :nome, 
 endereco = :endereco,
 curso = :curso,
 salario = :salario 
 WHERE id = :id
 ";

    $statement = $connect->prepare($query);

    $statement->execute($data);

    $output = array(
        'message' => 'Professor Atualizado'
    );

    echo json_encode($output);
}

//definem uma condição para excluir um registro de aluno do banco de dados, com base no ID fornecido pela aplicação Vue.js.
if ($received_data->action == 'delete') {
    $query = "
 DELETE FROM fatec_professores 
 WHERE id = '" . $received_data->id . "'
 ";

    $statement = $connect->prepare($query);

    $statement->execute();

    $output = array(
        'message' => 'Professor Deletado'
    );

    echo json_encode($output);
}

?>