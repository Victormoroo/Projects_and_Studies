<?php

ob_start(); // ativa o buffer de saída de dados do PHP. Isso significa que a saída do script é armazenada em um buffer em vez de ser enviada diretamente para o navegador. Isso é útil porque permite que o script manipule a saída antes que ela seja enviada para o navegador.

session_start(); // inicia a sessão do usuário. As variáveis de sessão podem ser usadas para armazenar informações do usuário enquanto ele navega no site.

require_once 'config.php'; // é uma instrução que inclui o arquivo 'config.php' no script atual. Esse arquivo pode conter informações de configuração do banco de dados ou outras configurações globais usadas pelo site.

if ($_SERVER['REQUEST_METHOD'] == 'POST') { //é uma verificação para garantir que o formulário foi enviado por meio do método POST. Isso garante que o script seja executado apenas quando o formulário é enviado.
    $email = $_POST['email_login'];
    $senha = $_POST['senha_login'];

    // Verifica se o email e senha são válidos
    $query = "SELECT id, nome FROM fatec_admin WHERE email='$email' AND senha=md5('$senha')";
    $result = mysqli_query($conn, $query); //executa a consulta SQL e retorna um objeto de resultado.

    if (mysqli_num_rows($result) == 1) { // verifica se a consulta SQL retornou exatamente uma linha, o que significa que o email e senha fornecidos são válidos.
        $row = mysqli_fetch_assoc($result);
        $_SESSION['id'] = $row['id'];
        $_SESSION['nome'] = $row['nome'];
        header('Location: dashboard.html'); // Redireciona para a página de dashboard
    } else {
        echo '<script>alert("Email ou senha incorretos!")</script>'; // exibe uma mensagem de erro se o email e senha fornecidos pelo usuário não correspondem a uma entrada na tabela de administração do site.
        header("Location: index.html#paralogin");               
    }
}

ob_end_flush();

?>

