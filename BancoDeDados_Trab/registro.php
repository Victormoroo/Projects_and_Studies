<?php

ob_start();

session_start(); // Inicia a sessão

require_once 'config.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') { // verifica se o método HTTP utilizado na requisição é POST, ou seja, se os dados do formulário de cadastro foram submetidos ao servidor.
    $nome = $_POST['nome_cad'];
    $email = $_POST['email_cad'];
    $senha = $_POST['senha_cad'];
    // obtém os dados do formulário de cadastro submetidos pelo usuário e armazena em variáveis PHP.

    // Verifica se o email já está em uso
    $query = "SELECT * FROM fatec_admin WHERE email='$email'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) > 0) { // verifica se a consulta retornou algum resultado, ou seja, se o email já está em uso.
        echo "<script>alert('Este email já está em uso!');</script>"; // exibe uma mensagem de erro caso o email já esteja cadastrado no sistema.
    } else { // caso o email não esteja em uso, o código abaixo é executado:
        // Insere o novo usuário no banco de dados
        $query = "INSERT INTO fatec_admin (nome, email, senha) VALUES ('$nome', '$email', md5('$senha'))";
        if (mysqli_query($conn, $query)) { //  verifica se a query foi executada com sucesso no banco de dados.
            echo '<script>alert("Usuário cadastrado com sucesso!")</script>';
            header("Location: index.html#paralogin"); // exibe uma mensagem de sucesso e redireciona o usuário para a página de login.
        } else { // caso ocorra um erro na inserção do usuário no banco de dados, uma mensagem de erro é exibida e o usuário é redirecionado para a página de cadastro.
            echo '<script>alert("Erro ao cadastrar usuário!")</script>';
            header("Location: index.html#paracadastro");
        }
    }
}

ob_end_flush();

/*
CREATE TABLE fatec_admin (
id INT(11) NOT NULL AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
senha VARCHAR(100) NOT NULL,
PRIMARY KEY (id),
UNIQUE KEY email (email)
);
*/


?>