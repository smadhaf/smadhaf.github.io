<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nama = $_POST["nama"];
    $email = $_POST["email"];
    $telepon = $_POST["telepon"];
    $pesan = $_POST["pesan"];
    
    echo "<h2>Terima kasih, $nama, pesan Anda telah diterima.</h2>";
    


    echo '<table class="double-border-table">';
    echo "<tr><td>Nama:</td><td>$nama</td></tr>";
    echo "<tr><td>Email:</td><td>$email</td></tr>";
    echo "<tr><td>Nomor Telepon:</td><td>$telepon</td></tr>";
    echo "<tr><td>Pesan:</td><td>$pesan</td></tr>";
    echo "</table>";

}
?>
